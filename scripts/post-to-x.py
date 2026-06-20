#!/usr/bin/env python3
"""Pubblica news crypto virali su X (@TheRiser100x) — 5 post/giorno con foto.

Env: scripts/.env oppure X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
Guida: x-auto-setup.html

  python post-to-x.py --dry-run --auto --slot 0
  python post-to-x.py --auto --now
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
import secrets
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
from x_images import SLOT_LABELS, SLOT_TYPES, generate_slot_times, image_path_for_slot, slot_type_for_index
from x_viral import build_viral_post, is_bitcoin_item, is_elon_item, is_regulation_item, score_viral

NEWS_PATH = ROOT / "data" / "crypto-news.json"
NEWS_FALLBACK = ROOT / "data" / "bitcoin-news.json"
SCHEDULE_PATH = ROOT / "data" / "x-schedule.json"
ENV_PATH = Path(__file__).resolve().parent / ".env"
X_POSTS_PER_DAY = 5


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    env.update({k: v for k, v in os.environ.items() if k.startswith("X_")})
    return env


def load_schedule() -> dict:
    slot_times = generate_slot_times(X_POSTS_PER_DAY)
    default = {
        "startDate": date.today().isoformat(),
        "postsPerDay": X_POSTS_PER_DAY,
        "timezone": "Europe/Rome",
        "account": "https://x.com/TheRiser100x",
        "slots": slot_times,
        "slotTypes": SLOT_TYPES,
        "posted": [],
    }
    if not SCHEDULE_PATH.exists():
        return default
    data = json.loads(SCHEDULE_PATH.read_text(encoding="utf-8"))
    return {**default, **data}


def save_schedule(schedule: dict) -> None:
    SCHEDULE_PATH.write_text(
        json.dumps(schedule, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def load_news() -> dict:
    path = NEWS_PATH if NEWS_PATH.exists() else NEWS_FALLBACK
    if not path.exists():
        raise SystemExit("News non trovate: esegui fetch-crypto-news.py")
    return json.loads(path.read_text(encoding="utf-8"))


def today_in_timezone(tz_name: str = "Europe/Rome") -> date:
    if ZoneInfo is not None:
        try:
            return datetime.now(ZoneInfo(tz_name)).date()
        except Exception:
            pass
    return date.today()


def now_in_timezone_iso(tz_name: str = "Europe/Rome") -> str:
    if ZoneInfo is not None:
        try:
            return datetime.now(ZoneInfo(tz_name)).isoformat()
        except Exception:
            pass
    return datetime.now().isoformat()


def already_posted(schedule: dict, date_str: str, slot: int) -> bool:
    return any(p.get("date") == date_str and p.get("slot") == slot for p in schedule.get("posted", []))


def posted_news_ids(schedule: dict) -> set[str]:
    return {p.get("newsId") for p in schedule.get("posted", []) if p.get("newsId")}


def record_post(schedule: dict, date_str: str, slot: int, news_id: str, tweet_id: str, media: bool = False) -> None:
    schedule.setdefault("posted", []).append({
        "date": date_str,
        "slot": slot,
        "slotType": slot_type_for_index(slot),
        "newsId": news_id,
        "tweetId": tweet_id,
        "withImage": media,
        "publishedAt": now_in_timezone_iso(schedule.get("timezone", "Europe/Rome")),
    })


def current_slot_index(per_day: int = X_POSTS_PER_DAY, tz_name: str = "Europe/Rome", tolerance: int = 30) -> int | None:
    if ZoneInfo is None:
        return None
    try:
        now = datetime.now(ZoneInfo(tz_name))
    except Exception:
        return None
    now_mins = now.hour * 60 + now.minute
    for i, t in enumerate(generate_slot_times(per_day)):
        h, m = map(int, t.split(":"))
        if abs(now_mins - (h * 60 + m)) <= tolerance:
            return i
    return None


def filter_for_slot(items: list[dict], slot: int) -> list[dict]:
    slot_type = slot_type_for_index(slot)
    if slot_type == "elon":
        return [i for i in items if is_elon_item(i)]
    if slot_type == "regulation":
        return [i for i in items if is_regulation_item(i)]
    if slot_type == "bitcoin_breaking":
        return [i for i in items if is_bitcoin_item(i) and i.get("breaking")]
    if slot_type in ("bitcoin", "bitcoin_viral"):
        return [i for i in items if is_bitcoin_item(i)]
    return list(items)


def ranked_news(items: list[dict], slot: int, used_ids: set[str]) -> list[dict]:
    fresh = [i for i in items if i.get("id") not in used_ids]
    if not fresh:
        fresh = list(items)

    candidates = filter_for_slot(fresh, slot)
    if not candidates:
        candidates = fresh

    slot_type = slot_type_for_index(slot)
    if slot_type == "elon":
        candidates.sort(key=score_viral, reverse=True)
    elif slot_type == "regulation":
        candidates.sort(key=lambda x: (1 if is_regulation_item(x) else 0, score_viral(x)), reverse=True)
    elif slot_type == "bitcoin_breaking":
        candidates.sort(key=lambda x: (1 if x.get("breaking") else 0, score_viral(x)), reverse=True)
    else:
        candidates.sort(key=lambda x: (1 if is_bitcoin_item(x) else 0, score_viral(x)), reverse=True)
    return candidates


def pick_news(data: dict, schedule: dict, slot: int) -> dict | None:
    items = data.get("items") or []
    if not items:
        return None
    used = posted_news_ids(schedule)
    ranked = ranked_news(items, slot, used)
    return ranked[0] if ranked else None


def oauth1_signature(method: str, url: str, params: dict, consumer_secret: str, token_secret: str) -> str:
    encoded = "&".join(
        f"{urllib.parse.quote(k, safe='')}={urllib.parse.quote(str(v), safe='')}"
        for k, v in sorted(params.items())
    )
    base = f"{method.upper()}&{urllib.parse.quote(url, safe='')}&{urllib.parse.quote(encoded, safe='')}"
    key = f"{urllib.parse.quote(consumer_secret, safe='')}&{urllib.parse.quote(token_secret, safe='')}"
    digest = hmac.new(key.encode(), base.encode(), hashlib.sha1).digest()
    return base64.b64encode(digest).decode()


def oauth1_header(method: str, url: str, consumer_key: str, consumer_secret: str, token: str, token_secret: str, extra_params: dict | None = None) -> str:
    oauth = {
        "oauth_consumer_key": consumer_key,
        "oauth_nonce": secrets.token_hex(16),
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(int(datetime.now().timestamp())),
        "oauth_token": token,
        "oauth_version": "1.0",
    }
    sign_params = {**oauth, **(extra_params or {})}
    oauth["oauth_signature"] = oauth1_signature(method, url, sign_params, consumer_secret, token_secret)
    parts = [f'{urllib.parse.quote(k, safe="")}="{urllib.parse.quote(str(v), safe="")}"' for k, v in sorted(oauth.items())]
    return "OAuth " + ", ".join(parts)


def upload_media(image_path: Path, env: dict, dry_run: bool) -> str | None:
    if not image_path or not image_path.exists():
        return None
    if dry_run:
        print(f"[DRY RUN] UPLOAD media {image_path}")
        return "dry-run-media"

    url = "https://upload.twitter.com/1.1/media/upload.json"
    media_b64 = base64.b64encode(image_path.read_bytes()).decode()
    body_params = {"media_data": media_b64, "media_category": "tweet_image"}
    body = urllib.parse.urlencode(body_params).encode("utf-8")
    auth = oauth1_header(
        "POST", url,
        env["X_API_KEY"], env["X_API_SECRET"],
        env["X_ACCESS_TOKEN"], env["X_ACCESS_TOKEN_SECRET"],
        body_params,
    )
    req = urllib.request.Request(url, data=body, method="POST", headers={
        "Authorization": auth,
        "Content-Type": "application/x-www-form-urlencoded",
    })
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return str(data.get("media_id_string") or data.get("media_id") or "")
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")
        print(f"Media upload warning: {e.code} {err}", file=sys.stderr)
        return None


def post_tweet(text: str, env: dict, dry_run: bool, media_id: str | None = None) -> dict:
    url = "https://api.twitter.com/2/tweets"
    if dry_run:
        print("[DRY RUN] POST", url)
        if media_id:
            print(f"[DRY RUN] media_id={media_id}")
        print(text)
        print(f"Length: {len(text)}")
        return {"dry_run": True, "id": "dry-run"}

    payload: dict = {"text": text}
    if media_id and media_id != "dry-run-media":
        payload["media"] = {"media_ids": [media_id]}

    body = json.dumps(payload).encode("utf-8")
    auth = oauth1_header(
        "POST", url,
        env["X_API_KEY"], env["X_API_SECRET"],
        env["X_ACCESS_TOKEN"], env["X_ACCESS_TOKEN_SECRET"],
    )
    req = urllib.request.Request(url, data=body, method="POST", headers={
        "Authorization": auth,
        "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")
        if e.code == 403 and "oauth1-permissions" in err:
            raise SystemExit(
                f"X API error 403: app lacks Read and Write permission.\n"
                f"Fix: developer.x.com → your app → Settings → User authentication → "
                f"OAuth 1.0a → App permissions: Read and Write → Save → "
                f"Regenerate Access Token + Secret → update scripts/.env\n"
                f"Guide: x-fix-permissions.html\n{err}"
            ) from e
        raise SystemExit(f"X API error {e.code}: {err}") from e


def main() -> None:
    parser = argparse.ArgumentParser(description="Pubblica news crypto su X")
    parser.add_argument("--auto", action="store_true", help="Modalità automatica (5 post/giorno)")
    parser.add_argument("--now", action="store_true", help="Rileva slot dall'orario Roma")
    parser.add_argument("--slot", type=int, default=0, help="Slot 0-4")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-image", action="store_true", help="Pubblica senza immagine")
    parser.add_argument("--news-id", help="Pubblica una news specifica per id")
    args = parser.parse_args()

    env = load_env()
    required = ["X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"]
    if not args.dry_run and any(not env.get(k) for k in required):
        print("Mancano credenziali X API in scripts/.env", file=sys.stderr)
        print("Guida: x-auto-setup.html", file=sys.stderr)
        sys.exit(1)

    schedule = load_schedule()
    per_day = int(schedule.get("postsPerDay") or X_POSTS_PER_DAY)
    slot_times = generate_slot_times(per_day)
    tz_name = schedule.get("timezone", "Europe/Rome")
    today_str = today_in_timezone(tz_name).isoformat()

    if args.auto and args.now:
        detected = current_slot_index(per_day, tz_name)
        if detected is None:
            labels = [f"{slot_times[i]} ({SLOT_LABELS.get(slot_type_for_index(i), '')})" for i in range(per_day)]
            print(f"Nessuno slot attivo. Orari: {', '.join(labels)} ({tz_name})")
            return
        args.slot = detected
        print(f"Slot {detected} — {slot_times[detected]} · {SLOT_LABELS.get(slot_type_for_index(detected), '')}")

    if args.slot < 0 or args.slot >= per_day:
        raise SystemExit(f"Slot {args.slot} non valido (0–{per_day - 1})")

    if args.auto and already_posted(schedule, today_str, args.slot):
        print(f"Già pubblicato oggi slot {args.slot} ({slot_times[args.slot]})")
        return

    data = load_news()
    slot_type = slot_type_for_index(args.slot)

    if args.news_id:
        matches = [i for i in data.get("items", []) if i.get("id") == args.news_id]
        if not matches:
            raise SystemExit(f"News non trovata: {args.news_id}")
        item = matches[0]
    elif args.auto:
        item = pick_news(data, schedule, args.slot)
        if not item:
            print("Nessuna news disponibile")
            return
    else:
        raise SystemExit("Usa --auto o --news-id")

    raw = item.get("title") or item.get("summary") or ""
    text = build_viral_post(
        raw,
        item.get("sourceHandle", ""),
        item.get("link") or item.get("url", ""),
        item.get("source", ""),
        slot_type,
    )

    image_path = None if args.no_image else image_path_for_slot(args.slot)
    media_id = upload_media(image_path, env, args.dry_run) if image_path else None

    print(f"\n--- {item.get('title', '')[:80]} ---")
    print(f"Fonte: {item.get('sourceHandle', '')} | Tipo: {slot_type} | Score: {item.get('viralScore', 0)}")
    if image_path:
        print(f"Immagine: {image_path.name}")

    result = post_tweet(text, env, args.dry_run, media_id)
    print(json.dumps(result, indent=2))

    if not args.dry_run and args.auto:
        tweet_id = (result.get("data") or {}).get("id", "")
        if tweet_id:
            record_post(schedule, today_str, args.slot, item.get("id", ""), tweet_id, bool(media_id))
            save_schedule(schedule)


if __name__ == "__main__":
    main()
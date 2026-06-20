#!/usr/bin/env python3
"""Pubblica news crypto virali su X (@TheRiser100x) — 2 post/giorno.

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
import sys
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
from x_viral import build_viral_post, score_viral
NEWS_PATH = ROOT / "data" / "crypto-news.json"
NEWS_FALLBACK = ROOT / "data" / "bitcoin-news.json"
SCHEDULE_PATH = ROOT / "data" / "x-schedule.json"
ENV_PATH = Path(__file__).resolve().parent / ".env"
X_POSTS_PER_DAY = 2
SLOT_TIMES = ["10:00", "19:00"]


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
    default = {
        "startDate": date.today().isoformat(),
        "postsPerDay": X_POSTS_PER_DAY,
        "timezone": "Europe/Rome",
        "account": "https://x.com/TheRiser100x",
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
        raise SystemExit(f"News non trovate: esegui fetch-crypto-news.py")
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


def day_index_from_start(start_date: str, today: date | None = None) -> int:
    start = date.fromisoformat(start_date[:10])
    current = today or date.today()
    return (current - start).days


def already_posted(schedule: dict, date_str: str, slot: int) -> bool:
    return any(p.get("date") == date_str and p.get("slot") == slot for p in schedule.get("posted", []))


def posted_news_ids(schedule: dict) -> set[str]:
    return {p.get("newsId") for p in schedule.get("posted", []) if p.get("newsId")}


def record_post(schedule: dict, date_str: str, slot: int, news_id: str, tweet_id: str) -> None:
    schedule.setdefault("posted", []).append({
        "date": date_str,
        "slot": slot,
        "newsId": news_id,
        "tweetId": tweet_id,
        "publishedAt": now_in_timezone_iso(schedule.get("timezone", "Europe/Rome")),
    })


def current_slot_index(per_day: int = X_POSTS_PER_DAY, tz_name: str = "Europe/Rome", tolerance: int = 35) -> int | None:
    if ZoneInfo is None:
        return None
    try:
        now = datetime.now(ZoneInfo(tz_name))
    except Exception:
        return None
    now_mins = now.hour * 60 + now.minute
    times = SLOT_TIMES[:per_day]
    for i, t in enumerate(times):
        h, m = map(int, t.split(":"))
        if abs(now_mins - (h * 60 + m)) <= tolerance:
            return i
    return None


def ranked_news(items: list[dict], slot: int, used_ids: set[str]) -> list[dict]:
    fresh = [i for i in items if i.get("id") not in used_ids]
    if not fresh:
        fresh = list(items)

    # Mattina: White House / breaking — Sera: top viral generale
    if slot == 0:
        fresh.sort(key=lambda x: (
            1 if x.get("sourceHandle") == "@WhiteHouse" else 0,
            score_viral(x),
        ), reverse=True)
    else:
        fresh.sort(key=score_viral, reverse=True)
    return fresh


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


def oauth1_header(method: str, url: str, consumer_key: str, consumer_secret: str, token: str, token_secret: str) -> str:
    oauth = {
        "oauth_consumer_key": consumer_key,
        "oauth_nonce": secrets.token_hex(16),
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(int(datetime.now().timestamp())),
        "oauth_token": token,
        "oauth_version": "1.0",
    }
    oauth["oauth_signature"] = oauth1_signature(method, url, oauth, consumer_secret, token_secret)
    parts = [f'{urllib.parse.quote(k, safe="")}="{urllib.parse.quote(str(v), safe="")}"' for k, v in sorted(oauth.items())]
    return "OAuth " + ", ".join(parts)


def post_tweet(text: str, env: dict, dry_run: bool) -> dict:
    url = "https://api.twitter.com/2/tweets"
    if dry_run:
        print("[DRY RUN] POST", url)
        print(text)
        print(f"Length: {len(text)}")
        return {"dry_run": True, "id": "dry-run"}

    body = json.dumps({"text": text}).encode("utf-8")
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
        raise SystemExit(f"X API error {e.code}: {err}") from e


def main() -> None:
    parser = argparse.ArgumentParser(description="Pubblica news crypto su X")
    parser.add_argument("--auto", action="store_true", help="Modalità automatica (2 post/giorno)")
    parser.add_argument("--now", action="store_true", help="Rileva slot dall'orario Roma")
    parser.add_argument("--slot", type=int, default=0, help="Slot 0=10:00, 1=19:00")
    parser.add_argument("--dry-run", action="store_true")
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
    tz_name = schedule.get("timezone", "Europe/Rome")
    today_str = today_in_timezone(tz_name).isoformat()

    if args.auto and args.now:
        detected = current_slot_index(per_day, tz_name)
        if detected is None:
            print(f"Nessuno slot attivo. Orari: {', '.join(SLOT_TIMES[:per_day])} ({tz_name})")
            return
        args.slot = detected
        print(f"Slot {detected} — {SLOT_TIMES[detected]}")

    if args.slot < 0 or args.slot >= per_day:
        raise SystemExit(f"Slot {args.slot} non valido (0–{per_day - 1})")

    if args.auto and already_posted(schedule, today_str, args.slot):
        print(f"Già pubblicato oggi slot {args.slot} ({SLOT_TIMES[args.slot]})")
        return

    data = load_news()
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
    )
    print(f"\n--- {item.get('title', '')[:80]} ---")
    print(f"Fonte: {item.get('sourceHandle', '')} | Score: {item.get('viralScore', 0)}")

    result = post_tweet(text, env, args.dry_run)
    print(json.dumps(result, indent=2))

    if not args.dry_run and args.auto:
        tweet_id = (result.get("data") or {}).get("id", "")
        if tweet_id:
            record_post(schedule, today_str, args.slot, item.get("id", ""), tweet_id)
            save_schedule(schedule)


if __name__ == "__main__":
    main()
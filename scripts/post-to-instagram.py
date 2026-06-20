#!/usr/bin/env python3
"""Pubblica articoli su Instagram (@krown.82 / @bitcoin.is.hope2030) via Graph API.

Setup: scripts/.env — INSTAGRAM_ACCOUNT_ID + FACEBOOK_PAGE_ACCESS_TOKEN
Guida: instagram-auto-setup.html

Automazione (20 post/giorno, 07:00–22:00 Roma):
  python post-to-instagram.py --auto --now
  python post-to-instagram.py --auto --slot 0
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime
from pathlib import Path

from chill_cyber_playlist import track_for_slot
from instagram_auth import graph_url, is_instagram_login_token, resolve_credentials
from story_publish import publish_instagram_story
from story_video import prepare_story_video

try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_PATH = ROOT / "data" / "articles.json"
SCHEDULE_PATH = ROOT / "data" / "instagram-schedule.json"
SITE_URL = "https://satoshiallien.github.io/cryptoitaliafacile/"
IMAGE_BASE = f"{SITE_URL}assets/img/instagram/posts/"
STORY_IMAGE_BASE = f"{SITE_URL}assets/img/instagram/stories/"
ENV_PATH = Path(__file__).resolve().parent / ".env"
GRAPH = "https://graph.facebook.com/v21.0"
IG_HANDLE = "krown.82"
IG_POSTS_PER_DAY = 20

EMOJI = {
    "guide": "📖", "tip": "💡", "trend": "📈", "tutorial": "🎓",
    "cardano": "🔷", "sicurezza": "🔒",
}
LABELS = {
    "guide": "Guide", "tip": "Crypto Tip", "trend": "Trend", "tutorial": "Tutorial",
    "cardano": "Cardano", "sicurezza": "Security",
}
HOOKS = {
    "guide": "🔥 FREE GUIDE — Don't skip this:",
    "tip": "⚡ TIP TO USE RIGHT NOW:",
    "trend": "📈 HOT TREND — What you need to know:",
    "tutorial": "🎓 STEP-BY-STEP TUTORIAL:",
    "cardano": "🔷 CARDANO — Explained simply:",
    "sicurezza": "🚨 WARNING — Avoid this mistake:",
}
IMAGE_DEFAULTS = {
    "guide": "guide.jpg", "tip": "tip.jpg", "trend": "trend.jpg", "tutorial": "guide.jpg",
    "cardano": "cardano.jpg", "sicurezza": "sicurezza.jpg",
}
IMAGE_BY_TAG = {
    "bitcoin": "bitcoin.jpg", "btc": "bitcoin.jpg", "exchange": "exchange.jpg",
    "revolut": "exchange.jpg", "kraken": "exchange.jpg", "wallet": "wallet.jpg",
    "seed phrase": "sicurezza.jpg", "sicurezza": "sicurezza.jpg", "phishing": "sicurezza.jpg",
    "truffe": "sicurezza.jpg", "cardano": "cardano.jpg", "ada": "cardano.jpg",
    "ethereum": "ethereum.jpg", "eth": "ethereum.jpg", "defi": "defi.jpg",
    "uniswap": "defi.jpg", "staking": "ethereum.jpg", "ledger": "wallet.jpg",
    "metamask": "wallet.jpg",
}


def generate_slot_times(per_day: int = IG_POSTS_PER_DAY, start_h: int = 7, end_h: int = 22) -> list[str]:
    start_m = start_h * 60
    end_m = end_h * 60
    times: list[str] = []
    for i in range(per_day):
        if per_day == 1:
            mins = start_m
        else:
            mins = round(start_m + (end_m - start_m) * i / (per_day - 1))
        times.append(f"{mins // 60:02d}:{mins % 60:02d}")
    return times


def slot_label(index: int, per_day: int = IG_POSTS_PER_DAY) -> str:
    times = generate_slot_times(per_day)
    if 0 <= index < len(times):
        return f"Post {index + 1} ({times[index]})"
    return f"Post {index + 1}"


def current_slot_index(per_day: int = IG_POSTS_PER_DAY, tz_name: str = "Europe/Rome", tolerance: int = 22) -> int | None:
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


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    for prefix in ("INSTAGRAM_", "FACEBOOK_"):
        env.update({k: v for k, v in os.environ.items() if k.startswith(prefix)})
    return env


def load_schedule() -> dict:
    default = {
        "startDate": date.today().isoformat(),
        "postsPerDay": IG_POSTS_PER_DAY,
        "timezone": "Europe/Rome",
        "account": f"https://www.instagram.com/{IG_HANDLE}/",
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


def article_url(slug: str) -> str:
    return f"{SITE_URL}articolo.html?slug={urllib.parse.quote(slug)}"


def instagram_image_file(article: dict) -> str:
    if article.get("igImage"):
        return article["igImage"]
    if article.get("fbImage"):
        return article["fbImage"]
    for raw in article.get("tags") or []:
        tag = str(raw).lower().lstrip("#").strip()
        if tag in IMAGE_BY_TAG:
            return IMAGE_BY_TAG[tag]
    title = (article.get("title") or "").lower()
    slug = (article.get("slug") or "").lower()
    if "bitcoin" in title or "bitcoin" in slug:
        return "bitcoin.jpg"
    if "ethereum" in title or "ethereum" in slug:
        return "ethereum.jpg"
    if "cardano" in title or "cardano" in slug or "ada" in slug:
        return "cardano.jpg"
    if "exchange" in title or "exchange" in slug:
        return "exchange.jpg"
    if "wallet" in title or "wallet" in slug or "seed" in slug:
        return "wallet.jpg"
    if "sicurezz" in title or "phishing" in slug:
        return "sicurezza.jpg"
    if "defi" in title or "defi" in slug:
        return "defi.jpg"
    return IMAGE_DEFAULTS.get(article.get("category", "guide"), "guide.jpg")


def instagram_image_url(article: dict) -> str:
    return IMAGE_BASE + instagram_image_file(article)


def instagram_story_image_url(article: dict) -> str:
    return STORY_IMAGE_BASE + instagram_image_file(article)


def build_caption(article: dict) -> str:
    cat = article.get("category", "guide")
    emoji = EMOJI.get(cat, "📖")
    label = LABELS.get(cat, "Guide")
    hook = HOOKS.get(cat, "🔥 Don't miss this guide:")
    tags: list[str] = []
    for t in (article.get("tags") or [])[:5]:
        clean = t.lstrip("#").strip()
        if clean:
            tags.append(f"#{clean}")
    base = "#Bitcoin #BTC #Crypto #BitcoinIsHope #CryptoEducation"
    tag_line = " ".join(tags)
    excerpt = article.get("excerptEn") or article.get("excerpt", "")
    return (
        f"{hook}\n\n"
        f"{emoji} {label}: {article['title']}\n\n"
        f"{excerpt}\n\n"
        f"🔗 Full guide — link in bio\n"
        f"{article_url(article['slug'])}\n\n"
        f"{tag_line} {base}".strip()
    )[:2200]


def graph_request(
    path: str,
    data: dict | None = None,
    method: str = "GET",
    *,
    token: str = "",
) -> dict:
    url = graph_url(path, token) if token and not path.startswith("http") else path
    body = None
    if data is not None:
        body = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=body, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode("utf-8", errors="replace")
        try:
            err = json.loads(payload)
        except json.JSONDecodeError:
            err = {"error": {"message": payload, "code": exc.code}}
        err.setdefault("error", {})["http_status"] = exc.code
        return err


def post_to_instagram(caption: str, image_url: str, ig_id: str, token: str, dry_run: bool) -> dict:
    if dry_run:
        print("[DRY RUN] CREATE media container")
        print("IMAGE:", image_url)
        print(caption)
        print(f"Length: {len(caption)}")
        return {"dry_run": True, "id": "dry-run"}

    container = graph_request(
        f"/{ig_id}/media",
        {
            "image_url": image_url,
            "caption": caption,
            "access_token": token,
        },
        method="POST",
        token=token,
    )
    if container.get("error"):
        return container

    creation_id = container.get("id")
    if not creation_id:
        return {"error": {"message": f"No creation_id: {container}"}}

    for attempt in range(8):
        time.sleep(3 if attempt == 0 else 5)
        status = graph_request(
            f"/{creation_id}?fields=status_code&access_token={urllib.parse.quote(token)}",
            token=token,
        )
        code = (status.get("status_code") or "").upper()
        if code in ("FINISHED", ""):
            break
        if code == "ERROR":
            return {"error": {"message": f"Media processing failed: {status}"}}
        print(f"Media status: {code or 'processing'}...")

    return graph_request(
        f"/{ig_id}/media_publish",
        {
            "creation_id": creation_id,
            "access_token": token,
        },
        method="POST",
        token=token,
    )


def article_score(article: dict) -> int:
    return (4 if article.get("featured") else 0) + (2 if article.get("popular") else 0)


def balanced_queue(articles: list[dict]) -> list[dict]:
    buckets: dict[str, list[dict]] = {
        "guide": sorted(
            [a for a in articles if a.get("category") in ("guide", "tutorial")],
            key=article_score, reverse=True,
        ),
        "tip": sorted([a for a in articles if a.get("category") == "tip"], key=article_score, reverse=True),
        "trend": sorted([a for a in articles if a.get("category") == "trend"], key=article_score, reverse=True),
        "other": sorted(
            [a for a in articles if a.get("category") in ("cardano", "sicurezza")],
            key=article_score, reverse=True,
        ),
    }
    queue: list[dict] = []
    max_len = max((len(v) for v in buckets.values()), default=0)
    for i in range(max_len):
        for key in ("guide", "tip", "trend", "other"):
            if i < len(buckets[key]):
                queue.append(buckets[key][i])
    seen: set[str] = set()
    unique: list[dict] = []
    for item in queue:
        if item["slug"] not in seen:
            seen.add(item["slug"])
            unique.append(item)
    return unique


def daily_plan(articles: list[dict], per_day: int) -> list[list[dict]]:
    queue = balanced_queue(articles)
    if not queue:
        return []
    min_days = max((len(queue) + per_day - 1) // per_day, 30)
    days: list[list[dict]] = []
    cursor = 0
    for _ in range(min_days):
        days.append([queue[cursor % len(queue)] for _ in range(per_day)])
        cursor += per_day
    return days


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
    return any(
        p.get("date") == date_str and p.get("slot") == slot
        for p in schedule.get("posted", [])
    )


def record_post(
    schedule: dict,
    date_str: str,
    slot: int,
    slug: str,
    media_id: str,
    *,
    story_id: str = "",
    story_track: str = "",
) -> None:
    entry = {
        "date": date_str,
        "slot": slot,
        "slug": slug,
        "mediaId": media_id,
        "publishedAt": now_in_timezone_iso(schedule.get("timezone", "Europe/Rome")),
    }
    if story_id:
        entry["storyId"] = story_id
    if story_track:
        entry["storyTrack"] = story_track
    schedule.setdefault("posted", []).append(entry)


def get_auto_article(articles: list[dict], schedule: dict, slot: int, env: dict) -> tuple[dict | None, int, str]:
    per_day = int(env.get("INSTAGRAM_POSTS_PER_DAY") or schedule.get("postsPerDay") or IG_POSTS_PER_DAY)
    start_date = env.get("INSTAGRAM_SCHEDULE_START") or schedule.get("startDate")
    tz_name = schedule.get("timezone", "Europe/Rome")
    today = today_in_timezone(tz_name)
    today_str = today.isoformat()

    if slot >= per_day:
        return None, day_index_from_start(start_date, today), today_str
    if already_posted(schedule, today_str, slot):
        print(f"Già pubblicato oggi slot {slot} ({slot_label(slot, per_day)})")
        return None, day_index_from_start(start_date, today), today_str

    day_idx = day_index_from_start(start_date, today)
    if day_idx < 0:
        print(f"Piano non ancora iniziato (startDate={start_date})")
        return None, day_idx, today_str

    days = daily_plan(articles, per_day)
    if not days:
        return None, day_idx, today_str

    day_posts = days[day_idx % len(days)]
    if slot >= len(day_posts):
        return None, day_idx, today_str
    return day_posts[slot], day_idx, today_str


def select_articles(data: dict, args: argparse.Namespace) -> list[dict]:
    articles = data["articles"]
    if args.slug:
        found = [a for a in articles if a["slug"] == args.slug]
        if not found:
            raise SystemExit(f"Articolo non trovato: {args.slug}")
        return found

    if args.auto:
        env = load_env()
        schedule = load_schedule()
        article, day_idx, today_str = get_auto_article(articles, schedule, args.slot, env)
        if not article:
            return []
        per_day = int(env.get("INSTAGRAM_POSTS_PER_DAY") or schedule.get("postsPerDay") or IG_POSTS_PER_DAY)
        print(f"Auto post — giorno {day_idx + 1}, slot {args.slot} ({slot_label(args.slot, per_day)}), data {today_str}")
        return [article]

    return balanced_queue(articles)[: args.limit]


def main() -> None:
    parser = argparse.ArgumentParser(description="Pubblica articoli su Instagram")
    parser.add_argument("--slug", help="Slug articolo singolo")
    parser.add_argument("--limit", type=int, default=1)
    parser.add_argument("--auto", action="store_true")
    parser.add_argument("--now", action="store_true")
    parser.add_argument("--slot", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-story", action="store_true", help="Pubblica solo il post feed, senza Story")
    args = parser.parse_args()

    env = load_env()
    ig_id, token, api_mode = resolve_credentials(env)

    if not args.dry_run and (not ig_id or not token):
        print("Mancano INSTAGRAM_ACCESS_TOKEN (IGAA) o FACEBOOK_PAGE_ACCESS_TOKEN + INSTAGRAM_ACCOUNT_ID.", file=sys.stderr)
        print(f"File: {ENV_PATH}", file=sys.stderr)
        print("Guida: instagram-auto-setup.html", file=sys.stderr)
        sys.exit(1)

    if not args.dry_run:
        print(f"API Instagram: {api_mode} — @{env.get('INSTAGRAM_USERNAME', IG_HANDLE)}")

    page_id = env.get("FACEBOOK_PAGE_ID", "")
    page_token = env.get("FACEBOOK_PAGE_ACCESS_TOKEN", "")
    if (
        not args.dry_run
        and api_mode == "facebook"
        and page_id
        and page_token
    ):
        page_check = graph_request(
            f"/{page_id}?fields=instagram_business_account,page_backed_instagram_accounts"
            f"&access_token={page_token}",
            method="GET",
            token=page_token,
        )
        has_business = bool((page_check.get("instagram_business_account") or {}).get("id"))
        has_backed = bool((page_check.get("page_backed_instagram_accounts") or {}).get("data"))
        if has_backed and not has_business:
            primary = env.get("INSTAGRAM_USERNAME", IG_HANDLE).lstrip("@")
            print(
                "Instagram non collegato come Business alla Page (solo page_backed). "
                f"Usa token IGAA: python scripts/aggiorna-token-facebook.py IGAA...",
                file=sys.stderr,
            )

    data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
    schedule = load_schedule()
    per_day = int(schedule.get("postsPerDay") or IG_POSTS_PER_DAY)

    if args.auto and args.now:
        tz_name = schedule.get("timezone", "Europe/Rome")
        detected = current_slot_index(per_day, tz_name)
        if detected is None:
            print(f"Nessuno slot attivo ora ({tz_name}). Orari: {', '.join(generate_slot_times(per_day))}")
            return
        args.slot = detected
        print(f"Slot rilevato: {detected} — {slot_label(detected, per_day)}")

    if args.slot < 0 or args.slot >= per_day:
        raise SystemExit(f"Slot {args.slot} non valido. Usa 0–{per_day - 1}.")

    selected = select_articles(data, args)
    if not selected:
        print("Nessun post da pubblicare.")
        return

    start_date = env.get("INSTAGRAM_SCHEDULE_START") or schedule.get("startDate")
    tz_name = schedule.get("timezone", "Europe/Rome")
    day_idx = max(0, day_index_from_start(start_date, today_in_timezone(tz_name)))

    for i, article in enumerate(selected):
        caption = build_caption(article)
        image_url = instagram_image_url(article)
        story_url = instagram_story_image_url(article)
        print(f"\n--- [{i + 1}/{len(selected)}] {article['title']} ---")
        print(f"IMAGE: {image_url}")
        print(f"STORY: {story_url}")
        result = post_to_instagram(caption, image_url, ig_id, token, args.dry_run)
        print(json.dumps(result, indent=2))

        if result.get("error"):
            err = result["error"]
            msg = err.get("message", err)
            hint = ""
            if "instagram" in str(msg).lower() or err.get("code") == 100:
                hint = "\n→ instagram-auto-setup.html (collega IG alla Page + permessi)"
            raise SystemExit(f"Instagram API error: {msg}{hint}")

        story_id = ""
        story_track = ""
        story_link = article_url(article["slug"])
        if not args.no_story:
            try:
                story_video_path = None
                if not args.dry_run:
                    story_video_path, track = prepare_story_video(
                        "instagram",
                        instagram_image_file(article),
                        args.slot,
                        day_idx,
                        per_day,
                        link_url=story_link,
                    )
                    story_track = track["title"]
                    print(f"MUSICA: {track['title']} — {track['artist']}")
                    print(f"VIDEO: {story_video_path}")
                else:
                    track = track_for_slot(args.slot, day_idx, per_day)
                    story_track = track["title"]
                    print(f"MUSICA: {track['title']} — {track['artist']} (dry-run)")

                print(f"STORY LINK: {story_link}")
                story_result = publish_instagram_story(
                    ig_id,
                    story_url,
                    token,
                    args.dry_run,
                    video_path=story_video_path,
                    use_video=not args.no_story,
                    link_url=story_link,
                )
                print("STORY:", json.dumps(story_result, indent=2))
                if story_result.get("error"):
                    print(f"AVVISO Story non pubblicata: {story_result['error']}", file=sys.stderr)
                else:
                    story_id = str(story_result.get("id") or "")
            except Exception as exc:
                print(f"AVVISO Story non pubblicata: {exc}", file=sys.stderr)

        if not args.dry_run and result.get("id"):
            today_str = today_in_timezone(schedule.get("timezone", "Europe/Rome")).isoformat()
            if args.auto:
                record_post(
                    schedule, today_str, args.slot, article["slug"], result["id"],
                    story_id=story_id,
                    story_track=story_track,
                )
                save_schedule(schedule)


if __name__ == "__main__":
    main()
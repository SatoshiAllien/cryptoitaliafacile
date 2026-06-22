#!/usr/bin/env python3
"""Pubblica Story FB + IG (senza link) — manuale o automatico."""

from __future__ import annotations

import argparse
import json
import os
from datetime import date, datetime
from pathlib import Path

from daily_post_queue import daily_plan
from instagram_auth import resolve_credentials
from instagram_story_queue import enqueue_story, is_quota_error, process_queue
from story_publish import publish_facebook_story, publish_instagram_story
from story_video import prepare_story_video, story_image_file

try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_PATH = ROOT / "data" / "articles.json"
SCHEDULE_PATH = ROOT / "data" / "story-schedule.json"
ENV_PATH = Path(__file__).resolve().parent / ".env"
SITE_URL = "https://satoshiallien.github.io/cryptoitaliafacile/"
FB_STORY_BASE = f"{SITE_URL}assets/img/facebook/stories/"
IG_STORY_BASE = f"{SITE_URL}assets/img/instagram/stories/"
STORIES_PER_DAY = 20
VARIANTS = ("abstract", "thematic", "minimal")


def generate_slot_times(per_day: int = STORIES_PER_DAY, start_h: int = 7, end_h: int = 22) -> list[str]:
    start_m = start_h * 60
    end_m = end_h * 60
    times: list[str] = []
    for i in range(per_day):
        mins = start_m if per_day == 1 else round(start_m + (end_m - start_m) * i / (per_day - 1))
        times.append(f"{mins // 60:02d}:{mins % 60:02d}")
    return times


def slot_label(index: int, per_day: int = STORIES_PER_DAY) -> str:
    times = generate_slot_times(per_day)
    if 0 <= index < len(times):
        return f"Story {index + 1} ({times[index]})"
    return f"Story {index + 1}"


def current_slot_index(per_day: int = STORIES_PER_DAY, tz_name: str = "Europe/Rome", tolerance: int = 22) -> int | None:
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
        "storiesPerDay": STORIES_PER_DAY,
        "timezone": "Europe/Rome",
        "posted": [],
    }
    if not SCHEDULE_PATH.exists():
        return default
    data = json.loads(SCHEDULE_PATH.read_text(encoding="utf-8"))
    return {**default, **data}


def save_schedule(schedule: dict) -> None:
    SCHEDULE_PATH.parent.mkdir(parents=True, exist_ok=True)
    SCHEDULE_PATH.write_text(json.dumps(schedule, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def day_index_from_start(start_date: str, today: date | None = None) -> int:
    start = date.fromisoformat(start_date[:10])
    current = today or date.today()
    return (current - start).days


def already_posted(schedule: dict, date_str: str, slot: int) -> bool:
    return any(p.get("date") == date_str and p.get("slot") == slot for p in schedule.get("posted", []))


def record_story(schedule: dict, *, date_str: str, slot: int, slug: str, fb_id: str = "", ig_id: str = "", track: str = "") -> None:
    entry = {
        "date": date_str,
        "slot": slot,
        "slug": slug,
        "publishedAt": now_in_timezone_iso(schedule.get("timezone", "Europe/Rome")),
    }
    if fb_id:
        entry["fbStoryId"] = fb_id
    if ig_id:
        entry["igStoryId"] = ig_id
    if track:
        entry["storyTrack"] = track
    schedule.setdefault("posted", []).append(entry)


def get_auto_article(articles: list[dict], schedule: dict, slot: int, env: dict) -> tuple[dict | None, int, str]:
    per_day = int(env.get("STORIES_PER_DAY") or schedule.get("storiesPerDay") or STORIES_PER_DAY)
    start_date = env.get("STORY_SCHEDULE_START") or schedule.get("startDate")
    tz_name = schedule.get("timezone", "Europe/Rome")
    today = today_in_timezone(tz_name)
    today_str = today.isoformat()

    if slot >= per_day:
        return None, day_index_from_start(start_date, today), today_str
    if already_posted(schedule, today_str, slot):
        print(f"Già pubblicata oggi slot {slot} ({slot_label(slot, per_day)})")
        return None, day_index_from_start(start_date, today), today_str

    day_idx = day_index_from_start(start_date, today)
    if day_idx < 0:
        print(f"Piano non ancora iniziato (startDate={start_date})")
        return None, day_idx, today_str

    days = daily_plan(articles)
    if not days:
        return None, day_idx, today_str

    day_posts = days[day_idx % len(days)]
    if slot >= len(day_posts):
        return None, day_idx, today_str
    return day_posts[slot], day_idx, today_str


def load_article(slug: str) -> dict:
    data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
    for article in data["articles"]:
        if article["slug"] == slug:
            return article
    raise SystemExit(f"Articolo non trovato: {slug}")


def publish_stories(
    article: dict,
    *,
    slot: int,
    dry_run: bool = False,
    skip_facebook: bool = False,
    skip_instagram: bool = False,
) -> int:
    code = 0
    env = load_env()
    track_title = ""

    print(f"Articolo: {article['title']}")
    print(f"Variante: {VARIANTS[slot % 3]} (slot {slot}) — nessun link")

    fb_id = ""
    if not skip_facebook:
        page_id = env.get("FACEBOOK_PAGE_ID", "")
        token = env.get("FACEBOOK_PAGE_ACCESS_TOKEN", "")
        if not dry_run and (not page_id or not token):
            print("ERRORE: manca token Facebook")
            code = 1
        else:
            img_file = story_image_file(article, slot)
            story_url = FB_STORY_BASE + img_file
            print(f"\n=== FACEBOOK STORY ===\n{story_url}")
            video_path = None
            if not dry_run:
                video_path, track = prepare_story_video("facebook", img_file, slot, 0, 20)
                track_title = track["title"]
                print(f"MUSICA: {track['title']} — {track['artist']}")
                print(f"VIDEO: {video_path}")
            result = publish_facebook_story(
                page_id, story_url, token, dry_run,
                video_path=video_path, use_video=True,
            )
            print("RISULTATO FB:", json.dumps(result, indent=2))
            if result.get("error"):
                code = 1
            else:
                fb_id = str(result.get("post_id") or result.get("id") or "")

    ig_id = ""
    if not skip_instagram:
        ig_account, token, api_mode = resolve_credentials(env)
        if not dry_run and (not ig_account or not token):
            print("ERRORE: manca token Instagram")
            code = 1
        else:
            img_file = story_image_file(article, slot)
            story_url = IG_STORY_BASE + img_file
            print(f"\n=== INSTAGRAM STORY ({api_mode}) ===\n{story_url}")
            video_path = None
            if not dry_run:
                video_path, track = prepare_story_video("instagram", img_file, slot, 0, 20)
                track_title = track_title or track["title"]
                print(f"MUSICA: {track['title']} — {track['artist']}")
                print(f"VIDEO: {video_path}")
            result = publish_instagram_story(
                ig_account, story_url, token, dry_run,
                video_path=video_path, use_video=True,
            )
            print("RISULTATO IG:", json.dumps(result, indent=2))
            if result.get("error"):
                if is_quota_error(result):
                    entry = enqueue_story(article["slug"], slot=slot, reason="quota_limit", note="Accodato da post-story-only.py")
                    print("\n⏳ Instagram in coda (limite API).")
                    print(f"   Coda: {entry['slug']} slot {entry['slot']}")
                code = 1
            else:
                ig_id = str(result.get("id") or result.get("creation_id") or "")

    if not dry_run and not code:
        schedule = load_schedule()
        tz_name = schedule.get("timezone", "Europe/Rome")
        record_story(
            schedule,
            date_str=today_in_timezone(tz_name).isoformat(),
            slot=slot,
            slug=article["slug"],
            fb_id=fb_id,
            ig_id=ig_id,
            track=track_title,
        )
        save_schedule(schedule)

    return code


def main() -> int:
    parser = argparse.ArgumentParser(description="Pubblica Story FB/IG (no link)")
    parser.add_argument("--slug", help="Slug articolo (opzionale con --auto)")
    parser.add_argument("--slot", type=int, default=0)
    parser.add_argument("--auto", action="store_true", help="Piano giornaliero 20 story")
    parser.add_argument("--now", action="store_true", help="Rileva slot dall'orario Roma")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-facebook", action="store_true")
    parser.add_argument("--skip-instagram", action="store_true")
    parser.add_argument("--process-queue", action="store_true", help="Pubblica story IG in coda")
    args = parser.parse_args()

    if args.process_queue:
        report = process_queue(dry_run=args.dry_run)
        print(json.dumps(report, indent=2))
        return 0 if report.get("published") or report.get("message") else 1

    schedule = load_schedule()
    per_day = int(schedule.get("storiesPerDay") or STORIES_PER_DAY)

    if args.auto and args.now:
        detected = current_slot_index(per_day, schedule.get("timezone", "Europe/Rome"))
        if detected is None:
            print(f"Nessuno slot story attivo ora. Orari: {', '.join(generate_slot_times(per_day))}")
            return 0
        args.slot = detected
        print(f"Slot rilevato: {detected} — {slot_label(detected, per_day)}")

    if args.auto:
        data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
        env = load_env()
        article, _day_idx, _today = get_auto_article(data["articles"], schedule, args.slot, env)
        if not article:
            return 0
        slug = article["slug"]
    elif args.slug:
        slug = args.slug
        article = load_article(slug)
    else:
        parser.error("Specifica --slug oppure --auto")

    if args.auto and not args.slug:
        article = load_article(slug)

    code = publish_stories(
        article,
        slot=args.slot,
        dry_run=args.dry_run,
        skip_facebook=args.skip_facebook,
        skip_instagram=args.skip_instagram,
    )

    if not args.dry_run and not args.skip_instagram:
        process_queue(max_items=1)

    return code


if __name__ == "__main__":
    raise SystemExit(main())
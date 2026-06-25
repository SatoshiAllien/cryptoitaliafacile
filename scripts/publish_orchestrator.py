#!/usr/bin/env python3
"""Orchestratore unificato auto-post Instagram + Facebook."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import time
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from meta_errors import error_summary, is_permission_error, is_quota_error, is_retryable, is_token_error
from publish_log import append_log
from queue_store import (
    circuit_is_open,
    count_published_on_date,
    due_items,
    item_by_id,
    last_published_at,
    load_queue,
    mark_status,
    record_failure,
    recover_stale_publishing,
    requeue_failed,
    reset_circuit,
    save_queue,
)
from social_post_config import load_config, stories_enabled

ENV_PATH = SCRIPTS / ".env"
ARTICLES_PATH = ROOT / "data" / "articles.json"
IG_SCHEDULE = ROOT / "data" / "instagram-schedule.json"
FB_SCHEDULE = ROOT / "data" / "facebook-schedule.json"


def _load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod


_post_ig = _load_module("post_to_instagram", "post-to-instagram.py")
_post_fb = _load_module("post_to_facebook", "post-to-facebook.py")

from chill_cyber_playlist import track_for_slot  # noqa: E402
from feed_post_content import build_caption as build_feed_caption  # noqa: E402
from instagram_auth import resolve_credentials  # noqa: E402
from story_publish import publish_facebook_story, publish_instagram_story  # noqa: E402
from story_video import prepare_story_video  # noqa: E402


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                env[key.strip()] = value.strip().strip('"').strip("'")
    for key, value in os.environ.items():
        if key.startswith(("INSTAGRAM_", "FACEBOOK_")):
            env[key] = value
    return env


def now_tz(tz_name: str) -> datetime:
    if ZoneInfo is None:
        return datetime.now()
    return datetime.now(ZoneInfo(tz_name))


def in_posting_window(now: datetime, start_h: int, end_h: int) -> bool:
    return start_h <= now.hour <= end_h


def article_by_slug(slug: str) -> dict | None:
    data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
    return next((a for a in data["articles"] if a["slug"] == slug), None)


def image_url_reachable(url: str) -> bool:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "CryptoFacile/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return 200 <= resp.status < 400
    except Exception:
        return False


def validate_item(item: dict, article: dict, config: dict) -> list[str]:
    errors: list[str] = []
    caption = build_feed_caption(article, variant=item.get("variant", "primary"), lang="it")
    if len(caption) > 2200:
        errors.append("caption_too_long")
    platform = item["platform"]
    if platform == "instagram":
        url = _post_ig.instagram_image_url(article, variant=item.get("variant", "primary"))
    else:
        url = _post_fb.facebook_image_url(article, variant=item.get("variant", "primary"))
    if not image_url_reachable(url):
        errors.append(f"image_unreachable:{url}")
    return errors


def sync_legacy_schedule(item: dict, external_id: str, story_id: str = "", story_track: str = "") -> None:
    platform = item["platform"]
    path = IG_SCHEDULE if platform == "instagram" else FB_SCHEDULE
    default = {
        "startDate": date.today().isoformat(),
        "postsPerDay": 20,
        "timezone": "Europe/Rome",
        "posted": [],
    }
    if path.exists():
        schedule = json.loads(path.read_text(encoding="utf-8"))
        schedule = {**default, **schedule}
    else:
        schedule = default

    exists = any(
        p.get("date") == item["date"] and p.get("slot") == item["slot"]
        for p in schedule.get("posted", [])
    )
    if exists:
        return

    entry = {
        "date": item["date"],
        "slot": item["slot"],
        "slug": item["slug"],
        "publishedAt": item.get("published_at"),
    }
    if platform == "instagram":
        entry["mediaId"] = external_id
    else:
        entry["postId"] = external_id
    if story_id:
        entry["storyId"] = story_id
    if story_track:
        entry["storyTrack"] = story_track
    schedule.setdefault("posted", []).append(entry)
    path.write_text(json.dumps(schedule, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def publish_feed(item: dict, article: dict, env: dict, dry_run: bool) -> dict:
    platform = item["platform"]
    variant = item.get("variant", "primary")
    caption = build_feed_caption(article, variant=variant, lang="it")

    if platform == "instagram":
        ig_id, token, _ = resolve_credentials(env)
        image_url = _post_ig.instagram_image_url(article, variant=variant)
        return _post_ig.post_to_instagram(caption, image_url, ig_id, token, dry_run)

    page_id = env.get("FACEBOOK_PAGE_ID", "")
    token = env.get("FACEBOOK_PAGE_ACCESS_TOKEN", "")
    image_url = _post_fb.facebook_image_url(article, variant=variant)
    link = _post_fb.article_url(article["slug"])
    return _post_fb.post_to_facebook(caption, link, image_url, page_id, token, dry_run)


def publish_story(item: dict, article: dict, env: dict, dry_run: bool, config: dict) -> dict:
    if not stories_enabled() and not config.get("auto_post", {}).get("publish_story_with_feed", True):
        return {"skipped": True}
    if not config.get("auto_post", {}).get("publish_story_with_feed", True):
        return {"skipped": True}

    platform = item["platform"]
    slot = int(item.get("slot", 0))
    day_idx = max(0, (date.fromisoformat(item["date"]) - date.fromisoformat(config.get("schedule", {}).get("startDate", item["date"]))).days)

    try:
        if platform == "instagram":
            ig_id, token, _ = resolve_credentials(env)
            story_url = _post_ig.instagram_story_image_url(article, slot)
            story_video_path = None
            if not dry_run:
                story_video_path, track = prepare_story_video(
                    "instagram",
                    _post_ig.instagram_story_image_file(article, slot),
                    slot,
                    day_idx,
                    int(config.get("auto_post", {}).get("max_posts_per_day", 20)),
                )
            else:
                track = track_for_slot(slot, day_idx, 20)
            result = publish_instagram_story(
                ig_id,
                story_url,
                token,
                dry_run,
                video_path=story_video_path,
                use_video=True,
            )
            if result.get("error"):
                return result
            return {"id": result.get("id"), "track": track.get("title", "")}

        page_id = env.get("FACEBOOK_PAGE_ID", "")
        token = env.get("FACEBOOK_PAGE_ACCESS_TOKEN", "")
        story_url = _post_fb.facebook_story_image_url(article, slot)
        story_video_path = None
        if not dry_run:
            story_video_path, track = prepare_story_video(
                "facebook",
                _post_fb.facebook_story_image_file(article, slot),
                slot,
                day_idx,
                int(config.get("auto_post", {}).get("max_posts_per_day", 20)),
            )
        else:
            track = track_for_slot(slot, day_idx, 20)
        result = publish_facebook_story(page_id, story_url, token, dry_run, video_path=story_video_path)
        if result.get("error"):
            return result
        return {"id": result.get("id"), "track": track.get("title", "")}
    except Exception as exc:
        return {"error": {"message": str(exc)}}


def process_item(item: dict, queue: dict, config: dict, env: dict, dry_run: bool) -> bool:
    auto = config.get("auto_post", {})
    retry_cfg = auto.get("retry", {})
    max_attempts = int(retry_cfg.get("max_attempts", 3))
    backoff = list(retry_cfg.get("backoff_seconds", [30, 120, 600]))

    article = article_by_slug(item["slug"])
    if not article:
        mark_status(item, "failed", error=f"article_not_found:{item['slug']}")
        record_failure(queue, config)
        append_log({
            "queue_id": item["id"],
            "platform": item["platform"],
            "slug": item["slug"],
            "status": "failed",
            "error": "article_not_found",
        })
        return False

    validation_errors = validate_item(item, article, config)
    if validation_errors:
        mark_status(item, "failed", error=";".join(validation_errors))
        record_failure(queue, config)
        append_log({
            "queue_id": item["id"],
            "platform": item["platform"],
            "slug": item["slug"],
            "status": "failed",
            "error": validation_errors,
        })
        return False

    if not dry_run:
        mark_status(item, "publishing", publishing_since=now_tz(queue.get("timezone", "Europe/Rome")).isoformat())
        save_queue(queue)

    try:
        return _process_item_attempts(
            item, queue, config, env, dry_run, article, max_attempts, backoff, auto,
        )
    except Exception as exc:
        summary = f"unexpected_error:{exc}"
        mark_status(item, "failed", error=summary)
        item.pop("publishing_since", None)
        record_failure(queue, config)
        append_log({
            "queue_id": item["id"],
            "platform": item["platform"],
            "slug": item["slug"],
            "status": "failed",
            "error": summary,
        })
        if not dry_run:
            save_queue(queue)
        return False


def _process_item_attempts(
    item: dict,
    queue: dict,
    config: dict,
    env: dict,
    dry_run: bool,
    article: dict,
    max_attempts: int,
    backoff: list,
    auto: dict,
) -> bool:
    for attempt in range(1, max_attempts + 1):
        item["attempts"] = attempt
        started = time.time()
        result = publish_feed(item, article, env, dry_run)
        duration_ms = int((time.time() - started) * 1000)

        if result.get("error"):
            err = result["error"]
            summary = error_summary(result)
            append_log({
                "queue_id": item["id"],
                "platform": item["platform"],
                "slug": item["slug"],
                "attempt": attempt,
                "status": "error",
                "error": summary,
                "duration_ms": duration_ms,
            })

            if is_token_error(result) or is_permission_error(result):
                mark_status(item, "failed", error=summary)
                item.pop("publishing_since", None)
                record_failure(queue, config)
                if auto.get("safety", {}).get("stop_on_token_error", True):
                    queue["circuit_breaker"]["open"] = True
                    queue["circuit_breaker"]["opened_at"] = now_tz(queue.get("timezone", "Europe/Rome")).isoformat()
                return False

            if is_quota_error(result) and attempt < max_attempts:
                wait = int(auto.get("quota_wait_seconds", 3600))
                print(f"Quota API — attendo {wait // 60} min...")
                if not dry_run:
                    time.sleep(min(wait, 300))
                continue

            if is_retryable(result) and attempt < max_attempts:
                wait = backoff[min(attempt - 1, len(backoff) - 1)]
                print(f"Retry {attempt}/{max_attempts} tra {wait}s — {summary}")
                if not dry_run:
                    time.sleep(wait)
                continue

            mark_status(item, "failed", error=summary)
            item.pop("publishing_since", None)
            record_failure(queue, config)
            return False

        external_id = str(result.get("id") or result.get("post_id") or "")
        story_id = ""
        story_track = ""
        story_result = publish_story(item, article, env, dry_run, config)
        if story_result.get("error"):
            item["story_status"] = "failed"
            append_log({
                "queue_id": item["id"],
                "platform": item["platform"],
                "slug": item["slug"],
                "status": "story_failed",
                "error": error_summary(story_result),
            })
        elif story_result.get("skipped"):
            item["story_status"] = "skipped"
        else:
            item["story_status"] = "published"
            story_id = str(story_result.get("id") or "")
            story_track = str(story_result.get("track") or "")

        if dry_run:
            print(f"[DRY RUN] OK — non salvato in coda")
            append_log({
                "queue_id": item["id"],
                "platform": item["platform"],
                "slug": item["slug"],
                "attempt": attempt,
                "status": "dry_run_ok",
                "external_id": external_id,
                "duration_ms": duration_ms,
            })
            return True

        published_at = now_tz(queue.get("timezone", "Europe/Rome")).isoformat()
        mark_status(
            item,
            "published",
            feed_status="published",
            external_id=external_id,
            story_id=story_id or None,
            published_at=published_at,
            error=None,
        )
        item.pop("publishing_since", None)
        sync_legacy_schedule(item, external_id, story_id, story_track)

        append_log({
            "queue_id": item["id"],
            "platform": item["platform"],
            "slug": item["slug"],
            "attempt": attempt,
            "status": "published",
            "external_id": external_id,
            "story_id": story_id,
            "duration_ms": duration_ms,
        })
        reset_circuit(queue)
        return True

    mark_status(item, "failed", error="max_retries_exceeded")
    item.pop("publishing_since", None)
    record_failure(queue, config)
    return False


def print_status(queue: dict, config: dict) -> None:
    recovered = recover_stale_publishing(queue)
    if recovered:
        save_queue(queue)
        print(f"Recuperati {recovered} post bloccati in 'publishing'")
    items = queue.get("items", [])
    counts: dict[str, int] = {}
    for item in items:
        status = item.get("status", "pending")
        counts[status] = counts.get(status, 0) + 1
    print("=== Publish Queue Status ===")
    print(f"Timezone: {queue.get('timezone')}")
    print(f"Start: {queue.get('startDate')}")
    for status, count in sorted(counts.items()):
        print(f"  {status}: {count}")
    breaker = queue.get("circuit_breaker", {})
    if breaker.get("open"):
        print(f"Circuit breaker: OPEN since {breaker.get('opened_at')}")
    else:
        print("Circuit breaker: closed")


def run_auto(config: dict, *, dry_run: bool = False, limit: int = 1) -> int:
    auto = config.setdefault("auto_post", {})
    if not auto.get("enabled", True):
        print("Auto-post disabilitato in social-post-config.json")
        return 0

    if dry_run:
        print("[DRY RUN] Nessuna pubblicazione reale")

    queue = load_queue()
    tz_name = queue.get("timezone", "Europe/Rome")
    now = now_tz(tz_name)

    recovered = recover_stale_publishing(queue, now=now)
    if recovered:
        print(f"Recuperati {recovered} post bloccati in 'publishing'")
        if not dry_run:
            save_queue(queue)

    if not dry_run and circuit_is_open(queue):
        print("Circuit breaker aperto — pubblicazione sospesa.")
        print("Usa: python publish_orchestrator.py --reset-circuit")
        return 1
    if dry_run and circuit_is_open(queue):
        print("Circuit breaker aperto — dry-run continua (nessuna pubblicazione reale)")

    schedule = config.get("schedule", {})
    start_h = int(schedule.get("start_hour", 7))
    end_h = int(schedule.get("end_hour", 22))
    if not in_posting_window(now, start_h, end_h):
        print(f"Fuori finestra oraria ({start_h}:00–{end_h}:00 {tz_name})")
        return 0

    max_per_day = int(auto.get("max_posts_per_day", 20))
    min_interval = int(auto.get("min_interval_minutes", 30))
    platforms = list(auto.get("platforms") or ["instagram", "facebook"])
    today_str = now.date().isoformat()

    published_today = count_published_on_date(queue, today_str)
    if published_today >= max_per_day * len(platforms):
        print(f"Limite giornaliero raggiunto ({published_today} pubblicazioni)")
        return 0

    last_pub = last_published_at(queue)
    if last_pub and now - last_pub < timedelta(minutes=min_interval):
        print(f"Intervallo minimo {min_interval} min non ancora trascorso")
        return 0

    env = load_env()
    due = due_items(queue, now=now, platforms=platforms, limit=limit)
    if not due:
        print("Nessun post in scadenza nella coda")
        return 0

    ok = 0
    fail = 0
    for item in due:
        if not dry_run and circuit_is_open(queue):
            print("Circuit breaker aperto — interrompo batch")
            break
        print(f"\n→ {item['id']} | @{item['platform']} | {item['slug']} | slot {item['slot']}")
        if process_item(item, queue, config, env, dry_run):
            ok += 1
        else:
            fail += 1
        if not dry_run:
            save_queue(queue)
        if not dry_run and circuit_is_open(queue):
            print("Circuit breaker aperto dopo errore token/permessi")
            break

    print(f"\nCompletato: {ok} ok, {fail} errori")
    return 0 if fail == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Orchestratore auto-post social")
    parser.add_argument("--auto", action="store_true", help="Pubblica prossimo post in scadenza")
    parser.add_argument("--dry-run", action="store_true", help="Simula senza pubblicare")
    parser.add_argument("--status", action="store_true", help="Mostra stato coda")
    parser.add_argument("--generate", action="store_true", help="Genera/aggiorna publish-queue.json")
    parser.add_argument("--days", type=int, default=14, help="Giorni da generare con --generate")
    parser.add_argument("--requeue", metavar="ID", help="Rimetti in coda un post failed")
    parser.add_argument("--reset-circuit", action="store_true", help="Chiudi circuit breaker")
    parser.add_argument("--limit", type=int, default=1, help="Max post per esecuzione")
    parser.add_argument("--slug", help="Pubblica subito uno slug su tutte le piattaforme")
    parser.add_argument("--platform", choices=["instagram", "facebook"], help="Con --slug, solo una piattaforma")
    args = parser.parse_args()

    config = load_config()

    if args.generate:
        from generate_publish_queue import main as gen_main

        sys.argv = ["generate_publish_queue.py", "--days", str(args.days)]
        return gen_main()

    queue = load_queue()

    if args.reset_circuit:
        reset_circuit(queue)
        save_queue(queue)
        print("Circuit breaker resettato")
        return 0

    if args.requeue:
        if requeue_failed(queue, args.requeue):
            save_queue(queue)
            print(f"Requeued: {args.requeue}")
            return 0
        print(f"Non trovato o non in failed: {args.requeue}")
        return 1

    if args.status:
        print_status(queue, config)
        return 0

    if args.slug:
        platforms = [args.platform] if args.platform else list(
            config.get("auto_post", {}).get("platforms") or ["instagram", "facebook"]
        )
        env = load_env()
        article = article_by_slug(args.slug)
        if not article:
            print(f"Articolo non trovato: {args.slug}")
            return 1
        today = date.today().isoformat()
        for platform in platforms:
            item = {
                "id": f"{platform}:{today}:manual",
                "platform": platform,
                "slug": args.slug,
                "slot": 0,
                "date": today,
                "variant": "primary",
                "status": "pending",
            }
            process_item(item, queue, config, env, args.dry_run)
        save_queue(queue)
        return 0

    if args.auto:
        return run_auto(config, dry_run=args.dry_run, limit=args.limit)

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
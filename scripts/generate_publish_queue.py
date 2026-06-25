#!/usr/bin/env python3
"""Genera la coda unificata publish-queue.json da articles.json + piano giornaliero."""

from __future__ import annotations

import argparse
import json
import sys
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

from daily_post_queue import POSTS_PER_DAY, daily_plan, variant_for_slot
from queue_store import QUEUE_PATH, load_queue, save_queue
from social_post_config import load_config

ARTICLES_PATH = ROOT / "data" / "articles.json"


def generate_slot_times(per_day: int, start_h: int, end_h: int) -> list[str]:
    start_m = start_h * 60
    end_m = end_h * 60
    times: list[str] = []
    for i in range(per_day):
        if per_day == 1:
            mins = start_m
        else:
            mins = round(start_m + (end_m - start_m) * i / max(per_day - 1, 1))
        times.append(f"{mins // 60:02d}:{mins % 60:02d}")
    return times


def scheduled_iso(day: date, hhmm: str, tz_name: str) -> str:
    hour, minute = map(int, hhmm.split(":"))
    if ZoneInfo is None:
        return datetime(day.year, day.month, day.day, hour, minute).isoformat()
    return datetime(day.year, day.month, day.day, hour, minute, tzinfo=ZoneInfo(tz_name)).isoformat()


def build_items(
    *,
    days: int,
    start_date: date,
    platforms: list[str],
    per_day: int,
    start_hour: int,
    end_hour: int,
    tz_name: str,
    articles: list[dict],
) -> list[dict]:
    plan = daily_plan(articles)
    if not plan:
        return []

    slot_times = generate_slot_times(per_day, start_hour, end_hour)
    items: list[dict] = []
    for day_offset in range(days):
        current = start_date + timedelta(days=day_offset)
        day_str = current.isoformat()
        day_idx = day_offset
        day_posts = plan[day_idx % len(plan)]

        for slot in range(min(per_day, len(day_posts))):
            article = day_posts[slot]
            slug = article["slug"]
            variant = variant_for_slot(slot, day_idx)
            scheduled = scheduled_iso(current, slot_times[slot], tz_name)

            for platform in platforms:
                item_id = f"{platform}:{day_str}:slot-{slot:02d}"
                items.append(
                    {
                        "id": item_id,
                        "idempotency_key": f"{platform}:{day_str}:{slot}",
                        "platform": platform,
                        "post_type": "feed",
                        "date": day_str,
                        "slot": slot,
                        "scheduled_at": scheduled,
                        "slug": slug,
                        "variant": variant,
                        "status": "pending",
                        "feed_status": "pending",
                        "story_status": "pending",
                        "attempts": 0,
                        "external_id": None,
                        "story_id": None,
                        "error": None,
                    }
                )
    return items


def merge_preserve_published(existing: dict, fresh_items: list[dict]) -> list[dict]:
    published = {
        item.get("idempotency_key"): item
        for item in existing.get("items", [])
        if item.get("status") == "published"
    }
    merged: list[dict] = []
    for item in fresh_items:
        key = item["idempotency_key"]
        if key in published:
            merged.append(published[key])
        else:
            old = next(
                (x for x in existing.get("items", []) if x.get("idempotency_key") == key),
                None,
            )
            if old and old.get("status") in ("failed", "publishing"):
                merged.append(old)
            else:
                merged.append(item)
    return merged


def main() -> int:
    parser = argparse.ArgumentParser(description="Genera publish-queue.json")
    parser.add_argument("--days", type=int, default=14, help="Giorni da precompilare")
    parser.add_argument("--force", action="store_true", help="Rigenera tutto (mantiene published)")
    args = parser.parse_args()

    cfg = load_config()
    auto = cfg.get("auto_post", {})
    schedule = cfg.get("schedule", {})
    tz_name = schedule.get("timezone", "Europe/Rome")
    per_day = int(auto.get("max_posts_per_day") or schedule.get("slots") or POSTS_PER_DAY)
    start_hour = int(schedule.get("start_hour", 7))
    end_hour = int(schedule.get("end_hour", 22))
    platforms = list(auto.get("platforms") or cfg.get("platforms") or ["instagram", "facebook"])

    articles = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))["articles"]
    existing = load_queue()
    start_date = date.fromisoformat(existing.get("startDate") or date.today().isoformat())

    fresh = build_items(
        days=args.days,
        start_date=start_date,
        platforms=platforms,
        per_day=per_day,
        start_hour=start_hour,
        end_hour=end_hour,
        tz_name=tz_name,
        articles=articles,
    )

    if args.force or not existing.get("items"):
        items = merge_preserve_published(existing, fresh)
    else:
        items = merge_preserve_published(existing, fresh)

    payload = {
        "version": 1,
        "timezone": tz_name,
        "startDate": start_date.isoformat(),
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "items": items,
        "circuit_breaker": existing.get("circuit_breaker") or {
            "open": False,
            "errors_in_window": 0,
            "window_start": None,
            "opened_at": None,
        },
    }
    save_queue(payload)
    pending = sum(1 for i in items if i.get("status") == "pending")
    published = sum(1 for i in items if i.get("status") == "published")
    print(f"Saved {QUEUE_PATH}")
    print(f"Items: {len(items)} | pending: {pending} | published: {published}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
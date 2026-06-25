#!/usr/bin/env python3
"""Coda unificata pubblicazione social (Instagram + Facebook)."""

from __future__ import annotations

import json
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "data" / "publish-queue.json"

STATUSES = {"pending", "publishing", "published", "failed", "skipped"}


def load_queue() -> dict:
    default = {
        "version": 1,
        "timezone": "Europe/Rome",
        "startDate": date.today().isoformat(),
        "items": [],
        "circuit_breaker": {
            "open": False,
            "errors_in_window": 0,
            "window_start": None,
            "opened_at": None,
        },
    }
    if not QUEUE_PATH.exists():
        return default
    data = json.loads(QUEUE_PATH.read_text(encoding="utf-8"))
    return {**default, **data, "items": list(data.get("items") or [])}


def save_queue(data: dict) -> None:
    QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUEUE_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def parse_dt(value: str, tz_name: str) -> datetime:
    if ZoneInfo is None:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=ZoneInfo(tz_name))
        return dt
    except ValueError:
        return datetime.now(ZoneInfo(tz_name))


def item_by_id(data: dict, item_id: str) -> dict | None:
    return next((item for item in data.get("items", []) if item.get("id") == item_id), None)


def due_items(
    data: dict,
    *,
    now: datetime | None = None,
    platforms: list[str] | None = None,
    limit: int = 1,
) -> list[dict]:
    tz_name = data.get("timezone", "Europe/Rome")
    if now is None:
        now = datetime.now(ZoneInfo(tz_name) if ZoneInfo else timezone.utc)
    allowed = set(platforms or [])
    due: list[dict] = []
    for item in data.get("items", []):
        if item.get("status") != "pending":
            continue
        if allowed and item.get("platform") not in allowed:
            continue
        scheduled = item.get("scheduled_at")
        if not scheduled:
            continue
        if parse_dt(scheduled, tz_name) <= now:
            due.append(item)
    due.sort(key=lambda x: x.get("scheduled_at", ""))
    return due[:limit]


def count_published_on_date(data: dict, day: str, platform: str | None = None) -> int:
    count = 0
    for item in data.get("items", []):
        if item.get("date") != day:
            continue
        if platform and item.get("platform") != platform:
            continue
        if item.get("status") == "published":
            count += 1
    return count


def last_published_at(data: dict, platform: str | None = None) -> datetime | None:
    tz_name = data.get("timezone", "Europe/Rome")
    latest: datetime | None = None
    for item in data.get("items", []):
        if item.get("status") != "published":
            continue
        if platform and item.get("platform") != platform:
            continue
        stamp = item.get("published_at")
        if not stamp:
            continue
        dt = parse_dt(stamp, tz_name)
        if latest is None or dt > latest:
            latest = dt
    return latest


def mark_status(item: dict, status: str, **extra) -> None:
    if status not in STATUSES:
        raise ValueError(f"Invalid status: {status}")
    item["status"] = status
    item.update(extra)


def record_failure(data: dict, config: dict) -> None:
    breaker = data.setdefault("circuit_breaker", {})
    safety = config.get("auto_post", {}).get("safety", {})
    if not safety.get("enabled", True):
        return

    window_minutes = 60
    max_errors = int(safety.get("max_errors_per_hour", 5))
    tz_name = data.get("timezone", "Europe/Rome")
    now = datetime.now(ZoneInfo(tz_name) if ZoneInfo else timezone.utc)

    window_start = breaker.get("window_start")
    if not window_start:
        breaker["window_start"] = now.isoformat()
        breaker["errors_in_window"] = 1
    else:
        start_dt = parse_dt(window_start, tz_name)
        if now - start_dt > timedelta(minutes=window_minutes):
            breaker["window_start"] = now.isoformat()
            breaker["errors_in_window"] = 1
        else:
            breaker["errors_in_window"] = int(breaker.get("errors_in_window", 0)) + 1

    if breaker["errors_in_window"] >= max_errors:
        breaker["open"] = True
        breaker["opened_at"] = now.isoformat()


def reset_circuit(data: dict) -> None:
    data["circuit_breaker"] = {
        "open": False,
        "errors_in_window": 0,
        "window_start": None,
        "opened_at": None,
    }


def circuit_is_open(data: dict) -> bool:
    return bool((data.get("circuit_breaker") or {}).get("open"))


def requeue_failed(data: dict, item_id: str) -> bool:
    item = item_by_id(data, item_id)
    if not item or item.get("status") != "failed":
        return False
    item["status"] = "pending"
    item["attempts"] = 0
    item.pop("error", None)
    item.pop("published_at", None)
    item.pop("external_id", None)
    return True
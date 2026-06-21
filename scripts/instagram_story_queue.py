"""Coda story Instagram in attesa (limite API) + pubblicazione."""

from __future__ import annotations

import json
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

from instagram_auth import resolve_credentials
from story_links import SATOSHI_AI_STORY_LINK
from story_publish import publish_instagram_story
from story_video import prepare_story_video, story_image_file

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_PATH = ROOT / "data" / "articles.json"
QUEUE_PATH = ROOT / "data" / "instagram-story-queue.json"
ENV_PATH = Path(__file__).resolve().parent / ".env"
HOME_LINK = SATOSHI_AI_STORY_LINK
IG_STORY_BASE = f"{SITE_URL}assets/img/instagram/stories/"


def is_quota_error(result: dict) -> bool:
    err = result.get("error") or {}
    if err.get("code") == 9 and err.get("error_subcode") == 2207042:
        return True
    msg = str(err.get("message", "")).lower()
    return "too many actions" in msg or "maximum number of post" in msg


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def load_articles() -> list[dict]:
    return json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))["articles"]


def article_by_slug(slug: str) -> dict | None:
    return next((a for a in load_articles() if a["slug"] == slug), None)


def article_link(slug: str) -> str:
    return SATOSHI_AI_STORY_LINK


def load_queue() -> dict:
    if not QUEUE_PATH.exists():
        return {"pending": [], "completed": []}
    try:
        return json.loads(QUEUE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"pending": [], "completed": []}


def save_queue(data: dict) -> None:
    QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUEUE_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def enqueue_story(
    slug: str,
    *,
    slot: int = 0,
    link_url: str | None = None,
    reason: str = "manual",
    note: str = "",
) -> dict:
    article = article_by_slug(slug)
    if not article:
        raise ValueError(f"Articolo non trovato: {slug}")

    data = load_queue()
    pending = data.setdefault("pending", [])
    for item in pending:
        if item.get("slug") == slug and item.get("slot", 0) == slot:
            return item

    entry = {
        "slug": slug,
        "title": article["title"],
        "slot": slot,
        "link_url": link_url or HOME_LINK,
        "reason": reason,
        "note": note,
        "enqueued_at": datetime.now(timezone.utc).isoformat(),
        "attempts": 0,
    }
    pending.append(entry)
    save_queue(data)
    return entry


def publish_instagram_queued_item(item: dict, *, dry_run: bool = False) -> dict:
    article = article_by_slug(item["slug"])
    if not article:
        return {"error": {"message": f"Articolo non trovato: {item['slug']}"}}

    slot = int(item.get("slot", 0))
    link_url = item.get("link_url") or HOME_LINK
    env = load_env()
    ig_id, token, api_mode = resolve_credentials(env)

    if not dry_run and (not ig_id or not token):
        return {"error": {"message": "Credenziali Instagram mancanti in scripts/.env"}}

    img_file = story_image_file(article, slot)
    story_url = IG_STORY_BASE + img_file
    video_path = None

    if not dry_run:
        video_path, track = prepare_story_video(
            "instagram", img_file, slot, 0, 20, link_url=link_url
        )
        print(f"MUSICA: {track['title']} — {track['artist']}")
        print(f"VIDEO: {video_path}")

    result = publish_instagram_story(
        ig_id,
        story_url,
        token,
        dry_run=dry_run,
        video_path=video_path,
        use_video=True,
        link_url=link_url,
    )
    result["_meta"] = {
        "api_mode": api_mode,
        "story_url": story_url,
        "link_url": link_url,
        "slug": item["slug"],
        "slot": slot,
    }
    return result


def process_queue(*, dry_run: bool = False, max_items: int = 3) -> dict:
    data = load_queue()
    pending: list[dict] = list(data.get("pending", []))
    completed: list[dict] = data.setdefault("completed", [])

    report: dict = {
        "processed": 0,
        "published": 0,
        "quota_blocked": False,
        "errors": [],
        "successes": [],
    }

    if not pending:
        report["message"] = "Nessuna story in coda"
        return report

    still_pending: list[dict] = []
    quota_blocked = False
    attempted = 0

    for item in pending:
        if quota_blocked or attempted >= max_items:
            still_pending.append(item)
            continue

        slug = item.get("slug", "?")
        print(f"\n→ Story in coda: {item.get('title', slug)} (slot {item.get('slot', 0)})")
        print(f"  Link: {item.get('link_url', HOME_LINK)}")

        result = publish_instagram_queued_item(item, dry_run=dry_run)
        attempted += 1
        report["processed"] += 1
        item["attempts"] = int(item.get("attempts", 0)) + 1
        item["last_attempt_at"] = datetime.now(timezone.utc).isoformat()

        if dry_run and result.get("dry_run"):
            report["published"] += 1
            report["successes"].append({"slug": slug, "dry_run": True})
            if not dry_run:
                completed.append({**item, "published_at": item["last_attempt_at"], "result": result})
            continue

        if result.get("error"):
            err = result["error"]
            print(f"  ✗ Errore: {err}")
            report["errors"].append({"slug": slug, "error": err})
            item["last_error"] = err
            still_pending.append(item)
            if is_quota_error(result):
                report["quota_blocked"] = True
                quota_blocked = True
            continue

        media_id = result.get("id") or result.get("creation_id")
        print(f"  ✓ Story pubblicata: {media_id}")
        report["published"] += 1
        report["successes"].append({"slug": slug, "media_id": media_id})
        completed.append({
            **item,
            "published_at": datetime.now(timezone.utc).isoformat(),
            "media_id": str(media_id or ""),
            "result": {k: v for k, v in result.items() if k != "_meta"},
        })

    if not dry_run:
        data["pending"] = still_pending
        data["completed"] = completed[-100:]
        save_queue(data)

    return report
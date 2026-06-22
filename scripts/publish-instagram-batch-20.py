#!/usr/bin/env python3
"""Pubblica batch 20 post feed Instagram (senza Story) con delay, resume e anti-quota.

Non interrompe finché tutti i 20 non sono completati (o in coda quota).
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import importlib.util


def _load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod


_post_ig = _load_module("post_to_instagram", "post-to-instagram.py")
post_to_instagram = _post_ig.post_to_instagram

from instagram_auth import resolve_credentials  # noqa: E402
from instagram_batch_20_content import BATCH_20, HOME_LINK, build_caption_it  # noqa: E402
from instagram_batch_20_lib import SITE_BASE, load_state, save_state  # noqa: E402
from instagram_story_queue import is_quota_error  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DELAY_SECONDS = 120
QUOTA_WAIT_SECONDS = 3600
MAX_QUOTA_RETRIES = 6


def feed_image_url(slug: str) -> str:
    return SITE_BASE + f"{slug}-feed-it.jpg"


def publish_one(item: dict, *, slot: int, ig_id: str, token: str, dry_run: bool) -> dict:
    slug = item["slug"]
    caption = build_caption_it(item)
    feed_url = feed_image_url(slug)

    print(f"\n{'='*60}")
    print(f"#{item['id']} {item['hook_it'].replace(chr(10), ' ')}")
    print(f"FEED: {feed_url}")
    print(f"LINK: {HOME_LINK}")

    feed_result = post_to_instagram(caption, feed_url, ig_id, token, dry_run)
    if feed_result.get("error"):
        return {"ok": False, "stage": "feed", "error": feed_result["error"], "slug": slug}

    feed_id = feed_result.get("id") or feed_result.get("dry_run")
    return {
        "ok": True,
        "slug": slug,
        "feed_id": str(feed_id or ""),
    }


def run_batch(*, dry_run: bool = False, start_from: int = 1, delay: int = DELAY_SECONDS) -> int:
    env = {}
    env_path = SCRIPTS / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.strip().startswith("#"):
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"')

    import os
    for k, v in os.environ.items():
        if k.startswith("INSTAGRAM_") or k.startswith("FACEBOOK_"):
            env[k] = v

    ig_id, token, api_mode = resolve_credentials(env)
    if not dry_run and (not ig_id or not token):
        print("ERRORE: credenziali Instagram mancanti (INSTAGRAM_ACCESS_TOKEN o Page token)")
        return 1

    state = load_state()
    done_slugs = {p["slug"] for p in state.get("published", [])}
    pending = [x for x in BATCH_20 if x["id"] >= start_from and x["slug"] not in done_slugs]

    if not pending:
        print(f"✅ Tutti i 20 contenuti già pubblicati ({len(done_slugs)} in stato).")
        return 0

    print(f"API: {api_mode} | Da pubblicare: {len(pending)} | Delay: {delay}s")
    print(f"Link obbligatorio: {HOME_LINK}")

    quota_retries = 0
    for item in pending:
        slot = (item["id"] - 1) % 20
        attempt = 0
        while attempt < 3:
            attempt += 1
            result = publish_one(item, slot=slot, ig_id=ig_id, token=token, dry_run=dry_run)
            if result.get("ok"):
                entry = {
                    "id": item["id"],
                    "slug": item["slug"],
                    "feed_id": result.get("feed_id"),
                    "story_id": result.get("story_id"),
                    "published_at": datetime.now(timezone.utc).isoformat(),
                    "link": HOME_LINK,
                }
                state.setdefault("published", []).append(entry)
                state["last_id"] = item["id"]
                save_state(state)
                print(f"✓ #{item['id']} completato (feed {result.get('feed_id')})")
                quota_retries = 0
                break

            err = result.get("error", {})
            print(f"✗ #{item['id']} errore ({result.get('stage')}): {err}")
            if is_quota_error({"error": err}) and not dry_run:
                quota_retries += 1
                if quota_retries > MAX_QUOTA_RETRIES:
                    print("Limite quota persistente — salvo stato e esco.")
                    state.setdefault("failed", []).append({"id": item["id"], "slug": item["slug"], "error": err})
                    save_state(state)
                    return 1
                wait = QUOTA_WAIT_SECONDS
                print(f"⏳ Quota API — attendo {wait // 60} min e riprovo (tentativo {quota_retries}/{MAX_QUOTA_RETRIES})...")
                time.sleep(wait)
                continue
            state.setdefault("failed", []).append({"id": item["id"], "slug": item["slug"], "error": err})
            save_state(state)
            if attempt < 3:
                print(f"↻ Retry {attempt}/3 tra {delay}s...")
                time.sleep(delay)
            else:
                print(f"⚠ Salto temporaneo #{item['id']}, continuo con il prossimo...")
                break

        remaining = [x for x in BATCH_20 if x["slug"] not in {p["slug"] for p in state.get("published", [])}]
        if item != pending[-1] and not dry_run:
            print(f"⏱ Pausa {delay}s (protezione token/quota)...")
            time.sleep(delay)
        if not remaining:
            break

    published = len(state.get("published", []))
    print(f"\n{'='*60}")
    print(f"RISULTATO: {published}/20 pubblicati")
    if published == 20:
        print("✅ BATCH COMPLETO — tutti i 20 contenuti pubblicati.")
        return 0
    print(f"⚠ Mancanti: {20 - published} — riesegui lo script per riprendere.")
    return 0 if dry_run else (0 if published == 20 else 1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Pubblica batch 20 Instagram")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--start", type=int, default=1, help="ID contenuto da cui riprendere")
    parser.add_argument("--delay", type=int, default=DELAY_SECONDS)
    parser.add_argument("--verify", action="store_true", help="Solo verifica manifest/stato")
    args = parser.parse_args()

    if args.verify:
        from instagram_batch_20_lib import MANIFEST_PATH
        if MANIFEST_PATH.exists():
            data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
            assert data["count"] == 20
            for it in data["items"]:
                assert HOME_LINK in it["caption_it"]
                assert HOME_LINK in it["caption_en"]
            print(f"✓ Manifest OK: 20 contenuti, link presente")
        state = load_state()
        print(f"Stato: {len(state.get('published', []))}/20 pubblicati")
        return 0

    return run_batch(dry_run=args.dry_run, start_from=args.start, delay=args.delay)


if __name__ == "__main__":
    raise SystemExit(main())
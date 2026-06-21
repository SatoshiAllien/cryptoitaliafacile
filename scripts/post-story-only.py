#!/usr/bin/env python3
"""Pubblica solo Story FB + IG per un articolo (senza post feed)."""

from __future__ import annotations

import argparse
import json
import os
import urllib.parse
from pathlib import Path

from instagram_auth import resolve_credentials
from story_links import SATOSHI_AI_STORY_LINK
from instagram_story_queue import HOME_LINK, enqueue_story, is_quota_error
from story_publish import publish_facebook_story, publish_instagram_story
from story_video import prepare_story_video, story_image_file

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_PATH = ROOT / "data" / "articles.json"
ENV_PATH = Path(__file__).resolve().parent / ".env"
SITE_URL = "https://satoshiallien.github.io/cryptoitaliafacile/"
FB_STORY_BASE = f"{SITE_URL}assets/img/facebook/stories/"
IG_STORY_BASE = f"{SITE_URL}assets/img/instagram/stories/"


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


def load_article(slug: str) -> dict:
    data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
    for article in data["articles"]:
        if article["slug"] == slug:
            return article
    raise SystemExit(f"Articolo non trovato: {slug}")


def article_url(slug: str) -> str:
    return f"{SITE_URL}articolo.html?slug={urllib.parse.quote(slug)}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Pubblica solo Story FB/IG")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--slot", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-facebook", action="store_true")
    parser.add_argument("--skip-instagram", action="store_true")
    parser.add_argument("--link", default=SATOSHI_AI_STORY_LINK, help="URL sticker Satoshi AI")
    args = parser.parse_args()

    article = load_article(args.slug)
    link = args.link
    variants = ("abstract", "thematic", "minimal")
    code = 0

    print(f"Articolo: {article['title']}")
    print(f"Link: {link}")
    print(f"Variante: {variants[args.slot % 3]} (slot {args.slot})")

    if not args.skip_facebook:
        env = load_env()
        page_id = env.get("FACEBOOK_PAGE_ID", "")
        token = env.get("FACEBOOK_PAGE_ACCESS_TOKEN", "")
        if not args.dry_run and (not page_id or not token):
            print("ERRORE: manca token Facebook")
            code = 1
        else:
            img_file = story_image_file(article, args.slot)
            story_url = FB_STORY_BASE + img_file
            print(f"\n=== FACEBOOK STORY ===\n{story_url}")
            video_path = None
            if not args.dry_run:
                video_path, track = prepare_story_video(
                    "facebook", img_file, args.slot, 0, 20, link_url=link
                )
                print(f"MUSICA: {track['title']} — {track['artist']}")
                print(f"VIDEO: {video_path}")
            result = publish_facebook_story(
                page_id, story_url, token, args.dry_run,
                video_path=video_path, use_video=True, link_url=link,
            )
            print("RISULTATO FB:", json.dumps(result, indent=2))
            if result.get("error"):
                code = 1

    if not args.skip_instagram:
        env = load_env()
        ig_id, token, api_mode = resolve_credentials(env)
        if not args.dry_run and (not ig_id or not token):
            print("ERRORE: manca token Instagram")
            code = 1
        else:
            img_file = story_image_file(article, args.slot)
            story_url = IG_STORY_BASE + img_file
            print(f"\n=== INSTAGRAM STORY ({api_mode}) ===\n{story_url}")
            video_path = None
            if not args.dry_run:
                video_path, track = prepare_story_video(
                    "instagram", img_file, args.slot, 0, 20, link_url=link
                )
                print(f"MUSICA: {track['title']} — {track['artist']}")
                print(f"VIDEO: {video_path}")
            result = publish_instagram_story(
                ig_id, story_url, token, args.dry_run,
                video_path=video_path, use_video=True, link_url=link,
            )
            print("RISULTATO IG:", json.dumps(result, indent=2))
            if result.get("error"):
                if is_quota_error(result):
                    entry = enqueue_story(
                        args.slug,
                        slot=args.slot,
                        link_url=link,
                        reason="quota_limit",
                        note="Accodato automaticamente da post-story-only.py",
                    )
                    print(
                        "\n⏳ Instagram in coda (limite API). "
                        "Ripubblicazione automatica via Krown82-IG-StoryRetry"
                    )
                    print(f"   Coda: {entry['slug']} slot {entry['slot']}")
                code = 1

    return code


if __name__ == "__main__":
    raise SystemExit(main())
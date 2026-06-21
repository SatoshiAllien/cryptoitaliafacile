#!/usr/bin/env python3
"""Integra anteprime Little Satoshi News nel sito e negli asset social."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
PREVIEWS = Path(r"C:\Users\krown\little-satoshi-news-previews\output")
ARTICLES_PATH = ROOT / "data" / "articles.json"
FB_POSTS = ROOT / "assets" / "img" / "facebook" / "posts"
FB_STORIES = ROOT / "assets" / "img" / "facebook" / "stories"
IG_POSTS = ROOT / "assets" / "img" / "instagram" / "posts"
IG_STORIES = ROOT / "assets" / "img" / "instagram" / "stories"
JPEG_QUALITY = 88


def to_fb_post(src: Path, dest: Path) -> None:
    img = Image.open(src).convert("RGB")
    target_w, target_h = 1200, 630
    scale = target_w / img.width
    resized = img.resize((target_w, int(img.height * scale)), Image.LANCZOS)
    top = max(0, (resized.height - target_h) // 2)
    cropped = resized.crop((0, top, target_w, top + target_h))
    dest.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(dest, "JPEG", quality=JPEG_QUALITY, optimize=True)


def to_jpg(src: Path, dest: Path) -> None:
    img = Image.open(src).convert("RGB")
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, "JPEG", quality=JPEG_QUALITY, optimize=True)


def integrate() -> dict[str, int]:
    if not PREVIEWS.exists():
        raise SystemExit(f"Cartella anteprime non trovata: {PREVIEWS}")

    data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
    stats = {"ok": 0, "missing": 0, "updated": 0}

    for article in data["articles"]:
        slug = article["slug"]
        slug_dir = PREVIEWS / slug
        post_src = slug_dir / "variant-1-hero_square_1080x1080.png"
        story_src = slug_dir / "variant-3-overlay_stories_1080x1920.png"

        if not post_src.exists() or not story_src.exists():
            stats["missing"] += 1
            print(f"SKIP {slug} — anteprime mancanti")
            continue

        fname = f"{slug}.jpg"
        to_fb_post(post_src, FB_POSTS / fname)
        to_jpg(post_src, IG_POSTS / fname)
        to_jpg(story_src, FB_STORIES / fname)
        to_jpg(story_src, IG_STORIES / fname)

        article["fbImage"] = fname
        article["igImage"] = fname
        article["fbStoryImage"] = fname
        article["igStoryImage"] = fname
        article["previewVariant"] = "variant-1-hero"
        article["storyVariant"] = "variant-3-overlay"
        stats["ok"] += 1
        stats["updated"] += 1
        print(f"OK {slug}")

    ARTICLES_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return stats


if __name__ == "__main__":
    result = integrate()
    print(f"\nIntegrati: {result['ok']} | Mancanti: {result['missing']} | Aggiornati in articles.json: {result['updated']}")
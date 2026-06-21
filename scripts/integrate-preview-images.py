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
STORY_CACHE = ROOT / "assets" / "video" / "stories" / "cache"
JPEG_QUALITY = 88

STORY_VARIANTS = (
    ("variant-1-hero", "abstract"),
    ("variant-2-abstract", "thematic"),
    ("variant-3-overlay", "minimal"),
)


def clear_story_cache() -> None:
    """Invalida video story generati con immagini precedenti."""
    if STORY_CACHE.exists():
        shutil.rmtree(STORY_CACHE)
    STORY_CACHE.mkdir(parents=True, exist_ok=True)
    print("Cache video story svuotata")


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


def integrate(*, refresh_cache: bool = True) -> dict[str, int]:
    if not PREVIEWS.exists():
        raise SystemExit(f"Cartella anteprime non trovata: {PREVIEWS}")

    if refresh_cache:
        clear_story_cache()

    data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
    stats = {"ok": 0, "missing": 0, "updated": 0}

    for article in data["articles"]:
        slug = article["slug"]
        slug_dir = PREVIEWS / slug
        post_src = slug_dir / "variant-1-hero_square_1080x1080.png"

        if not post_src.exists():
            stats["missing"] += 1
            print(f"SKIP {slug} — anteprima post mancante")
            continue

        story_ok = 0
        for variant_key, suffix in STORY_VARIANTS:
            story_src = slug_dir / f"{variant_key}_stories_1080x1920.png"
            if not story_src.exists():
                continue
            story_fname = f"{slug}-{suffix}.jpg"
            to_jpg(story_src, FB_STORIES / story_fname)
            to_jpg(story_src, IG_STORIES / story_fname)
            story_ok += 1

        if story_ok == 0:
            stats["missing"] += 1
            print(f"SKIP {slug} — story mancanti")
            continue

        post_fname = f"{slug}.jpg"
        to_fb_post(post_src, FB_POSTS / post_fname)
        to_jpg(post_src, IG_POSTS / post_fname)

        # Default story = abstract; rotazione per slot via suffisso
        default_story = f"{slug}-abstract.jpg"
        to_jpg(
            slug_dir / "variant-1-hero_stories_1080x1920.png",
            FB_STORIES / post_fname,
        )
        to_jpg(
            slug_dir / "variant-1-hero_stories_1080x1920.png",
            IG_STORIES / post_fname,
        )

        article["fbImage"] = post_fname
        article["igImage"] = post_fname
        article["fbStoryImage"] = default_story
        article["igStoryImage"] = default_story
        article["previewVariant"] = "variant-1-hero"
        article["storyVariant"] = "variant-1-hero"
        article["storyVariants"] = [v[0] for v in STORY_VARIANTS]
        stats["ok"] += 1
        stats["updated"] += 1
        print(f"OK {slug} ({story_ok} story)")

    ARTICLES_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return stats


if __name__ == "__main__":
    result = integrate()
    print(
        f"\nIntegrati: {result['ok']} | Mancanti: {result['missing']} "
        f"| Aggiornati in articles.json: {result['updated']}"
    )
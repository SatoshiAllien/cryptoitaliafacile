#!/usr/bin/env python3
"""Genera 20×4 immagini professionali (story primary/alt + feed IT/EN 4:5)."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from image_style import JPEG_QUALITY
from instagram_batch_20_content import BATCH_20, HOME_LINK, validate_batch
from instagram_batch_20_lib import (
    OUT_DIR,
    ROOT,
    render_advanced_story,
    render_feed_post,
    render_minimal_story,
    write_manifest,
)

STORIES_LINK_DIR = ROOT / "assets" / "img" / "instagram" / "stories"


def generate_all() -> list[str]:
    validate_batch()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    created: list[str] = []

    for item in BATCH_20:
        slug = item["slug"]
        n = item["id"]
        print(f"\n[{n}/20] {slug}")

        pairs = [
            (f"{slug}-story-minimal.jpg", render_minimal_story(item, lang="it")),
            (f"{slug}-story-advanced.jpg", render_advanced_story(item, lang="it")),
            (f"{slug}-feed-it.jpg", render_feed_post(item, lang="it")),
            (f"{slug}-feed-en.jpg", render_feed_post(item, lang="en")),
        ]
        for name, img in pairs:
            path = OUT_DIR / name
            img.save(path, "JPEG", quality=JPEG_QUALITY, optimize=True)
            created.append(str(path.relative_to(ROOT)))
            print(f"  ✓ {name} ({img.size[0]}×{img.size[1]})")

        adv = OUT_DIR / f"{slug}-story-advanced.jpg"
        STORIES_LINK_DIR.mkdir(parents=True, exist_ok=True)
        shutil.copy2(adv, STORIES_LINK_DIR / f"{slug}-story-advanced.jpg")

    write_manifest()
    print(f"\n✓ Manifest: data/instagram-batch-20.json")
    return created


def verify() -> None:
    assert len(BATCH_20) == 20
    expected = len(BATCH_20) * 4
    files = list(OUT_DIR.glob("*.jpg"))
    assert len(files) == expected, f"Expected {expected} images, found {len(files)}"
    manifest_items = 20
    for item in BATCH_20:
        for suffix in ("story-minimal", "story-advanced", "feed-it", "feed-en"):
            p = OUT_DIR / f"{item['slug']}-{suffix}.jpg"
            assert p.exists(), f"Missing {p}"
    print(f"CHECK OK: {expected} immagini, 20 contenuti, link={HOME_LINK}")


if __name__ == "__main__":
    generate_all()
    verify()
    print("\n✅ Generazione completata — 20 contenuti, nessuna interruzione.")
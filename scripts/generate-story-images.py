#!/usr/bin/env python3
"""Genera story topic template senza link (1080×1920 IG, 1080×1350 FB)."""

from __future__ import annotations

from pathlib import Path

from image_style import CTA, JPEG_QUALITY, TOPICS, render_story, topic_cfg
from story_post_style import render_story_post

ROOT = Path(__file__).resolve().parent.parent
FB_OUT = ROOT / "assets" / "img" / "facebook" / "stories"
IG_OUT = ROOT / "assets" / "img" / "instagram" / "stories"


def main() -> None:
    FB_OUT.mkdir(parents=True, exist_ok=True)
    IG_OUT.mkdir(parents=True, exist_ok=True)
    for name in TOPICS:
        if name in ("regulation", "elon", "breaking"):
            continue
        cfg_it = topic_cfg(name, lang="it")
        cfg_en = topic_cfg(name, lang="en")

        ig = render_story_post(
            platform="instagram",
            topic=name,
            title=cfg_it["hook"].replace("\n", " "),
            subtitle=cfg_it.get("sub", "Spiegato facile"),
            body=cfg_it.get("sub", ""),
            variant="primary",
            accent=cfg_it["accent"],
        )
        p = IG_OUT / f"{name}.jpg"
        ig.save(p, "JPEG", quality=JPEG_QUALITY, optimize=True)
        print("OK IG", p.relative_to(ROOT))

        fb = render_story_post(
            platform="facebook",
            topic=name,
            title=cfg_it["hook"].replace("\n", " "),
            subtitle=cfg_it.get("sub", "Spiegato facile"),
            body=cfg_it.get("sub", ""),
            variant="primary",
            accent=cfg_it["accent"],
        )
        p = FB_OUT / f"{name}.jpg"
        fb.save(p, "JPEG", quality=JPEG_QUALITY, optimize=True)
        print("OK FB", p.relative_to(ROOT))

        # Legacy render_story senza URL (topic templates)
        legacy = render_story(name, cfg_en, cta=CTA["ig_story"], footer="✨ @krown.82", width=1080, height=1920)
        legacy.save(IG_OUT / f"{name}-legacy.jpg", "JPEG", quality=JPEG_QUALITY, optimize=True)


if __name__ == "__main__":
    main()
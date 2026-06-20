#!/usr/bin/env python3
"""Genera immagini Stories 9:16 (1080x1920) per Facebook e Instagram."""

from __future__ import annotations

from pathlib import Path

from image_style import CTA, TOPICS, render_story, topic_cfg

ROOT = Path(__file__).resolve().parent.parent
FB_OUT = ROOT / "assets" / "img" / "facebook" / "stories"
IG_OUT = ROOT / "assets" / "img" / "instagram" / "stories"


def main() -> None:
    FB_OUT.mkdir(parents=True, exist_ok=True)
    IG_OUT.mkdir(parents=True, exist_ok=True)
    for name in TOPICS:
        if name in ("regulation", "elon", "breaking"):
            continue
        fb = render_story(
            name,
            topic_cfg(name, lang="it"),
            cta=CTA["fb_story"],
            footer="📰 The Little Satoshi News · cryptoitaliafacile",
        )
        p = FB_OUT / f"{name}.jpg"
        fb.save(p, "JPEG", quality=93, optimize=True)
        print("OK FB", p.relative_to(ROOT))

        ig = render_story(
            name,
            topic_cfg(name, lang="en"),
            cta=CTA["ig_story"],
            footer="✨ @krown.82 · cryptoitaliafacile",
        )
        p = IG_OUT / f"{name}.jpg"
        ig.save(p, "JPEG", quality=93, optimize=True)
        print("OK IG", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
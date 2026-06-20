#!/usr/bin/env python3
"""Genera thumbnail clickbait per post Facebook (1200x630)."""

from __future__ import annotations

from pathlib import Path

from image_style import CTA, TOPICS, render_post, topic_cfg

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img" / "facebook" / "posts"
W, H = 1200, 630


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name in TOPICS:
        if name in ("regulation", "elon", "breaking"):
            continue
        cfg = topic_cfg(name, lang="it")
        img = render_post(
            name,
            cfg,
            width=W,
            height=H,
            cta=CTA["fb_post"],
            footer="📰 The Little Satoshi News · cryptoitaliafacile",
            icon_box=(920, 120, 1160, 360),
            hook_size=56,
            sub_size=28,
            badge_size=32,
            brand_scale=0.07,
        )
        path = OUT / f"{name}.jpg"
        img.save(path, "JPEG", quality=93, optimize=True)
        print("OK", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
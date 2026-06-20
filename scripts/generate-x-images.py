#!/usr/bin/env python3
"""Genera thumbnail clickbait per post X (1200x675)."""

from __future__ import annotations

from pathlib import Path

from image_style import CTA, TOPICS, render_post, topic_cfg

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img" / "x" / "posts"
W, H = 1200, 675

X_TOPICS = ("bitcoin", "regulation", "elon", "breaking")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name in X_TOPICS:
        cfg = topic_cfg(name, lang="en")
        img = render_post(
            name,
            cfg,
            width=W,
            height=H,
            cta=CTA["x_post"],
            footer="🐦 @TheRiser100x · cryptoitaliafacile",
            icon_box=(920, 140, 1140, 360),
            hook_size=52,
            sub_size=26,
            badge_size=30,
            brand_scale=0.07,
        )
        path = OUT / f"{name}.jpg"
        img.save(path, "JPEG", quality=93, optimize=True)
        print("OK", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
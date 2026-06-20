#!/usr/bin/env python3
"""Genera immagini quadrate 1080x1080 per post Instagram @krown.82."""

from __future__ import annotations

from pathlib import Path

from image_style import CTA, TOPICS, render_post, topic_cfg

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img" / "instagram" / "posts"
W, H = 1080, 1080


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name in TOPICS:
        if name in ("regulation", "elon", "breaking"):
            continue
        cfg = topic_cfg(name, lang="en")
        img = render_post(
            name,
            cfg,
            width=W,
            height=H,
            cta=CTA["ig_post"],
            footer="✨ @krown.82 · cryptoitaliafacile",
            icon_box=(760, 420, 1020, 680),
            hook_size=64,
            sub_size=32,
            badge_size=36,
            brand_scale=0.08,
        )
        path = OUT / f"{name}.jpg"
        img.save(path, "JPEG", quality=93, optimize=True)
        print("OK", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
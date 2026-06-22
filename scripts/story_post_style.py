#!/usr/bin/env python3
"""Story senza link — Instagram 1080×1920, Facebook 1080×1350."""

from __future__ import annotations

import random
from dataclasses import dataclass

from PIL import Image, ImageDraw

from brand_overlay import apply_topic_logo_top_left, draw_center_topic_icon, paste_brand_watermark
from feed_post_style import PALETTE, _draw_centered_lines, _line_height, _text_width, _wrap_pixels
from image_style import JPEG_QUALITY, _hex, gradient2, load_font
from topic_detect import topic_label

__all__ = ["JPEG_QUALITY", "INSTAGRAM_STORY", "FACEBOOK_STORY", "render_story_post", "design_description"]


@dataclass(frozen=True)
class StoryLayout:
    width: int
    height: int
    safe: int
    title_size: int
    subtitle_size: int
    body_size: int
    logo_size: int
    center_icon: int
    platform: str


INSTAGRAM_STORY = StoryLayout(
    width=1080, height=1920, safe=80,
    title_size=58, subtitle_size=30, body_size=28,
    logo_size=72, center_icon=120, platform="instagram",
)
FACEBOOK_STORY = StoryLayout(
    width=1080, height=1350, safe=80,
    title_size=52, subtitle_size=28, body_size=26,
    logo_size=72, center_icon=108, platform="facebook",
)


def _draw_bg(draw: ImageDraw.ImageDraw, w: int, h: int, *, variant: str, seed: int, accent: str) -> None:
    gradient2(draw, w, h, PALETTE["bg_dark"], PALETTE["bg_mid"])
    spacing = 46 if variant == "primary" else 38
    grid = PALETTE["grid"] if variant == "primary" else (18, 22, 34)
    for x in range(0, w, spacing):
        draw.line([(x, 0), (x, h)], fill=grid, width=1)
    for y in range(0, h, spacing):
        draw.line([(0, y), (w, y)], fill=grid, width=1)

    rng = random.Random(seed)
    gold = _hex(PALETTE["gold"])
    for band_y in (int(h * 0.1), int(h * 0.88)):
        pts = []
        x = 80
        while x < w - 80:
            pts.append((x, band_y + rng.randint(-16, 16)))
            x += rng.randint(100, 140)
        if len(pts) >= 2:
            draw.line(pts, fill=gold, width=2)

    if variant == "alt":
        s = 80
        draw.rounded_rectangle(
            (s - 4, s - 4, w - s + 4, h - s + 4),
            radius=22,
            outline=_hex(PALETTE["electric"]),
            width=2,
        )


def _draw_topic_footer(
    draw: ImageDraw.ImageDraw,
    *,
    spec: StoryLayout,
    topic: str,
    accent: str,
) -> None:
    """Barra decorativa in basso — solo etichetta topic, nessun link."""
    label = topic_label(topic)
    font = load_font(22, bold=True)
    text = f"◆  {label}  ◆"
    tw = _text_width(text, font)
    bar_h = 52
    y1 = spec.height - spec.safe - bar_h - 16
    x1 = (spec.width - tw - 48) // 2
    x2 = x1 + tw + 48
    draw.rounded_rectangle((x1, y1, x2, y1 + bar_h), radius=bar_h // 2, outline=_hex(accent), width=2)
    draw.text((x1 + 24, y1 + 12), text, fill=_hex(PALETTE["gold"]), font=font)


def render_story_post(
    *,
    platform: str,
    topic: str,
    title: str,
    subtitle: str,
    body: str,
    variant: str = "primary",
    accent: str = PALETTE["accent"],
) -> Image.Image:
    spec = INSTAGRAM_STORY if platform == "instagram" else FACEBOOK_STORY
    seed = hash(f"{title}:{platform}:{variant}") % 10_000

    img = Image.new("RGB", (spec.width, spec.height), PALETTE["bg_dark"])
    draw = ImageDraw.Draw(img)
    _draw_bg(draw, spec.width, spec.height, variant=variant, seed=seed, accent=accent)

    content_w = spec.width - spec.safe * 2
    title_font = load_font(spec.title_size, bold=True)
    subtitle_font = load_font(spec.subtitle_size)
    body_font = load_font(spec.body_size)

    title_lines = _wrap_pixels(title, title_font, content_w, max_lines=3)
    subtitle_lines = _wrap_pixels(subtitle, subtitle_font, content_w, max_lines=2)
    body_lines = _wrap_pixels(body, body_font, int(content_w * 0.9), max_lines=3)

    y = spec.safe + spec.logo_size + 36
    y = _draw_centered_lines(
        draw, title_lines, y=y, font=title_font, fill=PALETTE["text"],
        canvas_w=spec.width, line_gap=10,
    )
    y += 18
    y = _draw_centered_lines(
        draw, subtitle_lines, y=y, font=subtitle_font, fill=PALETTE["gold"],
        canvas_w=spec.width, line_gap=8,
    )
    y += 32

    icon_cy = y + spec.center_icon // 2 + (40 if platform == "instagram" else 24)
    img = draw_center_topic_icon(
        img, topic, accent=accent,
        center=(spec.width // 2, icon_cy),
        size=spec.center_icon,
    )
    draw = ImageDraw.Draw(img)
    y = icon_cy + spec.center_icon // 2 + 36

    _draw_centered_lines(
        draw, body_lines, y=y, font=body_font, fill=PALETTE["muted"],
        canvas_w=spec.width, line_gap=10,
    )
    _draw_topic_footer(draw, spec=spec, topic=topic, accent=accent)

    img = apply_topic_logo_top_left(img, topic, accent=accent, size=spec.logo_size, margin=spec.safe)
    return paste_brand_watermark(img, scale=0.045)


def design_description(topic: str, variant: str, platform: str) -> str:
    size = "1080×1920" if platform == "instagram" else "1080×1350"
    style = "primario" if variant == "primary" else "alternativo"
    return (
        f"Story {platform} {size} · safe 80px · {style} · topic {topic_label(topic)} · "
        f"logo alto-sx · titolo centrato · icona centrale · zero link/URL."
    )
#!/usr/bin/env python3
"""Story premium senza link — Instagram 1080×1920 (safe 120px), FB 1080×1350."""

from __future__ import annotations

import random
from dataclasses import dataclass

from PIL import Image, ImageDraw

from brand_overlay import apply_topic_logo_top_left, draw_center_topic_icon, paste_brand_watermark
from feed_post_style import PALETTE, _draw_centered_lines, _text_width, _wrap_pixels
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
    cta_height: int
    cta_font: int
    body_max_lines: int
    platform: str


INSTAGRAM_STORY = StoryLayout(
    width=1080, height=1920, safe=120,
    title_size=56, subtitle_size=28, body_size=26,
    logo_size=76, center_icon=128,
    cta_height=72, cta_font=26, body_max_lines=2,
    platform="instagram",
)
FACEBOOK_STORY = StoryLayout(
    width=1080, height=1350, safe=80,
    title_size=52, subtitle_size=26, body_size=24,
    logo_size=72, center_icon=108,
    cta_height=68, cta_font=24, body_max_lines=2,
    platform="facebook",
)


def _draw_bg(draw: ImageDraw.ImageDraw, spec: StoryLayout, *, variant: str, seed: int) -> None:
    w, h, s = spec.width, spec.height, spec.safe
    gradient2(draw, w, h, PALETTE["bg_dark"], PALETTE["bg_mid"])
    spacing = 44 if variant == "primary" else 36
    grid = PALETTE["grid"] if variant == "primary" else (18, 22, 34)
    for x in range(s, w - s, spacing):
        draw.line([(x, s), (x, h - s)], fill=grid, width=1)
    for y in range(s, h - s, spacing):
        draw.line([(s, y), (w - s, y)], fill=grid, width=1)

    rng = random.Random(seed)
    gold = _hex(PALETTE["gold"])
    for band_y in (s + 20, h - s - 40):
        pts: list[tuple[int, int]] = []
        x = s
        while x < w - s:
            pts.append((x, band_y + rng.randint(-12, 12)))
            x += rng.randint(90, 130)
        if len(pts) >= 2:
            draw.line(pts, fill=gold, width=2)

    if variant == "alt":
        draw.rounded_rectangle(
            (s - 6, s - 6, w - s + 6, h - s + 6),
            radius=24,
            outline=_hex(PALETTE["electric"]),
            width=2,
        )


def _draw_story_cta(
    draw: ImageDraw.ImageDraw,
    *,
    spec: StoryLayout,
    cta: str,
    accent: str,
) -> None:
    """CTA visiva in basso — testo puro, nessun link."""
    font = load_font(spec.cta_font, bold=True)
    label = cta.strip()
    tw = _text_width(label, font)
    pad_x = 44
    btn_w = min(spec.width - spec.safe * 2, tw + pad_x * 2)
    btn_h = spec.cta_height
    x1 = (spec.width - btn_w) // 2
    y1 = spec.height - spec.safe - btn_h
    draw.rounded_rectangle((x1, y1, x1 + btn_w, y1 + btn_h), radius=btn_h // 2, fill=_hex(accent))
    draw.text(
        (x1 + (btn_w - tw) // 2, y1 + (btn_h - spec.cta_font) // 2 - 2),
        label,
        fill="#0F172A",
        font=font,
    )


def render_story_post(
    *,
    platform: str,
    topic: str,
    title: str,
    subtitle: str,
    body: str,
    cta: str = "Scopri di più",
    variant: str = "primary",
    accent: str = PALETTE["accent"],
) -> Image.Image:
    """
    Layout fisso:
    1. Logo argomento alto-sx (safe-area)
    2. Titolo centrato
    3. Sottotitolo
    4. Icona centrale
    5. Testo breve (max 2 frasi)
    6. CTA visiva in basso
    """
    spec = INSTAGRAM_STORY if platform == "instagram" else FACEBOOK_STORY
    seed = hash(f"{title}:{platform}:{variant}") % 10_000

    img = Image.new("RGB", (spec.width, spec.height), PALETTE["bg_dark"])
    draw = ImageDraw.Draw(img)
    _draw_bg(draw, spec, variant=variant, seed=seed)

    content_w = spec.width - spec.safe * 2
    title_font = load_font(spec.title_size, bold=True)
    subtitle_font = load_font(spec.subtitle_size)
    body_font = load_font(spec.body_size)

    title_lines = _wrap_pixels(title, title_font, content_w, max_lines=3)
    subtitle_lines = _wrap_pixels(subtitle, subtitle_font, content_w, max_lines=2)
    body_lines = _wrap_pixels(body, body_font, int(content_w * 0.88), max_lines=spec.body_max_lines)

    y = spec.safe + spec.logo_size + 32
    y = _draw_centered_lines(
        draw, title_lines, y=y, font=title_font, fill=PALETTE["text"],
        canvas_w=spec.width, line_gap=10,
    )
    y += 16
    y = _draw_centered_lines(
        draw, subtitle_lines, y=y, font=subtitle_font, fill=PALETTE["gold"],
        canvas_w=spec.width, line_gap=8,
    )
    y += 28

    icon_cy = y + spec.center_icon // 2 + (48 if platform == "instagram" else 28)
    img = draw_center_topic_icon(
        img, topic, accent=accent,
        center=(spec.width // 2, icon_cy),
        size=spec.center_icon,
    )
    draw = ImageDraw.Draw(img)
    y = icon_cy + spec.center_icon // 2 + 32

    _draw_centered_lines(
        draw, body_lines, y=y, font=body_font, fill=PALETTE["muted"],
        canvas_w=spec.width, line_gap=10,
    )
    _draw_story_cta(draw, spec=spec, cta=cta, accent=accent)

    img = apply_topic_logo_top_left(
        img, topic, accent=accent, size=spec.logo_size, margin=spec.safe,
    )
    scale = 0.042 if platform == "instagram" else 0.045
    return paste_brand_watermark(img, scale=scale)


def design_description(topic: str, variant: str, platform: str) -> str:
    if platform == "instagram":
        return (
            f"Story IG 1080×1920 · safe 120px · {variant} · {topic_label(topic)} · "
            f"logo alto-sx · titolo/sottotitolo centrati · icona centrale · "
            f"testo 2 frasi · CTA visiva · zero link/URL."
        )
    return (
        f"Story FB 1080×1350 · safe 80px · {variant} · {topic_label(topic)} · "
        f"layout ordinato · CTA visiva · zero link/URL."
    )
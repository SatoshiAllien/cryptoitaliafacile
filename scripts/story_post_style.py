#!/usr/bin/env python3
"""Story premium senza link — Instagram 1080×1920 (safe 120px), FB 1080×1350."""

from __future__ import annotations

import random
from dataclasses import dataclass

from PIL import Image, ImageDraw

from brand_overlay import (
    apply_topic_logo_top_left,
    draw_center_topic_icon,
    draw_hero_logo_centered,
    paste_brand_watermark,
)
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
    hero_logo: int
    cta_height: int
    cta_font: int
    body_max_lines: int
    platform: str


INSTAGRAM_STORY = StoryLayout(
    width=1080, height=1920, safe=120,
    title_size=58, subtitle_size=30, body_size=26,
    logo_size=0, center_icon=0,
    hero_logo=400,
    cta_height=72, cta_font=26, body_max_lines=2,
    platform="instagram",
)
FACEBOOK_STORY = StoryLayout(
    width=1080, height=1350, safe=80,
    title_size=52, subtitle_size=26, body_size=24,
    logo_size=72, center_icon=108, hero_logo=0,
    cta_height=68, cta_font=24, body_max_lines=2,
    platform="facebook",
)


def _draw_bg(draw: ImageDraw.ImageDraw, spec: StoryLayout, *, variant: str, seed: int, accent: str) -> None:
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
    orange = _hex(accent)
    for band_y, color in ((s + 24, gold), (h - s - 48, orange)):
        pts: list[tuple[int, int]] = []
        x = s
        while x < w - s:
            pts.append((x, band_y + rng.randint(-12, 12)))
            x += rng.randint(90, 130)
        if len(pts) >= 2:
            draw.line(pts, fill=color, width=2)

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


def _cta_top(spec: StoryLayout) -> int:
    return spec.height - spec.safe - spec.cta_height


def _render_instagram_story(
    *,
    spec: StoryLayout,
    topic: str,
    title: str,
    subtitle: str,
    body: str,
    cta: str,
    variant: str,
    accent: str,
) -> Image.Image:
    """
    Layout IG v3 — logo hero grande e centrato (30–40% area visiva):
    1. Titolo grande sopra o sotto il logo (variante)
    2. Sottotitolo breve
    3. Logo hero centrato con glow/neon
    4. Testo breve (max 2 frasi)
    5. CTA visiva in basso
    """
    seed = hash(f"{title}:instagram:{variant}") % 10_000
    img = Image.new("RGB", (spec.width, spec.height), PALETTE["bg_dark"])
    draw = ImageDraw.Draw(img)
    _draw_bg(draw, spec, variant=variant, seed=seed, accent=accent)

    content_w = spec.width - spec.safe * 2
    title_font = load_font(spec.title_size, bold=True)
    subtitle_font = load_font(spec.subtitle_size)
    body_font = load_font(spec.body_size)

    title_lines = _wrap_pixels(title, title_font, content_w, max_lines=2)
    subtitle_lines = _wrap_pixels(subtitle, subtitle_font, content_w, max_lines=2)
    body_lines = _wrap_pixels(body, body_font, int(content_w * 0.88), max_lines=spec.body_max_lines)

    title_above = variant == "primary"
    cta_y = _cta_top(spec)
    body_block_h = len(body_lines) * _line_height(body_font, 10) + 8
    hero_size = spec.hero_logo
    hero_cy = spec.height // 2 - 16

    if title_above:
        y = spec.safe + 8
        y = _draw_centered_lines(
            draw, title_lines, y=y, font=title_font, fill=PALETTE["text"],
            canvas_w=spec.width, line_gap=10,
        )
        y += 12
        y = _draw_centered_lines(
            draw, subtitle_lines, y=y, font=subtitle_font, fill=PALETTE["gold"],
            canvas_w=spec.width, line_gap=8,
        )
        top_text_bottom = y
        hero_cy = max(
            top_text_bottom + hero_size // 2 + 40,
            min(hero_cy, cta_y - body_block_h - hero_size // 2 - 48),
        )
    else:
        y = spec.safe + 8
        y = _draw_centered_lines(
            draw, subtitle_lines, y=y, font=subtitle_font, fill=PALETTE["gold"],
            canvas_w=spec.width, line_gap=8,
        )
        top_text_bottom = y
        hero_cy = max(
            top_text_bottom + hero_size // 2 + 56,
            min(spec.height // 2 + 20, cta_y - body_block_h - hero_size // 2 - 120),
        )

    img = draw_hero_logo_centered(
        img, topic, accent=accent,
        center=(spec.width // 2, hero_cy),
        size=hero_size,
        variant=variant,
    )
    draw = ImageDraw.Draw(img)

    if title_above:
        y = hero_cy + hero_size // 2 + 36
    else:
        y = hero_cy + hero_size // 2 + 28
        y = _draw_centered_lines(
            draw, title_lines, y=y, font=title_font, fill=PALETTE["text"],
            canvas_w=spec.width, line_gap=10,
        )
        y += 16

    max_body_y = cta_y - body_block_h - 12
    y = min(y, max_body_y)
    _draw_centered_lines(
        draw, body_lines, y=y, font=body_font, fill=PALETTE["muted"],
        canvas_w=spec.width, line_gap=10,
    )
    _draw_story_cta(draw, spec=spec, cta=cta, accent=accent)
    return paste_brand_watermark(img, scale=0.038)


def _render_facebook_story(
    *,
    spec: StoryLayout,
    topic: str,
    title: str,
    subtitle: str,
    body: str,
    cta: str,
    variant: str,
    accent: str,
) -> Image.Image:
    """Layout FB invariato — logo alto-sx + icona centrale."""
    seed = hash(f"{title}:facebook:{variant}") % 10_000
    img = Image.new("RGB", (spec.width, spec.height), PALETTE["bg_dark"])
    draw = ImageDraw.Draw(img)
    _draw_bg(draw, spec, variant=variant, seed=seed, accent=accent)

    content_w = spec.width - spec.safe * 2
    title_font = load_font(spec.title_size, bold=True)
    subtitle_font = load_font(spec.subtitle_size)
    body_font = load_font(spec.body_size)

    title_lines = _wrap_pixels(title, title_font, content_w, max_lines=3)
    subtitle_lines = _wrap_pixels(subtitle, subtitle_font, content_w, max_lines=2)
    body_lines = _wrap_pixels(body, body_font, int(content_w * 0.88), max_lines=spec.body_max_lines)

    y = spec.safe + spec.logo_size + 28
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

    icon_cy = y + spec.center_icon // 2 + 28
    img = draw_center_topic_icon(
        img, topic, accent=accent,
        center=(spec.width // 2, icon_cy),
        size=spec.center_icon,
    )
    draw = ImageDraw.Draw(img)
    y = icon_cy + spec.center_icon // 2 + 28

    _draw_centered_lines(
        draw, body_lines, y=y, font=body_font, fill=PALETTE["muted"],
        canvas_w=spec.width, line_gap=10,
    )
    _draw_story_cta(draw, spec=spec, cta=cta, accent=accent)

    img = apply_topic_logo_top_left(
        img, topic, accent=accent, size=spec.logo_size, margin=spec.safe,
    )
    return paste_brand_watermark(img, scale=0.045)


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
    spec = INSTAGRAM_STORY if platform == "instagram" else FACEBOOK_STORY
    if platform == "instagram":
        return _render_instagram_story(
            spec=spec, topic=topic, title=title, subtitle=subtitle,
            body=body, cta=cta, variant=variant, accent=accent,
        )
    return _render_facebook_story(
        spec=spec, topic=topic, title=title, subtitle=subtitle,
        body=body, cta=cta, variant=variant, accent=accent,
    )


def design_description(topic: str, variant: str, platform: str) -> str:
    if platform == "instagram":
        title_pos = "sopra" if variant == "primary" else "sotto"
        return (
            f"Story IG 1080×1920 · safe 120px · {variant} · {topic_label(topic)} · "
            f"logo hero centrato ~37% · PNG trasparente · glow/neon · titolo {title_pos} logo · "
            f"sottotitolo · testo 2 frasi · CTA visiva · zero link/URL."
        )
    return (
        f"Story FB 1080×1350 · safe 80px · {variant} · {topic_label(topic)} · "
        f"layout ordinato · CTA visiva · zero link/URL."
    )
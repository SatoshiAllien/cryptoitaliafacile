#!/usr/bin/env python3
"""Renderer feed ordinato — IG/FB 1080×1350, logo hero centrato, safe 100px."""

from __future__ import annotations

import random
from dataclasses import dataclass

from PIL import Image, ImageDraw

from brand_overlay import draw_hero_logo_centered, paste_brand_watermark
from image_style import JPEG_QUALITY, _hex, gradient2, load_font
from topic_detect import topic_label

PALETTE = {
    "bg_dark": (6, 8, 14),
    "bg_mid": (12, 16, 28),
    "accent": "#F7931A",
    "gold": "#F4C430",
    "electric": "#3B82F6",
    "text": "#FFFFFF",
    "muted": "#B8C4D4",
    "grid": (24, 30, 44),
}


@dataclass(frozen=True)
class LayoutSpec:
    width: int
    height: int
    safe: int
    title_size: int
    subtitle_size: int
    body_size: int
    hero_logo: int
    cta_height: int
    cta_font: int
    body_max_lines: int
    platform: str
    line_gap_title: int = 10
    line_gap_body: int = 8


INSTAGRAM = LayoutSpec(
    width=1080, height=1350, safe=100,
    title_size=52, subtitle_size=28, body_size=26,
    hero_logo=340, cta_height=72, cta_font=26,
    body_max_lines=3, platform="instagram",
)
FACEBOOK = LayoutSpec(
    width=1080, height=1350, safe=100,
    title_size=50, subtitle_size=26, body_size=24,
    hero_logo=340, cta_height=72, cta_font=24,
    body_max_lines=3, platform="facebook",
)


def _text_width(text: str, font) -> int:
    tmp = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    bbox = tmp.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def _line_height(font, gap: int = 0) -> int:
    tmp = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    bbox = tmp.textbbox((0, 0), "Ay", font=font)
    return bbox[3] - bbox[1] + gap


def _wrap_pixels(text: str, font, max_width: int, *, max_lines: int = 4) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if _text_width(trial, font) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
            if len(lines) >= max_lines:
                break
    if current and len(lines) < max_lines:
        lines.append(current)
    if len(lines) == max_lines and " ".join(words) != " ".join(lines):
        last = lines[-1]
        while _text_width(last + "…", font) > max_width and len(last) > 8:
            last = last[:-1]
        lines[-1] = last + "…"
    return lines[:max_lines]


def _draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    *,
    y: int,
    font,
    fill: str,
    canvas_w: int,
    line_gap: int,
) -> int:
    cy = y
    for line in lines:
        tw = _text_width(line, font)
        x = (canvas_w - tw) // 2
        draw.text((x, cy), line, fill=fill, font=font)
        cy += _line_height(font, line_gap)
    return cy


def _draw_bg(
    draw: ImageDraw.ImageDraw,
    spec: LayoutSpec,
    *,
    variant: str,
    seed: int,
    accent: str,
) -> None:
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
    for band_y, color in ((s + 20, gold), (h - s - 40, orange)):
        pts: list[tuple[int, int]] = []
        x = s
        while x < w - s:
            pts.append((x, band_y + rng.randint(-14, 14)))
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


def _cta_top(spec: LayoutSpec) -> int:
    return spec.height - spec.safe - spec.cta_height


def _draw_cta(
    draw: ImageDraw.ImageDraw,
    *,
    spec: LayoutSpec,
    text: str,
    accent: str,
) -> None:
    font = load_font(spec.cta_font, bold=True)
    label = text.strip()
    tw = _text_width(label, font)
    pad_x = 40
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


def _render_feed_hero(
    *,
    spec: LayoutSpec,
    topic: str,
    title: str,
    subtitle: str,
    body: str,
    cta: str,
    variant: str,
    accent: str,
) -> Image.Image:
    """
    Layout feed v4 — logo hero grande e centrato (30–40% area visiva):
    1. Titolo grande sopra o sotto il logo (variante)
    2. Sottotitolo breve
    3. Logo hero centrato con glow/neon
    4. Testo breve
    5. CTA visiva in basso
    """
    seed = hash(f"{title}:{spec.platform}:{variant}") % 10_000
    img = Image.new("RGB", (spec.width, spec.height), PALETTE["bg_dark"])
    draw = ImageDraw.Draw(img)
    _draw_bg(draw, spec, variant=variant, seed=seed, accent=accent)

    content_w = spec.width - spec.safe * 2
    title_font = load_font(spec.title_size, bold=True)
    subtitle_font = load_font(spec.subtitle_size)
    body_font = load_font(spec.body_size)

    title_lines = _wrap_pixels(title, title_font, content_w, max_lines=2)
    subtitle_lines = _wrap_pixels(subtitle, subtitle_font, content_w, max_lines=2)
    body_lines = _wrap_pixels(body, body_font, int(content_w * 0.9), max_lines=spec.body_max_lines)

    title_above = variant == "primary"
    cta_y = _cta_top(spec)
    body_block_h = len(body_lines) * _line_height(body_font, spec.line_gap_body) + 8
    hero_size = spec.hero_logo
    hero_cy = spec.height // 2 - 12

    if title_above:
        y = spec.safe + 6
        y = _draw_centered_lines(
            draw, title_lines, y=y, font=title_font, fill=PALETTE["text"],
            canvas_w=spec.width, line_gap=spec.line_gap_title,
        )
        y += 10
        y = _draw_centered_lines(
            draw, subtitle_lines, y=y, font=subtitle_font, fill=PALETTE["gold"],
            canvas_w=spec.width, line_gap=6,
        )
        top_text_bottom = y
        hero_cy = max(
            top_text_bottom + hero_size // 2 + 32,
            min(hero_cy, cta_y - body_block_h - hero_size // 2 - 40),
        )
    else:
        y = spec.safe + 6
        y = _draw_centered_lines(
            draw, subtitle_lines, y=y, font=subtitle_font, fill=PALETTE["gold"],
            canvas_w=spec.width, line_gap=6,
        )
        top_text_bottom = y
        hero_cy = max(
            top_text_bottom + hero_size // 2 + 44,
            min(spec.height // 2 + 8, cta_y - body_block_h - hero_size // 2 - 100),
        )

    img = draw_hero_logo_centered(
        img, topic, accent=accent,
        center=(spec.width // 2, hero_cy),
        size=hero_size,
        variant=variant,
    )
    draw = ImageDraw.Draw(img)

    if title_above:
        y = hero_cy + hero_size // 2 + 28
    else:
        y = hero_cy + hero_size // 2 + 24
        y = _draw_centered_lines(
            draw, title_lines, y=y, font=title_font, fill=PALETTE["text"],
            canvas_w=spec.width, line_gap=spec.line_gap_title,
        )
        y += 12

    max_body_y = cta_y - body_block_h - 10
    y = min(y, max_body_y)
    _draw_centered_lines(
        draw, body_lines, y=y, font=body_font, fill=PALETTE["muted"],
        canvas_w=spec.width, line_gap=spec.line_gap_body,
    )
    _draw_cta(draw, spec=spec, text=cta, accent=accent)
    return paste_brand_watermark(img, scale=0.042)


def render_feed_post(
    *,
    platform: str,
    topic: str,
    title: str,
    subtitle: str,
    body: str,
    cta: str,
    variant: str = "primary",
    accent: str = PALETTE["accent"],
) -> Image.Image:
    spec = INSTAGRAM if platform == "instagram" else FACEBOOK
    return _render_feed_hero(
        spec=spec, topic=topic, title=title, subtitle=subtitle,
        body=body, cta=cta, variant=variant, accent=accent,
    )


def design_description(topic: str, variant: str, platform: str) -> str:
    title_pos = "sopra" if variant == "primary" else "sotto"
    style = "griglia oro/arancione" if variant == "primary" else "bordo blu elettrico"
    return (
        f"{platform.upper()} 1080×1350 · safe 100px · {variant} · {topic_label(topic)} · "
        f"logo hero centrato ~38% · PNG trasparente · glow/neon · titolo {title_pos} logo · "
        f"{style} · CTA visiva · zero link/URL."
    )


def render_feed_portrait(**kwargs) -> Image.Image:
    return render_feed_post(platform="instagram", **kwargs)
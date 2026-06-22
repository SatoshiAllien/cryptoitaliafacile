#!/usr/bin/env python3
"""Renderer feed ordinato — Instagram 1080×1350, Facebook 1200×1200."""

from __future__ import annotations

import random
from dataclasses import dataclass

from PIL import Image, ImageDraw

from brand_overlay import apply_topic_logo_top_left, draw_center_topic_icon, paste_brand_watermark
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
    logo_size: int
    center_icon: int
    cta_height: int
    cta_font: int
    line_gap_title: int = 10
    line_gap_body: int = 8


INSTAGRAM = LayoutSpec(
    width=1080, height=1350, safe=80,
    title_size=54, subtitle_size=28, body_size=26,
    logo_size=72, center_icon=112, cta_height=76, cta_font=26,
)
FACEBOOK = LayoutSpec(
    width=1200, height=1200, safe=100,
    title_size=50, subtitle_size=26, body_size=24,
    logo_size=72, center_icon=104, cta_height=72, cta_font=24,
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


def _draw_bg(draw: ImageDraw.ImageDraw, w: int, h: int, *, variant: str, seed: int, accent: str) -> None:
    gradient2(draw, w, h, PALETTE["bg_dark"], PALETTE["bg_mid"])
    spacing = 48 if variant == "primary" else 40
    grid = PALETTE["grid"] if variant == "primary" else (18, 22, 34)
    for x in range(0, w, spacing):
        draw.line([(x, 0), (x, h)], fill=grid, width=1)
    for y in range(0, h, spacing):
        draw.line([(0, y), (w, y)], fill=grid, width=1)

    rng = random.Random(seed)
    gold = _hex(PALETTE["gold"])
    orange = _hex(accent)
    for band_y, color in ((int(h * 0.08), gold), (int(h * 0.9), orange)):
        pts: list[tuple[int, int]] = []
        x = 80
        while x < w - 80:
            pts.append((x, band_y + rng.randint(-18, 18)))
            x += rng.randint(90, 130)
        if len(pts) >= 2:
            draw.line(pts, fill=color, width=2)

    if variant == "alt":
        s = 80 if w == 1080 else 100
        draw.rounded_rectangle(
            (s - 4, s - 4, w - s + 4, h - s + 4),
            radius=24,
            outline=_hex(PALETTE["electric"]),
            width=2,
        )


def _draw_cta(
    draw: ImageDraw.ImageDraw,
    *,
    spec: LayoutSpec,
    text: str,
    accent: str,
) -> None:
    font = load_font(spec.cta_font, bold=True)
    label = text.upper() if len(text) < 28 else text
    tw = _text_width(label, font)
    pad_x = 40
    btn_w = min(spec.width - spec.safe * 2, tw + pad_x * 2)
    btn_h = spec.cta_height
    x1 = (spec.width - btn_w) // 2
    y1 = spec.height - spec.safe - btn_h
    x2, y2 = x1 + btn_w, y1 + btn_h
    draw.rounded_rectangle((x1, y1, x2, y2), radius=btn_h // 2, fill=_hex(accent))
    draw.text(
        (x1 + (btn_w - tw) // 2, y1 + (btn_h - spec.cta_font) // 2 - 2),
        label,
        fill="#0F172A",
        font=font,
    )


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
    """Layout fisso: logo alto-sx, titolo centrato, sottotitolo, icona centrale, testo, CTA."""
    spec = INSTAGRAM if platform == "instagram" else FACEBOOK
    seed = hash(f"{title}:{platform}:{variant}") % 10_000

    img = Image.new("RGB", (spec.width, spec.height), PALETTE["bg_dark"])
    draw = ImageDraw.Draw(img)
    _draw_bg(draw, spec.width, spec.height, variant=variant, seed=seed, accent=accent)

    safe = spec.safe
    content_w = spec.width - safe * 2

    title_font = load_font(spec.title_size, bold=True)
    subtitle_font = load_font(spec.subtitle_size)
    body_font = load_font(spec.body_size)

    title_lines = _wrap_pixels(title, title_font, content_w, max_lines=3)
    subtitle_lines = _wrap_pixels(subtitle, subtitle_font, content_w, max_lines=2)
    body_lines = _wrap_pixels(body, body_font, int(content_w * 0.92), max_lines=3)

    y = safe + spec.logo_size + 28
    y = _draw_centered_lines(
        draw, title_lines, y=y, font=title_font, fill=PALETTE["text"],
        canvas_w=spec.width, line_gap=spec.line_gap_title,
    )
    y += 16
    y = _draw_centered_lines(
        draw, subtitle_lines, y=y, font=subtitle_font, fill=PALETTE["gold"],
        canvas_w=spec.width, line_gap=6,
    )
    y += 28

    icon_y = y
    img = draw_center_topic_icon(
        img, topic, accent=accent,
        center=(spec.width // 2, icon_y + spec.center_icon // 2),
        size=spec.center_icon,
    )
    draw = ImageDraw.Draw(img)
    y = icon_y + spec.center_icon + 32

    y = _draw_centered_lines(
        draw, body_lines, y=y, font=body_font, fill=PALETTE["muted"],
        canvas_w=spec.width, line_gap=spec.line_gap_body,
    )

    _draw_cta(draw, spec=spec, text=cta, accent=accent)

    img = apply_topic_logo_top_left(
        img, topic, accent=accent,
        size=spec.logo_size, margin=safe,
    )
    img = paste_brand_watermark(img, scale=0.045 if platform == "facebook" else 0.05)
    return img


def design_description(topic: str, variant: str, platform: str) -> str:
    size = "1080×1350" if platform == "instagram" else "1200×1200"
    safe = "80px" if platform == "instagram" else "100px"
    style = "griglia oro/arancione" if variant == "primary" else "bordo blu elettrico"
    return (
        f"{platform.upper()} {size} · safe-area {safe} · topic {topic_label(topic)} · "
        f"{style} · logo alto-sx · titolo/sottotitolo centrati · icona centrale · CTA · nessun link."
    )


# Retrocompatibilità
def render_feed_portrait(**kwargs) -> Image.Image:
    return render_feed_post(platform="instagram", **kwargs)
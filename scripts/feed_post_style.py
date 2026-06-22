#!/usr/bin/env python3
"""Renderer premium 1080×1350 per feed Instagram e Facebook."""

from __future__ import annotations

import random

from PIL import Image, ImageDraw

from brand_overlay import apply_topic_logo_top_left, paste_brand_watermark
from image_style import JPEG_QUALITY, _hex, draw_cta_button, draw_multiline, gradient2, load_font
from topic_detect import topic_label

W, H = 1080, 1350

PALETTE = {
    "bg_dark": (8, 10, 18),
    "bg_mid": (14, 18, 32),
    "accent": "#F7931A",
    "gold": "#F4C430",
    "electric": "#3B82F6",
    "text": "#FFFFFF",
    "muted": "#94A3B8",
    "grid": (30, 38, 55),
}


def _draw_grid(draw: ImageDraw.ImageDraw, w: int, h: int, *, spacing: int = 48, color: tuple[int, int, int] = PALETTE["grid"]) -> None:
    for x in range(0, w, spacing):
        draw.line([(x, 0), (x, h)], fill=color, width=1)
    for y in range(0, h, spacing):
        draw.line([(0, y), (w, y)], fill=color, width=1)


def _draw_circuit_lines(draw: ImageDraw.ImageDraw, w: int, h: int, seed: int, accent: str) -> None:
    rng = random.Random(seed)
    gold = _hex(PALETTE["gold"])
    orange = _hex(accent)
    for band_y, color in ((int(h * 0.12), gold), (int(h * 0.82), orange)):
        pts: list[tuple[int, int]] = []
        x = 60
        while x < w - 60:
            y = band_y + rng.randint(-30, 30)
            pts.append((x, y))
            x += rng.randint(80, 140)
        if len(pts) >= 2:
            draw.line(pts, fill=color, width=2)
            for px, py in pts[::2]:
                draw.ellipse((px - 4, py - 4, px + 4, py + 4), fill=color)


def _draw_vignette(img: Image.Image) -> Image.Image:
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    w, h = img.size
    for i in range(40):
        alpha = int(i * 2.2)
        margin = i * 3
        draw.rectangle((margin, margin, w - margin, h - margin), outline=(0, 0, 0, alpha), width=2)
    return Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")


def _wrap_title(title: str, max_chars: int = 38) -> str:
    words = title.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if len(trial) <= max_chars:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return "\n".join(lines[:4])


def render_feed_portrait(
    *,
    topic: str,
    hook: str,
    body: str,
    cta: str,
    variant: str = "primary",
    accent: str = PALETTE["accent"],
) -> Image.Image:
    """Genera immagine 1080×1350 con logo topic in alto a sinistra."""
    seed = hash(f"{hook}:{variant}") % 10_000
    img = Image.new("RGB", (W, H), PALETTE["bg_dark"])
    draw = ImageDraw.Draw(img)
    gradient2(draw, W, H, PALETTE["bg_dark"], PALETTE["bg_mid"])

    grid_color = (22, 30, 48) if variant == "primary" else (18, 24, 40)
    _draw_grid(draw, W, H, spacing=54 if variant == "primary" else 42, color=grid_color)
    _draw_circuit_lines(draw, W, H, seed, accent)

    logo_size = 96
    logo_margin = 36
    content_x = logo_margin + logo_size + 28
    m = 64
    accent_hex = accent
    badge = topic_label(topic)
    badge_y = logo_margin + 18
    draw.rectangle((content_x, badge_y + 34, content_x + min(280, len(badge) * 11), badge_y + 38), fill=_hex(accent_hex))
    draw.text((content_x, badge_y), badge[:24], fill=_hex(PALETTE["gold"]), font=load_font(22, bold=True))

    title_y = logo_margin + logo_size + 36
    title_text = _wrap_title(hook, max_chars=34 if variant == "primary" else 32)
    title_size = 62 if variant == "primary" else 56
    draw_multiline(
        draw,
        (m, title_y),
        title_text,
        load_font(title_size, bold=True),
        PALETTE["text"],
        line_gap=8,
    )

    body_y = title_y + title_size * (title_text.count("\n") + 1) + 48
    body_lines = body
    if len(body) > 140:
        body_lines = body[:137] + "…"
    draw_multiline(draw, (m, body_y), f"⚡ {body_lines}", load_font(30), PALETTE["muted"], line_gap=10)

    cta_h = 88
    cta_y = H - m - cta_h - 48
    cta_w = W - m * 2
    draw_cta_button(
        draw,
        (m, cta_y, m + cta_w, cta_y + cta_h),
        f"👉 {cta.upper()}",
        accent_hex,
        font_size=28,
    )

    if variant == "alt":
        draw.rounded_rectangle(
            (m - 8, title_y - 24, W - m + 8, body_y + 120),
            radius=20,
            outline=_hex(PALETTE["electric"]),
            width=2,
        )

    img = _draw_vignette(img)
    img = apply_topic_logo_top_left(img, topic, accent=accent_hex)
    img = paste_brand_watermark(img)
    return img


def design_description(topic: str, variant: str) -> str:
    layout = "griglia tech + linee circuito oro/arancione" if variant == "primary" else "layout alternativo con bordo blu elettrico"
    return (
        f"Post 1080×1350 · topic {topic_label(topic)} · {layout} · "
        f"logo {topic} alto-sinistra · titolo grande bianco · CTA arancione Satoshi · nessun link."
    )
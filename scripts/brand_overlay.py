#!/usr/bin/env python3
"""Applica il logo brand su immagini post (angolo in basso a destra)."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LOGO = ROOT / "assets" / "img" / "brand" / "logo.png"


def load_logo(path: Path | None = None) -> Image.Image:
    logo_path = path or DEFAULT_LOGO
    if not logo_path.exists():
        raise FileNotFoundError(f"Logo non trovato: {logo_path}")
    return Image.open(logo_path).convert("RGBA")


def apply_logo(
    base: Image.Image,
    logo: Image.Image | None = None,
    *,
    scale: float = 0.16,
    margin: int | None = None,
    corner: str = "bottom-right",
    pad: int = 8,
    bg_alpha: int = 200,
) -> Image.Image:
    """Sovrappone logo con sfondo arrotondato semi-trasparente."""
    canvas = base.convert("RGBA")
    mark = logo or load_logo()

    target_w = max(48, int(canvas.width * scale))
    ratio = target_w / mark.width
    target_h = max(48, int(mark.height * ratio))
    mark = mark.resize((target_w, target_h), Image.Resampling.LANCZOS)

    m = margin if margin is not None else max(16, int(canvas.width * 0.03))
    box_w, box_h = target_w + pad * 2, target_h + pad * 2

    if corner == "bottom-right":
        x = canvas.width - box_w - m
        y = canvas.height - box_h - m
    elif corner == "bottom-left":
        x, y = m, canvas.height - box_h - m
    elif corner == "top-right":
        x, y = canvas.width - box_w - m, m
    else:
        x, y = m, m

    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw.rounded_rectangle(
        (x, y, x + box_w, y + box_h),
        radius=max(8, pad),
        fill=(255, 255, 255, bg_alpha),
    )
    overlay.paste(mark, (x + pad, y + pad), mark)
    return Image.alpha_composite(canvas, overlay).convert("RGB")


def apply_logo_file(src: Path, dst: Path | None = None, **kwargs) -> Path:
    out = dst or src
    result = apply_logo(Image.open(src), **kwargs)
    out.parent.mkdir(parents=True, exist_ok=True)
    result.save(out, quality=92, optimize=True)
    return out
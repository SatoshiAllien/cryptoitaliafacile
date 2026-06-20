#!/usr/bin/env python3
"""Genera thumbnail clickbait per post X (1200x675 — formato tweet)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from brand_overlay import apply_logo

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img" / "x" / "posts"
W, H = 1200, 675

TEMPLATES = {
    "bitcoin": {
        "bg": [(15, 23, 42), (180, 83, 9)],
        "accent": "#F7931A",
        "badge": "BITCOIN",
        "hook": "₿ YOU NEED TO SEE THIS",
        "sub": "BTC news · tap to learn more",
    },
    "regulation": {
        "bg": [(30, 27, 75), (67, 56, 202)],
        "accent": "#A5B4FC",
        "badge": "REGULATION",
        "hook": "⚖️ CRYPTO ALERT",
        "sub": "SEC · MiCA · laws that change everything",
    },
    "elon": {
        "bg": [(15, 23, 42), (30, 41, 59)],
        "accent": "#38BDF8",
        "badge": "ELON MUSK",
        "hook": "🔄 VIRAL REPOST",
        "sub": "What Elon said about Bitcoin & crypto",
    },
    "breaking": {
        "bg": [(127, 29, 29), (220, 38, 38)],
        "accent": "#FCA5A5",
        "badge": "BREAKING",
        "hook": "🚨 BTC BREAKING NEWS",
        "sub": "Real-time market update",
    },
}


def gradient(draw: ImageDraw.ImageDraw, c1: tuple[int, int, int], c2: tuple[int, int, int]) -> None:
    for y in range(H):
        t = y / max(H - 1, 1)
        color = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
        draw.line([(0, y), (W, y)], fill=color)


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def render(name: str, cfg: dict) -> Path:
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    gradient(draw, cfg["bg"][0], cfg["bg"][1])

    accent = cfg["accent"]
    draw.rounded_rectangle((48, 48, 420, 118), radius=28, fill=accent)
    draw.text((84, 72), cfg["badge"], fill=(15, 23, 42), font=load_font(32, bold=True))

    draw.text((48, 160), cfg["hook"], fill="#FFFFFF", font=load_font(58, bold=True))
    draw.text((48, 250), cfg["sub"], fill="#E2E8F0", font=load_font(28))

    draw.rounded_rectangle((48, 480, 560, 570), radius=22, outline=accent, width=4)
    draw.text((78, 510), "TAP TO READ MORE →", fill=accent, font=load_font(24, bold=True))
    draw.text((48, 600), "@TheRiser100x · cryptoitaliafacile", fill="#94A3B8", font=load_font(20))

    draw.ellipse((920, 140, 1140, 360), outline=accent, width=6)
    draw.text((968, 220), "₿", fill=accent, font=load_font(88, bold=True))

    img = apply_logo(img, scale=0.14)
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{name}.jpg"
    img.save(path, "JPEG", quality=92, optimize=True)
    return path


def main() -> None:
    for name, cfg in TEMPLATES.items():
        path = render(name, cfg)
        print("OK", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
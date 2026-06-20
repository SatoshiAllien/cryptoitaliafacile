#!/usr/bin/env python3
"""Genera immagini quadrate 1080x1080 per post Instagram @bitcoin.is.hope2030."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from brand_overlay import apply_branding

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img" / "instagram" / "posts"
W, H = 1080, 1080

TEMPLATES = {
    "bitcoin": {
        "bg": [(15, 23, 42), (180, 83, 9)],
        "accent": "#F7931A",
        "badge": "BITCOIN",
        "hook": "HOPE STARTS HERE",
        "sub": "Simple guide · zero hype",
    },
    "exchange": {
        "bg": [(6, 78, 59), (14, 116, 144)],
        "accent": "#34D399",
        "badge": "EXCHANGE",
        "hook": "BUY CRYPTO SAFELY",
        "sub": "Step by step for beginners",
    },
    "wallet": {
        "bg": [(30, 27, 75), (88, 28, 135)],
        "accent": "#A78BFA",
        "badge": "WALLET",
        "hook": "PROTECT YOUR CRYPTO",
        "sub": "Methods that actually work",
    },
    "sicurezza": {
        "bg": [(127, 29, 29), (69, 10, 10)],
        "accent": "#FCA5A5",
        "badge": "SECURITY",
        "hook": "AVOID THIS MISTAKE",
        "sub": "Anti-scam checklist",
    },
    "cardano": {
        "bg": [(15, 52, 96), (30, 64, 175)],
        "accent": "#60A5FA",
        "badge": "CARDANO",
        "hook": "ADA MADE SIMPLE",
        "sub": "For absolute beginners",
    },
    "ethereum": {
        "bg": [(49, 46, 129), (99, 102, 241)],
        "accent": "#C4B5FD",
        "badge": "ETHEREUM",
        "hook": "ETH WITHOUT CONFUSION",
        "sub": "Clear concepts in 5 min",
    },
    "defi": {
        "bg": [(20, 83, 45), (6, 95, 70)],
        "accent": "#6EE7B7",
        "badge": "DeFi",
        "hook": "HOW IT REALLY WORKS",
        "sub": "No useless jargon",
    },
    "trend": {
        "bg": [(15, 118, 110), (13, 148, 136)],
        "accent": "#FDE047",
        "badge": "TREND 2026",
        "hook": "WHAT'S CHANGING NOW",
        "sub": "Macro trends explained",
    },
    "tip": {
        "bg": [(113, 63, 18), (217, 119, 6)],
        "accent": "#FDE68A",
        "badge": "CRYPTO TIP",
        "hook": "USE THIS TODAY",
        "sub": "30 seconds that save you",
    },
    "guide": {
        "bg": [(15, 23, 42), (27, 94, 63)],
        "accent": "#4ADE80",
        "badge": "FREE GUIDE",
        "hook": "TAP & LEARN",
        "sub": "@bitcoin.is.hope2030",
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

    draw.rounded_rectangle((56, 56, 380, 140), radius=32, fill=accent)
    draw.text((92, 88), cfg["badge"], fill=(15, 23, 42), font=load_font(40, bold=True))

    draw.text((56, 200), cfg["hook"], fill="#FFFFFF", font=load_font(72, bold=True))
    draw.text((56, 310), cfg["sub"], fill="#E2E8F0", font=load_font(36))

    draw.rounded_rectangle((56, 780, 620, 900), radius=28, outline=accent, width=5)
    draw.text((96, 825), "LINK IN BIO →", fill=accent, font=load_font(38, bold=True))

    draw.text((56, 960), "Bitcoin is Hope · cryptoitaliafacile", fill="#94A3B8", font=load_font(26))

    img = apply_branding(img, name, icon_box=(760, 420, 1020, 680), accent=accent, brand_scale=0.08)
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
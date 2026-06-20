#!/usr/bin/env python3
"""Genera thumbnail clickbait per post Facebook (1200x630)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from brand_overlay import apply_branding

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img" / "facebook" / "posts"
W, H = 1200, 630

TEMPLATES = {
    "bitcoin": {
        "bg": [(15, 23, 42), (180, 83, 9)],
        "accent": "#F7931A",
        "badge": "BITCOIN",
        "hook": "LO DEVI SAPERE ORA",
        "sub": "Guida semplice · zero hype",
    },
    "exchange": {
        "bg": [(6, 78, 59), (14, 116, 144)],
        "accent": "#34D399",
        "badge": "EXCHANGE",
        "hook": "COMPRA CRYPTO IN SICUREZZA",
        "sub": "Passo dopo passo per principianti",
    },
    "wallet": {
        "bg": [(30, 27, 75), (88, 28, 135)],
        "accent": "#A78BFA",
        "badge": "WALLET",
        "hook": "PROTEGGI LE TUE CRYPTO",
        "sub": "Metodi che funzionano davvero",
    },
    "sicurezza": {
        "bg": [(127, 29, 29), (69, 10, 10)],
        "accent": "#FCA5A5",
        "badge": "SICUREZZA",
        "hook": "EVITA QUESTO ERRORE",
        "sub": "Checklist anti-truffa",
    },
    "cardano": {
        "bg": [(15, 52, 96), (30, 64, 175)],
        "accent": "#60A5FA",
        "badge": "CARDANO",
        "hook": "ADA SPIEGATO FACILE",
        "sub": "Per chi inizia da zero",
    },
    "ethereum": {
        "bg": [(49, 46, 129), (99, 102, 241)],
        "accent": "#C4B5FD",
        "badge": "ETHEREUM",
        "hook": "ETH SENZA CONFUSIONE",
        "sub": "Concetti chiari in 5 minuti",
    },
    "defi": {
        "bg": [(20, 83, 45), (6, 95, 70)],
        "accent": "#6EE7B7",
        "badge": "DeFi",
        "hook": "SCOPRI COME FUNZIONA",
        "sub": "Senza tecnicismi inutili",
    },
    "trend": {
        "bg": [(15, 118, 110), (13, 148, 136)],
        "accent": "#FDE047",
        "badge": "TREND 2026",
        "hook": "COSA STA CAMBIANDO",
        "sub": "Macro trend spiegati semplice",
    },
    "tip": {
        "bg": [(113, 63, 18), (217, 119, 6)],
        "accent": "#FDE68A",
        "badge": "CRYPTO TIP",
        "hook": "TIP DA APPLICARE SUBITO",
        "sub": "30 secondi che ti salvano",
    },
    "guide": {
        "bg": [(15, 23, 42), (27, 94, 63)],
        "accent": "#4ADE80",
        "badge": "GUIDA GRATIS",
        "hook": "CLICCA E IMPARA",
        "sub": "The Little Satoshi News",
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
    draw.rounded_rectangle((48, 48, 320, 118), radius=28, fill=accent)
    badge_font = load_font(34, bold=True)
    draw.text((84, 72), cfg["badge"], fill=(15, 23, 42), font=badge_font)

    hook_font = load_font(62, bold=True)
    sub_font = load_font(30)
    brand_font = load_font(24, bold=True)

    draw.text((48, 170), cfg["hook"], fill="#FFFFFF", font=hook_font)
    draw.text((48, 260), cfg["sub"], fill="#E2E8F0", font=sub_font)

    draw.rounded_rectangle((48, 470, 520, 560), radius=22, outline=accent, width=4)
    draw.text((78, 500), "LEGGI LA GUIDA COMPLETA →", fill=accent, font=brand_font)

    draw.text((48, 585), "The Little Satoshi News · cryptoitaliafacile", fill="#94A3B8", font=load_font(20))

    img = apply_branding(img, name, icon_box=(920, 120, 1160, 360), accent=accent, brand_scale=0.07)
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
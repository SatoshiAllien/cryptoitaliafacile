#!/usr/bin/env python3
"""Genera immagini Stories 9:16 (1080x1920) per Facebook e Instagram."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from brand_overlay import apply_branding

ROOT = Path(__file__).resolve().parent.parent
W, H = 1080, 1920

FB_OUT = ROOT / "assets" / "img" / "facebook" / "stories"
IG_OUT = ROOT / "assets" / "img" / "instagram" / "stories"

FB_TEMPLATES = {
    "bitcoin": {
        "bg": [(15, 23, 42), (180, 83, 9)],
        "accent": "#F7931A",
        "badge": "BITCOIN",
        "hook": "LO DEVI\nSAPERE ORA",
        "sub": "Guida semplice · zero hype",
        "cta": "SCORRI SU ↑",
    },
    "exchange": {
        "bg": [(6, 78, 59), (14, 116, 144)],
        "accent": "#34D399",
        "badge": "EXCHANGE",
        "hook": "COMPRA CRYPTO\nIN SICUREZZA",
        "sub": "Passo dopo passo",
        "cta": "LEGGI LA GUIDA ↑",
    },
    "wallet": {
        "bg": [(30, 27, 75), (88, 28, 135)],
        "accent": "#A78BFA",
        "badge": "WALLET",
        "hook": "PROTEGGI LE\nTUE CRYPTO",
        "sub": "Metodi che funzionano",
        "cta": "APRI LA GUIDA ↑",
    },
    "sicurezza": {
        "bg": [(127, 29, 29), (69, 10, 10)],
        "accent": "#FCA5A5",
        "badge": "SICUREZZA",
        "hook": "EVITA QUESTO\nERRORE",
        "sub": "Checklist anti-truffa",
        "cta": "SCOPRI COME ↑",
    },
    "cardano": {
        "bg": [(15, 52, 96), (30, 64, 175)],
        "accent": "#60A5FA",
        "badge": "CARDANO",
        "hook": "ADA SPIEGATO\nFACILE",
        "sub": "Per chi inizia da zero",
        "cta": "LEGGI ORA ↑",
    },
    "ethereum": {
        "bg": [(49, 46, 129), (99, 102, 241)],
        "accent": "#C4B5FD",
        "badge": "ETHEREUM",
        "hook": "ETH SENZA\nCONFUSIONE",
        "sub": "Concetti chiari in 5 min",
        "cta": "GUIDA GRATIS ↑",
    },
    "defi": {
        "bg": [(20, 83, 45), (6, 95, 70)],
        "accent": "#6EE7B7",
        "badge": "DeFi",
        "hook": "SCOPRI COME\nFUNZIONA",
        "sub": "Senza tecnicismi",
        "cta": "APPROFONDISCI ↑",
    },
    "trend": {
        "bg": [(15, 118, 110), (13, 148, 136)],
        "accent": "#FDE047",
        "badge": "TREND 2026",
        "hook": "COSA STA\nCAMBIANDO",
        "sub": "Macro trend spiegati",
        "cta": "LEGGI TUTTO ↑",
    },
    "tip": {
        "bg": [(113, 63, 18), (217, 119, 6)],
        "accent": "#FDE68A",
        "badge": "CRYPTO TIP",
        "hook": "TIP DA\nAPPLICARE SUBITO",
        "sub": "30 secondi che ti salvano",
        "cta": "SALVA IL POST ↑",
    },
    "guide": {
        "bg": [(15, 23, 42), (27, 94, 63)],
        "accent": "#4ADE80",
        "badge": "GUIDA GRATIS",
        "hook": "CLICCA E\nIMPARA",
        "sub": "The Little Satoshi News",
        "cta": "LEGGI LA GUIDA ↑",
    },
}

IG_TEMPLATES = {
    "bitcoin": {
        "bg": [(15, 23, 42), (180, 83, 9)],
        "accent": "#F7931A",
        "badge": "BITCOIN",
        "hook": "HOPE STARTS\nHERE",
        "sub": "Simple guide · zero hype",
        "cta": "LINK IN BIO ↑",
    },
    "exchange": {
        "bg": [(6, 78, 59), (14, 116, 144)],
        "accent": "#34D399",
        "badge": "EXCHANGE",
        "hook": "BUY CRYPTO\nSAFELY",
        "sub": "Step by step",
        "cta": "TAP TO LEARN ↑",
    },
    "wallet": {
        "bg": [(30, 27, 75), (88, 28, 135)],
        "accent": "#A78BFA",
        "badge": "WALLET",
        "hook": "PROTECT YOUR\nCRYPTO",
        "sub": "Methods that work",
        "cta": "READ MORE ↑",
    },
    "sicurezza": {
        "bg": [(127, 29, 29), (69, 10, 10)],
        "accent": "#FCA5A5",
        "badge": "SECURITY",
        "hook": "AVOID THIS\nMISTAKE",
        "sub": "Anti-scam checklist",
        "cta": "LEARN HOW ↑",
    },
    "cardano": {
        "bg": [(15, 52, 96), (30, 64, 175)],
        "accent": "#60A5FA",
        "badge": "CARDANO",
        "hook": "ADA MADE\nSIMPLE",
        "sub": "For beginners",
        "cta": "READ NOW ↑",
    },
    "ethereum": {
        "bg": [(49, 46, 129), (99, 102, 241)],
        "accent": "#C4B5FD",
        "badge": "ETHEREUM",
        "hook": "ETH WITHOUT\nCONFUSION",
        "sub": "Clear in 5 min",
        "cta": "FREE GUIDE ↑",
    },
    "defi": {
        "bg": [(20, 83, 45), (6, 95, 70)],
        "accent": "#6EE7B7",
        "badge": "DeFi",
        "hook": "HOW IT REALLY\nWORKS",
        "sub": "No useless jargon",
        "cta": "DIVE IN ↑",
    },
    "trend": {
        "bg": [(15, 118, 110), (13, 148, 136)],
        "accent": "#FDE047",
        "badge": "TREND 2026",
        "hook": "WHAT'S\nCHANGING",
        "sub": "Macro trends explained",
        "cta": "READ ALL ↑",
    },
    "tip": {
        "bg": [(113, 63, 18), (217, 119, 6)],
        "accent": "#FDE68A",
        "badge": "CRYPTO TIP",
        "hook": "USE THIS\nTODAY",
        "sub": "30 seconds that save you",
        "cta": "SAVE THIS ↑",
    },
    "guide": {
        "bg": [(15, 23, 42), (27, 94, 63)],
        "accent": "#4ADE80",
        "badge": "FREE GUIDE",
        "hook": "TAP &\nLEARN",
        "sub": "@bitcoin.is.hope2030",
        "cta": "LINK IN BIO ↑",
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
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_multiline(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, font, fill: str, line_gap: int = 12) -> None:
    x, y = xy
    for line in text.split("\n"):
        draw.text((x, y), line, fill=fill, font=font)
        bbox = draw.textbbox((x, y), line, font=font)
        y = bbox[3] + line_gap


def render(name: str, cfg: dict, out_dir: Path, footer: str) -> Path:
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    gradient(draw, cfg["bg"][0], cfg["bg"][1])
    accent = cfg["accent"]

    draw.rounded_rectangle((72, 120, 420, 220), radius=36, fill=accent)
    draw.text((108, 158), cfg["badge"], fill=(15, 23, 42), font=load_font(44, bold=True))

    draw_multiline(draw, (72, 300), cfg["hook"], load_font(88, bold=True), "#FFFFFF", line_gap=8)
    draw.text((72, 620), cfg["sub"], fill="#E2E8F0", font=load_font(40))

    draw.rounded_rectangle((72, 1580, 720, 1720), radius=32, outline=accent, width=6)
    draw.text((120, 1635), cfg["cta"], fill=accent, font=load_font(46, bold=True))

    draw.text((72, 1780), footer, fill="#94A3B8", font=load_font(28))

    img = apply_branding(img, name, icon_box=(700, 820, 980, 1100), accent=accent, brand_scale=0.09)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{name}.jpg"
    img.save(path, "JPEG", quality=92, optimize=True)
    return path


def main() -> None:
    for name, cfg in FB_TEMPLATES.items():
        path = render(name, cfg, FB_OUT, "The Little Satoshi News · cryptoitaliafacile")
        print("OK FB", path.relative_to(ROOT))
    for name, cfg in IG_TEMPLATES.items():
        path = render(name, cfg, IG_OUT, "Bitcoin is Hope · cryptoitaliafacile")
        print("OK IG", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
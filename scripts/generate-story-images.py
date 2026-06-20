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
        "bg": [(8, 12, 28), (120, 53, 15), (247, 147, 26)],
        "accent": "#00F0FF",
        "accent2": "#F7931A",
        "emoji": "₿",
        "badge": "BITCOIN",
        "hook": "🔥 LO DEVI\nSAPERE ORA",
        "sub": "✨ Guida semplice · zero hype",
        "cta": "📱 SCANSIONA QR ↓",
    },
    "exchange": {
        "bg": [(6, 20, 35), (6, 78, 59), (14, 165, 233)],
        "accent": "#34D399",
        "accent2": "#00F0FF",
        "emoji": "💱",
        "badge": "EXCHANGE",
        "hook": "🚀 COMPRA CRYPTO\nIN SICUREZZA",
        "sub": "📋 Passo dopo passo",
        "cta": "📱 SCANSIONA QR ↓",
    },
    "wallet": {
        "bg": [(15, 10, 40), (49, 46, 129), (168, 85, 247)],
        "accent": "#A78BFA",
        "accent2": "#FF2A6D",
        "emoji": "🔐",
        "badge": "WALLET",
        "hook": "🛡️ PROTEGGI LE\nTUE CRYPTO",
        "sub": "💪 Metodi che funzionano",
        "cta": "📱 SCANSIONA QR ↓",
    },
    "sicurezza": {
        "bg": [(30, 8, 18), (127, 29, 29), (248, 113, 113)],
        "accent": "#FCA5A5",
        "accent2": "#FDE047",
        "emoji": "⚠️",
        "badge": "SICUREZZA",
        "hook": "🚨 EVITA QUESTO\nERRORE",
        "sub": "✅ Checklist anti-truffa",
        "cta": "📱 SCANSIONA QR ↓",
    },
    "cardano": {
        "bg": [(8, 15, 40), (15, 52, 96), (59, 130, 246)],
        "accent": "#60A5FA",
        "accent2": "#34D399",
        "emoji": "🔷",
        "badge": "CARDANO",
        "hook": "💎 ADA SPIEGATO\nFACILE",
        "sub": "🎯 Per chi inizia da zero",
        "cta": "📱 SCANSIONA QR ↓",
    },
    "ethereum": {
        "bg": [(12, 10, 45), (49, 46, 129), (129, 140, 248)],
        "accent": "#C4B5FD",
        "accent2": "#00F0FF",
        "emoji": "⟠",
        "badge": "ETHEREUM",
        "hook": "⚡ ETH SENZA\nCONFUSIONE",
        "sub": "🧠 Concetti chiari in 5 min",
        "cta": "📱 SCANSIONA QR ↓",
    },
    "defi": {
        "bg": [(6, 25, 20), (20, 83, 45), (52, 211, 153)],
        "accent": "#6EE7B7",
        "accent2": "#FDE047",
        "emoji": "🌊",
        "badge": "DeFi",
        "hook": "🔬 SCOPRI COME\nFUNZIONA",
        "sub": "📖 Senza tecnicismi",
        "cta": "📱 SCANSIONA QR ↓",
    },
    "trend": {
        "bg": [(8, 20, 30), (15, 118, 110), (45, 212, 191)],
        "accent": "#FDE047",
        "accent2": "#FF2A6D",
        "emoji": "📈",
        "badge": "TREND 2026",
        "hook": "🌍 COSA STA\nCAMBIANDO",
        "sub": "🔭 Macro trend spiegati",
        "cta": "📱 SCANSIONA QR ↓",
    },
    "tip": {
        "bg": [(25, 15, 8), (113, 63, 18), (251, 191, 36)],
        "accent": "#FDE68A",
        "accent2": "#FF2A6D",
        "emoji": "💡",
        "badge": "CRYPTO TIP",
        "hook": "⚡ TIP DA\nAPPLICARE SUBITO",
        "sub": "⏱️ 30 secondi che ti salvano",
        "cta": "📱 SCANSIONA QR ↓",
    },
    "guide": {
        "bg": [(8, 12, 28), (15, 23, 42), (34, 197, 94)],
        "accent": "#4ADE80",
        "accent2": "#00F0FF",
        "emoji": "📚",
        "badge": "GUIDA GRATIS",
        "hook": "🎯 CLICCA E\nIMPARA",
        "sub": "✨ The Little Satoshi News",
        "cta": "📱 SCANSIONA QR ↓",
    },
}

IG_TEMPLATES = {
    "bitcoin": {
        "bg": [(8, 12, 28), (120, 53, 15), (247, 147, 26)],
        "accent": "#00F0FF",
        "accent2": "#FF2A6D",
        "emoji": "₿",
        "badge": "BITCOIN",
        "hook": "🔥 HOPE STARTS\nHERE",
        "sub": "✨ Simple guide · zero hype",
        "cta": "📱 SCAN QR ↓",
    },
    "exchange": {
        "bg": [(6, 20, 35), (6, 78, 59), (14, 165, 233)],
        "accent": "#34D399",
        "accent2": "#00F0FF",
        "emoji": "💱",
        "badge": "EXCHANGE",
        "hook": "🚀 BUY CRYPTO\nSAFELY",
        "sub": "📋 Step by step",
        "cta": "📱 SCAN QR ↓",
    },
    "wallet": {
        "bg": [(15, 10, 40), (49, 46, 129), (168, 85, 247)],
        "accent": "#A78BFA",
        "accent2": "#FF2A6D",
        "emoji": "🔐",
        "badge": "WALLET",
        "hook": "🛡️ PROTECT YOUR\nCRYPTO",
        "sub": "💪 Methods that work",
        "cta": "📱 SCAN QR ↓",
    },
    "sicurezza": {
        "bg": [(30, 8, 18), (127, 29, 29), (248, 113, 113)],
        "accent": "#FCA5A5",
        "accent2": "#FDE047",
        "emoji": "⚠️",
        "badge": "SECURITY",
        "hook": "🚨 AVOID THIS\nMISTAKE",
        "sub": "✅ Anti-scam checklist",
        "cta": "📱 SCAN QR ↓",
    },
    "cardano": {
        "bg": [(8, 15, 40), (15, 52, 96), (59, 130, 246)],
        "accent": "#60A5FA",
        "accent2": "#34D399",
        "emoji": "🔷",
        "badge": "CARDANO",
        "hook": "💎 ADA MADE\nSIMPLE",
        "sub": "🎯 For beginners",
        "cta": "📱 SCAN QR ↓",
    },
    "ethereum": {
        "bg": [(12, 10, 45), (49, 46, 129), (129, 140, 248)],
        "accent": "#C4B5FD",
        "accent2": "#00F0FF",
        "emoji": "⟠",
        "badge": "ETHEREUM",
        "hook": "⚡ ETH WITHOUT\nCONFUSION",
        "sub": "🧠 Clear in 5 min",
        "cta": "📱 SCAN QR ↓",
    },
    "defi": {
        "bg": [(6, 25, 20), (20, 83, 45), (52, 211, 153)],
        "accent": "#6EE7B7",
        "accent2": "#FDE047",
        "emoji": "🌊",
        "badge": "DeFi",
        "hook": "🔬 HOW IT REALLY\nWORKS",
        "sub": "📖 No useless jargon",
        "cta": "📱 SCAN QR ↓",
    },
    "trend": {
        "bg": [(8, 20, 30), (15, 118, 110), (45, 212, 191)],
        "accent": "#FDE047",
        "accent2": "#FF2A6D",
        "emoji": "📈",
        "badge": "TREND 2026",
        "hook": "🌍 WHAT'S\nCHANGING",
        "sub": "🔭 Macro trends explained",
        "cta": "📱 SCAN QR ↓",
    },
    "tip": {
        "bg": [(25, 15, 8), (113, 63, 18), (251, 191, 36)],
        "accent": "#FDE68A",
        "accent2": "#FF2A6D",
        "emoji": "💡",
        "badge": "CRYPTO TIP",
        "hook": "⚡ USE THIS\nTODAY",
        "sub": "⏱️ 30 seconds that save you",
        "cta": "📱 SCAN QR ↓",
    },
    "guide": {
        "bg": [(8, 12, 28), (15, 23, 42), (34, 197, 94)],
        "accent": "#4ADE80",
        "accent2": "#00F0FF",
        "emoji": "📚",
        "badge": "FREE GUIDE",
        "hook": "🎯 TAP &\nLEARN",
        "sub": "✨ @krown.82",
        "cta": "📱 SCAN QR ↓",
    },
}


def gradient3(draw: ImageDraw.ImageDraw, c1: tuple[int, int, int], c2: tuple[int, int, int], c3: tuple[int, int, int]) -> None:
    mid = H // 2
    for y in range(H):
        if y < mid:
            t = y / max(mid - 1, 1)
            color = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
        else:
            t = (y - mid) / max(H - mid - 1, 1)
            color = tuple(int(c2[i] + (c3[i] - c2[i]) * t) for i in range(3))
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
    gradient3(draw, cfg["bg"][0], cfg["bg"][1], cfg["bg"][2])
    accent = cfg["accent"]
    accent2 = cfg.get("accent2", accent)

    # Glow decorativo
    draw.ellipse((680, 80, 1060, 460), fill=(40, 55, 90))
    draw.ellipse((-80, 700, 280, 1060), fill=(35, 48, 75))

    draw.rounded_rectangle((56, 100, 500, 240), radius=40, fill=accent2)
    draw.rounded_rectangle((72, 116, 484, 224), radius=32, fill=accent)
    emoji = cfg.get("emoji", "✨")
    draw.text((96, 138), f"{emoji} {cfg['badge']}", fill=(15, 23, 42), font=load_font(42, bold=True))

    draw_multiline(draw, (56, 280), cfg["hook"], load_font(82, bold=True), "#FFFFFF", line_gap=6)
    draw.text((56, 600), cfg["sub"], fill="#E2E8F0", font=load_font(38))

    draw.rounded_rectangle((56, 820, 1024, 940), radius=28, fill=(10, 15, 32), outline=accent, width=4)
    draw.text((96, 868), "🌐 cryptoitaliafacile.com", fill=accent, font=load_font(40, bold=True))

    draw.rounded_rectangle((56, 1540, 820, 1680), radius=36, fill=(10, 15, 32), outline=accent2, width=5)
    draw.text((96, 1595), cfg["cta"], fill=accent, font=load_font(44, bold=True))

    draw.text((56, 1760), footer, fill="#94A3B8", font=load_font(28))

    img = apply_branding(img, name, icon_box=(700, 980, 980, 1260), accent=accent, brand_scale=0.09)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{name}.jpg"
    img.save(path, "JPEG", quality=93, optimize=True)
    return path


def main() -> None:
    for name, cfg in FB_TEMPLATES.items():
        path = render(name, cfg, FB_OUT, "📰 The Little Satoshi News · cryptoitaliafacile")
        print("OK FB", path.relative_to(ROOT))
    for name, cfg in IG_TEMPLATES.items():
        path = render(name, cfg, IG_OUT, "✨ @krown.82 · cryptoitaliafacile")
        print("OK IG", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
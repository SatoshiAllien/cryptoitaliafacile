#!/usr/bin/env python3
"""Stile condiviso clickbait: gradienti, griglia, glow, CTA 'Clicca qui'."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from brand_overlay import apply_branding

# Palette unica per ogni topic — colori ben distinti
TOPICS: dict[str, dict] = {
    "bitcoin": {
        "bg": [(8, 10, 28), (120, 55, 8), (251, 146, 60)],
        "accent": "#FBBF24",
        "accent2": "#F97316",
        "glow": (251, 191, 36),
        "grid": (60, 45, 25),
        "emoji": "₿",
        "badge": "BITCOIN",
        "hook_it": "🔥 LO DEVI\nSAPERE ORA",
        "hook_en": "🔥 HOPE STARTS\nHERE",
        "sub_it": "✨ Guida semplice · zero hype",
        "sub_en": "✨ Simple guide · zero hype",
    },
    "exchange": {
        "bg": [(5, 18, 38), (6, 95, 70), (56, 189, 248)],
        "accent": "#22D3EE",
        "accent2": "#34D399",
        "glow": (45, 212, 191),
        "grid": (20, 55, 60),
        "emoji": "💱",
        "badge": "EXCHANGE",
        "hook_it": "🚀 COMPRA CRYPTO\nIN SICUREZZA",
        "hook_en": "🚀 BUY CRYPTO\nSAFELY",
        "sub_it": "📋 Passo dopo passo",
        "sub_en": "📋 Step by step",
    },
    "wallet": {
        "bg": [(18, 8, 42), (88, 28, 135), (192, 132, 252)],
        "accent": "#C084FC",
        "accent2": "#FF2A6D",
        "glow": (216, 180, 254),
        "grid": (45, 25, 65),
        "emoji": "🔐",
        "badge": "WALLET",
        "hook_it": "🛡️ PROTEGGI LE\nTUE CRYPTO",
        "hook_en": "🛡️ PROTECT YOUR\nCRYPTO",
        "sub_it": "💪 Metodi che funzionano",
        "sub_en": "💪 Methods that work",
    },
    "sicurezza": {
        "bg": [(35, 6, 16), (153, 27, 27), (248, 113, 113)],
        "accent": "#FCA5A5",
        "accent2": "#FDE047",
        "glow": (252, 165, 165),
        "grid": (70, 25, 30),
        "emoji": "⚠️",
        "badge": "SICUREZZA",
        "badge_en": "SECURITY",
        "hook_it": "🚨 EVITA QUESTO\nERRORE",
        "hook_en": "🚨 AVOID THIS\nMISTAKE",
        "sub_it": "✅ Checklist anti-truffa",
        "sub_en": "✅ Anti-scam checklist",
    },
    "cardano": {
        "bg": [(8, 14, 42), (29, 78, 216), (96, 165, 250)],
        "accent": "#60A5FA",
        "accent2": "#34D399",
        "glow": (96, 165, 250),
        "grid": (25, 40, 75),
        "emoji": "🔷",
        "badge": "CARDANO",
        "hook_it": "💎 ADA SPIEGATO\nFACILE",
        "hook_en": "💎 ADA MADE\nSIMPLE",
        "sub_it": "🎯 Per chi inizia da zero",
        "sub_en": "🎯 For beginners",
    },
    "ethereum": {
        "bg": [(12, 8, 48), (67, 56, 202), (165, 180, 252)],
        "accent": "#A5B4FC",
        "accent2": "#00F0FF",
        "glow": (129, 140, 248),
        "grid": (35, 35, 80),
        "emoji": "⟠",
        "badge": "ETHEREUM",
        "hook_it": "⚡ ETH SENZA\nCONFUSIONE",
        "hook_en": "⚡ ETH WITHOUT\nCONFUSION",
        "sub_it": "🧠 Concetti chiari in 5 min",
        "sub_en": "🧠 Clear in 5 min",
    },
    "defi": {
        "bg": [(4, 28, 18), (21, 128, 61), (74, 222, 128)],
        "accent": "#4ADE80",
        "accent2": "#FDE047",
        "glow": (74, 222, 128),
        "grid": (18, 55, 40),
        "emoji": "🌊",
        "badge": "DeFi",
        "hook_it": "🔬 SCOPRI COME\nFUNZIONA",
        "hook_en": "🔬 HOW IT REALLY\nWORKS",
        "sub_it": "📖 Senza tecnicismi",
        "sub_en": "📖 No useless jargon",
    },
    "trend": {
        "bg": [(6, 38, 32), (15, 100, 75), (45, 212, 191)],
        "accent": "#FDE047",
        "accent2": "#FBBF24",
        "glow": (250, 204, 21),
        "grid": (22, 55, 48),
        "emoji": "📈",
        "badge": "TREND 2026",
        "hook_it": "🌍 COSA STA\nCAMBIANDO",
        "hook_en": "🌍 WHAT'S\nCHANGING",
        "sub_it": "🔭 Macro trend spiegati",
        "sub_en": "🔭 Macro trends explained",
    },
    "tip": {
        "bg": [(28, 12, 6), (146, 64, 14), (251, 191, 36)],
        "accent": "#FCD34D",
        "accent2": "#FF2A6D",
        "glow": (251, 191, 36),
        "grid": (65, 40, 18),
        "emoji": "💡",
        "badge": "CRYPTO TIP",
        "hook_it": "⚡ TIP DA\nAPPLICARE SUBITO",
        "hook_en": "⚡ USE THIS\nTODAY",
        "sub_it": "⏱️ 30 secondi che ti salvano",
        "sub_en": "⏱️ 30 seconds that save you",
    },
    "guide": {
        "bg": [(8, 12, 28), (15, 50, 90), (34, 197, 94)],
        "accent": "#4ADE80",
        "accent2": "#00F0FF",
        "glow": (52, 211, 153),
        "grid": (20, 45, 55),
        "emoji": "📚",
        "badge": "GUIDA GRATIS",
        "badge_en": "FREE GUIDE",
        "hook_it": "🎯 CLICCA E\nIMPARA",
        "hook_en": "🎯 TAP &\nLEARN",
        "sub_it": "✨ The Little Satoshi News",
        "sub_en": "✨ @krown.82",
    },
    "regulation": {
        "bg": [(20, 12, 50), (67, 56, 202), (129, 140, 248)],
        "accent": "#A5B4FC",
        "accent2": "#FDE047",
        "glow": (165, 180, 252),
        "grid": (35, 30, 70),
        "emoji": "⚖️",
        "badge": "REGULATION",
        "hook_it": "⚖️ CRYPTO ALERT",
        "hook_en": "⚖️ CRYPTO ALERT",
        "sub_it": "📜 SEC · MiCA · normative",
        "sub_en": "📜 SEC · MiCA · laws",
    },
    "elon": {
        "bg": [(10, 15, 35), (30, 58, 95), (56, 189, 248)],
        "accent": "#38BDF8",
        "accent2": "#FBBF24",
        "glow": (56, 189, 248),
        "grid": (25, 45, 65),
        "emoji": "🔄",
        "badge": "ELON MUSK",
        "hook_it": "🔄 VIRAL REPOST",
        "hook_en": "🔄 VIRAL REPOST",
        "sub_it": "🗣️ Cosa dice Elon sul crypto",
        "sub_en": "🗣️ What Elon said about BTC",
    },
    "breaking": {
        "bg": [(40, 6, 12), (185, 28, 28), (252, 165, 165)],
        "accent": "#FCA5A5",
        "accent2": "#FDE047",
        "glow": (248, 113, 113),
        "grid": (75, 20, 25),
        "emoji": "🚨",
        "badge": "BREAKING",
        "hook_it": "🚨 BTC BREAKING\nNEWS",
        "hook_en": "🚨 BTC BREAKING\nNEWS",
        "sub_it": "📡 Aggiornamento in tempo reale",
        "sub_en": "📡 Real-time market update",
    },
}

CTA = {
    "fb_post": "👉 CLICCA QUI",
    "fb_story": "👉 CLICCA QUI · SCANSIONA QR ↓",
    "ig_post": "👆 TAP HERE",
    "ig_story": "👆 TAP HERE · SCAN QR ↓",
    "x_post": "👉 TAP TO READ",
}


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def load_emoji_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in [
        "C:/Windows/Fonts/seguiemj.ttf",
        "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf",
        "/System/Library/Fonts/Apple Color Emoji.ttc",
    ]:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return load_font(size)


def _is_emoji_char(ch: str) -> bool:
    o = ord(ch)
    return o > 0x238C or ch in "₿⟠"


def draw_mixed_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font,
    fill: str,
    *,
    emoji_font=None,
) -> tuple[int, int]:
    ef = emoji_font or load_emoji_font(getattr(font, "size", 32))
    x, y = xy
    for ch in text:
        f = ef if _is_emoji_char(ch) else font
        draw.text((x, y), ch, fill=fill, font=f, embedded_color=True)
        bbox = draw.textbbox((x, y), ch, font=f)
        x = bbox[2]
    return x, y


def _hex(c: str) -> tuple[int, int, int]:
    c = c.lstrip("#")
    return tuple(int(c[i : i + 2], 16) for i in (0, 2, 4))


def gradient3(
    draw: ImageDraw.ImageDraw,
    w: int,
    h: int,
    c1: tuple[int, int, int],
    c2: tuple[int, int, int],
    c3: tuple[int, int, int],
) -> None:
    mid = h // 2
    for y in range(h):
        if y < mid:
            t = y / max(mid - 1, 1)
            color = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
        else:
            t = (y - mid) / max(h - mid - 1, 1)
            color = tuple(int(c2[i] + (c3[i] - c2[i]) * t) for i in range(3))
        draw.line([(0, y), (w, y)], fill=color)


def draw_grid(draw: ImageDraw.ImageDraw, w: int, h: int, grid_rgb: tuple[int, int, int], step: int = 44) -> None:
    gc = tuple(min(255, int(c * 1.35)) for c in grid_rgb)
    for x in range(0, w, step):
        draw.line([(x, 0), (x, h)], fill=gc, width=1)
    for y in range(0, h, step):
        draw.line([(0, y), (w, y)], fill=gc, width=1)


def draw_multiline(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font,
    fill: str,
    line_gap: int = 8,
) -> int:
    x, y = xy
    ef = load_emoji_font(getattr(font, "size", 48))
    for line in text.split("\n"):
        draw_mixed_text(draw, (x, y), line, font, fill, emoji_font=ef)
        tmp = ImageDraw.Draw(Image.new("RGB", (4, 4)))
        lh = 0
        for ch in line:
            f = ef if _is_emoji_char(ch) else font
            bbox = tmp.textbbox((0, 0), ch, font=f)
            lh = max(lh, bbox[3] - bbox[1])
        y += lh + line_gap
    return y


def draw_badge_pill(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, accent: str, accent2: str, font) -> None:
    ef = load_emoji_font(getattr(font, "size", 32))
    tmp = ImageDraw.Draw(Image.new("RGB", (4, 4)))
    tw, th = 0, 0
    for ch in text:
        f = ef if _is_emoji_char(ch) else font
        bbox = tmp.textbbox((0, 0), ch, font=f)
        tw += bbox[2] - bbox[0]
        th = max(th, bbox[3] - bbox[1])
    pad_x, pad_y = 36, 22
    w, h = tw + pad_x * 2, th + pad_y * 2
    draw.rounded_rectangle((x, y, x + w + 8, y + h + 8), radius=28, fill=_hex(accent2))
    draw.rounded_rectangle((x + 4, y + 4, x + w + 4, y + h + 4), radius=24, fill=_hex(accent))
    draw_mixed_text(draw, (x + pad_x, y + pad_y - 2), text, font, (15, 23, 42), emoji_font=ef)


def draw_cta_button(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    accent: str,
    accent2: str,
    *,
    font_size: int = 32,
) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle((x1, y1, x2, y2), radius=28, fill=_hex(accent2))
    draw.rounded_rectangle((x1 + 4, y1 + 4, x2 - 4, y2 - 4), radius=24, fill=_hex(accent))
    font = load_font(font_size, bold=True)
    ef = load_emoji_font(font_size)
    tmp = ImageDraw.Draw(Image.new("RGB", (4, 4)))
    tw, th = 0, 0
    for ch in text:
        f = ef if _is_emoji_char(ch) else font
        bbox = tmp.textbbox((0, 0), ch, font=f)
        tw += bbox[2] - bbox[0]
        th = max(th, bbox[3] - bbox[1])
    tx = x1 + (x2 - x1 - tw) // 2
    ty = y1 + (y2 - y1 - th) // 2 - 2
    draw_mixed_text(draw, (tx, ty), text, font, (15, 23, 42), emoji_font=ef)


def topic_cfg(name: str, *, lang: str = "it") -> dict:
    t = TOPICS[name]
    badge = t.get("badge_en", t["badge"]) if lang == "en" else t["badge"]
    hook = t["hook_en"] if lang == "en" else t["hook_it"]
    sub = t["sub_en"] if lang == "en" else t["sub_it"]
    return {
        **t,
        "badge_text": f"{t['emoji']} {badge}",
        "hook": hook,
        "sub": sub,
    }


def render_post(
    name: str,
    cfg: dict,
    *,
    width: int,
    height: int,
    cta: str,
    footer: str,
    icon_box: tuple[int, int, int, int],
    hook_size: int,
    sub_size: int,
    badge_size: int = 34,
    brand_scale: float = 0.08,
) -> Image.Image:
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)
    gradient3(draw, width, height, cfg["bg"][0], cfg["bg"][1], cfg["bg"][2])
    draw_grid(draw, width, height, cfg["grid"])

    margin = int(width * 0.04)

    draw_badge_pill(
        draw, margin, margin, cfg["badge_text"], cfg["accent"], cfg["accent2"], load_font(badge_size, bold=True)
    )

    hook_y = margin + int(height * 0.18)
    draw_multiline(draw, (margin, hook_y), cfg["hook"], load_font(hook_size, bold=True), "#FFFFFF", line_gap=4)

    sub_y = hook_y + int(height * 0.22)
    draw_mixed_text(draw, (margin, sub_y), cfg["sub"], load_font(sub_size), "#E2E8F0")

    cta_h = int(height * 0.14)
    cta_y = int(height * 0.72)
    cta_w = int(width * 0.55)
    draw_cta_button(
        draw,
        (margin, cta_y, margin + cta_w, cta_y + cta_h),
        cta,
        cfg["accent"],
        cfg["accent2"],
        font_size=max(22, int(height * 0.045)),
    )

    draw_mixed_text(
        draw,
        (margin, height - margin - 28),
        f"🌐 {footer}",
        load_font(max(18, int(height * 0.028))),
        "#94A3B8",
    )

    return apply_branding(img, name, icon_box=icon_box, accent=cfg["accent"], brand_scale=brand_scale)


def render_story(
    name: str,
    cfg: dict,
    *,
    cta: str,
    footer: str,
    width: int = 1080,
    height: int = 1920,
) -> Image.Image:
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)
    gradient3(draw, width, height, cfg["bg"][0], cfg["bg"][1], cfg["bg"][2])
    draw_grid(draw, width, height, cfg["grid"])

    draw_badge_pill(draw, 56, 90, cfg["badge_text"], cfg["accent"], cfg["accent2"], load_font(40, bold=True))
    draw_multiline(draw, (56, 280), cfg["hook"], load_font(78, bold=True), "#FFFFFF", line_gap=6)
    draw_mixed_text(draw, (56, 580), cfg["sub"], load_font(36), "#E2E8F0")

    draw.rounded_rectangle((56, 760, 1024, 880), radius=28, fill=(10, 15, 32), outline=_hex(cfg["accent"]), width=4)
    draw_mixed_text(draw, (96, 808), "🌐 cryptoitaliafacile.com", load_font(38, bold=True), cfg["accent"])

    draw_cta_button(draw, (56, 1480, 900, 1600), cta, cfg["accent"], cfg["accent2"], font_size=36)
    draw_mixed_text(draw, (56, 1760), footer, load_font(28), "#94A3B8")

    return apply_branding(img, name, icon_box=(700, 960, 980, 1220), accent=cfg["accent"], brand_scale=0.09)
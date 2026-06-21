#!/usr/bin/env python3
"""Stile professionale per post e story: pulito, emoji, palette per topic."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from brand_overlay import apply_branding

TOPICS: dict[str, dict] = {
    "bitcoin": {
        "bg": [(11, 17, 33), (30, 41, 59)],
        "accent": "#F59E0B",
        "emoji": "₿",
        "badge": "BITCOIN",
        "hook_it": "Lo devi sapere\nora 🔥",
        "hook_en": "Hope starts\nhere 🔥",
        "sub_it": "✨ Guida semplice, zero hype",
        "sub_en": "✨ Simple guide, zero hype",
    },
    "exchange": {
        "bg": [(10, 25, 38), (15, 55, 65)],
        "accent": "#14B8A6",
        "emoji": "💱",
        "badge": "EXCHANGE",
        "hook_it": "Compra crypto\nin sicurezza 🚀",
        "hook_en": "Buy crypto\nsafely 🚀",
        "sub_it": "📋 Passo dopo passo",
        "sub_en": "📋 Step by step",
    },
    "wallet": {
        "bg": [(18, 12, 48), (49, 46, 129)],
        "accent": "#A78BFA",
        "emoji": "🔐",
        "badge": "WALLET",
        "hook_it": "Proteggi le tue\ncrypto 🛡️",
        "hook_en": "Protect your\ncrypto 🛡️",
        "sub_it": "💪 Metodi che funzionano",
        "sub_en": "💪 Methods that work",
    },
    "sicurezza": {
        "bg": [(35, 10, 20), (100, 25, 35)],
        "accent": "#F87171",
        "emoji": "⚠️",
        "badge": "SICUREZZA",
        "badge_en": "SECURITY",
        "hook_it": "Evita questo\nerrore 🚨",
        "hook_en": "Avoid this\nmistake 🚨",
        "sub_it": "✅ Checklist anti-truffa",
        "sub_en": "✅ Anti-scam checklist",
    },
    "cardano": {
        "bg": [(12, 20, 48), (30, 64, 120)],
        "accent": "#38BDF8",
        "emoji": "🔷",
        "badge": "CARDANO",
        "hook_it": "ADA spiegato\nfacile 💎",
        "hook_en": "ADA made\nsimple 💎",
        "sub_it": "🎯 Per chi inizia da zero",
        "sub_en": "🎯 For beginners",
    },
    "ethereum": {
        "bg": [(15, 12, 45), (55, 48, 140)],
        "accent": "#818CF8",
        "emoji": "⟠",
        "badge": "ETHEREUM",
        "hook_it": "ETH senza\nconfusione ⚡",
        "hook_en": "ETH without\nconfusion ⚡",
        "sub_it": "🧠 Concetti chiari in 5 min",
        "sub_en": "🧠 Clear in 5 min",
    },
    "defi": {
        "bg": [(8, 28, 24), (20, 70, 50)],
        "accent": "#34D399",
        "emoji": "🌊",
        "badge": "DeFi",
        "hook_it": "Scopri come\nfunziona 🔬",
        "hook_en": "How it really\nworks 🔬",
        "sub_it": "📖 Senza tecnicismi",
        "sub_en": "📖 No useless jargon",
    },
    "trend": {
        "bg": [(8, 32, 30), (15, 80, 65)],
        "accent": "#FACC15",
        "emoji": "📈",
        "badge": "TREND 2026",
        "hook_it": "Cosa sta\ncambiando 🌍",
        "hook_en": "What's\nchanging 🌍",
        "sub_it": "🔭 Macro trend spiegati",
        "sub_en": "🔭 Macro trends explained",
    },
    "tip": {
        "bg": [(32, 18, 8), (120, 55, 18)],
        "accent": "#FBBF24",
        "emoji": "💡",
        "badge": "CRYPTO TIP",
        "hook_it": "Tip da usare\nsubito ⚡",
        "hook_en": "Use this\ntoday ⚡",
        "sub_it": "⏱️ 30 secondi che ti salvano",
        "sub_en": "⏱️ 30 seconds that save you",
    },
    "guide": {
        "bg": [(11, 17, 33), (22, 78, 55)],
        "accent": "#4ADE80",
        "emoji": "📚",
        "badge": "GUIDA GRATIS",
        "badge_en": "FREE GUIDE",
        "hook_it": "Clicca e\nimpara 🎯",
        "hook_en": "Tap &\nlearn 🎯",
        "sub_it": "✨ The Little Satoshi News",
        "sub_en": "✨ @krown.82",
    },
    "regulation": {
        "bg": [(18, 14, 48), (45, 45, 110)],
        "accent": "#93C5FD",
        "emoji": "⚖️",
        "badge": "REGULATION",
        "hook_it": "Crypto alert ⚖️",
        "hook_en": "Crypto alert ⚖️",
        "sub_it": "📜 SEC · MiCA · normative",
        "sub_en": "📜 SEC · MiCA · laws",
    },
    "elon": {
        "bg": [(12, 18, 38), (25, 60, 95)],
        "accent": "#38BDF8",
        "emoji": "🔄",
        "badge": "ELON MUSK",
        "hook_it": "Viral repost 🔄",
        "hook_en": "Viral repost 🔄",
        "sub_it": "🗣️ Cosa dice Elon sul crypto",
        "sub_en": "🗣️ What Elon said about BTC",
    },
    "breaking": {
        "bg": [(40, 8, 14), (140, 28, 35)],
        "accent": "#FB7185",
        "emoji": "🚨",
        "badge": "BREAKING",
        "hook_it": "BTC breaking\nnews 🚨",
        "hook_en": "BTC breaking\nnews 🚨",
        "sub_it": "📡 Aggiornamento in tempo reale",
        "sub_en": "📡 Real-time market update",
    },
}

CTA = {
    "fb_post": "👉 Clicca qui",
    "fb_story": "👉 Clicca qui · QR ↓",
    "ig_post": "👆 Tap here",
    "ig_story": "👆 Tap here · QR ↓",
    "x_post": "👉 Tap to read",
}

JPEG_QUALITY = 95


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


def _hex(c: str) -> tuple[int, int, int]:
    c = c.lstrip("#")
    return tuple(int(c[i : i + 2], 16) for i in (0, 2, 4))


def _text_width(text: str, font, emoji_font) -> int:
    tmp = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    w = 0
    for ch in text:
        f = emoji_font if _is_emoji_char(ch) else font
        bbox = tmp.textbbox((0, 0), ch, font=f)
        w += bbox[2] - bbox[0]
    return w


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


def gradient2(draw: ImageDraw.ImageDraw, w: int, h: int, c1: tuple[int, int, int], c2: tuple[int, int, int]) -> None:
    for y in range(h):
        t = y / max(h - 1, 1)
        color = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
        draw.line([(0, y), (w, y)], fill=color)


def draw_accent_bar(draw: ImageDraw.ImageDraw, w: int, accent: str, height: int = 6) -> None:
    draw.rectangle((0, 0, w, height), fill=_hex(accent))


def draw_badge(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, accent: str, font) -> None:
    ef = load_emoji_font(getattr(font, "size", 28))
    tw = _text_width(text, font, ef)
    pad_x, pad_y = 28, 14
    w, h = tw + pad_x * 2, getattr(font, "size", 28) + pad_y * 2
    draw.rounded_rectangle((x, y, x + w, y + h), radius=20, fill=_hex(accent))
    draw_mixed_text(draw, (x + pad_x, y + pad_y - 2), text, font, "#0F172A", emoji_font=ef)


def draw_multiline(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font,
    fill: str,
    line_gap: int = 10,
) -> int:
    x, y = xy
    ef = load_emoji_font(getattr(font, "size", 48))
    tmp = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    for line in text.split("\n"):
        draw_mixed_text(draw, (x, y), line, font, fill, emoji_font=ef)
        lh = 0
        for ch in line:
            f = ef if _is_emoji_char(ch) else font
            bbox = tmp.textbbox((0, 0), ch, font=f)
            lh = max(lh, bbox[3] - bbox[1])
        y += lh + line_gap
    return y


def draw_cta_button(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    accent: str,
    *,
    font_size: int = 30,
    outline: bool = False,
) -> None:
    x1, y1, x2, y2 = box
    text_color = accent if outline else "#0F172A"
    if outline:
        draw.rounded_rectangle((x1, y1, x2, y2), radius=22, outline=_hex(accent), width=3)
    else:
        draw.rounded_rectangle((x1, y1, x2, y2), radius=22, fill=_hex(accent))
    font = load_font(font_size, bold=True)
    ef = load_emoji_font(font_size)
    tw = _text_width(text, font, ef)
    th = font_size + 4
    tx = x1 + (x2 - x1 - tw) // 2
    ty = y1 + (y2 - y1 - th) // 2
    draw_mixed_text(draw, (tx, ty), text, font, text_color, emoji_font=ef)


def topic_cfg(name: str, *, lang: str = "it") -> dict:
    t = TOPICS[name]
    badge = t.get("badge_en", t["badge"]) if lang == "en" else t["badge"]
    return {
        **t,
        "badge_text": f"{t['emoji']} {badge}",
        "hook": t["hook_en"] if lang == "en" else t["hook_it"],
        "sub": t["sub_en"] if lang == "en" else t["sub_it"],
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
    badge_size: int = 28,
    brand_scale: float = 0.08,
) -> Image.Image:
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)
    gradient2(draw, width, height, cfg["bg"][0], cfg["bg"][1])
    draw_accent_bar(draw, width, cfg["accent"])

    m = int(width * 0.06)
    draw_badge(draw, m, m + 16, cfg["badge_text"], cfg["accent"], load_font(badge_size, bold=True))

    card_y = m + 80
    card_h = int(height * 0.52)
    draw.rounded_rectangle((m, card_y, width - m, card_y + card_h), radius=24, fill=(15, 23, 42), outline=_hex(cfg["accent"]), width=2)

    hook_y = card_y + int(card_h * 0.12)
    draw_multiline(draw, (m + 32, hook_y), cfg["hook"], load_font(hook_size, bold=True), "#F8FAFC", line_gap=6)

    sub_y = hook_y + int(card_h * 0.55)
    draw_mixed_text(draw, (m + 32, sub_y), cfg["sub"], load_font(sub_size), "#94A3B8")

    cta_h = int(height * 0.11)
    cta_y = int(height * 0.78)
    cta_w = int(width * 0.52)
    draw_cta_button(draw, (m, cta_y, m + cta_w, cta_y + cta_h), cta, cfg["accent"], font_size=max(20, int(height * 0.04)))

    draw_mixed_text(draw, (m, height - m - 24), f"🌐 {footer}", load_font(max(16, int(height * 0.025))), "#64748B")

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
    gradient2(draw, width, height, cfg["bg"][0], cfg["bg"][1])
    draw_accent_bar(draw, width, cfg["accent"], height=8)

    m = 56
    draw_badge(draw, m, 72, cfg["badge_text"], cfg["accent"], load_font(32, bold=True))

    draw.rounded_rectangle((m, 240, width - m, 720), radius=28, fill=(15, 23, 42))
    draw_multiline(draw, (m + 36, 290), cfg["hook"], load_font(68, bold=True), "#F8FAFC", line_gap=8)
    draw_mixed_text(draw, (m + 36, 580), cfg["sub"], load_font(34), "#94A3B8")

    draw.rounded_rectangle((m, 780, width - m, 900), radius=22, fill=(15, 23, 42), outline=_hex(cfg["accent"]), width=3)
    draw_mixed_text(draw, (m + 32, 828), "🌐 cryptoitaliafacile.com", load_font(34, bold=True), cfg["accent"])

    draw_cta_button(draw, (m, 1500, width - m - 80, 1600), cta, cfg["accent"], font_size=34)
    draw_mixed_text(draw, (m, 1780), footer, load_font(26), "#64748B")

    return apply_branding(img, name, icon_box=(720, 940, 980, 1200), accent=cfg["accent"], brand_scale=0.09)
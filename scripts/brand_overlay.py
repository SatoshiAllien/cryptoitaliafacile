#!/usr/bin/env python3
"""Logo brand piccolo + icona crypto per immagini post."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
BRAND_LOGO = ROOT / "assets" / "img" / "brand" / "logo.png"
CRYPTO_DIR = ROOT / "assets" / "img" / "crypto-icons"

CRYPTO_SOURCES: dict[str, Path] = {
    "bitcoin": ROOT / "assets" / "img" / "bitcoin-btc.png",
    "cardano": ROOT / "assets" / "img" / "cardano-ada.png",
    "ethereum": CRYPTO_DIR / "ethereum.png",
    "exchange": CRYPTO_DIR / "exchange.png",
    "wallet": CRYPTO_DIR / "wallet.png",
    "sicurezza": CRYPTO_DIR / "sicurezza.png",
    "defi": CRYPTO_DIR / "defi.png",
    "trend": CRYPTO_DIR / "trend.png",
    "tip": CRYPTO_DIR / "tip.png",
    "guide": CRYPTO_DIR / "guide.png",
    "breaking": ROOT / "assets" / "img" / "bitcoin-btc.png",
    "regulation": CRYPTO_DIR / "ethereum.png",
    "elon": ROOT / "assets" / "img" / "bitcoin-btc.png",
    "eu": CRYPTO_DIR / "eu.png",
    "usa": CRYPTO_DIR / "usa.png",
    "nft": CRYPTO_DIR / "nft.png",
    "stablecoin": CRYPTO_DIR / "stablecoin.png",
    "blockchain": CRYPTO_DIR / "blockchain.png",
    "cefi": CRYPTO_DIR / "cefi.png",
    "tokenomics": CRYPTO_DIR / "tokenomics.png",
    "news": CRYPTO_DIR / "trend.png",
}


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def _save_icon(path: Path, draw_fn) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    draw_fn(ImageDraw.Draw(img), 256)
    img.save(path, "PNG")


def _hex_rgb(color: str) -> tuple[int, int, int]:
    c = color.lstrip("#")
    return tuple(int(c[i : i + 2], 16) for i in (0, 2, 4))


def _draw_ethereum_icon(draw: ImageDraw.ImageDraw, size: int, color: str) -> None:
    cx, cy = size // 2, size // 2
    w = size // 3
    top = (cx, cy - int(size * 0.28))
    mid_l = (cx - w, cy - int(size * 0.02))
    mid_r = (cx + w, cy - int(size * 0.02))
    bot = (cx, cy + int(size * 0.30))
    light = "#C4B5FD"
    draw.polygon([top, mid_l, (cx, cy - int(size * 0.02))], fill=light)
    draw.polygon([(cx, cy - int(size * 0.02)), mid_r, bot], fill=color)
    draw.polygon([top, mid_r, bot], outline=color, width=max(2, size // 64))


def _draw_exchange_icon(draw: ImageDraw.ImageDraw, size: int, color: str) -> None:
    m = size // 5
    base = size - m
    cw = max(10, size // 10)
    gap = max(8, size // 14)
    specs = (
        (m + gap, base - int(size * 0.35), m + gap + cw, base),
        (m + gap * 2 + cw, base - int(size * 0.55), m + gap * 2 + cw * 2, base),
        (m + gap * 3 + cw * 2, base - int(size * 0.25), m + gap * 3 + cw * 3, base),
    )
    for x1, y1, x2, y2 in specs:
        body = (x1, y1 + cw, x2, y2)
        draw.rectangle(body, fill=color)
        draw.rectangle((x1 + cw // 3, y1, x2 - cw // 3, y1 + cw), fill=color)


def _draw_defi_icon(draw: ImageDraw.ImageDraw, size: int, color: str) -> None:
    cx, cy = size // 2, size // 2
    r = size // 7
    nodes = []
    for i in range(6):
        ang = math.radians(i * 60 - 90)
        nodes.append((cx + int(math.cos(ang) * size * 0.30), cy + int(math.sin(ang) * size * 0.30)))
    for a, b in zip(nodes, nodes[1:] + nodes[:1]):
        draw.line([a, b], fill=color, width=max(3, size // 32))
    for nx, ny in nodes:
        draw.ellipse((nx - r, ny - r, nx + r, ny + r), fill=color)


def _draw_nft_icon(draw: ImageDraw.ImageDraw, size: int, color: str) -> None:
    cx, cy = size // 2, size // 2
    r = int(size * 0.34)
    pts = [(cx + int(math.cos(math.radians(a)) * r), cy + int(math.sin(math.radians(a)) * r)) for a in range(0, 360, 60)]
    draw.polygon(pts, outline=color, fill=None)
    draw.polygon(pts, fill=(*_hex_rgb(color), 48))
    inner = [(cx + int(math.cos(math.radians(a)) * r * 0.55), cy + int(math.sin(math.radians(a)) * r * 0.55)) for a in range(0, 360, 60)]
    draw.polygon(inner, fill=color)


def _draw_sicurezza_icon(draw: ImageDraw.ImageDraw, size: int, color: str) -> None:
    cx = size // 2
    top = size // 6
    w = int(size * 0.34)
    shield = [
        (cx, top),
        (cx + w, top + int(size * 0.18)),
        (cx + w, top + int(size * 0.52)),
        (cx, size - size // 6),
        (cx - w, top + int(size * 0.52)),
        (cx - w, top + int(size * 0.18)),
    ]
    draw.polygon(shield, fill=color)
    draw.polygon(shield, outline="#FFFFFF", width=max(2, size // 64))


def _draw_stablecoin_icon(draw: ImageDraw.ImageDraw, size: int, color: str) -> None:
    font = _font(int(size * 0.52), bold=True)
    sym = "$"
    bbox = draw.textbbox((0, 0), sym, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((size - tw) // 2, (size - th) // 2 - 6), sym, fill=color, font=font)
    ring = size // 8
    draw.ellipse((ring, ring, size - ring, size - ring), outline=color, width=max(3, size // 28))


def _draw_eu_flag_transparent(draw: ImageDraw.ImageDraw, size: int) -> None:
    m = size // 14
    draw.ellipse((m, m, size - m, size - m), fill="#003399")
    cx, cy = size // 2, size // 2
    r = (size - m * 2) // 5
    for i in range(12):
        ang = math.radians(i * 30 - 90)
        sx = cx + int(math.cos(ang) * r * 1.55)
        sy = cy + int(math.sin(ang) * r * 1.55)
        sr = max(3, size // 28)
        draw.ellipse((sx - sr, sy - sr, sx + sr, sy + sr), fill="#FFCC00")


def _draw_usa_flag_transparent(draw: ImageDraw.ImageDraw, size: int) -> None:
    m = size // 14
    box = (m, m, size - m, size - m)
    draw.ellipse(box, fill="#B91C1C")
    x1, y1, x2, y2 = box
    w, h = x2 - x1, y2 - y1
    stripe_h = max(2, h // 13)
    for i in range(7):
        y = y1 + i * stripe_h * 2
        draw.rectangle((x1, y, x2, y + stripe_h), fill="#FFFFFF")
    draw.pieslice((x1, y1, x1 + w, y1 + h), 180, 270, fill="#1D4ED8")
    draw.rectangle((x1, y1, x1 + w // 2, y1 + stripe_h * 7), fill="#1D4ED8")


def _draw_simple_symbol(draw: ImageDraw.ImageDraw, size: int, color: str, symbol: str) -> None:
    font = _font(int(size * 0.42), bold=True)
    bbox = draw.textbbox((0, 0), symbol, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((size - tw) // 2, (size - th) // 2 - 4), symbol, fill=color, font=font)


_TRANSPARENT_ICON_BUILDERS: dict[str, tuple] = {
    "ethereum": (_draw_ethereum_icon, "#627EEA"),
    "exchange": (_draw_exchange_icon, "#34D399"),
    "wallet": (_draw_simple_symbol, "#A78BFA", "W"),
    "sicurezza": (_draw_sicurezza_icon, "#FCA5A5"),
    "defi": (_draw_defi_icon, "#6EE7B7"),
    "trend": (_draw_simple_symbol, "#FDE047", "↗"),
    "tip": (_draw_simple_symbol, "#FDE68A", "★"),
    "guide": (_draw_simple_symbol, "#4ADE80", "≡"),
    "eu": (_draw_eu_flag_transparent, None),
    "usa": (_draw_usa_flag_transparent, None),
    "nft": (_draw_nft_icon, "#A855F7"),
    "stablecoin": (_draw_stablecoin_icon, "#22C55E"),
    "blockchain": (_draw_simple_symbol, "#38BDF8", "⛓"),
    "cefi": (_draw_simple_symbol, "#F59E0B", "C"),
    "tokenomics": (_draw_simple_symbol, "#EAB308", "T"),
}


def _build_transparent_icon(name: str) -> None:
    spec = _TRANSPARENT_ICON_BUILDERS.get(name)
    if not spec:
        return
    path = CRYPTO_DIR / f"{name}.png"

    def _draw(draw: ImageDraw.ImageDraw, size: int) -> None:
        if name in ("eu", "usa"):
            spec[0](draw, size)
        elif len(spec) == 3:
            spec[0](draw, size, spec[1], spec[2])
        else:
            spec[0](draw, size, spec[1])

    _save_icon(path, _draw)


def ensure_crypto_icons(*, force_transparent: bool = False) -> None:
    """Crea icone crypto trasparenti (senza sfondo pieno)."""
    for name in _TRANSPARENT_ICON_BUILDERS:
        path = CRYPTO_DIR / f"{name}.png"
        if force_transparent or not path.exists():
            _build_transparent_icon(name)


_ICONS_V3_READY = False


def _strip_light_background(icon: Image.Image, *, thresh: int = 220) -> Image.Image:
    """Rimuove sfondi bianchi/grigi dai PNG importati."""
    out = icon.convert("RGBA")
    px = out.load()
    for y in range(out.height):
        for x in range(out.width):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            if r >= thresh and g >= thresh and b >= thresh and max(r, g, b) - min(r, g, b) <= 18:
                px[x, y] = (r, g, b, 0)
    return out


def load_crypto_icon(topic: str) -> Image.Image:
    global _ICONS_V3_READY
    if not _ICONS_V3_READY:
        ensure_crypto_icons(force_transparent=True)
        _ICONS_V3_READY = True
    else:
        ensure_crypto_icons()
    key = topic if topic in CRYPTO_SOURCES else "guide"
    path = CRYPTO_SOURCES.get(key) or CRYPTO_SOURCES["guide"]
    if not path.exists():
        path = CRYPTO_SOURCES["bitcoin"]
    icon = Image.open(path).convert("RGBA")
    if path.name in {"bitcoin-btc.png", "cardano-ada.png"}:
        icon = _strip_light_background(icon, thresh=200)
    return icon


def _fit_icon(icon: Image.Image, size: int) -> Image.Image:
    fitted = icon.copy()
    fitted.thumbnail((size, size), Image.Resampling.LANCZOS)
    return fitted


def _accent_glow(icon: Image.Image, accent: str, *, radius: int, alpha: int) -> Image.Image:
    r, g, b = _hex_rgb(accent)
    glow = Image.new("RGBA", icon.size, (r, g, b, 0))
    glow.putalpha(icon.split()[3])
    glow = glow.filter(ImageFilter.GaussianBlur(radius=radius))
    if alpha < 255:
        a = glow.split()[3].point(lambda x: int(x * alpha / 255))
        glow.putalpha(a)
    return glow


def draw_hero_logo_centered(
    img: Image.Image,
    topic: str,
    *,
    accent: str = "#F7931A",
    center: tuple[int, int],
    size: int,
    variant: str = "primary",
) -> Image.Image:
    """Logo argomento grande, centrato, PNG trasparente con glow/neon leggero."""
    icon = load_crypto_icon(topic)
    fitted = _fit_icon(icon, size)
    cx, cy = center
    layer = img.convert("RGBA")
    overlay = Image.new("RGBA", layer.size, (0, 0, 0, 0))

    glow_specs = (
        (max(18, size // 12), 90),
        (max(10, size // 18), 140),
        (max(5, size // 28), 200),
    )
    for blur_r, alpha in glow_specs:
        glow = _accent_glow(fitted, accent, radius=blur_r, alpha=alpha)
        gx = cx - glow.width // 2
        gy = cy - glow.height // 2
        overlay.alpha_composite(glow, (gx, gy))

    draw = ImageDraw.Draw(overlay)
    ring = size // 2 + max(10, size // 24)
    ring_color = (*_hex_rgb(accent), 120 if variant == "alt" else 90)
    draw.ellipse((cx - ring, cy - ring, cx + ring, cy + ring), outline=ring_color, width=max(2, size // 64))
    inner_ring = ring - max(6, size // 32)
    draw.ellipse(
        (cx - inner_ring, cy - inner_ring, cx + inner_ring, cy + inner_ring),
        outline=(*_hex_rgb(accent), 50),
        width=1,
    )

    px, py = cx - fitted.width // 2, cy - fitted.height // 2
    overlay.alpha_composite(fitted, (px, py))
    result = Image.alpha_composite(layer, overlay)
    out = img.copy()
    out.paste(result.convert("RGB"))
    return out


def load_brand_logo() -> Image.Image:
    if not BRAND_LOGO.exists():
        raise FileNotFoundError(f"Logo non trovato: {BRAND_LOGO}")
    return Image.open(BRAND_LOGO).convert("RGBA")


def _paste_in_box(canvas: Image.Image, icon: Image.Image, box: tuple[int, int, int, int], *, outline: str | None = None) -> None:
    x1, y1, x2, y2 = box
    w, h = x2 - x1, y2 - y1
    layer = canvas.convert("RGBA")
    draw = ImageDraw.Draw(layer)
    draw.ellipse(box, fill=(30, 41, 59, 230))
    if outline:
        draw.ellipse(box, outline=outline, width=max(2, w // 60))
    fitted = icon.copy()
    fitted.thumbnail((int(w * 0.72), int(h * 0.72)), Image.Resampling.LANCZOS)
    px = x1 + (w - fitted.width) // 2
    py = y1 + (h - fitted.height) // 2
    layer.paste(fitted, (px, py), fitted)
    canvas.paste(layer.convert("RGB"))


def _paste_small_logo(canvas: Image.Image, *, scale: float = 0.07, corner: str = "bottom-right") -> None:
    logo = load_brand_logo()
    layer = canvas.convert("RGBA")
    target_w = max(36, int(layer.width * scale))
    ratio = target_w / logo.width
    target_h = max(36, int(logo.height * ratio))
    logo = logo.resize((target_w, target_h), Image.Resampling.LANCZOS)
    margin = max(12, int(layer.width * 0.02))
    pad = 4
    box_w, box_h = target_w + pad * 2, target_h + pad * 2
    if corner == "bottom-right":
        x = layer.width - box_w - margin
        y = layer.height - box_h - margin
    else:
        x, y = margin, layer.height - box_h - margin
    overlay = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw.rounded_rectangle((x, y, x + box_w, y + box_h), radius=6, fill=(255, 255, 255, 180))
    overlay.paste(logo, (x + pad, y + pad), logo)
    result = Image.alpha_composite(layer, overlay)
    canvas.paste(result.convert("RGB"))


def apply_branding(
    img: Image.Image,
    topic: str,
    *,
    icon_box: tuple[int, int, int, int],
    accent: str = "#F7931A",
    brand_scale: float = 0.07,
) -> Image.Image:
    """Ripristina stile template + icona crypto nel cerchio + logo piccolo."""
    out = img.copy()
    crypto = load_crypto_icon(topic)
    _paste_in_box(out, crypto, icon_box, outline=accent)
    _paste_small_logo(out, scale=brand_scale)
    return out


def apply_branding_file(src: Path, topic: str, icon_box: tuple[int, int, int, int], accent: str = "#F7931A") -> Path:
    img = Image.open(src)
    result = apply_branding(img, topic, icon_box=icon_box, accent=accent)
    result.save(src, quality=92, optimize=True)
    return src


def _draw_eu_flag(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x1, y1, x2, y2 = box
    draw.ellipse(box, fill="#003399")
    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
    r = (x2 - x1) // 5
    import math

    for i in range(12):
        ang = math.radians(i * 30 - 90)
        sx = cx + int(math.cos(ang) * r * 1.6)
        sy = cy + int(math.sin(ang) * r * 1.6)
        draw.ellipse((sx - 3, sy - 3, sx + 3, sy + 3), fill="#FFCC00")


def _draw_usa_flag(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x1, y1, x2, y2 = box
    w, h = x2 - x1, y2 - y1
    draw.ellipse(box, fill="#B91C1C")
    stripe_h = max(2, h // 13)
    for i in range(7):
        y = y1 + i * stripe_h * 2
        draw.rectangle((x1, y, x2, y + stripe_h), fill="#FFFFFF")
    draw.rectangle((x1, y1, x1 + w // 2, y1 + stripe_h * 7), fill="#1D4ED8")


def apply_topic_logo_top_left(
    img: Image.Image,
    topic: str,
    *,
    accent: str = "#F7931A",
    size: int = 96,
    margin: int = 36,
) -> Image.Image:
    """Logo argomento in alto a sinistra — cerchio minimal."""
    out = img.copy()
    layer = out.convert("RGBA")
    draw = ImageDraw.Draw(layer)
    x1, y1 = margin, margin
    x2, y2 = margin + size, margin + size
    draw.ellipse((x1, y1, x2, y2), fill=(15, 23, 42, 240), outline=accent, width=3)

    if topic == "eu":
        _draw_eu_flag(draw, (x1 + 8, y1 + 8, x2 - 8, y2 - 8))
    elif topic == "usa":
        _draw_usa_flag(draw, (x1 + 8, y1 + 8, x2 - 8, y2 - 8))
    else:
        crypto = load_crypto_icon(topic)
        fitted = crypto.copy()
        fitted.thumbnail((int(size * 0.62), int(size * 0.62)), Image.Resampling.LANCZOS)
        px = x1 + (size - fitted.width) // 2
        py = y1 + (size - fitted.height) // 2
        layer.paste(fitted, (px, py), fitted)

    out.paste(layer.convert("RGB"))
    return out


def draw_center_topic_icon(
    img: Image.Image,
    topic: str,
    *,
    accent: str = "#F7931A",
    center: tuple[int, int],
    size: int = 110,
) -> Image.Image:
    """Icona argomento grande al centro del layout."""
    out = img.copy()
    layer = out.convert("RGBA")
    draw = ImageDraw.Draw(layer)
    cx, cy = center
    half = size // 2
    box = (cx - half, cy - half, cx + half, cy + half)
    draw.ellipse(box, fill=(15, 23, 42, 235), outline=accent, width=3)

    inner = (box[0] + 10, box[1] + 10, box[2] - 10, box[3] - 10)
    if topic == "eu":
        _draw_eu_flag(draw, inner)
    elif topic == "usa":
        _draw_usa_flag(draw, inner)
    else:
        crypto = load_crypto_icon(topic)
        fitted = crypto.copy()
        fitted.thumbnail((int(size * 0.58), int(size * 0.58)), Image.Resampling.LANCZOS)
        px = cx - fitted.width // 2
        py = cy - fitted.height // 2
        layer.paste(fitted, (px, py), fitted)

    out.paste(layer.convert("RGB"))
    return out


def paste_brand_watermark(img: Image.Image, *, scale: float = 0.05) -> Image.Image:
    """Logo brand piccolo in basso a destra."""
    out = img.copy()
    _paste_small_logo(out, scale=scale, corner="bottom-right")
    return out
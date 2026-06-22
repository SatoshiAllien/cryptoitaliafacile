#!/usr/bin/env python3
"""Logo brand piccolo + icona crypto per immagini post."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

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


def ensure_crypto_icons() -> None:
    """Crea icone crypto mancanti (ethereum, exchange, ecc.)."""
    specs = {
        "ethereum": ("#627EEA", "◆"),
        "exchange": ("#34D399", "⇄"),
        "wallet": ("#A78BFA", "👛"),
        "sicurezza": ("#FCA5A5", "🛡"),
        "defi": ("#6EE7B7", "◎"),
        "trend": ("#FDE047", "↗"),
        "tip": ("#FDE68A", "💡"),
        "guide": ("#4ADE80", "📖"),
        "eu": ("#2563EB", "EU"),
        "usa": ("#DC2626", "US"),
        "nft": ("#A855F7", "⬡"),
        "stablecoin": ("#22C55E", "$"),
        "blockchain": ("#38BDF8", "⛓"),
        "cefi": ("#F59E0B", "C"),
        "tokenomics": ("#EAB308", "T"),
    }
    for name, (color, symbol) in specs.items():
        path = CRYPTO_DIR / f"{name}.png"
        if path.exists():
            continue

        def _draw(draw: ImageDraw.ImageDraw, size: int, col=color, sym=symbol) -> None:
            m = size // 16
            draw.ellipse((m, m, size - m, size - m), fill=col)
            font = _font(size // 2, bold=True)
            bbox = draw.textbbox((0, 0), sym, font=font)
            tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
            draw.text(((size - tw) // 2, (size - th) // 2 - 4), sym, fill="#0F172A", font=font)

        _save_icon(path, _draw)


def load_crypto_icon(topic: str) -> Image.Image:
    ensure_crypto_icons()
    key = topic if topic in CRYPTO_SOURCES else "guide"
    path = CRYPTO_SOURCES.get(key) or CRYPTO_SOURCES["guide"]
    if not path.exists():
        path = CRYPTO_SOURCES["bitcoin"]
    return Image.open(path).convert("RGBA")


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


def paste_brand_watermark(img: Image.Image, *, scale: float = 0.05) -> Image.Image:
    """Logo brand piccolo in basso a destra."""
    out = img.copy()
    _paste_small_logo(out, scale=scale, corner="bottom-right")
    return out
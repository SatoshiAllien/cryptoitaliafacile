#!/usr/bin/env python3
"""Genera immagini post stile BREAKING NEWS con logo brand su FB, IG e X."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from brand_overlay import apply_logo

ROOT = Path(__file__).resolve().parent.parent
HERO = ROOT / "assets" / "img" / "welcome-bitcoin-boss.png"
OUT_FB = ROOT / "assets" / "img" / "facebook" / "posts"
OUT_IG = ROOT / "assets" / "img" / "instagram" / "posts"
OUT_X = ROOT / "assets" / "img" / "x" / "posts"

FORMATS = {
    "facebook": (OUT_FB, 1200, 630),
    "instagram": (OUT_IG, 1080, 1080),
    "x": (OUT_X, 1200, 675),
}

HEADLINES = {
    "bitcoin": "BITCOIN BOSS: MYSTERY BRIEFING | MARKETS TUMBLE",
    "exchange": "EXCHANGE SHOCK: SAFER CRYPTO BUYS EXPLAINED",
    "wallet": "WALLET ALERT: PROTECT YOUR CRYPTO NOW",
    "sicurezza": "SECURITY WARNING: AVOID THIS CRYPTO MISTAKE",
    "cardano": "CARDANO BREAKING: ADA EXPLAINED IN 5 MINUTES",
    "ethereum": "ETHEREUM UPDATE: ETH WITHOUT THE JARGON",
    "defi": "DeFi BREAKING: HOW IT REALLY WORKS",
    "trend": "TREND 2026: WHAT CHANGES FOR CRYPTO NOW",
    "tip": "CRYPTO TIP: USE THIS TODAY OR REGRET IT",
    "guide": "FREE GUIDE: TAP BEFORE THE NEXT BTC MOVE",
    "breaking": "BTC CRASH ALERT: WHAT TRADERS MUST KNOW",
    "regulation": "REGULATION BOMBSHELL: CRYPTO RULES SHIFT",
    "elon": "ELON MUSK CRYPTO POST: MARKETS REACT FAST",
}


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def cover_resize(img: Image.Image, w: int, h: int) -> Image.Image:
    src = img.convert("RGB")
    scale = max(w / src.width, h / src.height)
    nw, nh = int(src.width * scale), int(src.height * scale)
    resized = src.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - w) // 2
    top = (nh - h) // 2
    return resized.crop((left, top, left + w, top + h))


def draw_headline(img: Image.Image, headline: str) -> Image.Image:
    draw = ImageDraw.Draw(img)
    bar_h = max(72, int(img.height * 0.14))
    draw.rectangle((0, img.height - bar_h, img.width, img.height), fill=(0, 0, 0, 180))
    font_size = max(22, int(img.width * 0.028))
    font = load_font(font_size, bold=True)
    text = headline.upper()
    max_w = img.width - 40
    # wrap roughly
    words = text.split()
    lines: list[str] = []
    line = ""
    for word in words:
        test = f"{line} {word}".strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_w:
            line = test
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    lines = lines[:2]
    y = img.height - bar_h + (bar_h - len(lines) * (font_size + 6)) // 2
    for ln in lines:
        draw.text((20, y), ln, fill="#FDE047", font=font)
        y += font_size + 6
    return img


def render_one(name: str, headline: str, out_dir: Path, w: int, h: int) -> Path:
    if not HERO.exists():
        raise SystemExit(f"Manca immagine hero: {HERO}")
    img = cover_resize(Image.open(HERO), w, h)
    img = draw_headline(img, headline)
    img = apply_logo(img, scale=0.14 if w >= 1080 else 0.18)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{name}.jpg"
    img.save(path, "JPEG", quality=92, optimize=True)
    return path


def main() -> None:
    targets = {
        **{k: HEADLINES[k] for k in ("bitcoin", "exchange", "wallet", "sicurezza", "cardano", "ethereum", "defi", "trend", "tip", "guide")},
        "breaking": HEADLINES["breaking"],
        "regulation": HEADLINES["regulation"],
        "elon": HEADLINES["elon"],
    }
    for platform, (out_dir, w, h) in FORMATS.items():
        for name, headline in targets.items():
            if platform == "x" and name not in ("bitcoin", "breaking", "regulation", "elon"):
                continue
            path = render_one(name, headline, out_dir, w, h)
            print("OK", platform, path.relative_to(ROOT))


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""Immagini clickbait per post X — mappa slot/topic → thumbnail locale."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
X_IMAGE_DIR = ROOT / "assets" / "img" / "x" / "posts"
FB_IMAGE_DIR = ROOT / "assets" / "img" / "facebook" / "posts"
SITE_URL = "https://satoshiallien.github.io/cryptoitaliafacile/"

SLOT_TYPES = ["bitcoin", "regulation", "elon", "bitcoin_breaking", "bitcoin_viral"]

SLOT_IMAGES = {
    "bitcoin": "bitcoin.jpg",
    "regulation": "regulation.jpg",
    "elon": "elon.jpg",
    "bitcoin_breaking": "breaking.jpg",
    "bitcoin_viral": "bitcoin.jpg",
}

SLOT_LABELS = {
    "bitcoin": "₿ Bitcoin + foto clickbait",
    "regulation": "⚖️ Regolamentazione crypto",
    "elon": "🔄 Repost Elon Musk",
    "bitcoin_breaking": "🚨 Breaking BTC",
    "bitcoin_viral": "🔥 Top viral Bitcoin",
}


def generate_slot_times(per_day: int = 5, start_h: int = 8, end_h: int = 21) -> list[str]:
    start_m = start_h * 60
    end_m = end_h * 60
    times: list[str] = []
    for i in range(per_day):
        if per_day == 1:
            mins = start_m
        else:
            mins = round(start_m + (end_m - start_m) * i / (per_day - 1))
        times.append(f"{mins // 60:02d}:{mins % 60:02d}")
    return times


def slot_type_for_index(slot: int) -> str:
    if 0 <= slot < len(SLOT_TYPES):
        return SLOT_TYPES[slot]
    return "bitcoin"


def image_path_for_slot(slot: int) -> Path | None:
    slot_type = slot_type_for_index(slot)
    name = SLOT_IMAGES.get(slot_type, "bitcoin.jpg")
    path = X_IMAGE_DIR / name
    if path.exists():
        return path
    fallback = FB_IMAGE_DIR / name
    if fallback.exists():
        return fallback
    btc = FB_IMAGE_DIR / "bitcoin.jpg"
    return btc if btc.exists() else None


def image_url_for_slot(slot: int) -> str | None:
    path = image_path_for_slot(slot)
    if not path:
        return None
    rel = path.relative_to(ROOT).as_posix()
    return f"{SITE_URL}{rel}"
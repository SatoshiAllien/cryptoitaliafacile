"""Rendering e utilità per batch 20 post/storie Instagram."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw

from image_style import (
    CTA,
    JPEG_QUALITY,
    STORY_HOME_URL,
    _hex,
    draw_accent_bar,
    draw_badge,
    draw_cta_button,
    draw_mixed_text,
    draw_multiline,
    gradient2,
    load_font,
    topic_cfg,
)
from brand_overlay import apply_branding
from instagram_batch_20_content import BATCH_20, HOME_LINK, build_caption_en, build_caption_it

ROOT = Path(__file__).resolve().parent.parent  # noqa: used by generate script
OUT_DIR = ROOT / "assets" / "img" / "instagram" / "batch-20"
MANIFEST_PATH = ROOT / "data" / "instagram-batch-20.json"
STATE_PATH = ROOT / "data" / "instagram-batch-20-state.json"
SITE_BASE = "https://satoshiallien.github.io/cryptoitaliafacile/assets/img/instagram/batch-20/"


def render_minimal_story(item: dict, *, lang: str = "it") -> Image.Image:
    """1080×1920 — layout pulito: nero, bianco, arancione Satoshi."""
    w, h = 1080, 1920
    accent = "#F59E0B"
    img = Image.new("RGB", (w, h), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_accent_bar(draw, w, accent, height=10)

    m = 64
    cat = item["category_it"] if lang == "it" else item["category_en"]
    draw_badge(draw, m, 80, f"#{item['id']} {cat[:18]}", accent, load_font(26, bold=True))

    hook = item["hook_it"] if lang == "it" else item["hook_en"]
    draw_multiline(draw, (m, 200), hook, load_font(72, bold=True), "#FFFFFF", line_gap=10)

    body = item["body_it"] if lang == "it" else item["body_en"]
    draw_multiline(draw, (m, 520), body, load_font(32), "#CBD5E1", line_gap=8)

    draw.rounded_rectangle((m, 820, w - m, 940), radius=16, outline=_hex(accent), width=2)
    desc = item["desc_it"] if lang == "it" else item["desc_en"]
    draw_multiline(draw, (m + 24, 848), desc[:120], load_font(28), "#94A3B8", line_gap=6)

    cta = item["cta_it"] if lang == "it" else item["cta_en"]
    draw_cta_button(draw, (m, 1380, w - m, 1480), f"👉 {cta[:42]}", accent, font_size=30)
    draw_mixed_text(draw, (m, 1520), f"🔗 {HOME_LINK}", load_font(22, bold=True), accent)
    draw_mixed_text(draw, (m, 1580), "📍 Sticker LINK qui", load_font(20), "#64748B")
    draw_mixed_text(draw, (m, 1620), item["sticker_position"], load_font(18), "#475569")
    footer = "✨ @krown.82 · Crypto Italia Facile" if lang == "en" else "✨ @krown.82 · Crypto Italia Facile"
    draw_mixed_text(draw, (m, 1780), footer, load_font(24), "#64748B")

    topic = item.get("topic", "bitcoin")
    return apply_branding(img, topic, icon_box=(760, 1000, 1000, 1240), accent=accent, brand_scale=0.08)


def render_advanced_story(item: dict, *, lang: str = "it") -> Image.Image:
    """1080×1920 — layout premium con topic_cfg."""
    from image_style import render_story

    topic = item.get("topic", "bitcoin")
    cfg = topic_cfg(topic, lang=lang)
    cfg["hook"] = item["hook_it"] if lang == "it" else item["hook_en"]
    cfg["sub"] = item["body_it"] if lang == "it" else item["body_en"]
    cta_text = (item["cta_it"] if lang == "it" else item["cta_en"])[:36]
    footer = f"🔗 {HOME_LINK[:48]}..."
    story = render_story(
        topic,
        cfg,
        cta=f"👉 {cta_text}",
        footer=footer,
    )
    draw = ImageDraw.Draw(story)
    draw_mixed_text(draw, (56, 1660), f"🔗 {STORY_HOME_URL}", load_font(20, bold=True), cfg["accent"])
    return story


def render_feed_post(item: dict, *, lang: str = "it") -> Image.Image:
    """1080×1080 feed post."""
    story = render_minimal_story(item, lang=lang)
    return story.resize((1080, 1080), Image.Resampling.LANCZOS).crop((0, 200, 1080, 1280))


def image_urls(slug: str) -> dict[str, str]:
    return {
        "story_minimal": SITE_BASE + f"{slug}-story-minimal.jpg",
        "story_advanced": SITE_BASE + f"{slug}-story-advanced.jpg",
        "feed_it": SITE_BASE + f"{slug}-feed-it.jpg",
        "feed_en": SITE_BASE + f"{slug}-feed-en.jpg",
    }


def write_manifest() -> None:
    manifest = {
        "version": 1,
        "count": 20,
        "link": HOME_LINK,
        "size": "1080x1920",
        "items": [],
    }
    for item in BATCH_20:
        manifest["items"].append({
            **{k: v for k, v in item.items() if not k.startswith("_")},
            "caption_it": build_caption_it(item),
            "caption_en": build_caption_en(item),
            "images": image_urls(item["slug"]),
        })
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {"published": [], "failed": [], "last_id": 0}


def save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
"""Rendering batch 20 post/storie — layout professionale hero logo centrato."""

from __future__ import annotations

import json
import re
from pathlib import Path

from feed_post_style import render_feed_post as render_feed_image
from story_post_style import render_story_post

from instagram_batch_20_content import BATCH_20, HOME_LINK, build_caption_en, build_caption_it

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "assets" / "img" / "instagram" / "batch-20"
MANIFEST_PATH = ROOT / "data" / "instagram-batch-20.json"
STATE_PATH = ROOT / "data" / "instagram-batch-20-state.json"
SITE_BASE = "https://satoshiallien.github.io/cryptoitaliafacile/assets/img/instagram/batch-20/"

ACCENT_BY_TOPIC = {
    "bitcoin": "#F7931A",
    "cardano": "#38BDF8",
    "ethereum": "#818CF8",
    "eu": "#93C5FD",
    "usa": "#60A5FA",
    "sicurezza": "#F87171",
    "defi": "#34D399",
    "nft": "#A855F7",
    "exchange": "#14B8A6",
    "stablecoin": "#22C55E",
    "blockchain": "#38BDF8",
    "cefi": "#F59E0B",
    "tokenomics": "#EAB308",
    "trend": "#FACC15",
    "guide": "#4ADE80",
}

STORY_CTAS_IT = ("Scopri di più", "Continua", "Approfondisci", "Swipe")
STORY_CTAS_EN = ("Learn more", "Continue", "Explore", "Swipe")
POST_CTAS_IT = ("Leggi l'articolo", "Scopri di più")
POST_CTAS_EN = ("Read article", "Learn more")

_LINK_WORDS = re.compile(
    r"link|sotto|below|bio|clicca|tap|http|satoshiallien|cryptoitaliafacile",
    re.I,
)


def _sanitize_cta(raw: str, *, lang: str, for_feed: bool) -> str:
    if _LINK_WORDS.search(raw or ""):
        pool = (POST_CTAS_IT if for_feed else STORY_CTAS_IT) if lang == "it" else (
            POST_CTAS_EN if for_feed else STORY_CTAS_EN
        )
        return pool[0]
    text = (raw or "").strip()
    if len(text) > 28:
        return (POST_CTAS_IT if for_feed else STORY_CTAS_IT)[0] if lang == "it" else (
            POST_CTAS_EN if for_feed else STORY_CTAS_EN
        )[0]
    return text or (POST_CTAS_IT[0] if for_feed else STORY_CTAS_IT[0])


def _fields(item: dict, *, lang: str) -> dict:
    hook = item["hook_it"] if lang == "it" else item["hook_en"]
    cat = item["category_it"] if lang == "it" else item["category_en"]
    body = item["body_it"] if lang == "it" else item["body_en"]
    raw_cta = item["cta_it"] if lang == "it" else item["cta_en"]
    return {
        "title": hook.replace("\n", " "),
        "subtitle": f"{cat} · #{item['id']}",
        "body": body,
        "story_cta": _sanitize_cta(raw_cta, lang=lang, for_feed=False),
        "post_cta": _sanitize_cta(raw_cta, lang=lang, for_feed=True),
    }


def _accent(item: dict) -> str:
    return ACCENT_BY_TOPIC.get(item.get("topic", "bitcoin"), "#F7931A")


def render_minimal_story(item: dict, *, lang: str = "it"):
    """1080×1920 — primary, logo hero centrato."""
    f = _fields(item, lang=lang)
    return render_story_post(
        platform="instagram",
        topic=item.get("topic", "bitcoin"),
        title=f["title"],
        subtitle=f["subtitle"],
        body=f["body"],
        cta=f["story_cta"],
        variant="primary",
        accent=_accent(item),
    )


def render_advanced_story(item: dict, *, lang: str = "it"):
    """1080×1920 — alt, logo hero centrato."""
    f = _fields(item, lang=lang)
    return render_story_post(
        platform="instagram",
        topic=item.get("topic", "bitcoin"),
        title=f["title"],
        subtitle=f["subtitle"],
        body=f["body"],
        cta=f["story_cta"],
        variant="alt",
        accent=_accent(item),
    )


def render_feed_post(item: dict, *, lang: str = "it"):
    """1080×1350 — feed 4:5, logo hero centrato."""
    f = _fields(item, lang=lang)
    return render_feed_image(
        platform="instagram",
        topic=item.get("topic", "bitcoin"),
        title=f["title"],
        subtitle=f["subtitle"],
        body=f["body"],
        cta=f["post_cta"],
        variant="primary" if item["id"] % 2 else "alt",
        accent=_accent(item),
    )


def image_urls(slug: str) -> dict[str, str]:
    return {
        "story_minimal": SITE_BASE + f"{slug}-story-minimal.jpg",
        "story_advanced": SITE_BASE + f"{slug}-story-advanced.jpg",
        "feed_it": SITE_BASE + f"{slug}-feed-it.jpg",
        "feed_en": SITE_BASE + f"{slug}-feed-en.jpg",
    }


def write_manifest() -> None:
    manifest = {
        "version": 2,
        "count": 20,
        "links_enabled": False,
        "layout": "hero_logo_centered",
        "formats": {
            "story": {"size": "1080x1920", "safe_area_px": 120},
            "feed": {"size": "1080x1350", "safe_area_px": 100},
        },
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
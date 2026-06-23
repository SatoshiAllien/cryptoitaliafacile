#!/usr/bin/env python3
"""Genera story pulite senza link da articles.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from feed_post_content import story_payload
from story_post_style import design_description, render_story_post
from topic_detect import detect_topic

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_PATH = ROOT / "data" / "articles.json"
IG_OUT = ROOT / "assets" / "img" / "instagram" / "stories"
FB_OUT = ROOT / "assets" / "img" / "facebook" / "stories"
MANIFEST_PATH = ROOT / "data" / "story-posts.json"

ACCENT_BY_TOPIC = {
    "bitcoin": "#F7931A",
    "cardano": "#38BDF8",
    "ethereum": "#818CF8",
    "eu": "#3B82F6",
    "usa": "#EF4444",
    "sicurezza": "#F87171",
    "defi": "#34D399",
    "nft": "#A855F7",
    "exchange": "#14B8A6",
    "stablecoin": "#22C55E",
    "blockchain": "#38BDF8",
    "cefi": "#F59E0B",
    "tokenomics": "#EAB308",
    "news": "#60A5FA",
    "trend": "#FACC15",
    "guide": "#4ADE80",
}

VARIANT_SUFFIX = {
    "primary": "abstract",
    "alt": "thematic",
    "minimal": "minimal",
}


def story_filename(slug: str, *, variant_key: str) -> str:
    return f"{slug}-{VARIANT_SUFFIX[variant_key]}.jpg"


def generate_variant(article: dict, *, variant_key: str, variant: str) -> dict:
    payload = story_payload(article, variant=variant)
    topic = detect_topic(article)
    accent = ACCENT_BY_TOPIC.get(topic, "#F7931A")
    common = dict(
        topic=topic,
        title=payload["title"],
        subtitle=payload["subtitle"],
        body=payload["body"],
        cta=payload["cta"],
        variant=variant,
        accent=accent,
    )

    fname = story_filename(article["slug"], variant_key=variant_key)
    ig = render_story_post(platform="instagram", **common)
    fb = render_story_post(platform="facebook", **common)

    IG_OUT.mkdir(parents=True, exist_ok=True)
    FB_OUT.mkdir(parents=True, exist_ok=True)
    ig.save(IG_OUT / fname, "JPEG", quality=95, optimize=True)
    fb.save(FB_OUT / fname, "JPEG", quality=95, optimize=True)

    return {
        **payload,
        "variant_key": variant_key,
        "instagram": {
            "image": fname,
            "size": "1080x1920",
            "design": design_description(topic, variant, "instagram"),
        },
        "facebook": {
            "image": fname,
            "size": "1080x1350",
            "safe_area": "100px",
            "layout": "hero_logo_centered",
            "design": design_description(topic, variant, "facebook"),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera story senza link")
    parser.add_argument("--slug")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
    articles = data["articles"]
    if args.slug:
        articles = [a for a in articles if a["slug"] == args.slug]
    if args.limit:
        articles = articles[: args.limit]

    manifest = {
        "version": 3,
        "links_enabled": False,
        "instagram_format": "1080x1920",
        "instagram_safe_area": "120px",
        "instagram_layout": "hero_logo_centered",
        "hero_logo_pct": "30-40%",
        "posts": [],
    }

    for article in articles:
        slug = article["slug"]
        v1 = generate_variant(article, variant_key="primary", variant="primary")
        v2 = generate_variant(article, variant_key="alt", variant="alt")
        v3 = generate_variant(article, variant_key="minimal", variant="alt")

        article["igStoryImage"] = story_filename(slug, variant_key="primary")
        article["fbStoryImage"] = story_filename(slug, variant_key="primary")
        article["storyVariants"] = [f"variant-1-{VARIANT_SUFFIX[k]}" for k in ("primary", "alt", "minimal")]
        article["storyNoLinks"] = True
        article["storySafeArea"] = "120px"
        article["storyFormat"] = "1080x1920"

        manifest["posts"].append({"slug": slug, "abstract": v1, "thematic": v2, "minimal": v3})
        print(f"OK {slug} → 3 varianti IG+FB (no link)")

    ARTICLES_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\n{len(articles)} story generate — {MANIFEST_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
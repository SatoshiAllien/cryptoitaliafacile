#!/usr/bin/env python3
"""Genera post feed ordinati da articles.json — IG 1080×1350 + FB 1200×1200."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from feed_post_content import post_payload
from feed_post_style import JPEG_QUALITY, design_description, render_feed_post
from topic_detect import detect_topic

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_PATH = ROOT / "data" / "articles.json"
IG_OUT = ROOT / "assets" / "img" / "instagram" / "posts"
FB_OUT = ROOT / "assets" / "img" / "facebook" / "posts"
MANIFEST_PATH = ROOT / "data" / "daily-feed-posts.json"

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


def ig_filename(slug: str, *, variant: str = "primary") -> str:
    return f"{slug}-portrait-alt.jpg" if variant == "alt" else f"{slug}-portrait.jpg"


def fb_filename(slug: str, *, variant: str = "primary") -> str:
    return f"{slug}-square-alt.jpg" if variant == "alt" else f"{slug}-square.jpg"


def generate_variant(article: dict, *, variant: str) -> dict:
    payload = post_payload(article, variant=variant)
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

    ig_name = ig_filename(article["slug"], variant=variant)
    ig_img = render_feed_post(platform="instagram", **common)
    IG_OUT.mkdir(parents=True, exist_ok=True)
    ig_img.save(IG_OUT / ig_name, "JPEG", quality=JPEG_QUALITY, optimize=True)

    fb_name = fb_filename(article["slug"], variant=variant)
    fb_img = render_feed_post(platform="facebook", **common)
    FB_OUT.mkdir(parents=True, exist_ok=True)
    fb_img.save(FB_OUT / fb_name, "JPEG", quality=JPEG_QUALITY, optimize=True)

    return {
        **payload,
        "instagram": {
            "image": ig_name,
            "size": "1080x1350",
            "safe_area": "80px",
            "design": design_description(topic, variant, "instagram"),
        },
        "facebook": {
            "image": fb_name,
            "size": "1200x1200",
            "safe_area": "100px",
            "design": design_description(topic, variant, "facebook"),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera post feed IG + FB")
    parser.add_argument("--slug", help="Solo uno slug")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
    articles = data["articles"]
    if args.slug:
        articles = [a for a in articles if a["slug"] == args.slug]
        if not articles:
            raise SystemExit(f"Slug non trovato: {args.slug}")
    if args.limit:
        articles = articles[: args.limit]

    manifest: dict = {
        "version": 3,
        "instagram": "1080x1350",
        "facebook": "1200x1200",
        "posts": [],
    }
    ok = 0

    for article in articles:
        slug = article["slug"]
        primary = generate_variant(article, variant="primary")
        alt = generate_variant(article, variant="alt")

        article["igPortraitImage"] = ig_filename(slug)
        article["igPortraitImageAlt"] = ig_filename(slug, variant="alt")
        article["fbSquareImage"] = fb_filename(slug)
        article["fbSquareImageAlt"] = fb_filename(slug, variant="alt")
        article["fbPortraitImage"] = article["fbSquareImage"]
        article["feedPostVariant"] = "layout-v3"

        manifest["posts"].append({"slug": slug, "primary": primary, "alt": alt})
        ok += 1
        print(f"OK {slug} → IG {ig_filename(slug)} + FB {fb_filename(slug)} (+alt)")

    ARTICLES_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"\nGenerati {ok} articoli × 2 varianti × 2 piattaforme — {MANIFEST_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""Genera post feed 1080×1350 da articles.json — primario + alternativo per slug."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from feed_post_content import post_payload
from feed_post_style import JPEG_QUALITY, design_description, render_feed_portrait
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


def portrait_filename(slug: str, *, variant: str = "primary") -> str:
    if variant == "alt":
        return f"{slug}-portrait-alt.jpg"
    return f"{slug}-portrait.jpg"


def generate_one(article: dict, *, variant: str) -> tuple[Path, dict]:
    payload = post_payload(article, variant=variant)
    topic = detect_topic(article)
    accent = ACCENT_BY_TOPIC.get(topic, "#F7931A")
    img = render_feed_portrait(
        topic=topic,
        hook=payload["hook"],
        body=payload["body"],
        cta=payload["cta"],
        variant=variant,
        accent=accent,
    )
    fname = portrait_filename(article["slug"], variant=variant)
    out = IG_OUT / fname
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "JPEG", quality=JPEG_QUALITY, optimize=True)
    FB_OUT.mkdir(parents=True, exist_ok=True)
    img.save(FB_OUT / fname, "JPEG", quality=JPEG_QUALITY, optimize=True)
    meta = {
        **payload,
        "image": fname,
        "design": design_description(topic, variant),
        "size": "1080x1350",
    }
    return out, meta


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera post feed 1080×1350")
    parser.add_argument("--slug", help="Solo uno slug")
    parser.add_argument("--limit", type=int, default=0, help="Limita numero articoli")
    args = parser.parse_args()

    data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
    articles = data["articles"]
    if args.slug:
        articles = [a for a in articles if a["slug"] == args.slug]
        if not articles:
            raise SystemExit(f"Slug non trovato: {args.slug}")
    if args.limit:
        articles = articles[: args.limit]

    manifest: dict = {"version": 2, "format": "1080x1350", "posts": []}
    ok = 0

    for article in articles:
        slug = article["slug"]
        primary_path, primary_meta = generate_one(article, variant="primary")
        alt_path, alt_meta = generate_one(article, variant="alt")
        article["igPortraitImage"] = portrait_filename(slug)
        article["fbPortraitImage"] = portrait_filename(slug)
        article["igPortraitImageAlt"] = portrait_filename(slug, variant="alt")
        article["feedPostVariant"] = "portrait-v2"
        manifest["posts"].append({
            "slug": slug,
            "primary": primary_meta,
            "alt": alt_meta,
        })
        ok += 1
        print(f"OK {slug} → {primary_path.name} + {alt_path.name}")

    ARTICLES_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"\nGenerati {ok} post (×2 varianti) — manifest: {MANIFEST_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
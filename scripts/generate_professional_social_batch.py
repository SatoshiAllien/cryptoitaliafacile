#!/usr/bin/env python3
"""Genera batch professionale IG Stories + IG/FB Feed — logo hero centrato."""

from __future__ import annotations

import json
from pathlib import Path

from feed_post_style import design_description as feed_design
from feed_post_style import render_feed_post
from story_post_style import design_description as story_design
from story_post_style import render_story_post

ROOT = Path(__file__).resolve().parent.parent
IG_STORY_OUT = ROOT / "assets" / "img" / "instagram" / "stories" / "professional-batch"
IG_POST_OUT = ROOT / "assets" / "img" / "instagram" / "posts" / "professional-batch"
FB_POST_OUT = ROOT / "assets" / "img" / "facebook" / "posts" / "professional-batch"
META = ROOT / "data" / "professional-social-batch.json"

CONTENT: list[dict] = [
    {
        "slug": "bitcoin",
        "topic": "bitcoin",
        "accent": "#F7931A",
        "title": "Bitcoin spiegato facile",
        "subtitle": "La guida essenziale · BITCOIN",
        "body": "Scopri cos'è Bitcoin e perché resta il re delle crypto. Due concetti chiave, zero confusione.",
        "story_cta": "Scopri di più",
        "post_cta": "Leggi l'articolo",
    },
    {
        "slug": "cardano",
        "topic": "cardano",
        "accent": "#38BDF8",
        "title": "Cardano in 60 secondi",
        "subtitle": "ADA per principianti · CARDANO",
        "body": "Proof-of-stake, smart contract e community globale. Tutto quello che serve per capire ADA.",
        "story_cta": "Continua",
        "post_cta": "Scopri di più",
    },
    {
        "slug": "ethereum",
        "topic": "ethereum",
        "accent": "#818CF8",
        "title": "Ethereum senza confusione",
        "subtitle": "ETH · smart contract · DeFi",
        "body": "La rete che ha rivoluzionato le crypto. Gas, staking e Layer 2 spiegati in modo chiaro.",
        "story_cta": "Scopri di più",
        "post_cta": "Leggi l'articolo",
    },
    {
        "slug": "regolamentazione-eu",
        "topic": "eu",
        "accent": "#93C5FD",
        "title": "Regolamentazione EU",
        "subtitle": "MiCA · normative · compliance",
        "body": "Cosa cambia per le crypto in Europa. Le regole che ogni investitore deve conoscere.",
        "story_cta": "Approfondisci",
        "post_cta": "Leggi l'articolo",
    },
    {
        "slug": "usa-news",
        "topic": "usa",
        "accent": "#60A5FA",
        "title": "Crypto negli USA",
        "subtitle": "SEC · ETF · Congresso",
        "body": "Le ultime novità dal mercato americano. Trend, regolamentazione e impatto su Bitcoin.",
        "story_cta": "Continua",
        "post_cta": "Scopri di più",
    },
    {
        "slug": "defi",
        "topic": "defi",
        "accent": "#34D399",
        "title": "DeFi spiegato semplice",
        "subtitle": "Finanza decentralizzata",
        "body": "Lending, liquidity pool e yield senza banche tradizionali. Come funziona davvero il DeFi.",
        "story_cta": "Scopri di più",
        "post_cta": "Leggi l'articolo",
    },
    {
        "slug": "nft",
        "topic": "nft",
        "accent": "#A855F7",
        "title": "NFT: cosa sono davvero",
        "subtitle": "Collezioni · arte digitale",
        "body": "Token unici sulla blockchain. Valore, utilità e rischi spiegati senza hype.",
        "story_cta": "Swipe",
        "post_cta": "Scopri di più",
    },
    {
        "slug": "sicurezza",
        "topic": "sicurezza",
        "accent": "#F87171",
        "title": "Proteggi le tue crypto",
        "subtitle": "Sicurezza · anti-truffa",
        "body": "Seed phrase, 2FA e cold wallet. La checklist che ti salva da errori costosi.",
        "story_cta": "Scopri di più",
        "post_cta": "Leggi l'articolo",
    },
    {
        "slug": "stablecoin",
        "topic": "stablecoin",
        "accent": "#22C55E",
        "title": "Stablecoin in breve",
        "subtitle": "USDT · USDC · DAI",
        "body": "Monete ancorate al dollaro per stabilità e trading. Come funzionano e quando usarle.",
        "story_cta": "Continua",
        "post_cta": "Scopri di più",
    },
    {
        "slug": "exchange",
        "topic": "exchange",
        "accent": "#14B8A6",
        "title": "Exchange crypto guidati",
        "subtitle": "Trading · acquisto · sicurezza",
        "body": "Come scegliere e usare un exchange in sicurezza. Candlestick, spread e primi passi.",
        "story_cta": "Scopri di più",
        "post_cta": "Leggi l'articolo",
    },
]


def _save(img, path: Path) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "JPEG", quality=95, optimize=True)
    return str(path.relative_to(ROOT))


def main() -> None:
    catalog: dict = {
        "version": 2,
        "brand": "CryptoItaliaFacile",
        "palette": ["nero", "bianco", "arancione Satoshi #F7931A", "oro #F4C430"],
        "formats": {
            "instagram_story": {"size": "1080x1920", "safe_area_px": 120},
            "instagram_feed": {"size": "1080x1350", "safe_area_px": 100},
            "facebook_post": {"size": "1080x1350", "safe_area_px": 100},
        },
        "items": [],
    }

    for item in CONTENT:
        slug = item["slug"]
        entry = {
            "slug": slug,
            "topic": item["topic"],
            "title": item["title"],
            "subtitle": item["subtitle"],
            "body": item["body"],
            "accent": item["accent"],
            "stories": {},
            "posts": {},
        }

        for variant in ("primary", "alt"):
            story_img = render_story_post(
                platform="instagram",
                topic=item["topic"],
                title=item["title"],
                subtitle=item["subtitle"],
                body=item["body"],
                cta=item["story_cta"],
                variant=variant,
                accent=item["accent"],
            )
            story_path = IG_STORY_OUT / f"{slug}-{variant}.jpg"
            entry["stories"][variant] = {
                "image": _save(story_img, story_path),
                "size": "1080x1920",
                "cta": item["story_cta"],
                "title_position": "sopra" if variant == "primary" else "sotto",
                "design": story_design(item["topic"], variant, "instagram"),
            }
            print(f"OK story {slug}-{variant}")

            for platform, out_dir in (("instagram", IG_POST_OUT), ("facebook", FB_POST_OUT)):
                post_img = render_feed_post(
                    platform=platform,
                    topic=item["topic"],
                    title=item["title"],
                    subtitle=item["subtitle"],
                    body=item["body"],
                    cta=item["post_cta"],
                    variant=variant,
                    accent=item["accent"],
                )
                prefix = "ig" if platform == "instagram" else "fb"
                post_path = out_dir / f"{slug}-{prefix}-{variant}.jpg"
                post_entry = {
                    "image": _save(post_img, post_path),
                    "size": "1080x1350",
                    "cta": item["post_cta"],
                    "title_position": "sopra" if variant == "primary" else "sotto",
                    "design": feed_design(item["topic"], variant, platform),
                }
                entry["posts"].setdefault(variant, {})[platform] = post_entry
                print(f"OK post {slug}-{prefix}-{variant}")

        catalog["items"].append(entry)

    META.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
    total = len(CONTENT) * 2 * 3
    print(f"\nGenerati {total} asset ({len(CONTENT)} topic × 2 varianti × 3 formati)")
    print(f"Metadata → {META.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
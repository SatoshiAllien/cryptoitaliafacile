#!/usr/bin/env python3
"""Genera batch storie IG professionali CryptoItaliaFacile — 1080×1920, logo hero centrato."""

from __future__ import annotations

import json
from pathlib import Path

from story_post_style import design_description, render_story_post

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img" / "instagram" / "stories" / "professional-batch"
META = ROOT / "data" / "instagram-stories-professional.json"

STORIES: list[dict] = [
    {
        "slug": "bitcoin",
        "topic": "bitcoin",
        "accent": "#F7931A",
        "title": "Bitcoin spiegato facile",
        "subtitle": "La guida essenziale · BITCOIN",
        "body": "Scopri cos'è Bitcoin e perché resta il re delle crypto. Due concetti chiave, zero confusione.",
        "cta": "Scopri di più",
    },
    {
        "slug": "cardano",
        "topic": "cardano",
        "accent": "#38BDF8",
        "title": "Cardano in 60 secondi",
        "subtitle": "ADA per principianti · CARDANO",
        "body": "Proof-of-stake, smart contract e community globale. Tutto quello che serve per capire ADA.",
        "cta": "Continua",
    },
    {
        "slug": "ethereum",
        "topic": "ethereum",
        "accent": "#818CF8",
        "title": "Ethereum senza confusione",
        "subtitle": "ETH · smart contract · DeFi",
        "body": "La rete che ha rivoluzionato le crypto. Gas, staking e Layer 2 spiegati in modo chiaro.",
        "cta": "Scopri di più",
    },
    {
        "slug": "regolamentazione-eu",
        "topic": "eu",
        "accent": "#93C5FD",
        "title": "Regolamentazione EU",
        "subtitle": "MiCA · normative · compliance",
        "body": "Cosa cambia per le crypto in Europa. Le regole che ogni investitore deve conoscere.",
        "cta": "Approfondisci",
    },
    {
        "slug": "usa-news",
        "topic": "usa",
        "accent": "#60A5FA",
        "title": "Crypto negli USA",
        "subtitle": "SEC · ETF · Congresso",
        "body": "Le ultime novità dal mercato americano. Trend, regolamentazione e impatto su Bitcoin.",
        "cta": "Continua",
    },
    {
        "slug": "defi",
        "topic": "defi",
        "accent": "#34D399",
        "title": "DeFi spiegato semplice",
        "subtitle": "Finanza decentralizzata",
        "body": "Lending, liquidity pool e yield senza banche tradizionali. Come funziona davvero il DeFi.",
        "cta": "Scopri di più",
    },
    {
        "slug": "nft",
        "topic": "nft",
        "accent": "#A855F7",
        "title": "NFT: cosa sono davvero",
        "subtitle": "Collezioni · arte digitale",
        "body": "Token unici sulla blockchain. Valore, utilità e rischi spiegati senza hype.",
        "cta": "Swipe",
    },
    {
        "slug": "sicurezza",
        "topic": "sicurezza",
        "accent": "#F87171",
        "title": "Proteggi le tue crypto",
        "subtitle": "Sicurezza · anti-truffa",
        "body": "Seed phrase, 2FA e cold wallet. La checklist che ti salva da errori costosi.",
        "cta": "Scopri di più",
    },
    {
        "slug": "stablecoin",
        "topic": "stablecoin",
        "accent": "#22C55E",
        "title": "Stablecoin in breve",
        "subtitle": "USDT · USDC · DAI",
        "body": "Monete ancorate al dollaro per stabilità e trading. Come funzionano e quando usarle.",
        "cta": "Continua",
    },
    {
        "slug": "exchange",
        "topic": "exchange",
        "accent": "#14B8A6",
        "title": "Exchange crypto guidati",
        "subtitle": "Trading · acquisto · sicurezza",
        "body": "Come scegliere e usare un exchange in sicurezza. Candlestick, spread e primi passi.",
        "cta": "Scopri di più",
    },
]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    catalog: dict = {
        "version": 1,
        "format": "1080x1920",
        "safe_area_px": 120,
        "brand": "CryptoItaliaFacile",
        "palette": ["nero", "bianco", "arancione Satoshi #F7931A", "oro #F4C430"],
        "stories": [],
    }

    for item in STORIES:
        slug = item["slug"]
        entry = {**item, "variants": {}}
        for variant in ("primary", "alt"):
            img = render_story_post(
                platform="instagram",
                topic=item["topic"],
                title=item["title"],
                subtitle=item["subtitle"],
                body=item["body"],
                cta=item["cta"],
                variant=variant,
                accent=item["accent"],
            )
            fname = f"{slug}-{variant}.jpg"
            path = OUT / fname
            img.save(path, "JPEG", quality=95, optimize=True)
            desc = design_description(item["topic"], variant, "instagram")
            entry["variants"][variant] = {
                "image": str(path.relative_to(ROOT)),
                "size": "1080x1920",
                "title_position": "sopra" if variant == "primary" else "sotto",
                "design": desc,
            }
            print(f"OK {fname}")
        catalog["stories"].append(entry)

    META.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Metadata → {META.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
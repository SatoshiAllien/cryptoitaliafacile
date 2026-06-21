#!/usr/bin/env python3
"""Selezione 20 articoli per highlights Instagram @krown.82."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_PATH = ROOT / "data" / "articles.json"
PLAN_PATH = ROOT / "data" / "instagram-highlights-plan.json"
HIGHLIGHT_COUNT = 20

MONTH_ORDER = {
    "Gennaio": 1, "Febbraio": 2, "Marzo": 3, "Aprile": 4,
    "Maggio": 5, "Giugno": 6, "Luglio": 7, "Agosto": 8,
    "Settembre": 9, "Ottobre": 10, "Novembre": 11, "Dicembre": 12,
}

VARIANTS = ("abstract", "thematic", "minimal")
VARIANT_KEYS = {
    "abstract": "variant-1-hero",
    "thematic": "variant-2-abstract",
    "minimal": "variant-3-overlay",
}


def article_score(article: dict) -> int:
    return (4 if article.get("featured") else 0) + (2 if article.get("popular") else 0)


def balanced_queue(articles: list[dict]) -> list[dict]:
    buckets: dict[str, list[dict]] = {
        "guide": sorted(
            [a for a in articles if a.get("category") in ("guide", "tutorial")],
            key=article_score, reverse=True,
        ),
        "tip": sorted([a for a in articles if a.get("category") == "tip"], key=article_score, reverse=True),
        "trend": sorted([a for a in articles if a.get("category") == "trend"], key=article_score, reverse=True),
        "other": sorted(
            [a for a in articles if a.get("category") in ("cardano", "sicurezza", "bitcoin", "ethereum", "smart-contract")],
            key=article_score, reverse=True,
        ),
    }
    queue: list[dict] = []
    max_len = max((len(v) for v in buckets.values()), default=0)
    for i in range(max_len):
        for key in ("guide", "tip", "trend", "other"):
            if i < len(buckets[key]):
                queue.append(buckets[key][i])
    seen: set[str] = set()
    unique: list[dict] = []
    for item in queue:
        slug = item["slug"]
        if slug in seen:
            continue
        seen.add(slug)
        unique.append(item)
    return unique


def parse_date_key(date_str: str) -> tuple[int, int]:
    parts = (date_str or "Gennaio 2026").split()
    month = MONTH_ORDER.get(parts[0], 99)
    year = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 2026
    return year, month


def select_highlight_articles(count: int = HIGHLIGHT_COUNT) -> list[dict]:
    data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
    queue = balanced_queue(data["articles"])[:count]
    queue.sort(key=lambda a: (parse_date_key(a.get("date", "")), a.get("slug", "")))
    return queue


def build_plan(articles: list[dict]) -> dict:
    items = []
    for i, article in enumerate(articles):
        variant = VARIANTS[i % len(VARIANTS)]
        items.append({
            "order": i + 1,
            "slug": article["slug"],
            "title": article["title"],
            "category": article.get("category", "guide"),
            "date": article.get("date", ""),
            "variant": variant,
            "variantKey": VARIANT_KEYS[variant],
            "link": f"https://satoshiallien.github.io/cryptoitaliafacile/articolo.html?slug={article['slug']}",
            "imageFile": f"{i + 1:02d}-{article['slug']}-{variant}.jpg",
        })
    return {
        "account": "krown.82",
        "highlightTitle": "Guide Crypto",
        "count": len(items),
        "articles": items,
    }


def save_plan(plan: dict | None = None) -> dict:
    if plan is None:
        articles = select_highlight_articles()
        plan = build_plan(articles)
    PLAN_PATH.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return plan


if __name__ == "__main__":
    p = save_plan()
    print(f"Piano highlights: {p['count']} articoli → {PLAN_PATH}")
#!/usr/bin/env python3
"""Compatibilità script legacy — delega a highlight_categories."""

from __future__ import annotations

from highlight_categories import (
    PLAN_PATH,
    VARIANT_KEYS,
    VARIANTS,
    build_category_plan,
    save_plan,
)

HIGHLIGHT_COUNT = 20


def select_highlight_articles(count: int = HIGHLIGHT_COUNT):
    """Legacy: primi N articoli dal piano flat (ordine globale)."""
    plan = build_category_plan()
    stories = plan["stories"][:count]
    return [{"slug": s["slug"], "title": s["title"], "category": s["category"], "date": s.get("date", "")} for s in stories]


def build_plan(articles: list[dict]) -> dict:
    """Legacy flat plan per publish-instagram-highlights.py."""
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


if __name__ == "__main__":
    p = save_plan()
    print(f"Piano highlights v2: {p['storyCount']} storie, {p['categoryCount']} categorie → {PLAN_PATH}")
#!/usr/bin/env python3
"""Categorie highlights Instagram allineate alla homepage CryptoItaliaFacile."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_PATH = ROOT / "data" / "articles.json"
BITCOIN_NEWS_PATH = ROOT / "data" / "bitcoin-news.json"
PLAN_PATH = ROOT / "data" / "instagram-highlights-plan.json"
SITE_URL = "https://satoshiallien.github.io/cryptoitaliafacile/"
SATOSHI_STORY_LINK = f"{SITE_URL}index.html"

VARIANTS = ("abstract", "thematic", "minimal")
VARIANT_KEYS = {
    "abstract": "variant-1-hero",
    "thematic": "variant-2-abstract",
    "minimal": "variant-3-overlay",
}

# Ordine album sul profilo (come richiesto + logica homepage)
HIGHLIGHT_CATEGORIES: tuple[dict, ...] = (
    {"id": "bitcoin", "title": "Bitcoin", "renderCategory": "bitcoin", "order": 1},
    {"id": "cardano", "title": "Cardano", "renderCategory": "cardano", "order": 2},
    {"id": "regolamentazione", "title": "Regolamentazione", "renderCategory": "regolamentazione", "order": 3},
    {"id": "news", "title": "News", "renderCategory": "news", "order": 4},
    {"id": "sicurezza", "title": "Sicurezza", "renderCategory": "sicurezza", "order": 5},
    {"id": "mercati", "title": "Mercati", "renderCategory": "mercati", "order": 6},
    {"id": "trend", "title": "Trend", "renderCategory": "trend", "order": 7},
    {"id": "guide", "title": "Guide", "renderCategory": "guide", "order": 8},
)

MONTH_ORDER = {
    "Gennaio": 1, "Febbraio": 2, "Marzo": 3, "Aprile": 4,
    "Maggio": 5, "Giugno": 6, "Luglio": 7, "Agosto": 8,
    "Settembre": 9, "Ottobre": 10, "Novembre": 11, "Dicembre": 12,
}

REG_KEYWORDS = ("regolament", "dichiarare", "fisco", "normativ", "kyc", "compliance")
REG_TAG_KEYWORDS = ("mica", "regolamentazione", "#mica", "#regolamentazione")
MERCATI_KEYWORDS = ("mercat", "etf", "halving", "prezzo", "volatil", "grafico", "spread", "candele", "hedging")


def article_score(article: dict) -> int:
    return (4 if article.get("featured") else 0) + (2 if article.get("popular") else 0)


def parse_date_key(date_str: str) -> tuple[int, int]:
    parts = (date_str or "Gennaio 2026").split()
    month = MONTH_ORDER.get(parts[0], 99)
    year = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 2026
    return year, month


def article_text(article: dict) -> str:
    tags = " ".join(article.get("tags") or [])
    return f"{article.get('title', '')} {article.get('excerpt', '')} {tags}".lower()


def is_regolamentazione(article: dict) -> bool:
    tags = [str(t).lower().lstrip("#") for t in article.get("tags") or []]
    if any(t in ("mica", "regolamentazione") for t in tags):
        return True
    text = article_text(article)
    if re.search(r"\bmica\b", text):
        return True
    return any(k in text for k in REG_KEYWORDS)


def is_mercati(article: dict) -> bool:
    text = article_text(article)
    return any(k in text for k in MERCATI_KEYWORDS)


def is_bitcoin(article: dict) -> bool:
    if article.get("category") == "bitcoin":
        return True
    return any("bitcoin" in (tag or "").lower() or tag == "#Bitcoin" for tag in article.get("tags") or [])


def is_sicurezza(article: dict) -> bool:
    return article.get("category") == "sicurezza"


def is_cardano(article: dict) -> bool:
    return article.get("category") == "cardano"


def is_trend(article: dict) -> bool:
    return article.get("category") == "trend"


def is_guide(article: dict) -> bool:
    return article.get("category") in ("guide", "tutorial", "tip")


def classify_article(article: dict) -> str:
    """Assegna ogni articolo a una sola categoria highlight (priorità specificità)."""
    if is_cardano(article):
        return "cardano"
    if is_regolamentazione(article):
        return "regolamentazione"
    if is_sicurezza(article):
        return "sicurezza"
    if is_bitcoin(article):
        return "bitcoin"
    if is_mercati(article):
        return "mercati"
    if is_trend(article):
        return "trend"
    if is_guide(article):
        return "guide"
    return "guide"


def load_site_articles() -> list[dict]:
    data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
    return data["articles"]


def load_bitcoin_news_items() -> list[dict]:
    if not BITCOIN_NEWS_PATH.exists():
        return []
    data = json.loads(BITCOIN_NEWS_PATH.read_text(encoding="utf-8"))
    return data.get("items") or []


def sort_articles(articles: list[dict]) -> list[dict]:
    return sorted(
        articles,
        key=lambda a: (-article_score(a), parse_date_key(a.get("date", "")), a.get("slug", "")),
    )


def group_articles_by_category(articles: list[dict] | None = None) -> dict[str, list[dict]]:
    articles = articles or load_site_articles()
    buckets: dict[str, list[dict]] = {c["id"]: [] for c in HIGHLIGHT_CATEGORIES}
    for article in articles:
        cat_id = classify_article(article)
        buckets[cat_id].append(article)
    for cat_id in buckets:
        buckets[cat_id] = sort_articles(buckets[cat_id])
    return buckets


def news_story_entries(*, max_items: int | None = 12) -> list[dict]:
    """Voci News dalla sessione homepage (bitcoin-news.json)."""
    items = load_bitcoin_news_items()
    items = sorted(items, key=lambda i: (-(i.get("priority") or 0), -(i.get("viralScore") or 0), i.get("date", "")))
    if max_items:
        items = items[:max_items]
    entries: list[dict] = []
    for i, item in enumerate(items, 1):
        news_id = re.sub(r"[^a-zA-Z0-9_-]", "", str(item.get("id") or i))
        slug = f"news-{news_id}"
        link = SATOSHI_STORY_LINK
        title = (item.get("title") or "News Bitcoin").strip()
        if len(title) > 120:
            title = title[:117] + "…"
        entries.append({
            "slug": slug,
            "title": title,
            "category": "news",
            "renderCategory": "news",
            "date": item.get("date", ""),
            "link": link,
            "source": "bitcoin-news",
            "newsId": item.get("id"),
            "orderInCategory": i,
        })
    return entries


def article_link(slug: str) -> str:
    """Tutte le story highlights → homepage Satoshi AI."""
    return SATOSHI_STORY_LINK


def build_category_plan(
    *,
    max_news: int | None = 12,
    include_news: bool = True,
) -> dict:
    buckets = group_articles_by_category()
    categories_out: list[dict] = []
    render_slugs: list[dict] = []
    all_stories: list[dict] = []
    global_order = 0

    for cat in HIGHLIGHT_CATEGORIES:
        cat_id = cat["id"]
        stories: list[dict] = []

        if cat_id == "news" and include_news:
            for entry in news_story_entries(max_items=max_news):
                global_order += 1
                variant = VARIANTS[(global_order - 1) % len(VARIANTS)]
                story = {
                    "globalOrder": global_order,
                    "orderInCategory": entry["orderInCategory"],
                    "highlightId": cat_id,
                    "highlightTitle": cat["title"],
                    "slug": entry["slug"],
                    "title": entry["title"],
                    "category": entry["category"],
                    "renderCategory": entry["renderCategory"],
                    "date": entry.get("date", ""),
                    "variant": variant,
                    "variantKey": VARIANT_KEYS[variant],
                    "link": entry["link"],
                    "imageFile": f"{cat_id}/{entry['orderInCategory']:02d}-{entry['slug']}-{variant}.jpg",
                    "source": entry.get("source", "article"),
                }
                stories.append(story)
                render_slugs.append({
                    "slug": entry["slug"],
                    "title": entry["title"],
                    "category": entry["renderCategory"],
                })
        else:
            for i, article in enumerate(buckets.get(cat_id, []), 1):
                global_order += 1
                variant = VARIANTS[(global_order - 1) % len(VARIANTS)]
                slug = article["slug"]
                story = {
                    "globalOrder": global_order,
                    "orderInCategory": i,
                    "highlightId": cat_id,
                    "highlightTitle": cat["title"],
                    "slug": slug,
                    "title": article["title"],
                    "category": article.get("category", "guide"),
                    "renderCategory": cat["renderCategory"],
                    "date": article.get("date", ""),
                    "variant": variant,
                    "variantKey": VARIANT_KEYS[variant],
                    "link": article_link(slug),
                    "imageFile": f"{cat_id}/{i:02d}-{slug}-{variant}.jpg",
                    "source": "article",
                }
                stories.append(story)
                render_slugs.append({
                    "slug": slug,
                    "title": article["title"],
                    "category": cat["renderCategory"],
                })

        categories_out.append({
            "id": cat_id,
            "title": cat["title"],
            "order": cat["order"],
            "storyCount": len(stories),
            "coverImage": stories[0]["imageFile"] if stories else None,
            "stories": stories,
        })
        all_stories.extend(stories)

    return {
        "version": 2,
        "account": "krown.82",
        "siteUrl": SITE_URL,
        "categoryOrder": [c["id"] for c in HIGHLIGHT_CATEGORIES],
        "categoryCount": len(HIGHLIGHT_CATEGORIES),
        "storyCount": len(all_stories),
        "categories": categories_out,
        "stories": all_stories,
        "renderSlugs": render_slugs,
    }


def save_plan(plan: dict | None = None, **kwargs) -> dict:
    if plan is None:
        plan = build_category_plan(**kwargs)
    PLAN_PATH.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return plan


def plan_summary(plan: dict) -> str:
    lines = [
        f"Account: @{plan.get('account', 'krown.82')}",
        f"Categorie highlight: {plan['categoryCount']}",
        f"Story totali: {plan['storyCount']}",
        "",
    ]
    for cat in plan["categories"]:
        lines.append(f"  [{cat['order']}] {cat['title']}: {cat['storyCount']} storie")
    return "\n".join(lines)


if __name__ == "__main__":
    p = save_plan()
    print(plan_summary(p))
    print(f"\nPiano salvato → {PLAN_PATH}")
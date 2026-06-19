#!/usr/bin/env python3
"""Export Bitcoin-related articles to data/bitcoin-news.json for the site news session."""

import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLES = ROOT / "data" / "articles.json"
OUTPUT = ROOT / "data" / "bitcoin-news.json"
SITE_URL = "https://satoshiallien.github.io/cryptoitaliafacile/"


def is_bitcoin(article: dict) -> bool:
    if article.get("category") == "bitcoin":
        return True
    tags = [t.lower() for t in (article.get("tags") or [])]
    keywords = ("bitcoin", "btc", "lightning", "sats", "halving")
    return any(any(k in tag for k in keywords) for tag in tags)


def build_post(article: dict) -> str:
    url = f"{SITE_URL}articolo.html?slug={article['slug']}"
    return (
        f"₿ Bitcoin News — {article['title']}\n\n"
        f"{article['excerpt']}\n\n"
        f"👉 Leggi tutto:\n{url}\n\n"
        f"#Bitcoin #BTC #crypto #TheLittleSatoshiNews"
    )


def main() -> None:
    with ARTICLES.open(encoding="utf-8") as f:
        data = json.load(f)

    items = []
    for article in data["articles"]:
        if not is_bitcoin(article):
            continue
        items.append({
            "id": article["slug"],
            "title": article["title"],
            "summary": article["excerpt"],
            "date": article.get("date", ""),
            "category": article.get("category", "guide"),
            "slug": article["slug"],
            "breaking": bool(article.get("featured") or article.get("popular")),
            "readTime": article.get("readTime"),
            "postText": build_post(article),
        })

    items.sort(key=lambda x: (not x["breaking"], x["title"]))

    payload = {
        "session": "bitcoin-news",
        "title": "Sessione News Bitcoin",
        "exportedAt": datetime.now().strftime("%Y-%m-%dT%H:%M"),
        "source": "The Little Satoshi News",
        "count": len(items),
        "items": items,
    }

    with OUTPUT.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"Exported {len(items)} bitcoin news items -> {OUTPUT}")


if __name__ == "__main__":
    main()
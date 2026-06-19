#!/usr/bin/env python3
"""Fetch Bitcoin news from X accounts via Twitter syndication timeline."""

from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "bitcoin-news.json"

X_SOURCES = [
    {"handle": "BitcoinMagazine", "label": "Bitcoin Magazine"},
    {"handle": "Strategy", "label": "Strategy"},
    {"handle": "CPOfficialtx", "label": "Crypto Patriot"},
]

SYNDICATION_URL = "https://syndication.twitter.com/srv/timeline-profile/screen-name/{handle}"
USER_AGENT = (
    "Mozilla/5.0 (compatible; TheLittleSatoshiNews/1.0; +https://satoshiallien.github.io/cryptoitaliafacile/)"
)
PER_ACCOUNT = 8
MAX_ITEMS = 24


def parse_timeline_html(html: str, handle: str) -> dict:
    match = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if not match:
        raise ValueError(f"Missing __NEXT_DATA__ for @{handle}")
    data = json.loads(match.group(1))
    return data["props"]["pageProps"]["timeline"]


def fetch_timeline(handle: str) -> dict:
    url = SYNDICATION_URL.format(handle=handle)
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html"})
    with urlopen(req, timeout=30) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
    return parse_timeline_html(html, handle)


def load_cached_timeline(handle: str) -> dict | None:
    cache = Path(__file__).resolve().parent / f"_synd-{handle}.html"
    if not cache.exists():
        return None
    try:
        return parse_timeline_html(cache.read_text(encoding="utf-8", errors="ignore"), handle)
    except (ValueError, KeyError, json.JSONDecodeError):
        return None


def parse_created_at(value: str) -> datetime:
    try:
        return parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return datetime.now(timezone.utc)


def first_line(text: str, limit: int = 120) -> str:
    line = text.strip().split("\n", 1)[0]
    if len(line) <= limit:
        return line
    return line[: limit - 1].rstrip() + "…"


def build_post_text(tweet: dict, source: dict) -> str:
    handle = source["handle"]
    url = f"https://x.com/{handle}/status/{tweet['id_str']}"
    return (
        f"₿ Bitcoin News — @{handle}\n\n"
        f"{tweet['full_text']}\n\n"
        f"🔗 Fonte: {url}\n\n"
        f"#Bitcoin #BTC #crypto"
    )


def tweet_to_item(tweet: dict, source: dict) -> dict:
    handle = source["handle"]
    created = parse_created_at(tweet.get("created_at", ""))
    text = tweet.get("full_text") or tweet.get("text") or ""
    url = f"https://x.com/{handle}/status/{tweet['id_str']}"
    return {
        "id": tweet["id_str"],
        "title": first_line(text),
        "summary": text[:280] + ("…" if len(text) > 280 else ""),
        "date": created.astimezone().strftime("%d %b %Y %H:%M"),
        "dateSort": created.isoformat(),
        "category": "x",
        "source": source["label"],
        "sourceHandle": f"@{handle}",
        "slug": None,
        "external": True,
        "url": url,
        "breaking": False,
        "postText": build_post_text(tweet, source),
    }


def collect_items() -> list[dict]:
    items: list[dict] = []
    errors: list[str] = []

    for index, source in enumerate(X_SOURCES):
        handle = source["handle"]
        if index:
            time.sleep(2.5)
        timeline = None
        try:
            timeline = fetch_timeline(handle)
            print(f"@{handle}: fetched live")
        except (HTTPError, URLError) as exc:
            cached = load_cached_timeline(handle)
            if cached:
                timeline = cached
                print(f"@{handle}: using cache after {exc}")
            else:
                msg = f"@{handle}: {exc}"
                errors.append(msg)
                print(msg, file=sys.stderr)
        except (ValueError, KeyError, json.JSONDecodeError) as exc:
            msg = f"@{handle}: {exc}"
            errors.append(msg)
            print(msg, file=sys.stderr)

        if not timeline:
            continue

        entries = timeline.get("entries") or []
        count = 0
        for entry in entries:
            content = entry.get("content") or {}
            tweet = content.get("tweet")
            if not tweet or not tweet.get("id_str"):
                continue
            items.append(tweet_to_item(tweet, source))
            count += 1
            if count >= PER_ACCOUNT:
                break
        print(f"@{handle}: {count} post")

    if not items and errors:
        raise RuntimeError("; ".join(errors))

    items.sort(key=lambda x: x["dateSort"], reverse=True)
    deduped: list[dict] = []
    seen: set[str] = set()
    for item in items:
        if item["id"] in seen:
            continue
        seen.add(item["id"])
        deduped.append(item)
        if len(deduped) >= MAX_ITEMS:
            break

    for item in deduped:
        item.pop("dateSort", None)

    return deduped, errors


def main() -> None:
    items, errors = collect_items()
    payload = {
        "session": "bitcoin-news",
        "title": "Sessione News Bitcoin",
        "exportedAt": datetime.now().strftime("%Y-%m-%dT%H:%M"),
        "source": "X — BitcoinMagazine, Strategy, CPOfficialtx",
        "sources": X_SOURCES,
        "count": len(items),
        "items": items,
    }
    if errors:
        payload["warnings"] = errors

    with OUTPUT.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(items)} X news items -> {OUTPUT}")


if __name__ == "__main__":
    main()
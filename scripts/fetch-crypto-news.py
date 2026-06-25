#!/usr/bin/env python3
"""Fetch ultime news crypto da X (incluso White House) + testi virali."""

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
SCRIPTS = Path(__file__).resolve().parent
import sys
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
from fetch_theriser_news import HANDLE as THERISER_HANDLE, collect_items as collect_theriser_items
from x_viral import build_viral_post, categorize_post, score_viral
from x_images import SLOT_TYPES, image_url_for_slot
OUTPUT = ROOT / "data" / "crypto-news.json"
OUTPUT_LEGACY = ROOT / "data" / "bitcoin-news.json"

X_SOURCES = [
    {"handle": THERISER_HANDLE, "label": "The Little Satoshi News", "priority": 15},
    {"handle": "elonmusk", "label": "Elon Musk", "priority": 11},
    {"handle": "WhiteHouse", "label": "White House", "priority": 12},
    {"handle": "BitcoinMagazine", "label": "Bitcoin Magazine", "priority": 9},
    {"handle": "SECGov", "label": "SEC", "priority": 9},
    {"handle": "WatcherGuru", "label": "Watcher Guru", "priority": 8},
    {"handle": "CPOfficialtx", "label": "Crypto Patriot", "priority": 8},
    {"handle": "unusual_whales", "label": "Unusual Whales", "priority": 7},
    {"handle": "Strategy", "label": "Strategy", "priority": 6},
    {"handle": "Cointelegraph", "label": "Cointelegraph", "priority": 6},
]

SYNDICATION_URL = "https://syndication.twitter.com/srv/timeline-profile/screen-name/{handle}"
USER_AGENT = (
    "Mozilla/5.0 (compatible; TheRiser100x/1.0; +https://satoshiallien.github.io/cryptoitaliafacile/)"
)
PER_ACCOUNT = 6
MAX_ITEMS = 60


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


def tweet_to_item(tweet: dict, source: dict) -> dict:
    handle = source["handle"]
    created = parse_created_at(tweet.get("created_at", ""))
    text = tweet.get("full_text") or tweet.get("text") or ""
    url = f"https://x.com/{handle}/status/{tweet['id_str']}"
    source_handle = f"@{handle}"
    category = categorize_post(text, source_handle)
    viral = build_viral_post(text, source_handle, url, source["label"])
    low = text.lower()
    breaking = any(k in low for k in ("breaking", "just in", "🚨", "alert"))
    return {
        "id": tweet["id_str"],
        "title": first_line(text),
        "summary": text[:280] + ("…" if len(text) > 280 else ""),
        "date": created.astimezone().strftime("%d %b %Y %H:%M"),
        "dateSort": created.isoformat(),
        "category": "x",
        "source": source["label"],
        "sourceHandle": source_handle,
        "priority": source.get("priority", 5),
        "slug": None,
        "external": True,
        "url": url,
        "breaking": breaking,
        "postCategory": category,
        "viralScore": 0,
        "postText": viral,
        "viralPostText": viral,
    }


def load_existing_items() -> list[dict]:
    for path in (OUTPUT, OUTPUT_LEGACY):
        if not path.exists():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("items"):
                return list(data["items"])
        except (json.JSONDecodeError, OSError):
            continue
    return []


def collect_items() -> tuple[list[dict], list[str]]:
    items: list[dict] = []
    errors: list[str] = []

    try:
        theriser_items = collect_theriser_items()
        items.extend(theriser_items)
        print(f"@{THERISER_HANDLE}: {len(theriser_items)} own posts imported")
    except Exception as exc:
        msg = f"@{THERISER_HANDLE}: {exc}"
        errors.append(msg)
        print(msg, file=sys.stderr)

    for index, source in enumerate(X_SOURCES):
        if source["handle"] == THERISER_HANDLE:
            continue
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

        count = 0
        for entry in timeline.get("entries") or []:
            tweet = (entry.get("content") or {}).get("tweet")
            if not tweet or not tweet.get("id_str"):
                continue
            items.append(tweet_to_item(tweet, source))
            count += 1
            if count >= PER_ACCOUNT:
                break
        print(f"@{handle}: {count} post")

    if not items:
        cached = load_existing_items()
        if cached:
            print(f"Using {len(cached)} cached news items after fetch errors")
            items = cached
        elif errors:
            raise RuntimeError("; ".join(errors))

    items.sort(key=lambda x: x.get("dateSort", ""), reverse=True)
    deduped: list[dict] = []
    seen: set[str] = set()
    for item in items:
        if item["id"] in seen:
            continue
        seen.add(item["id"])
        item["viralScore"] = score_viral(item)
        deduped.append(item)
        if len(deduped) >= MAX_ITEMS:
            break

    for item in deduped:
        item.pop("dateSort", None)
        slot_type = item.get("postCategory") or "bitcoin"
        if slot_type == "crypto":
            slot_type = "bitcoin"
        if slot_type not in SLOT_TYPES:
            slot_type = "bitcoin_viral"
        item["xImage"] = image_url_for_slot(SLOT_TYPES.index(slot_type) if slot_type in SLOT_TYPES else 0)

    return deduped, errors


def main() -> None:
    items, errors = collect_items()
    source_names = ", ".join(s["handle"] for s in X_SOURCES)
    payload = {
        "session": "crypto-news",
        "title": "Ultime News Crypto",
        "account": "https://x.com/TheRiser100x",
        "exportedAt": datetime.now().strftime("%Y-%m-%dT%H:%M"),
        "source": f"X — {source_names}",
        "sources": X_SOURCES,
        "count": len(items),
        "items": items,
    }
    if errors:
        payload["warnings"] = errors

    for path in (OUTPUT, OUTPUT_LEGACY):
        with path.open("w", encoding="utf-8") as f:
            json.dump({**payload, "session": "bitcoin-news" if path == OUTPUT_LEGACY else "crypto-news",
                       "title": "Sessione News Bitcoin" if path == OUTPUT_LEGACY else "Ultime News Crypto"}, f,
                      ensure_ascii=False, indent=2)
        print(f"Saved -> {path}")

    print(f"{len(items)} news items ready for @TheRiser100x")


if __name__ == "__main__":
    main()
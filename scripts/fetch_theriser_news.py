#!/usr/bin/env python3
"""Importa i post di @TheRiser100x nel feed news del sito."""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from x_images import SLOT_TYPES, image_url_for_slot
from x_viral import build_viral_post, categorize_post, score_viral

HANDLE = "TheRiser100x"
USER_ID = "107646831"
SYNDICATION_URL = "https://syndication.twitter.com/srv/timeline-profile/screen-name/{handle}"
USER_AGENT = (
    "Mozilla/5.0 (compatible; TheRiser100x/1.0; +https://satoshiallien.github.io/cryptoitaliafacile/)"
)
SEARCH_QUERIES = [
    "site:x.com/TheRiser100x/status",
    "TheRiser100x twitter bitcoin",
    "TheRiser100x twitter cardano",
    "TheRiser100x twitter breaking",
    "from:TheRiser100x crypto",
]
SEED_IDS = [
    "2059917459381953020",
    "2043681234761462087",
    "2045503737171485116",
    "2044700234924655016",
    "2041649555419148309",
    "2041257347234828399",
    "2062952276998692912",
    "2062922038855999685",
    "2036564910318997898",
    "2035512461634244678",
    "2033313949438161306",
    "2032862555853516904",
    "2028540168177930655",
]


def first_line(text: str, limit: int = 120) -> str:
    line = text.strip().split("\n", 1)[0]
    if len(line) <= limit:
        return line
    return line[: limit - 1].rstrip() + "…"


def parse_created_at(value: str) -> datetime:
    try:
        return parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return datetime.now(timezone.utc)


def discover_tweet_ids() -> list[str]:
    found: list[str] = []
    pattern = re.compile(rf"{HANDLE}/status/(\d+)", re.I)

    for query in SEARCH_QUERIES:
        for offset in (0, 30, 60):
            url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(query)
            if offset:
                url += f"&s={offset}"
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            try:
                with urllib.request.urlopen(req, timeout=25) as resp:
                    html = resp.read().decode("utf-8", errors="ignore")
                found.extend(pattern.findall(html))
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
                print(f"search {query!r} offset={offset}: {exc}", file=sys.stderr)
            time.sleep(1.2)

    for tweet_id in SEED_IDS:
        found.append(tweet_id)

    deduped: list[str] = []
    seen: set[str] = set()
    for tweet_id in found:
        if tweet_id in seen:
            continue
        seen.add(tweet_id)
        deduped.append(tweet_id)
    return deduped


def fetch_vx_tweet(tweet_id: str) -> dict | None:
    url = f"https://api.vxtwitter.com/{HANDLE}/status/{tweet_id}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"@{HANDLE}/status/{tweet_id}: {exc}", file=sys.stderr)
        return None

    screen = (data.get("user_screen_name") or data.get("screen_name") or HANDLE).lower()
    if screen != HANDLE.lower():
        return None

    text = (data.get("text") or "").strip()
    if not text:
        return None

    return {
        "id_str": str(data.get("tweetID") or tweet_id),
        "full_text": text,
        "created_at": data.get("date") or "",
        "url": data.get("tweetURL") or f"https://x.com/{HANDLE}/status/{tweet_id}",
    }


def fetch_syndication_tweets() -> list[dict]:
    url = SYNDICATION_URL.format(handle=HANDLE)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        print(f"syndication @{HANDLE}: {exc}", file=sys.stderr)
        return []

    match = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if not match:
        return []

    try:
        timeline = json.loads(match.group(1))["props"]["pageProps"]["timeline"]
    except (KeyError, json.JSONDecodeError) as exc:
        print(f"syndication parse @{HANDLE}: {exc}", file=sys.stderr)
        return []

    tweets: list[dict] = []
    for entry in timeline.get("entries") or []:
        tweet = (entry.get("content") or {}).get("tweet")
        if not tweet or not tweet.get("id_str"):
            continue
        tweets.append(tweet)
    return tweets


def raw_to_item(raw: dict) -> dict:
    created = parse_created_at(raw.get("created_at", ""))
    text = raw.get("full_text") or raw.get("text") or ""
    tweet_id = raw["id_str"]
    source_handle = f"@{HANDLE}"
    url = raw.get("url") or f"https://x.com/{HANDLE}/status/{tweet_id}"
    category = categorize_post(text, source_handle)
    viral = build_viral_post(text, source_handle, url, "The Little Satoshi News")
    low = text.lower()
    breaking = any(k in low for k in ("breaking", "just in", "🚨", "alert"))

    return {
        "id": tweet_id,
        "title": first_line(text),
        "summary": text[:280] + ("…" if len(text) > 280 else ""),
        "date": created.astimezone().strftime("%d %b %Y %H:%M"),
        "dateSort": created.isoformat(),
        "category": "x",
        "source": "The Little Satoshi News",
        "sourceHandle": source_handle,
        "priority": 15,
        "slug": None,
        "external": True,
        "url": url,
        "breaking": breaking,
        "postCategory": category,
        "viralScore": 0,
        "postText": viral,
        "viralPostText": viral,
    }


def finalize_items(items: list[dict], *, keep_date_sort: bool = False) -> list[dict]:
    items.sort(key=lambda item: item.get("dateSort", ""), reverse=True)
    for item in items:
        item["viralScore"] = score_viral(item) + 10
        if not keep_date_sort:
            item.pop("dateSort", None)
        slot_type = item.get("postCategory") or "bitcoin"
        if slot_type == "crypto":
            slot_type = "bitcoin"
        if slot_type not in SLOT_TYPES:
            slot_type = "bitcoin_viral"
        item["xImage"] = image_url_for_slot(SLOT_TYPES.index(slot_type) if slot_type in SLOT_TYPES else 0)
    return items


def collect_items() -> list[dict]:
    raw_tweets: dict[str, dict] = {}

    for tweet in fetch_syndication_tweets():
        raw_tweets[tweet["id_str"]] = tweet
        print(f"syndication: {tweet['id_str']}")

    tweet_ids = discover_tweet_ids()
    print(f"discovered {len(tweet_ids)} tweet ids")

    for index, tweet_id in enumerate(tweet_ids):
        if index and index % 5 == 0:
            time.sleep(1.0)
        tweet = fetch_vx_tweet(tweet_id)
        if tweet:
            raw_tweets[tweet["id_str"]] = tweet

    items = [raw_to_item(raw) for raw in raw_tweets.values()]
    return finalize_items(items, keep_date_sort=True)


def main() -> int:
    items = collect_items()
    print(f"{len(items)} posts from @{HANDLE}")
    for item in items[:5]:
        print(f"  - {item['date']}: {item['title'][:80]}")
    return 0 if items else 1


if __name__ == "__main__":
    raise SystemExit(main())
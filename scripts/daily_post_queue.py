#!/usr/bin/env python3
"""Coda bilanciata 20 post/giorno per Instagram e Facebook."""

from __future__ import annotations

from topic_detect import DAILY_GROUPS, SLOT_RANGES, detect_daily_group

POSTS_PER_DAY = 20

GROUP_ORDER = DAILY_GROUPS


def article_score(article: dict) -> int:
    return (4 if article.get("featured") else 0) + (2 if article.get("popular") else 0)


def bucket_articles(articles: list[dict]) -> dict[str, list[dict]]:
    buckets: dict[str, list[dict]] = {g: [] for g in GROUP_ORDER}
    for article in articles:
        group = detect_daily_group(article)
        buckets[group].append(article)

    for group in GROUP_ORDER:
        buckets[group] = sorted(buckets[group], key=article_score, reverse=True)
    return buckets


def _fill_bucket(bucket: list[dict], count: int, cursor: int) -> tuple[list[dict], int]:
    if not bucket:
        return [], cursor
    picks: list[dict] = []
    seen: set[str] = set()
    attempts = 0
    while len(picks) < count and attempts < len(bucket) * 3:
        item = bucket[cursor % len(bucket)]
        cursor += 1
        attempts += 1
        if item["slug"] in seen:
            continue
        seen.add(item["slug"])
        picks.append(item)
    return picks, cursor


def build_day_posts(articles: list[dict], day_index: int) -> list[dict]:
    """20 articoli per un giorno: slot 0–4 BTC, 5–9 edu, 10–14 sicurezza, 15–19 news."""
    buckets = bucket_articles(articles)
    day_posts: list[dict | None] = [None] * POSTS_PER_DAY
    cursors = {g: day_index * 5 for g in GROUP_ORDER}

    for group in GROUP_ORDER:
        bucket = buckets[group]
        slot_range = SLOT_RANGES[group]
        picks, cursors[group] = _fill_bucket(bucket, len(slot_range), cursors[group])
        for slot, article in zip(slot_range, picks):
            day_posts[slot] = article

    fallback = sorted(articles, key=article_score, reverse=True)
    fb_i = day_index * POSTS_PER_DAY
    for i in range(POSTS_PER_DAY):
        if day_posts[i] is None:
            day_posts[i] = fallback[fb_i % len(fallback)]
            fb_i += 1
    return [a for a in day_posts if a is not None]


def daily_plan(articles: list[dict], *, min_days: int = 30) -> list[list[dict]]:
    if not articles:
        return []
    days = max(min_days, (len(articles) + 4) // 5)
    return [build_day_posts(articles, d) for d in range(days)]


def slot_group(slot: int) -> str:
    for group, slots in SLOT_RANGES.items():
        if slot in slots:
            return group
    return GROUP_ORDER[0]


def variant_for_slot(slot: int, day_index: int) -> str:
    """Alterna versione primaria/alternativa per varietà visiva."""
    return "alt" if (slot + day_index) % 2 else "primary"
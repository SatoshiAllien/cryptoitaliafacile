#!/usr/bin/env python3
"""Testi virali per post X — emoji, hook e hashtag (max 280 caratteri)."""

from __future__ import annotations

import re

X_ACCOUNT = "@TheRiser100x"
MAX_LEN = 280

HOOKS = {
    "breaking": "🚨 BREAKING",
    "whitehouse": "🇺🇸 WHITE HOUSE · CRYPTO",
    "bitcoin": "₿ BITCOIN ALERT",
    "ethereum": "⟠ ETH UPDATE",
    "regulation": "⚖️ REGOLAMENTAZIONE CRYPTO",
    "market": "📈 MERCATO CRYPTO",
    "default": "🔥 CRYPTO NEWS",
}

EMOJI_BOOST = ["👀", "🚀", "⚡", "💥", "🔥"]

HASHTAG_SETS = {
    "whitehouse": ["#WhiteHouse", "#Crypto", "#Bitcoin", "#USA", "#TheRiser100x"],
    "bitcoin": ["#Bitcoin", "#BTC", "#Crypto", "#CryptoNews", "#TheRiser100x"],
    "ethereum": ["#Ethereum", "#ETH", "#Crypto", "#DeFi", "#TheRiser100x"],
    "regulation": ["#Crypto", "#Regulation", "#SEC", "#Bitcoin", "#TheRiser100x"],
    "market": ["#Crypto", "#Bitcoin", "#Altcoins", "#CryptoNews", "#TheRiser100x"],
    "default": ["#Crypto", "#Bitcoin", "#CryptoNews", "#BTC", "#TheRiser100x"],
}


def clean_text(text: str) -> str:
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"RT\s+", "", text, flags=re.I)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def detect_topics(text: str, handle: str = "") -> list[str]:
    low = text.lower()
    h = handle.lower()
    topics: list[str] = []
    if h == "whitehouse" or any(k in low for k in ("white house", "whitehouse", "biden", "trump", "congress")):
        topics.append("whitehouse")
    if any(k in low for k in ("bitcoin", "btc", "satoshi")):
        topics.append("bitcoin")
    if any(k in low for k in ("ethereum", " eth", "$eth")):
        topics.append("ethereum")
    if any(k in low for k in ("sec", "regulation", "mica", "law", "ban", "legal", "fed", "treasury")):
        topics.append("regulation")
    if any(k in low for k in ("breaking", "just in", "alert", "🚨")):
        topics.append("breaking")
    if any(k in low for k in ("market", "price", "rally", "dump", "etf", "surge")):
        topics.append("market")
    return topics or ["default"]


def pick_hook(topics: list[str]) -> str:
    for key in ("breaking", "whitehouse", "regulation", "bitcoin", "ethereum", "market"):
        if key in topics:
            return HOOKS[key]
    return HOOKS["default"]


def pick_hashtags(topics: list[str]) -> str:
    for key in ("whitehouse", "regulation", "bitcoin", "ethereum", "market"):
        if key in topics:
            return " ".join(HASHTAG_SETS[key])
    return " ".join(HASHTAG_SETS["default"])


def maybe_emoji(text: str, topics: list[str]) -> str:
    if any(e in text for e in EMOJI_BOOST + ["🚨", "🇺🇸", "₿"]):
        return text
    if "breaking" in topics:
        return f"🚨 {text}"
    if "whitehouse" in topics:
        return f"🇺🇸 {text}"
    if "bitcoin" in topics:
        return f"₿ {text}"
    return f"👀 {text}"


def truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def build_viral_post(
    raw_text: str,
    source_handle: str = "",
    source_url: str = "",
    source_label: str = "",
) -> str:
    topics = detect_topics(raw_text, source_handle.lstrip("@"))
    hook = pick_hook(topics)
    body = clean_text(raw_text)
    body = maybe_emoji(body, topics)
    body = truncate(body, 160)

    tags = pick_hashtags(topics)
    via = f"via {source_handle}" if source_handle else ""
    if source_label and not via:
        via = f"via {source_label}"

    parts = [hook, "", body]
    if via:
        parts.extend(["", via])
    if source_url:
        parts.extend(["", truncate(source_url, 80)])
    parts.extend(["", tags])

    post = "\n".join(p for p in parts if p)
    if len(post) <= MAX_LEN:
        return post

    # Compatta se troppo lungo
    compact = f"{hook}\n\n{truncate(body, 120)}\n\n{tags}"
    return truncate(compact, MAX_LEN)


def score_viral(item: dict) -> int:
    text = (item.get("title") or "") + " " + (item.get("summary") or "")
    topics = detect_topics(text, (item.get("sourceHandle") or "").lstrip("@"))
    score = 0
    if "breaking" in topics:
        score += 8
    if "whitehouse" in topics:
        score += 10
    if "regulation" in topics:
        score += 6
    if "bitcoin" in topics:
        score += 5
    if item.get("breaking"):
        score += 4
    if item.get("priority"):
        score += int(item["priority"])
    return score
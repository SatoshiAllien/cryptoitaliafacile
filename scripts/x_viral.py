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
    "elon": "🔄 REPOST @elonmusk",
    "default": "🔥 CRYPTO NEWS",
}

CLICKBAIT_HOOKS = {
    "bitcoin": "₿ BITCOIN — LO DEVI VEDERE 👇",
    "regulation": "⚖️ REGOLAMENTAZIONE — ATTENZIONE 👇",
    "elon": "🔄 ELON MUSK HA DETTO 👇",
    "bitcoin_breaking": "🚨 BREAKING BTC — GUARDA 👇",
    "bitcoin_viral": "🔥 VIRAL BTC — NON PERDERE 👇",
}

EMOJI_BOOST = ["👀", "🚀", "⚡", "💥", "🔥"]

HASHTAG_SETS = {
    "whitehouse": ["#WhiteHouse", "#Crypto", "#Bitcoin", "#USA", "#TheRiser100x"],
    "bitcoin": ["#Bitcoin", "#BTC", "#Crypto", "#CryptoNews", "#TheRiser100x"],
    "ethereum": ["#Ethereum", "#ETH", "#Crypto", "#DeFi", "#TheRiser100x"],
    "regulation": ["#Crypto", "#Regulation", "#SEC", "#Bitcoin", "#TheRiser100x"],
    "market": ["#Crypto", "#Bitcoin", "#Altcoins", "#CryptoNews", "#TheRiser100x"],
    "elon": ["#ElonMusk", "#Bitcoin", "#Crypto", "#X", "#TheRiser100x"],
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
    h = handle.lower().lstrip("@")
    topics: list[str] = []
    if h == "elonmusk" or any(k in low for k in ("elon musk", "elonmusk", "tesla", "spacex", "dogecoin", "doge")):
        topics.append("elon")
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


def pick_hook(topics: list[str], slot_type: str = "") -> str:
    if slot_type and slot_type in CLICKBAIT_HOOKS:
        return CLICKBAIT_HOOKS[slot_type]
    for key in ("breaking", "elon", "whitehouse", "regulation", "bitcoin", "ethereum", "market"):
        if key in topics:
            return HOOKS[key]
    return HOOKS["default"]


def pick_hashtags(topics: list[str], slot_type: str = "") -> str:
    if slot_type == "elon":
        return " ".join(HASHTAG_SETS["elon"])
    if slot_type == "regulation":
        return " ".join(HASHTAG_SETS["regulation"])
    for key in ("elon", "whitehouse", "regulation", "bitcoin", "ethereum", "market"):
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
    slot_type: str = "",
) -> str:
    topics = detect_topics(raw_text, source_handle.lstrip("@"))
    hook = pick_hook(topics, slot_type)
    body = clean_text(raw_text)
    body = maybe_emoji(body, topics)
    body = truncate(body, 150 if slot_type else 160)

    tags = pick_hashtags(topics, slot_type)
    via = f"via {source_handle}" if source_handle else ""
    if source_label and not via:
        via = f"via {source_label}"

    parts = [hook, "", body]
    if slot_type == "elon" and source_url:
        parts.extend(["", "🔗 Post originale:", truncate(source_url, 80)])
    elif via:
        parts.extend(["", via])
        if source_url:
            parts.extend(["", truncate(source_url, 80)])
    elif source_url:
        parts.extend(["", truncate(source_url, 80)])
    parts.extend(["", tags])

    post = "\n".join(p for p in parts if p)
    if len(post) <= MAX_LEN:
        return post

    compact = f"{hook}\n\n{truncate(body, 110)}\n\n{tags}"
    return truncate(compact, MAX_LEN)


def is_bitcoin_item(item: dict) -> bool:
    text = (item.get("title") or "") + " " + (item.get("summary") or "")
    topics = detect_topics(text, (item.get("sourceHandle") or "").lstrip("@"))
    return "bitcoin" in topics or item.get("postCategory") == "bitcoin"


def is_regulation_item(item: dict) -> bool:
    text = (item.get("title") or "") + " " + (item.get("summary") or "")
    topics = detect_topics(text, (item.get("sourceHandle") or "").lstrip("@"))
    return "regulation" in topics or item.get("postCategory") == "regulation"


def is_elon_item(item: dict) -> bool:
    handle = (item.get("sourceHandle") or "").lstrip("@").lower()
    return handle == "elonmusk" or item.get("postCategory") == "elon"


def score_viral(item: dict) -> int:
    text = (item.get("title") or "") + " " + (item.get("summary") or "")
    topics = detect_topics(text, (item.get("sourceHandle") or "").lstrip("@"))
    score = 0
    if "breaking" in topics:
        score += 8
    if "elon" in topics:
        score += 9
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


def categorize_post(text: str, handle: str) -> str:
    topics = detect_topics(text, handle.lstrip("@"))
    h = handle.lstrip("@").lower()
    if h == "elonmusk":
        return "elon"
    if "regulation" in topics:
        return "regulation"
    if "bitcoin" in topics or "breaking" in topics:
        return "bitcoin"
    return "crypto"
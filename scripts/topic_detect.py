#!/usr/bin/env python3
"""Rileva il topic/logo corretto per un articolo CryptoItaliaFacile."""

from __future__ import annotations

import re

TOPICS = (
    "bitcoin",
    "cardano",
    "ethereum",
    "eu",
    "usa",
    "sicurezza",
    "defi",
    "nft",
    "exchange",
    "stablecoin",
    "blockchain",
    "cefi",
    "tokenomics",
    "news",
    "trend",
    "guide",
)

TOPIC_LABELS = {
    "bitcoin": "BITCOIN",
    "cardano": "CARDANO",
    "ethereum": "ETHEREUM",
    "eu": "REGOLAMENTAZIONE EU",
    "usa": "CRYPTO USA",
    "sicurezza": "SICUREZZA",
    "defi": "DeFi",
    "nft": "NFT",
    "exchange": "EXCHANGE",
    "stablecoin": "STABLECOIN",
    "blockchain": "BLOCKCHAIN",
    "cefi": "CeFi",
    "tokenomics": "TOKENOMICS",
    "news": "NEWS",
    "trend": "TREND",
    "guide": "GUIDA",
}

KEYWORDS: dict[str, tuple[str, ...]] = {
    "bitcoin": (
        "bitcoin", "btc", "satoshi", "halving", "lightning", "sats", "pow",
        "proof of work", "mining", "etf bitcoin",
    ),
    "cardano": ("cardano", "ada", "plutus", "hydra", "catalyst"),
    "ethereum": ("ethereum", "eth", "gas fee", "etherscan", "solidity", "layer2", "layer 2", "staking eth"),
    "eu": ("mica", "regolament", "normativ", "ue ", " unione europea", "europa crypto", "dichiarare"),
    "usa": ("sec ", "usa", "stati uniti", "america", "congress", "cftc"),
    "sicurezza": (
        "sicurezz", "phishing", "truff", "rug pull", "antifrod", "seed phrase",
        "hardware wallet", "cold wallet", "hot wallet", "compromess", "password manager",
        "2fa", "backup", "audit",
    ),
    "defi": ("defi", "uniswap", "aave", "yield", "liquidity", "liquida", "bridge", "mev", "multisig"),
    "nft": ("nft", "collezion", "opensea"),
    "exchange": ("exchange", "revolut", "kraken", "binance", "coinbase", "trading", "candele", "spread"),
    "stablecoin": ("stablecoin", "usdt", "usdc", "dai", "euro stable", "hedging"),
    "blockchain": ("blockchain", "block explorer", "nodo", "validator", "decentralizz", "smart contract"),
    "cefi": ("cefi", "custod", "centralizz"),
    "tokenomics": ("tokenomic", "supply", "burn", "emission", "market cap", "volume"),
}

DAILY_GROUPS = (
    "bitcoin_blockchain",
    "crypto_education",
    "security",
    "news_trend",
)

GROUP_TOPICS: dict[str, tuple[str, ...]] = {
    "bitcoin_blockchain": ("bitcoin", "blockchain", "ethereum"),
    "crypto_education": ("stablecoin", "defi", "cefi", "nft", "tokenomics", "exchange", "guide"),
    "security": ("sicurezza",),
    "news_trend": ("trend", "news", "eu", "usa"),
}

SLOT_RANGES: dict[str, range] = {
    "bitcoin_blockchain": range(0, 5),
    "crypto_education": range(5, 10),
    "security": range(10, 15),
    "news_trend": range(15, 20),
}


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").lower().strip())


def _article_text(article: dict) -> str:
    parts = [
        article.get("slug", ""),
        article.get("title", ""),
        article.get("excerpt", ""),
        article.get("category", ""),
        article.get("subcategory", ""),
        " ".join(str(t) for t in (article.get("tags") or [])),
    ]
    return _norm(" ".join(parts))


def score_topic(text: str, topic: str) -> int:
    score = 0
    for kw in KEYWORDS.get(topic, ()):
        if kw in text:
            score += 3 if " " in kw else 2
    return score


def detect_topic(article: dict) -> str:
    """Restituisce il topic per logo e palette."""
    text = _article_text(article)
    cat = _norm(article.get("category", ""))

    if cat == "sicurezza":
        return "sicurezza"
    if cat == "cardano":
        return "cardano"
    if cat == "trend":
        if score_topic(text, "eu") >= score_topic(text, "usa"):
            if score_topic(text, "eu") > 0:
                return "eu"
            if score_topic(text, "usa") > 0:
                return "usa"
        return "trend"

    scores = {topic: score_topic(text, topic) for topic in TOPICS if topic not in ("guide", "news")}
    best = max(scores, key=lambda k: scores[k])
    if scores[best] > 0:
        return best

    if cat == "tip":
        return "sicurezza"
    if cat in ("guide", "tutorial"):
        if "bitcoin" in text or "blockchain" in text:
            return "bitcoin"
        return "guide"
    return "guide"


def detect_daily_group(article: dict) -> str:
    """Assegna l'articolo a uno dei 4 blocchi giornalieri (20 post)."""
    text = _article_text(article)
    cat = _norm(article.get("category", ""))
    topic = detect_topic(article)

    if cat == "sicurezza" or topic == "sicurezza" or (
        cat == "tip" and any(k in text for k in ("phishing", "truff", "seed", "sicurezz", "wallet", "2fa"))
    ):
        return "security"

    if cat == "trend" or topic in ("trend", "news", "eu", "usa"):
        return "news_trend"

    if topic in ("stablecoin", "defi", "cefi", "nft", "tokenomics") or (
        cat == "tip" and topic not in ("bitcoin", "blockchain", "sicurezza")
    ):
        return "crypto_education"

    if topic in ("bitcoin", "blockchain", "ethereum") or "blockchain" in text or "bitcoin" in text:
        return "bitcoin_blockchain"

    if cat in ("guide", "tutorial"):
        if any(k in text for k in ("defi", "stablecoin", "nft", "tokenomic", "uniswap", "aave")):
            return "crypto_education"
        if any(k in text for k in ("phishing", "truff", "seed", "sicurezz")):
            return "security"
        return "bitcoin_blockchain"

    return "crypto_education"


def topic_label(topic: str) -> str:
    return TOPIC_LABELS.get(topic, topic.upper())
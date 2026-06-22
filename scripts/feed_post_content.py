#!/usr/bin/env python3
"""Genera titoli clickbait, testo breve e CTA da articoli del sito."""

from __future__ import annotations

import hashlib
import re

from topic_detect import detect_topic, topic_label

CTA_POOL = (
    "Scopri di più",
    "Leggi l'articolo completo",
    "Continua sul sito",
    "Approfondisci ora",
    "Impara in 2 minuti",
)

HOOK_TEMPLATES = (
    "La verità su {topic} in 10 secondi",
    "Il trucco che nessuno ti dice su {topic}",
    "{topic}: spiegato facile",
    "Quello che devi sapere su {topic}",
    "{topic} senza confusione",
    "Guida rapida: {topic}",
    "Perché {topic} cambia tutto",
    "Errori da evitare con {topic}",
)

ALT_HOOK_TEMPLATES = (
    "{short_title}? Ecco la risposta",
    "Hai capito davvero {topic}?",
    "{topic}: la guida che ti serviva",
    "Principianti: {topic} in parole semplici",
    "Il segreto di {topic} che pochi conoscono",
    "{topic} — tutto quello che conta",
)

SECURITY_HOOKS = (
    "Come evitare la prossima truffa crypto",
    "Attenzione: questo errore ti costa caro",
    "Proteggiti prima che sia troppo tardi",
    "La checklist anti-truffa che funziona",
    "Sicurezza crypto: non saltare questo",
)

TREND_HOOKS = (
    "Cosa sta cambiando nel mondo crypto",
    "Trend 2026: non restare indietro",
    "Aggiornamento che devi conoscere",
    "Il mercato si muove: ecco perché",
    "Novità crypto spiegate in modo semplice",
)


def _short_topic_name(topic: str, article: dict) -> str:
    label = topic_label(topic)
    names = {
        "bitcoin": "Bitcoin",
        "defi": "la DeFi",
        "sicurezza": "la sicurezza crypto",
        "exchange": "gli exchange",
        "stablecoin": "le stablecoin",
        "blockchain": "la blockchain",
        "nft": "gli NFT",
        "cardano": "Cardano",
        "ethereum": "Ethereum",
        "tokenomics": "la tokenomics",
        "cefi": "il CeFi",
    }
    if topic in names:
        return names[topic]
    title = (article.get("title") or "").split(":")[0].strip()
    if len(title) <= 42:
        return title
    return label if label != "GUIDA" else "questo argomento crypto"


def _seed(slug: str, variant: str) -> int:
    h = hashlib.md5(f"{slug}:{variant}".encode()).hexdigest()
    return int(h[:8], 16)


def _pick(pool: tuple[str, ...], slug: str, variant: str) -> str:
    return pool[_seed(slug, variant) % len(pool)]


def _clean_excerpt(article: dict, max_len: int = 160) -> str:
    text = (article.get("excerpt") or "").strip()
    text = re.sub(r"\s+", " ", text)
    if len(text) <= max_len:
        return text
    cut = text[: max_len - 1].rsplit(" ", 1)[0]
    return cut + "…"


def _short_title(article: dict, max_len: int = 48) -> str:
    title = (article.get("title") or "Crypto").strip()
    if len(title) <= max_len:
        return title
    return title[: max_len - 1].rsplit(" ", 1)[0] + "…"


def build_hook(article: dict, *, variant: str = "primary") -> str:
    slug = article.get("slug", "")
    topic = detect_topic(article)
    group_seed = _seed(slug, variant)

    if topic == "sicurezza" and variant == "primary":
        return _pick(SECURITY_HOOKS, slug, variant)
    if topic in ("trend", "news", "eu", "usa") and variant == "primary":
        return _pick(TREND_HOOKS, slug, variant)

    topic_name = _short_topic_name(topic, article)
    templates = HOOK_TEMPLATES if variant == "primary" else ALT_HOOK_TEMPLATES
    template = templates[group_seed % len(templates)]
    hook = template.format(topic=topic_name, short_title=_short_title(article))
    if len(hook) > 72:
        hook = hook[:69] + "…"
    return hook


def build_body(article: dict) -> str:
    return _clean_excerpt(article, max_len=155)


def build_cta(article: dict, *, variant: str = "primary") -> str:
    slug = article.get("slug", "")
    return _pick(CTA_POOL, slug, f"cta-{variant}")


def build_caption(article: dict, *, variant: str = "primary", lang: str = "it") -> str:
    """Caption senza link — solo hook, testo e CTA."""
    hook = build_hook(article, variant=variant)
    body = build_body(article)
    cta = build_cta(article, variant=variant)
    topic = detect_topic(article)
    badge = topic_label(topic)

    tags: list[str] = []
    for raw in (article.get("tags") or [])[:4]:
        clean = str(raw).lstrip("#").strip()
        if clean:
            tags.append(f"#{clean}")

    base = "#crypto #CryptoItaliaFacile #educazione #bitcoin"
    if lang == "en":
        return (
            f"🔥 {hook}\n\n"
            f"📌 {badge}\n\n"
            f"{body}\n\n"
            f"👉 {cta}\n\n"
            f"{' '.join(tags)} #CryptoEducation #Bitcoin"
        ).strip()[:2200]

    return (
        f"🔥 {hook}\n\n"
        f"📌 {badge}\n\n"
        f"{body}\n\n"
        f"👉 {cta}\n\n"
        f"{' '.join(tags)} {base}"
    ).strip()[:2200]


def post_payload(article: dict, *, variant: str = "primary") -> dict:
    """Dati per rendering grafico e pubblicazione."""
    return {
        "slug": article["slug"],
        "topic": detect_topic(article),
        "topic_label": topic_label(detect_topic(article)),
        "hook": build_hook(article, variant=variant),
        "body": build_body(article),
        "cta": build_cta(article, variant=variant),
        "caption_it": build_caption(article, variant=variant, lang="it"),
        "caption_en": build_caption(article, variant=variant, lang="en"),
        "variant": variant,
    }
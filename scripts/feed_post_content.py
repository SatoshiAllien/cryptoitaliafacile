#!/usr/bin/env python3
"""Genera titolo, sottotitolo, testo breve e CTA da articoli del sito."""

from __future__ import annotations

import hashlib
import re

from topic_detect import detect_topic, topic_label

CTA_POOL = (
    "Scopri di più",
    "Leggi l'articolo",
    "Continua sul sito",
    "Approfondisci ora",
    "Impara in 2 minuti",
)

TITLE_TEMPLATES = (
    "La verità su {topic} in 10 secondi",
    "Il trucco che nessuno ti dice su {topic}",
    "{topic}: spiegato facile",
    "Quello che devi sapere su {topic}",
    "{topic} senza confusione",
    "Guida rapida: {topic}",
    "Perché {topic} cambia tutto",
    "Errori da evitare con {topic}",
)

ALT_TITLE_TEMPLATES = (
    "{short_title}? Ecco la risposta",
    "Hai capito davvero {topic}?",
    "{topic}: la guida che ti serviva",
    "Principianti: {topic} in parole semplici",
    "Il segreto di {topic} che pochi conoscono",
    "{topic} — tutto quello che conta",
)

SUBTITLE_TEMPLATES = (
    "{topic_label} · Spiegato facile per tutti",
    "Crypto Italia Facile · {topic_label}",
    "Guida chiara · {topic_label}",
    "Per principianti · {topic_label}",
)

SECURITY_TITLES = (
    "Come evitare la prossima truffa crypto",
    "Attenzione: questo errore ti costa caro",
    "Proteggiti prima che sia troppo tardi",
    "La checklist anti-truffa che funziona",
    "Sicurezza crypto: non saltare questo",
)

TREND_TITLES = (
    "Cosa sta cambiando nel mondo crypto",
    "Trend 2026: non restare indietro",
    "Aggiornamento che devi conoscere",
    "Il mercato si muove: ecco perché",
    "Novità crypto spiegate in modo semplice",
)


def _short_topic_name(topic: str, article: dict) -> str:
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
    label = topic_label(topic)
    return label if label != "GUIDA" else "questo argomento crypto"


def _seed(slug: str, variant: str, salt: str = "") -> int:
    h = hashlib.md5(f"{slug}:{variant}:{salt}".encode()).hexdigest()
    return int(h[:8], 16)


def _pick(pool: tuple[str, ...], slug: str, variant: str, salt: str = "") -> str:
    return pool[_seed(slug, variant, salt) % len(pool)]


def _clean_text(text: str, max_len: int) -> str:
    text = re.sub(r"\s+", " ", (text or "").strip())
    if len(text) <= max_len:
        return text
    cut = text[: max_len - 1].rsplit(" ", 1)[0]
    return cut + "…"


def _short_title(article: dict, max_len: int = 48) -> str:
    title = (article.get("title") or "Crypto").strip()
    if len(title) <= max_len:
        return title
    return title[: max_len - 1].rsplit(" ", 1)[0] + "…"


def build_title(article: dict, *, variant: str = "primary") -> str:
    slug = article.get("slug", "")
    topic = detect_topic(article)
    group_seed = _seed(slug, variant, "title")

    if topic == "sicurezza" and variant == "primary":
        return _pick(SECURITY_TITLES, slug, variant, "title")
    if topic in ("trend", "news", "eu", "usa") and variant == "primary":
        return _pick(TREND_TITLES, slug, variant, "title")

    topic_name = _short_topic_name(topic, article)
    templates = TITLE_TEMPLATES if variant == "primary" else ALT_TITLE_TEMPLATES
    template = templates[group_seed % len(templates)]
    title = template.format(topic=topic_name, short_title=_short_title(article))
    return _clean_text(title, 72)


def build_subtitle(article: dict, *, variant: str = "primary") -> str:
    slug = article.get("slug", "")
    topic = detect_topic(article)
    label = topic_label(topic)
    template = _pick(SUBTITLE_TEMPLATES, slug, variant, "sub")
    subtitle = template.format(topic_label=label)
    difficulty = article.get("difficulty", "")
    if difficulty == "beginner":
        subtitle = f"Per principianti · {label}"
    return _clean_text(subtitle, 56)


def build_body(article: dict) -> str:
    return _clean_text(article.get("excerpt") or "", 200)


def build_cta(article: dict, *, variant: str = "primary") -> str:
    return _pick(CTA_POOL, article.get("slug", ""), variant, "cta")


def build_caption(article: dict, *, variant: str = "primary", lang: str = "it") -> str:
    title = build_title(article, variant=variant)
    body = build_body(article)
    cta = build_cta(article, variant=variant)
    badge = topic_label(detect_topic(article))

    tags: list[str] = []
    for raw in (article.get("tags") or [])[:4]:
        clean = str(raw).lstrip("#").strip()
        if clean:
            tags.append(f"#{clean}")

    base = "#crypto #CryptoItaliaFacile #educazione #bitcoin"
    if lang == "en":
        return (
            f"🔥 {title}\n\n"
            f"📌 {badge}\n\n"
            f"{body}\n\n"
            f"👉 {cta}\n\n"
            f"{' '.join(tags)} #CryptoEducation #Bitcoin"
        ).strip()[:2200]

    return (
        f"🔥 {title}\n\n"
        f"📌 {badge}\n\n"
        f"{body}\n\n"
        f"👉 {cta}\n\n"
        f"{' '.join(tags)} {base}"
    ).strip()[:2200]


def post_payload(article: dict, *, variant: str = "primary") -> dict:
    topic = detect_topic(article)
    title = build_title(article, variant=variant)
    subtitle = build_subtitle(article, variant=variant)
    body = build_body(article)
    cta = build_cta(article, variant=variant)
    return {
        "slug": article["slug"],
        "topic": topic,
        "topic_label": topic_label(topic),
        "title": title,
        "subtitle": subtitle,
        "body": body,
        "cta": cta,
        "hook": title,
        "caption_it": build_caption(article, variant=variant, lang="it"),
        "caption_en": build_caption(article, variant=variant, lang="en"),
        "variant": variant,
    }
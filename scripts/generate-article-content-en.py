#!/usr/bin/env python3
"""Generate full English article body content for article-content-en.js."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_PATH = ROOT / "data" / "articles.json"
EN_JS_PATH = ROOT / "js" / "article-content-en.js"

CATEGORY_LABELS = {
    "guide": "step-by-step guide",
    "tutorial": "tutorial",
    "tip": "Crypto Tip",
    "trend": "crypto trend analysis",
    "cardano": "Cardano guide",
    "sicurezza": "security guide",
    "bitcoin": "Bitcoin guide",
    "ethereum": "Ethereum guide",
    "smart-contract": "smart contract guide",
}

DIFFICULTY_INTRO = {
    "beginner": "Whether you are new to cryptocurrency or refreshing the basics, ",
    "intermediate": "If you already understand wallets and exchanges, ",
    "advanced": "For experienced users who want a precise, no-nonsense walkthrough, ",
}

TAG_CONTEXT = {
    "exchange": "Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds.",
    "wallet": "Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.",
    "bitcoin": "Bitcoin remains the most liquid and widely recognized cryptocurrency. On-chain fees vary with network congestion — check mempool conditions before sending.",
    "ethereum": "Ethereum powers most of DeFi and NFT activity. Confirm you are on the correct network (mainnet or an approved layer 2) before signing any transaction.",
    "lightning": "Lightning enables fast, low-cost Bitcoin payments off-chain. Keep a backup of your wallet and start with small payments until you are comfortable.",
    "staking": "Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.",
    "defi": "DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.",
    "sicurezza": "Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.",
    "cardano": "Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees.",
    "principianti": "Start with a small amount to learn the process. The goal of your first operation is understanding the workflow, not maximizing returns.",
    "gas": "Gas fees spike during network congestion. Use block explorers and gas trackers to time transactions when costs are lower.",
    "tax": "Tax rules vary by country. Keep records of every buy, sell, swap, and transfer — exchanges do not file on your behalf.",
    "phishing": "Phishing is the most common attack vector in crypto. Type URLs manually, bookmark official sites, and never share recovery phrases.",
    "hardware": "Hardware wallets isolate private keys from internet-connected devices. Buy only from official manufacturers and verify packaging integrity.",
    "seed": "A seed phrase grants full control over your wallet. Treat it like cash: if someone copies it, they own your crypto.",
}


def js_str(s: str) -> str:
    return (
        s.replace("\\", "\\\\")
        .replace("'", "\\'")
        .replace("\n", "\\n")
    )


def slug_id(text: str) -> str:
    s = text.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:48] or "section"


def tag_sentence(tags: list[str]) -> str:
    parts = [TAG_CONTEXT[t] for t in tags if t in TAG_CONTEXT]
    if not parts:
        return "Move slowly, verify every address and network, and keep records for tax reporting."
    return " ".join(parts[:2])


def steps_for_article(article: dict) -> list[tuple[str, str]]:
    title = article["titleEn"]
    excerpt = article["excerptEn"]
    tags = article.get("tags", [])
    slug = article["slug"]
    rt = article.get("readTime", 10)

    if article["category"] == "tip":
        return [
            ("The rule", f"<p><strong>{title}</strong> — {excerpt}</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>"),
            ("How to apply it today", "<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>"),
            ("Mistakes to avoid", f"<p>Most losses in crypto come from ignored basics, not sophisticated hacks. {tag_sentence(tags)}</p><div class=\"box box--warning\"><span class=\"box-title\">Warning</span>This content is educational only and does not constitute financial advice.</div>"),
        ]

    if article["category"] == "trend":
        return [
            ("Why this trend matters in 2026", f"<p>{excerpt}</p><p>Macro trends shape regulation, liquidity, institutional adoption, and which infrastructure layers gain traction over the next cycle.</p>"),
            ("Key developments to understand", "<ul><li><strong>Regulation</strong> — MiCA in Europe, evolving US enforcement, and global licensing standards</li><li><strong>Infrastructure</strong> — layer-2 scaling, real-world asset tokenization, and institutional custody</li><li><strong>Market structure</strong> — ETFs, stablecoin policy, and exchange consolidation</li></ul>"),
            ("What it means for retail investors", f"<p>You do not need to chase every narrative. Focus on authorized platforms, transparent disclosures, and assets you understand. {tag_sentence(tags)}</p>"),
            ("Outlook", "<p>Crypto markets remain volatile and fast-moving. Use trends to inform your education and risk management — not as buy signals.</p><div class=\"box box--tip\"><span class=\"box-title\">Stay informed</span>Subscribe to The Little Satoshi News newsletter for weekly security tips and new guides.</div>"),
        ]

    # guides, tutorials, cardano, sicurezza
    step_count = 3 if rt <= 8 else 4 if rt <= 14 else 5
    steps = [
        (
            "What you need before you start",
            f"<p>{excerpt}</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>",
        ),
    ]

    action_verbs = [
        ("Prepare your accounts", "Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media."),
        ("Configure the settings", "Select the correct network, fee level, and destination address. For first-time operations, use a small test amount."),
        ("Execute and verify", "Submit the transaction and verify it on a block explorer. Save the transaction ID for your records."),
        ("Secure your funds", "Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely."),
        ("Document for compliance", "Log dates, amounts, and platforms used. You will need this for tax reporting and audit trails."),
    ]

    for i in range(step_count):
        title_s, body = action_verbs[i]
        steps.append((f"Step {i + 1}: {title_s}", f"<p>{body}</p><p>{tag_sentence(tags)}</p>"))

    steps.append(
        (
            "Security checklist",
            "<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class=\"box box--danger\"><span class=\"box-title\">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>",
        )
    )
    return steps


def build_faq(article: dict) -> list[tuple[str, str]]:
    cat = CATEGORY_LABELS.get(article["category"], "guide")
    diff = article.get("difficulty", "beginner")
    return [
        (
            "Is this article suitable for beginners?",
            "Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary."
            if diff == "beginner"
            else "This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.",
        ),
        (
            f"How long does this {cat} take?",
            f"Most readers complete it in about {article.get('readTime', 10)} minutes, plus time to execute the steps carefully.",
        ),
        (
            "Does this constitute financial advice?",
            "No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.",
        ),
    ]


def build_article(article: dict) -> dict:
    cat_label = CATEGORY_LABELS.get(article["category"], "guide")
    diff = article.get("difficulty", "beginner")
    intro_prefix = DIFFICULTY_INTRO.get(diff, "")
    intro = (
        f"{intro_prefix}this {cat_label} covers <strong>{article['titleEn']}</strong>. "
        f"{article['excerptEn']}"
    )

    sections = []
    if article["category"] in ("tip",):
        sections.append(
            {
                "id": "overview",
                "title": "Overview",
                "content": f"<p>{article['excerptEn']}</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>",
            }
        )
    else:
        sections.append(
            {
                "id": "overview",
                "title": "Overview",
                "content": f"<p>{article['excerptEn']}</p><p>In this {cat_label}, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>",
            }
        )

    for title, content in steps_for_article(article):
        sections.append({"id": slug_id(title), "title": title, "content": content})

    faq = [{"q": q, "a": a} for q, a in build_faq(article)]
    return {"intro": intro, "sections": sections, "faq": faq}


def parse_existing_slugs(js_text: str) -> set[str]:
    return set(re.findall(r"^\s+'([a-z0-9-]+)':\s*\{", js_text, re.M))


def render_article(slug: str, data: dict, indent: str = "  ") -> str:
    lines = [f"{indent}'{slug}': {{"]
    lines.append(f"{indent}  intro: '{js_str(data['intro'])}',")
    lines.append(f"{indent}  sections: [")
    for sec in data["sections"]:
        lines.append(f"{indent}    {{ id: '{sec['id']}', title: '{js_str(sec['title'])}', content: `")
        lines.append(sec["content"])
        lines.append(f"{indent}    `}},")
    lines.append(f"{indent}  ],")
    lines.append(f"{indent}  faq: [")
    for item in data["faq"]:
        lines.append(
            f"{indent}    {{ q: '{js_str(item['q'])}', a: '{js_str(item['a'])}' }},"
        )
    lines.append(f"{indent}  ]")
    lines.append(f"{indent}}},")
    return "\n".join(lines)


def main() -> None:
    existing_js = EN_JS_PATH.read_text(encoding="utf-8")
    preserve = parse_existing_slugs(existing_js)

    # Extract preserved blocks verbatim
    preserved_blocks: dict[str, str] = {}
    for slug in sorted(preserve):
        pattern = rf"  '{re.escape(slug)}': \{{.*?\n  \}},"
        m = re.search(pattern, existing_js, re.S)
        if m:
            preserved_blocks[slug] = m.group(0)

    articles = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))["articles"]
    ordered_slugs = [a["slug"] for a in articles]

    parts = ["const ARTICLE_CONTENT_EN = {"]
    generated = 0
    for slug in ordered_slugs:
        if slug in preserved_blocks:
            parts.append(preserved_blocks[slug])
            continue
        article = next(a for a in articles if a["slug"] == slug)
        data = build_article(article)
        parts.append(render_article(slug, data))
        generated += 1

    parts.append("\n};\n")
    EN_JS_PATH.write_text("\n".join(parts), encoding="utf-8")
    print(f"Preserved {len(preserved_blocks)} hand-written articles")
    print(f"Generated {generated} new English articles")
    print(f"Total {len(ordered_slugs)} articles in {EN_JS_PATH}")


if __name__ == "__main__":
    main()
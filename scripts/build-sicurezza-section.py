#!/usr/bin/env python3
"""Build static Sicurezza section: HTML pages, index, and JS content bundles."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from sicurezza_content import (  # noqa: E402
    CONTENT,
    SECURITY_BOX_EN,
    SECURITY_BOX_IT,
    SICUREZZA_CATEGORY_SLUGS,
    SLUGS,
)

ARTICLES_PATH = ROOT / "data" / "articles.json"
SICUREZZA_DIR = ROOT / "sicurezza"
SICUREZZA_JS_PATH = ROOT / "js" / "article-content-sicurezza.js"
EN_JS_PATH = ROOT / "js" / "article-content-en.js"
CSS_VER = "20260703-sicurezza"

DIFF_IT = {"beginner": "Principiante", "intermediate": "Intermedio", "advanced": "Avanzato"}
DIFF_EN = {"beginner": "Beginner", "intermediate": "Intermediate", "advanced": "Advanced"}


def js_str(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n")


def normalize_article(raw: dict, lang: str) -> dict:
    """Convert sicurezza_content tuple format to {intro, sections, faq}."""
    box = SECURITY_BOX_IT if lang == "it" else SECURITY_BOX_EN
    sections = []
    for item in raw["sections"]:
        if len(item) == 3:
            sid, title, content = item
        else:
            sid, title, content = item[0], item[1], item[2]
        sections.append({"id": sid, "title": title, "content": content.strip() + box})
    faq = [{"q": q, "a": a} for q, a in raw["faq"]]
    return {"intro": raw["intro"], "sections": sections, "faq": faq}


def render_js_article(slug: str, data: dict, indent: str = "  ") -> str:
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
        lines.append(f"{indent}    {{ q: '{js_str(item['q'])}', a: '{js_str(item['a'])}' }},")
    lines.append(f"{indent}  ]")
    lines.append(f"{indent}}},")
    return "\n".join(lines)


def render_article_body(data: dict, lang: str) -> str:
    faq_label = "Domande frequenti" if lang == "it" else "FAQ"
    parts = [f'<p class="article-intro">{data["intro"]}</p>']
    for sec in data["sections"]:
        parts.append(f'<h2 id="{sec["id"]}">{sec["title"]}</h2>{sec["content"]}')
    if data.get("faq"):
        parts.append(f'<h2 id="faq">{faq_label}</h2>')
        for item in data["faq"]:
            parts.append(
                f'<details class="faq-item"><summary>{item["q"]}</summary>'
                f'<div class="faq-answer">{item["a"]}</div></details>'
            )
    return "\n".join(parts)


def render_toc(data: dict, lang: str) -> str:
    label = "Indice" if lang == "it" else "Contents"
    items = "".join(
        f'<li><a href="#{s["id"]}">{s["title"]}</a></li>' for s in data["sections"]
    )
    if data.get("faq"):
        faq_label = "Domande frequenti" if lang == "it" else "FAQ"
        items += f'<li><a href="#faq">{faq_label}</a></li>'
    return f'<nav class="toc"><h4>{label}</h4><ul class="toc-list">{items}</ul></nav>'


def social_fallback() -> str:
    return """    <div id="site-social-fallback" class="header-social-bar" role="navigation" aria-label="Social">
    <div class="container header-social-bar-inner">
      <span class="header-social-label">Seguici</span>
      <div class="header-socials">
        <a href="https://www.instagram.com/krown.82/" class="header-social header-social--instagram" target="_blank" rel="noopener noreferrer" aria-label="Instagram" title="@krown.82">IG</a>
        <a href="https://www.facebook.com/profile.php?id=61591151756348" class="header-social header-social--facebook" target="_blank" rel="noopener noreferrer" aria-label="Facebook" title="Facebook">FB</a>
        <a href="https://x.com/TheRiser100x" class="header-social header-social--x" target="_blank" rel="noopener noreferrer" aria-label="X" title="@TheRiser100x">X</a>
      </div>
    </div>
  </div>"""


def scripts_block() -> str:
    return f"""  <script src="../js/site-config.js?v={CSS_VER}"></script>
  <script src="../js/i18n.js?v={CSS_VER}"></script>
  <script src="../js/icons.js?v={CSS_VER}"></script>
  <script src="../js/components.js?v={CSS_VER}"></script>
  <script src="../js/main.js?v={CSS_VER}"></script>"""


def render_article_html(meta: dict, data: dict, lang: str) -> str:
    is_en = lang == "en"
    slug = meta["slug"]
    other = f"{slug}-en.html" if not is_en else f"{slug}.html"
    other_label = "English version" if not is_en else "Versione italiana"
    other_lang = "en" if not is_en else "it"
    home_label = "Home" if is_en else "Home"
    hub_label = "Security" if is_en else "Sicurezza"
    read_label = "min read" if is_en else "min di lettura"
    updated_label = "Updated" if is_en else "Aggiornato"
    back_label = "← All security guides" if is_en else "← Tutte le guide sicurezza"

    title = meta["titleEn"] if is_en else meta["title"]
    excerpt = meta.get("excerptEn", meta["excerpt"]) if is_en else meta["excerpt"]
    date = meta.get("dateEn", meta["date"]) if is_en else meta["date"]
    diff_map = DIFF_EN if is_en else DIFF_IT
    diff_label = diff_map.get(meta.get("difficulty", "beginner"), diff_map["beginner"])

    return f"""﻿<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{excerpt}">
  <title>{title} — The Little Satoshi News</title>
  <link rel="alternate" hreflang="{'en' if is_en else 'it'}" href="{other if is_en else slug + '.html'}">
  <link rel="alternate" hreflang="{'it' if is_en else 'en'}" href="{slug + '.html' if is_en else other}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css?v={CSS_VER}">
</head>
<body data-hub="sicurezza" data-page="article">
  <div class="progress-bar" id="progress-bar"></div>
{social_fallback()}
  <div id="site-header"></div>
  <main class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="../index.html">{home_label}</a><span class="breadcrumb-sep">›</span>
      <a href="index.html">{hub_label}</a><span class="breadcrumb-sep">›</span>
      <span>{title}</span>
    </nav>
    <div class="article-layout">
      <article>
        <header class="article-header">
          <h1>{title}</h1>
          <div class="article-meta-bar">
            <span class="badge badge--{meta.get('difficulty', 'beginner')}">{diff_label}</span>
            <span>📖 {meta['readTime']} {read_label}</span>
            <span>📅 {updated_label} {date}</span>
          </div>
          <p class="article-lang-switch" style="margin-top:1rem;">
            <a href="{other}" class="section-link" hreflang="{other_lang}" lang="{other_lang}">{other_label}</a>
            · <a href="index.html" class="section-link">{back_label}</a>
          </p>
        </header>
        <div class="article-content">
{render_article_body(data, lang)}
        </div>
      </article>
      <aside class="article-sidebar">
        {render_toc(data, lang)}
      </aside>
    </div>
  </main>
  <div id="site-footer"></div>
{scripts_block()}
  <script>
    (function() {{
      var bar = document.getElementById('progress-bar');
      if (!bar) return;
      window.addEventListener('scroll', function() {{
        var h = document.documentElement.scrollHeight - window.innerHeight;
        bar.style.width = (h > 0 ? (window.scrollY / h * 100) : 0) + '%';
      }});
    }})();
  </script>
</body>
</html>
"""


def render_index_card(meta: dict) -> str:
    diff = meta.get("difficulty", "beginner")
    diff_label = DIFF_IT.get(diff, "Principiante")
    return f"""      <a href="{meta['slug']}.html" class="article-card article-card--{diff}">
        <div class="article-card-accent"></div>
        <div class="article-card-body">
          <div class="article-card-top">
            <span class="badge badge--{diff}">{diff_label}</span>
            <span class="article-meta">{meta['readTime']} min</span>
            <a href="{meta['slug']}-en.html" class="section-link" style="margin-left:auto;font-size:0.75rem;" hreflang="en" onclick="event.stopPropagation();">EN</a>
          </div>
          <h3 class="article-card-title">{meta['title']}</h3>
          <p class="article-card-excerpt">{meta['excerpt']}</p>
          <span class="article-card-link">Leggi la guida →</span>
        </div>
      </a>"""


def render_index_html(articles: list[dict]) -> str:
    cards = "\n".join(render_index_card(a) for a in articles)
    return f"""﻿<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Guide sulla sicurezza crypto: seed phrase, hardware wallet, phishing, backup e protezione del portafoglio.">
  <title>Sicurezza Crypto — The Little Satoshi News</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css?v={CSS_VER}">
</head>
<body data-hub="sicurezza">
{social_fallback()}
  <div id="site-header"></div>
  <main class="container">
    <section class="page-hero">
      <h1>Sicurezza &amp; Protezione Wallet</h1>
      <p>Proteggi le tue crypto. Guide su seed phrase, hardware wallet, phishing e best practice.</p>
      <div class="box box--danger" style="margin-top:1.5rem;">
        <span class="box-title">Regola d'oro</span>
        Nessuno legittimo ti chiederà mai la seed phrase. Nemmeno il "supporto tecnico".
      </div>
    </section>
    <div class="articles-grid">
{cards}
    </div>
  </main>
  <div id="site-footer"></div>
{scripts_block()}
</body>
</html>
"""


def patch_en_js(en_blocks: dict[str, str]) -> None:
    text = EN_JS_PATH.read_text(encoding="utf-8")
    for slug, block in en_blocks.items():
        pattern = rf"  '{re.escape(slug)}': \{{.*?\n  \}},"
        if not re.search(pattern, text, re.S):
            print(f"  WARN: slug {slug} not found in article-content-en.js")
            continue
        text = re.sub(pattern, block.rstrip(","), text, count=1, flags=re.S)
    EN_JS_PATH.write_text(text, encoding="utf-8")


def sort_articles(articles: list[dict], slugs: list[str]) -> list[dict]:
    by_slug = {a["slug"]: a for a in articles}
    ordered = [by_slug[s] for s in slugs if s in by_slug]
    return ordered


def main() -> None:
    missing = [s for s in SLUGS if s not in CONTENT]
    if missing:
        raise SystemExit(f"Missing CONTENT for slugs: {missing}")

    articles_data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))["articles"]
    meta_by_slug = {a["slug"]: a for a in articles_data}
    ordered_meta = sort_articles(
        [meta_by_slug[s] for s in SLUGS if s in meta_by_slug],
        SLUGS,
    )

    SICUREZZA_DIR.mkdir(parents=True, exist_ok=True)
    created: list[str] = []

    # IT + EN HTML pages
    for slug in SLUGS:
        meta = meta_by_slug[slug]
        for lang in ("it", "en"):
            data = normalize_article(CONTENT[slug][lang], lang)
            suffix = "" if lang == "it" else "-en"
            path = SICUREZZA_DIR / f"{slug}{suffix}.html"
            path.write_text(render_article_html(meta, data, lang), encoding="utf-8")
            created.append(str(path.relative_to(ROOT)))

    # Index
    index_path = SICUREZZA_DIR / "index.html"
    index_path.write_text(render_index_html(ordered_meta), encoding="utf-8")
    created.append(str(index_path.relative_to(ROOT)))

    # article-content-sicurezza.js (IT only)
    it_parts = ["const ARTICLE_CONTENT_SICUREZZA = {"]
    for slug in SLUGS:
        data = normalize_article(CONTENT[slug]["it"], "it")
        it_parts.append(render_js_article(slug, data))
    it_parts.append("\n};\n")
    SICUREZZA_JS_PATH.write_text("\n".join(it_parts), encoding="utf-8")
    created.append(str(SICUREZZA_JS_PATH.relative_to(ROOT)))

    # Patch EN for category:sicurezza slugs
    en_blocks = {}
    for slug in SICUREZZA_CATEGORY_SLUGS:
        data = normalize_article(CONTENT[slug]["en"], "en")
        en_blocks[slug] = render_js_article(slug, data)
    patch_en_js(en_blocks)

    print(f"✓ Built {len(SLUGS)} articles × 2 languages = {len(SLUGS) * 2} HTML pages")
    print(f"✓ Regenerated sicurezza/index.html ({len(ordered_meta)} cards)")
    print(f"✓ Wrote {SICUREZZA_JS_PATH.name} ({len(SLUGS)} IT articles)")
    print(f"✓ Patched {len(en_blocks)} EN entries in article-content-en.js")
    print(f"✓ Total files touched: {len(created)}")


if __name__ == "__main__":
    main()
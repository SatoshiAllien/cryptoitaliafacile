#!/usr/bin/env python3
"""Gestione completa highlights Instagram @krown.82 per categoria sito.

Pipeline automatizzata:
  1. Piano per 8 categorie (Bitcoin, Cardano, Regolamentazione, News, …)
  2. Rendering grafiche 1080×1920 (modalità highlights)
  3. Push immagini su GitHub Pages
  4. Pubblicazione story con link API invisibile
  5. Istruzioni per rimuovere vecchie highlight e creare album (API limitata)

Uso:
  python manage-instagram-highlights.py --full
  python manage-instagram-highlights.py --plan-only
  python manage-instagram-highlights.py --generate
  python manage-instagram-highlights.py --publish --dry-run
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
import urllib.parse
from datetime import datetime
from pathlib import Path

from PIL import Image

from highlight_categories import (
    HIGHLIGHT_CATEGORIES,
    PLAN_PATH,
    SITE_URL,
    build_category_plan,
    plan_summary,
    save_plan,
)
from instagram_auth import fetch_json, graph_url, resolve_credentials
from story_publish import publish_instagram_story

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
PREVIEWS = Path(r"C:\Users\krown\little-satoshi-news-previews")
ARTICLES_SRC = ROOT / "data" / "articles.json"
ARTICLES_DST = PREVIEWS / "articles.json"
RENDER = PREVIEWS / "render.py"
HIGHLIGHTS_ROOT = ROOT / "assets" / "img" / "instagram" / "highlights"
SLUGS_FILE = ROOT / "data" / "highlights-render-slugs.json"
PUBLISHED_PATH = ROOT / "data" / "instagram-highlights-published.json"
JPEG_QUALITY = 92


def image_public_url(relative_path: str) -> str:
    return f"{SITE_URL}assets/img/instagram/highlights/{urllib.parse.quote(relative_path, safe='/')}"


def try_list_highlights(ig_id: str, token: str) -> dict:
    """Best-effort: l'API Instagram spesso non espone highlights per account business."""
    url = graph_url(
        f"/{ig_id}?fields=highlights{{id,title}}&access_token={urllib.parse.quote(token)}",
        token,
    )
    return fetch_json(url)


def print_api_limitations(existing: dict | None = None) -> None:
    print("\n" + "=" * 64)
    print("LIMITAZIONE API INSTAGRAM — HIGHLIGHTS")
    print("=" * 64)
    if existing and existing.get("error"):
        err = existing["error"]
        print(f"Tentativo API highlights: {err.get('message', err)} (codice {err.get('code', '?')})")
    print("""
L'API Graph Instagram NON supporta:
  • eliminare highlight esistenti
  • creare nuovi album highlight
  • aggiungere story a un album in automatico

Lo script automatizza: grafica, pubblicazione story, link articolo.
La gestione album richiede ~5 minuti manuali nell'app Instagram.
""")


def print_manual_album_steps(plan: dict) -> None:
    print("\n" + "=" * 64)
    print("PASSI MANUALI SU @krown.82 (obbligatori)")
    print("=" * 64)
    print("""
1. Profilo @krown.82 → tieni premuto su OGNI highlight esistente → Elimina
2. Apri le story appena pubblicate (bolla profilo o Archivio)
3. Crea un album per categoria nell'ordine seguente:
""")
    for cat in plan["categories"]:
        if not cat["stories"]:
            continue
        print(f"\n   ▶ Album: \"{cat['title']}\" ({cat['storyCount']} storie)")
        print(f"     Copertina suggerita: {cat.get('coverImage', '—')}")
        for story in cat["stories"]:
            print(f"       {story['orderInCategory']:02d}. {story['title'][:58]}…")
    print("""
4. Per ogni story → ⋯ → Evidenzia → seleziona l'album della categoria
5. Verifica link: swipe up / sticker link su ogni story
6. Ordine album sul profilo (da sinistra):
   Bitcoin → Cardano → Regolamentazione → News → Sicurezza → Mercati → Trend → Guide
""")


def sync_render_input(plan: dict) -> None:
    shutil.copy2(ARTICLES_SRC, ARTICLES_DST)
    SLUGS_FILE.write_text(
        json.dumps(plan["renderSlugs"], indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def render_all(plan: dict) -> int:
    sync_render_input(plan)
    print(f"\n→ Rendering {plan['storyCount']} articoli × 3 varianti (highlights)…\n")
    return subprocess.call(
        [sys.executable, str(RENDER), "--slugs-file", str(SLUGS_FILE), "--highlights"],
        cwd=PREVIEWS,
    )


def integrate_images(plan: dict) -> int:
    if HIGHLIGHTS_ROOT.exists():
        for old in HIGHLIGHTS_ROOT.rglob("*.jpg"):
            old.unlink()
        for old in HIGHLIGHTS_ROOT.rglob("*.json"):
            if old.name == "manifest.json":
                old.unlink()

    ok = 0
    missing: list[str] = []

    for story in plan["stories"]:
        slug = story["slug"]
        variant_key = story["variantKey"]
        src = PREVIEWS / "output" / slug / f"{variant_key}_stories_1080x1920.png"
        if not src.exists():
            missing.append(str(src))
            continue
        dest = HIGHLIGHTS_ROOT / story["imageFile"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        img = Image.open(src).convert("RGB")
        img.save(dest, "JPEG", quality=JPEG_QUALITY, optimize=True)
        print(f"✓ {story['imageFile']}")
        ok += 1

    manifest = HIGHLIGHTS_ROOT / "manifest.json"
    manifest.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"\nIntegrate: {ok}/{plan['storyCount']} immagini in {HIGHLIGHTS_ROOT}")
    if missing:
        print(f"MISSING: {len(missing)} file")
        for m in missing[:5]:
            print(f"  {m}")
        return 1
    return 0


def git_push_highlights(*, dry_run: bool = False) -> int:
    cmd_add = [
        "git", "add",
        "assets/img/instagram/highlights/",
        "data/instagram-highlights-plan.json",
        "data/highlights-render-slugs.json",
    ]
    cmd_commit = [
        "git", "commit", "-m",
        f"feat: highlights IG categorie ({datetime.now().strftime('%Y-%m-%d %H:%M')})",
    ]
    cmd_push = ["git", "push", "origin", "main"]

    for cmd in (cmd_add, cmd_commit, cmd_push):
        if dry_run:
            print(f"[DRY RUN] {' '.join(cmd)}")
            continue
        rc = subprocess.call(cmd, cwd=ROOT)
        if rc != 0 and cmd[1] == "commit":
            print("(commit saltato — niente da committare o già aggiornato)")
        elif rc != 0:
            return rc
    return 0


def wait_pages_deploy(seconds: int = 45) -> None:
    print(f"\n→ Attesa deploy GitHub Pages ({seconds}s)…")
    time.sleep(seconds)
    test_url = image_public_url(plan_cover_test_path())
    try:
        import urllib.request
        urllib.request.urlopen(test_url, timeout=20)
        print(f"✓ Immagini live: {test_url}")
    except Exception as exc:
        print(f"⚠ Pages non ancora pronto ({exc}) — verifica prima di --publish")


def plan_cover_test_path() -> str:
    if PLAN_PATH.exists():
        plan = json.loads(PLAN_PATH.read_text(encoding="utf-8"))
        for cat in plan.get("categories", []):
            if cat.get("coverImage"):
                return cat["coverImage"]
    return "bitcoin/01-comprare-bitcoin-prima-volta-abstract.jpg"


def publish_stories(plan: dict, *, dry_run: bool = False, delay: int = 45) -> dict:
    from instagram_auth import load_env

    env = load_env()
    ig_id, token, api_mode = resolve_credentials(env)
    if not dry_run and (not ig_id or not token):
        raise SystemExit("Manca token Instagram in scripts/.env")

    existing = try_list_highlights(ig_id, token) if ig_id and token and not dry_run else None
    print_api_limitations(existing)

    print(f"\nAccount: @{env.get('INSTAGRAM_USERNAME', 'krown.82')} — API {api_mode}")
    print(f"Story da pubblicare: {plan['storyCount']}\n")

    published: list[dict] = []
    errors: list[dict] = []
    total = plan["storyCount"]
    current_cat = ""

    for i, story in enumerate(plan["stories"], 1):
        if story["highlightTitle"] != current_cat:
            current_cat = story["highlightTitle"]
            print(f"\n{'─' * 40}\n📁 Categoria: {current_cat}\n{'─' * 40}")

        img_file = story["imageFile"]
        local = HIGHLIGHTS_ROOT / img_file
        if not local.exists() and not dry_run:
            errors.append({"story": story["slug"], "error": f"File mancante: {local}"})
            print(f"[{i}/{total}] SKIP — {img_file}")
            continue

        url = image_public_url(img_file)
        print(f"\n[{i}/{total}] {story['title'][:70]}")
        print(f"  Album: {story['highlightTitle']} | Variante: {story['variant']}")
        print(f"  Link API: {story['link']}")

        result = publish_instagram_story(
            ig_id,
            url,
            token,
            dry_run=dry_run,
            use_video=False,
            link_url=story["link"],
        )
        story_id = result.get("id")
        if result.get("error"):
            print(f"  ✗ Errore: {result['error']}")
            errors.append({"story": story["slug"], "error": result["error"]})
        else:
            print(f"  ✓ Story ID: {story_id}")
            published.append({
                **story,
                "storyId": str(story_id or "dry-run"),
                "publishedAt": datetime.now().isoformat(),
            })

        if i < total and not dry_run:
            print(f"  Pausa {delay}s…")
            time.sleep(delay)

    report = {
        "version": 2,
        "account": plan.get("account", "krown.82"),
        "publishedAt": datetime.now().isoformat(),
        "categoryCount": plan["categoryCount"],
        "storyCount": plan["storyCount"],
        "published": published,
        "errors": errors,
        "categories": [
            {"id": c["id"], "title": c["title"], "storyCount": c["storyCount"], "coverImage": c.get("coverImage")}
            for c in plan["categories"]
        ],
    }
    if not dry_run:
        PUBLISHED_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return report


def generate_phase(plan: dict) -> int:
    rc = render_all(plan)
    if rc != 0:
        return rc
    return integrate_images(plan)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Gestione completa highlights Instagram per categoria",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Esempi:
  python manage-instagram-highlights.py --plan-only
  python manage-instagram-highlights.py --generate
  python manage-instagram-highlights.py --publish --delay 30
  python manage-instagram-highlights.py --full --no-push
        """,
    )
    parser.add_argument("--plan-only", action="store_true", help="Solo genera piano JSON")
    parser.add_argument("--generate", action="store_true", help="Genera grafiche highlight")
    parser.add_argument("--publish", action="store_true", help="Pubblica story su Instagram")
    parser.add_argument("--full", action="store_true", help="Piano + generate + push + publish")
    parser.add_argument("--dry-run", action="store_true", help="Simula publish senza API reale")
    parser.add_argument("--no-push", action="store_true", help="Salta git push (full/generate)")
    parser.add_argument("--delay", type=int, default=45, help="Secondi tra story (default 45)")
    parser.add_argument("--max-news", type=int, default=12, help="Max voci News da homepage")
    args = parser.parse_args()

    if not any([args.plan_only, args.generate, args.publish, args.full]):
        parser.print_help()
        return 0

    print("=== Manage Instagram Highlights @krown.82 ===\n")
    print("Categorie:", ", ".join(c["title"] for c in HIGHLIGHT_CATEGORIES))

    plan = save_plan(max_news=args.max_news)
    print("\n" + plan_summary(plan))

    if args.plan_only and not (args.generate or args.publish or args.full):
        return 0

    if args.generate or args.full:
        rc = generate_phase(plan)
        if rc != 0:
            return rc
        if not args.no_push:
            git_push_highlights(dry_run=args.dry_run)
            if not args.dry_run:
                wait_pages_deploy()

    if args.publish or args.full:
        if not args.dry_run and not list(HIGHLIGHTS_ROOT.rglob("*.jpg")):
            raise SystemExit("Nessuna immagine highlight — esegui prima --generate")
        report = publish_stories(plan, dry_run=args.dry_run, delay=args.delay)
        print(f"\nPubblicate: {len(report['published'])}, errori: {len(report['errors'])}")
        print_manual_album_steps(plan)
        return 0 if not report["errors"] else 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
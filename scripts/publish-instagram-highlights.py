#!/usr/bin/env python3
"""Pubblica 20 story highlights su @krown.82 con link articolo (API, invisibile).

Nota: l'API Instagram non permette di creare/rimuovere album Highlights in automatico.
Questo script:
  1. Pubblica 20 story (immagine statica + link sticker API)
  2. Salva gli ID in data/instagram-highlights-published.json
  3. Stampa istruzioni per aggiornare l'album Highlights nel profilo (2 minuti)
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.parse
from datetime import datetime
from pathlib import Path

from highlight_articles import PLAN_PATH, save_plan
from instagram_auth import fetch_json, graph_url, resolve_credentials
from story_publish import publish_instagram_story

ROOT = Path(__file__).resolve().parent.parent
HIGHLIGHTS_DIR = ROOT / "assets" / "img" / "instagram" / "highlights"
PUBLISHED_PATH = ROOT / "data" / "instagram-highlights-published.json"
SITE_URL = "https://satoshiallien.github.io/cryptoitaliafacile/"


def image_url(filename: str) -> str:
    return f"{SITE_URL}assets/img/instagram/highlights/{urllib.parse.quote(filename)}"


def load_plan() -> dict:
    if not PLAN_PATH.exists():
        return save_plan()
    return json.loads(PLAN_PATH.read_text(encoding="utf-8"))


def publish_all(plan: dict, *, dry_run: bool = False, delay: int = 45) -> dict:
    from instagram_auth import load_env

    env = load_env()
    ig_id, token, api_mode = resolve_credentials(env)
    if not dry_run and (not ig_id or not token):
        raise SystemExit("Manca token Instagram in scripts/.env")

    print(f"Account: @{env.get('INSTAGRAM_USERNAME', 'krown.82')} — API {api_mode}")
    print(f"Story da pubblicare: {plan['count']}\n")

    published: list[dict] = []
    errors: list[dict] = []

    for i, item in enumerate(plan["articles"], 1):
        img_file = item["imageFile"]
        local = HIGHLIGHTS_DIR / img_file
        if not local.exists() and not dry_run:
            errors.append({"order": item["order"], "error": f"File mancante: {local}"})
            print(f"[{i}/{plan['count']}] SKIP — {img_file} non trovato")
            continue

        url = image_url(img_file)
        link = item["link"]
        print(f"\n[{i}/{plan['count']}] {item['title']}")
        print(f"  Immagine: {url}")
        print(f"  Link (API, invisibile): {link}")

        result = publish_instagram_story(
            ig_id,
            url,
            token,
            dry_run=dry_run,
            use_video=False,
            link_url=link,
        )
        print(f"  Risultato: {json.dumps(result, indent=2)}")

        if result.get("error"):
            errors.append({"order": item["order"], "slug": item["slug"], "error": result["error"]})
        else:
            entry = {
                **item,
                "storyId": str(result.get("id") or "dry-run"),
                "publishedAt": datetime.now().isoformat(),
            }
            published.append(entry)

        if i < plan["count"] and not dry_run:
            print(f"  Pausa {delay}s...")
            time.sleep(delay)

    report = {
        "account": plan.get("account", "krown.82"),
        "highlightTitle": plan.get("highlightTitle", "Guide Crypto"),
        "publishedAt": datetime.now().isoformat(),
        "published": published,
        "errors": errors,
    }
    if not dry_run:
        PUBLISHED_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return report


def print_manual_steps(plan: dict) -> None:
    title = plan.get("highlightTitle", "Guide Crypto")
    print("\n" + "=" * 60)
    print("AGGIORNA LE HIGHLIGHTS SU @krown.82 (l'API non le gestisce)")
    print("=" * 60)
    print("""
1. Apri Instagram → Profilo @krown.82
2. ELIMINA tutte le vecchie Highlights (tieni premuto → Elimina)
3. Vai alle STORY appena pubblicate (in alto nel feed o Archivio story)
4. Per ogni story → ⋯ → "Evidenzia" → Nuova raccolta "{title}"
   (oppure aggiungi tutte a un'unica raccolta "{title}")
5. Ordine cronologico (dal più vecchio al più recente):
""".format(title=title))
    for item in plan["articles"]:
        print(f"   {item['order']:02d}. {item['title'][:50]}…")
    print(f"""
6. Copertina: usa {plan['articles'][0]['imageFile']}
7. Verifica che il link "CLICCA QUI" / sticker funzioni su ogni story

Le immagini sono già su: {HIGHLIGHTS_DIR}
Manifest: {HIGHLIGHTS_DIR / 'manifest.json'}
""")


def main() -> int:
    parser = argparse.ArgumentParser(description="Pubblica highlights Instagram")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--delay", type=int, default=45)
    parser.add_argument("--plan-only", action="store_true", help="Solo genera piano JSON")
    args = parser.parse_args()

    plan = load_plan()
    if args.plan_only:
        print(json.dumps(plan, indent=2, ensure_ascii=False))
        return 0

    if not HIGHLIGHTS_DIR.exists() or not list(HIGHLIGHTS_DIR.glob("*.jpg")):
        raise SystemExit("Esegui prima: python scripts/generate-instagram-highlights.py")

    report = publish_all(plan, dry_run=args.dry_run, delay=args.delay)
    print(f"\nPubblicate: {len(report['published'])}, errori: {len(report['errors'])}")
    print_manual_steps(plan)
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
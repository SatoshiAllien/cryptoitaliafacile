#!/usr/bin/env python3
"""Genera 20×3 Stories professionali per highlights Instagram @krown.82."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

from highlight_articles import PLAN_PATH, VARIANT_KEYS, save_plan

ROOT = Path(__file__).resolve().parent.parent
PREVIEWS = Path(r"C:\Users\krown\little-satoshi-news-previews")
ARTICLES_SRC = ROOT / "data" / "articles.json"
ARTICLES_DST = PREVIEWS / "articles.json"
RENDER = PREVIEWS / "render.py"
HIGHLIGHTS_OUT = ROOT / "assets" / "img" / "instagram" / "highlights"
JPEG_QUALITY = 92


def sync_articles(plan: dict) -> None:
    shutil.copy2(ARTICLES_SRC, ARTICLES_DST)
    slugs_file = ROOT / "data" / "highlights-render-slugs.json"
    slugs_file.write_text(
        json.dumps([{"slug": a["slug"], "title": a["title"], "category": a["category"]} for a in plan["articles"]], indent=2),
        encoding="utf-8",
    )


def integrate(plan: dict) -> None:
    HIGHLIGHTS_OUT.mkdir(parents=True, exist_ok=True)
    for old in HIGHLIGHTS_OUT.glob("*.jpg"):
        old.unlink()

    ok = 0
    for item in plan["articles"]:
        slug = item["slug"]
        variant_key = item["variantKey"]
        src = PREVIEWS / "output" / slug / f"{variant_key}_stories_1080x1920.png"
        if not src.exists():
            print(f"MISSING {src}")
            continue
        dest = HIGHLIGHTS_OUT / item["imageFile"]
        img = Image.open(src).convert("RGB")
        img.save(dest, "JPEG", quality=JPEG_QUALITY, optimize=True)
        print(f"✓ {dest.name}")
        ok += 1

    manifest = HIGHLIGHTS_OUT / "manifest.json"
    manifest.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nIntegrate: {ok}/{plan['count']} highlights in {HIGHLIGHTS_OUT}")


def main() -> int:
    print("=== Highlights Instagram @krown.82 ===\n")
    plan = save_plan()
    print(f"Articoli selezionati: {plan['count']}")
    for item in plan["articles"]:
        print(f"  {item['order']:02d}. [{item['date']}] {item['slug']} → {item['variant']}")

    sync_articles(plan)

    print("\n→ Rendering 3 varianti × 20 articoli (modalità highlights)...\n")
    slugs_file = ROOT / "data" / "highlights-render-slugs.json"
    rc = subprocess.call(
        [sys.executable, str(RENDER), "--slugs-file", str(slugs_file), "--highlights"],
        cwd=PREVIEWS,
    )
    if rc != 0:
        return rc

    print("\n→ Copia in assets/img/instagram/highlights/...\n")
    integrate(plan)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
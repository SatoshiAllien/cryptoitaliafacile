#!/usr/bin/env python3
"""Genera Stories professionali 1080×1920 (3 varianti × articolo) e integra nel sito."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PREVIEWS = Path(r"C:\Users\krown\little-satoshi-news-previews")
ARTICLES_SRC = ROOT / "data" / "articles.json"
ARTICLES_DST = PREVIEWS / "articles.json"
RENDER = PREVIEWS / "render.py"
INTEGRATE = ROOT / "scripts" / "integrate-preview-images.py"


def sync_articles() -> None:
    shutil.copy2(ARTICLES_SRC, ARTICLES_DST)
    count = len(json.loads(ARTICLES_SRC.read_text(encoding="utf-8"))["articles"])
    print(f"Articoli sincronizzati: {count}")


def main() -> int:
    print("=== Stories professionali CryptoItaliaFacile ===\n")
    sync_articles()

    print("\n→ Rendering 3 varianti × 92 articoli (1080×1920)...\n")
    rc = subprocess.call(
        [sys.executable, str(RENDER), "--all", "--stories-only"],
        cwd=PREVIEWS,
    )
    if rc != 0:
        return rc

    print("\n→ Integrazione FB/IG stories...\n")
    return subprocess.call([sys.executable, str(INTEGRATE)])


if __name__ == "__main__":
    raise SystemExit(main())
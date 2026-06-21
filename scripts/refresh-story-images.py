#!/usr/bin/env python3
"""Ricopia anteprime story professionali e svuota cache video."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    integrate = ROOT / "scripts" / "integrate-preview-images.py"
    print("=== Aggiornamento immagini story (variant-3-overlay 1080x1920) ===\n")
    rc = subprocess.call([sys.executable, str(integrate)])
    if rc != 0:
        return rc
    print("\nStory JPG aggiornate per tutti gli articoli.")
    print("I prossimi post/story useranno automaticamente le nuove immagini.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
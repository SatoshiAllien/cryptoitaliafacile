#!/usr/bin/env python3
"""Applica logo brand a tutte le immagini post esistenti."""

from __future__ import annotations

from pathlib import Path

from brand_overlay import apply_logo_file

ROOT = Path(__file__).resolve().parent.parent
DIRS = [
    ROOT / "assets" / "img" / "facebook" / "posts",
    ROOT / "assets" / "img" / "instagram" / "posts",
    ROOT / "assets" / "img" / "x" / "posts",
]


def main() -> None:
    count = 0
    for folder in DIRS:
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.jpg")):
            apply_logo_file(path)
            print("LOGO", path.relative_to(ROOT))
            count += 1
    print(f"Completato: {count} immagini con logo.")


if __name__ == "__main__":
    main()
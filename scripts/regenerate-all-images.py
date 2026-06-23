#!/usr/bin/env python3
"""Rigenera tutte le immagini post/story professionali."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPTS = [
    "generate-daily-feed-posts.py",
    "generate-story-posts.py",
    "generate-instagram-batch-20.py",
    "generate-fb-images.py",
    "generate-ig-images.py",
    "generate-story-images.py",
    "generate-x-images.py",
]


def main() -> int:
    root = Path(__file__).resolve().parent
    for script in SCRIPTS:
        print(f"\n=== {script} ===")
        rc = subprocess.call([sys.executable, str(root / script)])
        if rc != 0:
            return rc
    print("\nFatto: immagini professionali rigenerate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
#!/usr/bin/env python3
"""Rigenera tutte le immagini post: template originali + crypto + logo piccolo."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent


def main() -> None:
    for script in (
        "generate-fb-images.py",
        "generate-ig-images.py",
        "generate-x-images.py",
        "generate-story-images.py",
        "fetch-mixkit-story-music.py",
    ):
        print(f"=== {script} ===")
        if script == "fetch-mixkit-story-music.py":
            subprocess.run([sys.executable, str(SCRIPTS / script)], check=False)
        else:
            subprocess.check_call([sys.executable, str(SCRIPTS / script)])
    print("=== sync-instagram-trending-audio.py ===")
    subprocess.run([sys.executable, str(SCRIPTS / "sync-instagram-trending-audio.py")], check=False)
    print("Fatto: immagini + stories + musica Mixkit pop/EDM.")


if __name__ == "__main__":
    main()
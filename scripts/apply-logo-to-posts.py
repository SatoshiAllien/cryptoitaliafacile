#!/usr/bin/env python3
"""Rigenera tutte le immagini post: template originali + crypto + logo piccolo."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent


def main() -> None:
    for script in ("generate-fb-images.py", "generate-ig-images.py", "generate-x-images.py"):
        print(f"=== {script} ===")
        subprocess.check_call([sys.executable, str(SCRIPTS / script)])
    print("Fatto: immagini originali con icona crypto + logo brand piccolo.")


if __name__ == "__main__":
    main()
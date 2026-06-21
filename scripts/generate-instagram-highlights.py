#!/usr/bin/env python3
"""Genera highlights Instagram per categoria — wrapper di manage-instagram-highlights."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
MANAGE = SCRIPTS / "manage-instagram-highlights.py"


def main() -> int:
    print("→ Usa manage-instagram-highlights.py --generate\n")
    return subprocess.call([sys.executable, str(MANAGE), "--generate"], cwd=SCRIPTS)


if __name__ == "__main__":
    raise SystemExit(main())
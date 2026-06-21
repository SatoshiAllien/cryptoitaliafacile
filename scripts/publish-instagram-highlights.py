#!/usr/bin/env python3
"""Wrapper legacy — delega a manage-instagram-highlights.py --publish."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

MANAGE = Path(__file__).resolve().parent / "manage-instagram-highlights.py"


def main() -> int:
    print("→ Usa manage-instagram-highlights.py --publish\n")
    cmd = [sys.executable, str(MANAGE), "--publish", *sys.argv[1:]]
    return subprocess.call(cmd, cwd=MANAGE.parent)


if __name__ == "__main__":
    raise SystemExit(main())
#!/usr/bin/env python3
"""Compat: usa fetch-crypto-news.py (White House + crypto virali)."""
import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    script = Path(__file__).resolve().parent / "fetch-crypto-news.py"
    sys.exit(subprocess.call([sys.executable, str(script)]))
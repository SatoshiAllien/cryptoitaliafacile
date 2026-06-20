#!/usr/bin/env python3
"""Pubblica lo stesso articolo su Facebook + Instagram (post feed + story con musica)."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent


def run(script: str, args: list[str]) -> int:
    cmd = [sys.executable, str(SCRIPTS / script), *args]
    print(f"\n{'=' * 60}\n$ {' '.join(cmd)}\n")
    return subprocess.call(cmd)


def main() -> int:
    parser = argparse.ArgumentParser(description="Post sincronizzato FB + IG")
    parser.add_argument("--slug", required=True, help="Slug articolo da pubblicare")
    parser.add_argument("--slot", type=int, default=0, help="Slot per rotazione musica story")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-story", action="store_true")
    parser.add_argument("--skip-facebook", action="store_true")
    parser.add_argument("--skip-instagram", action="store_true")
    args = parser.parse_args()

    common = ["--slug", args.slug, "--slot", str(args.slot)]
    if args.dry_run:
        common.append("--dry-run")
    if args.no_story:
        common.append("--no-story")

    code = 0
    if not args.skip_facebook:
        code = run("post-to-facebook.py", common) or code
    if not args.skip_instagram:
        ig_code = run("post-to-instagram.py", common)
        if ig_code != 0:
            print("\nInstagram fallito — esegui: python scripts/link-instagram-page.py --open")
            code = ig_code or code

    return code


if __name__ == "__main__":
    raise SystemExit(main())
#!/usr/bin/env python3
"""Salva un nuovo token Facebook in scripts/.env e verifica i permessi."""

import re
import subprocess
import sys
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent / ".env"
VERIFY = Path(__file__).resolve().parent / "verify-facebook-token.py"


def upsert_env(key: str, value: str) -> None:
    lines: list[str] = []
    found = False
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith(f"{key}="):
                lines.append(f"{key}={value}")
                found = True
            else:
                lines.append(line)
    if not found:
        lines.append(f"{key}={value}")
    ENV_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    token = " ".join(sys.argv[1:]).strip()
    if not token:
        print("Incolla il nuovo token (EAA...): ", end="", flush=True)
        token = sys.stdin.readline().strip()
    token = re.sub(r"\s+", "", token)
    if not token.startswith("EAA"):
        print("Token non valido. Deve iniziare con EAA")
        return 1

    upsert_env("FACEBOOK_PAGE_ACCESS_TOKEN", token)
    print("Token salvato in", ENV_PATH)
    return subprocess.call([sys.executable, str(VERIFY)])


if __name__ == "__main__":
    raise SystemExit(main())
#!/usr/bin/env python3
"""Salva un nuovo token Facebook in scripts/.env e verifica i permessi."""

import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent / ".env"
VERIFY = Path(__file__).resolve().parent / "verify-facebook-token.py"


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def resolve_page_token(user_token: str) -> str | None:
    """Se il token e' USER, estrae il token Pagina da me/accounts."""
    page_id = load_env().get("FACEBOOK_PAGE_ID", "")
    url = (
        "https://graph.facebook.com/v21.0/me/accounts"
        f"?fields=id,name,access_token&access_token={user_token}"
    )
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None

    pages = data.get("data") or []
    if not pages:
        return None

    for page in pages:
        if page_id and str(page.get("id")) == str(page_id):
            return page.get("access_token")

    return pages[0].get("access_token")


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
    if token.startswith("IG"):
        from instagram_auth import save_instagram_login_token

        try:
            profile = save_instagram_login_token(token)
        except ValueError as exc:
            print(exc)
            return 1
        print(f"Token Instagram Login salvato — @{profile.get('username')} (id={profile.get('id')})")
        verify_ig = Path(__file__).resolve().parent / "verify-instagram.py"
        return subprocess.call([sys.executable, str(verify_ig)]) if verify_ig.exists() else 0

    if not token.startswith("EAA"):
        print("Token non valido. Deve iniziare con EAA o IG (Instagram Login)")
        return 1

    page_token = resolve_page_token(token)
    if page_token and page_token != token:
        print("Token USER rilevato — estraggo token Pagina da me/accounts...")
        token = page_token

    upsert_env("FACEBOOK_PAGE_ACCESS_TOKEN", token)
    print("Token salvato in", ENV_PATH)
    return subprocess.call([sys.executable, str(VERIFY)])


if __name__ == "__main__":
    raise SystemExit(main())
#!/usr/bin/env python3
"""Verifica setup Instagram Graph API per @bitcoin.is.hope2030."""

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent / ".env"
REQUIRED_SCOPES = {
    "instagram_basic",
    "instagram_content_publish",
    "pages_read_engagement",
    "pages_show_list",
}


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def fetch(url: str) -> dict:
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            return json.loads(body)
        except json.JSONDecodeError:
            return {"error": {"message": body, "code": exc.code}}


def main() -> None:
    env = load_env()
    token = env.get("FACEBOOK_PAGE_ACCESS_TOKEN", "")
    ig_id = env.get("INSTAGRAM_ACCOUNT_ID", "")
    if not token:
        print("Manca FACEBOOK_PAGE_ACCESS_TOKEN")
        sys.exit(1)
    if not ig_id:
        print("Manca INSTAGRAM_ACCOUNT_ID — esegui: python scripts/discover-instagram-id.py")
        sys.exit(1)

    debug = fetch(f"https://graph.facebook.com/v21.0/debug_token?input_token={token}&access_token={token}")
    data = debug.get("data", {})
    scopes = set(data.get("scopes") or [])
    print("Token valido:", data.get("is_valid"))
    print("Permessi:", ", ".join(sorted(scopes)) or "(nessuno)")

    missing = sorted(REQUIRED_SCOPES - scopes)
    if missing:
        print("\nMANCANO permessi:", ", ".join(missing))
        print("Aggiungili in developer.facebook.com → App → Use cases → Instagram")
    else:
        print("\nPermessi Instagram OK.")

    profile = fetch(
        f"https://graph.facebook.com/v21.0/{ig_id}"
        f"?fields=id,username,name,profile_picture_url&access_token={token}"
    )
    if profile.get("error"):
        print("\nProfilo IG non accessibile:", profile["error"].get("message"))
        print("Collega @bitcoin.is.hope2030 a una Facebook Page e rigenera il token.")
        sys.exit(2)

    print(f"\nAccount: @{profile.get('username')} ({profile.get('name')})")
    print(f"ID: {profile.get('id')}")
    expected = env.get("INSTAGRAM_USERNAME", "bitcoin.is.hope2030")
    if profile.get("username", "").lower() != expected.lower().lstrip("@"):
        print(f"Attenzione: atteso @{expected}, trovato @{profile.get('username')}")

    print("\nPronto per 20 post/giorno. Test:")
    print("  python scripts/post-to-instagram.py --auto --slot 0 --dry-run")


if __name__ == "__main__":
    main()
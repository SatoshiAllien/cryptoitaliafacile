#!/usr/bin/env python3
"""Diagnostica e guida collegamento @bitcoin.is.hope2030 ↔ Facebook Page."""

from __future__ import annotations

import json
import subprocess
import sys
import urllib.error
import urllib.request
import webbrowser
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent / ".env"
APP_ID = "1058281383830078"
PAGE_ID_DEFAULT = "1179478878583152"
IG_HANDLE = "bitcoin.is.hope2030"


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
        with urllib.request.urlopen(url, timeout=25) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            return json.loads(body)
        except json.JSONDecodeError:
            return {"error": {"message": body, "code": exc.code}}


def main() -> int:
    env = load_env()
    token = env.get("FACEBOOK_PAGE_ACCESS_TOKEN", "")
    page_id = env.get("FACEBOOK_PAGE_ID", PAGE_ID_DEFAULT)
    ig_id = env.get("INSTAGRAM_ACCOUNT_ID", "")

    if not token:
        print("Manca FACEBOOK_PAGE_ACCESS_TOKEN in scripts/.env")
        return 1

    print("=== Collegamento profili Meta ===\n")
    print(f"Facebook Page: {page_id} (Crypto Italia Facile)")
    print(f"Instagram atteso: @{IG_HANDLE}")
    print(f"INSTAGRAM_ACCOUNT_ID in .env: {ig_id or '(mancante)'}\n")

    debug = fetch(f"https://graph.facebook.com/v21.0/debug_token?input_token={token}&access_token={token}")
    scopes = set((debug.get("data") or {}).get("scopes") or [])
    print("Token valido:", (debug.get("data") or {}).get("is_valid"))
    missing = sorted({"instagram_basic", "instagram_content_publish", "pages_read_engagement"} - scopes)
    if missing:
        print("Permessi mancanti:", ", ".join(missing))
    else:
        print("Permessi Instagram nel token: OK")

    page = fetch(
        f"https://graph.facebook.com/v21.0/{page_id}"
        f"?fields=id,name,link,business,instagram_business_account{{id,username}},"
        f"connected_instagram_account{{id,username}},page_backed_instagram_accounts{{id,username}}"
        f"&access_token={token}"
    )
    if page.get("error"):
        print("Errore Page:", page["error"].get("message"))
        return 2

    print(f"\nPage: {page.get('name')} — {page.get('link')}")
    biz = page.get("business") or {}
    if biz.get("id"):
        print(f"Business Portfolio: {biz.get('name')} (id={biz.get('id')})")

    ig_business = (page.get("instagram_business_account") or {}).get("id")
    ig_connected = (page.get("connected_instagram_account") or {}).get("id")
    backed = (page.get("page_backed_instagram_accounts") or {}).get("data") or []

    status = "NON COLLEGATO"
    if ig_business:
        ig_user = page["instagram_business_account"].get("username", "?")
        status = f"OK — instagram_business_account @{ig_user} (id={ig_business})"
    elif ig_connected:
        status = f"Parziale — connected_instagram_account id={ig_connected}"
    elif backed:
        status = f"SOLO page_backed (id={backed[0].get('id')}) — API publish NON funziona"

    print("\nStato collegamento IG:", status)

    if not ig_business:
        print("\n⚠️  Per pubblicare via API serve instagram_business_account (non page_backed).")
        print("   L'account @bitcoin.is.hope2030 va collegato manualmente alla Page.\n")
        print("Passi (5 minuti):")
        print("  1. Apri Meta Business Suite → Impostazioni account collegati")
        print("  2. Collega Instagram @bitcoin.is.hope2030 alla Page Crypto Italia Facile")
        print("  3. Su Instagram: Impostazioni → Account → Passa a professionale → Business")
        print("  4. Meta App → Ruoli → aggiungi @bitcoin.is.hope2030 come Instagram Tester")
        print("  5. Rigenera token Page e riesegui:")
        print("       python scripts/aggiorna-token-facebook.py <USER_TOKEN>")
        print("       python scripts/discover-instagram-id.py")
        print("       python scripts/verify-instagram.py\n")

        urls = [
            ("Business Suite — collega account", "https://business.facebook.com/settings/instagram-accounts"),
            ("Ruoli app Meta (Instagram Tester)", f"https://developers.facebook.com/apps/{APP_ID}/roles/roles/"),
            ("Graph API Explorer (nuovo token)", f"https://developers.facebook.com/tools/explorer/{APP_ID}/"),
            (f"Profilo Instagram @{IG_HANDLE}", f"https://www.instagram.com/{IG_HANDLE}/"),
            ("Pagina Facebook", f"https://www.facebook.com/{page_id}"),
        ]
        for label, url in urls:
            print(f"  → {label}: {url}")

        if "--open" in sys.argv:
            for _, url in urls[:3]:
                webbrowser.open(url)
            print("\nAperti link nel browser.")
    else:
        print("\nCollegamento OK. Test pubblicazione:")
        print("  python scripts/post-to-instagram.py --slug comprare-bitcoin-prima-volta")
        discover = Path(__file__).resolve().parent / "discover-instagram-id.py"
        if discover.exists():
            subprocess.call([sys.executable, str(discover)])

    return 0 if ig_business else 3


if __name__ == "__main__":
    raise SystemExit(main())
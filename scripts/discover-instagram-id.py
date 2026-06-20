#!/usr/bin/env python3
"""Trova INSTAGRAM_ACCOUNT_ID collegato alla Facebook Page."""

import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent / ".env"
UPDATE = Path(__file__).resolve().parent / "aggiorna-token-facebook.py"


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


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


def main() -> int:
    env = load_env()
    token = env.get("FACEBOOK_PAGE_ACCESS_TOKEN", "")
    page_id = env.get("FACEBOOK_PAGE_ID", "")
    if not token:
        print("Manca FACEBOOK_PAGE_ACCESS_TOKEN in scripts/.env")
        return 1

    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        ig_id = sys.argv[1].strip()
        upsert_env("INSTAGRAM_ACCOUNT_ID", ig_id)
        if len(sys.argv) > 2:
            upsert_env("INSTAGRAM_USERNAME", sys.argv[2].lstrip("@"))
        print(f"Salvato INSTAGRAM_ACCOUNT_ID={ig_id}")
        verify = Path(__file__).resolve().parent / "verify-instagram.py"
        return subprocess.call([sys.executable, str(verify)]) if verify.exists() else 0

    debug = fetch(f"https://graph.facebook.com/v21.0/debug_token?input_token={token}&access_token={token}")
    scopes = set((debug.get("data") or {}).get("scopes") or [])
    ig_scopes = {"instagram_basic", "instagram_content_publish"}
    missing_ig = sorted(ig_scopes - scopes)
    if missing_ig:
        print("Token Page OK ma MANCANO permessi Instagram:", ", ".join(missing_ig))
        print("Graph API Explorer → Generate Token → spunta instagram_basic + instagram_content_publish")
        print("Poi rigenera token PAGINA e: python scripts/aggiorna-token-facebook.py EAA...")
        print()

    candidates: list[tuple[str, str, str]] = []
    page_backed_only: list[tuple[str, str, str]] = []

    if page_id:
        data = fetch(
            f"https://graph.facebook.com/v21.0/{page_id}"
            f"?fields=id,name,instagram_business_account{{id,username}},connected_instagram_account{{id,username}}"
            f"&access_token={token}"
        )
        if data.get("error"):
            print(f"API Page ({page_id}):", data["error"].get("message"))
        for key in ("instagram_business_account", "connected_instagram_account"):
            ig = data.get(key) or {}
            if ig.get("id"):
                candidates.append((ig["id"], ig.get("username") or "?", data.get("name", page_id)))

        backed = fetch(
            f"https://graph.facebook.com/v21.0/{page_id}"
            f"?fields=page_backed_instagram_accounts{{id,username}}&access_token={token}"
        )
        for ig in (backed.get("page_backed_instagram_accounts") or {}).get("data") or []:
            if ig.get("id"):
                page_backed_only.append((ig["id"], ig.get("username") or "(page_backed)", backed.get("name", page_id)))

    accounts = fetch(
        "https://graph.facebook.com/v21.0/me/accounts"
        f"?fields=id,name,instagram_business_account{{id,username}}&access_token={token}"
    )
    for page in accounts.get("data") or []:
        ig = page.get("instagram_business_account") or {}
        if ig.get("id"):
            candidates.append((ig["id"], ig.get("username", "?"), page.get("name", "?")))

    if not candidates:
        if page_backed_only:
            print("ATTENZIONE: trovato solo page_backed (NON pubblicabile via API):")
            for ig_id, username, page_name in page_backed_only:
                print(f"  id={ig_id} ({username}) — Page: {page_name}")
            print()
            print("Il collegamento Business NON è attivo. Dopo aver collegato in Business Suite:")
            print("  1. Rigenera token USER in Graph API Explorer")
            print("  2. python scripts/aggiorna-token-facebook.py <USER_TOKEN>")
            print("  3. Riesegui questo script")
            print()
        print("Nessun instagram_business_account sulla Page", page_id or "(?)")
        if missing_ig:
            print("(Probabile causa: token senza permessi Instagram — rigenera il token.)")
        print()
        print("Passi:")
        print("  1. Apri instagram.com/bitcoin.is.hope2030 → Impostazioni → Account")
        print("  2. Passa a account Business o Creator")
        print("  3. Collegalo a una Facebook Page (Crypto Italia Facile o nuova)")
        print("  4. Meta App → Use cases → aggiungi Instagram API")
        print("     Permessi: instagram_basic, instagram_content_publish")
        print("  5. Rigenera il token Page e riesegui questo script")
        print()
        print("Guida: instagram-auto-setup.html")
        return 2

    print("Account Instagram Business trovati:")
    for ig_id, username, page_name in candidates:
        print(f"  @{username} (id={ig_id}) — collegato a Page: {page_name}")

    target = candidates[0]
    if len(candidates) > 1:
        for ig_id, username, _ in candidates:
            if username.lower() == "bitcoin.is.hope2030":
                target = (ig_id, username, _)
                break

    ig_id, username, page_name = target
    upsert_env("INSTAGRAM_ACCOUNT_ID", ig_id)
    upsert_env("INSTAGRAM_USERNAME", username)
    print(f"\nSalvato INSTAGRAM_ACCOUNT_ID={ig_id} (@{username})")
    verify = Path(__file__).resolve().parent / "verify-instagram.py"
    if verify.exists():
        return subprocess.call([sys.executable, str(verify)])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
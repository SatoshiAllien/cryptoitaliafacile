#!/usr/bin/env python3
"""Collega più account Instagram alla Page/Business Meta.

Account target di default:
  - @krown.82
  - @bitcoin.is.hope2030

Nota: Meta NON permette il link automatico via API senza login del proprietario
degli account. Questo script diagnostica, apre i link giusti e verifica lo stato.
"""

from __future__ import annotations

import json
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent / ".env"
APP_ID = "1058281383830078"
PAGE_ID_DEFAULT = "1179478878583152"
DEFAULT_HANDLES = ("krown.82", "bitcoin.is.hope2030")


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


def fetch(url: str, data: dict | None = None, method: str = "GET") -> dict:
    body = None
    if data is not None:
        body = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=body, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode("utf-8", errors="replace")
        try:
            return json.loads(payload)
        except json.JSONDecodeError:
            return {"error": {"message": payload, "code": exc.code}}


def parse_handles(argv: list[str]) -> list[str]:
    if "--handles" in argv:
        idx = argv.index("--handles")
        raw = argv[idx + 1] if idx + 1 < len(argv) else ""
        return [h.strip().lstrip("@") for h in raw.split(",") if h.strip()]
    return list(DEFAULT_HANDLES)


def page_instagram_state(page_id: str, token: str) -> dict:
    return fetch(
        f"https://graph.facebook.com/v21.0/{page_id}"
        f"?fields=id,name,instagram_business_account{{id,username}},"
        f"connected_instagram_account{{id,username}},"
        f"page_backed_instagram_accounts{{id,username}}"
        f"&access_token={token}"
    )


def business_instagram_state(biz_id: str, token: str) -> dict:
    return fetch(
        f"https://graph.facebook.com/v21.0/{biz_id}"
        f"?fields=id,name,owned_instagram_accounts{{id,username,ig_id}}"
        f"&access_token={token}"
    )


def try_business_discovery(ig_id: str, handle: str, token: str) -> dict | None:
    fields = f"business_discovery.username({handle}){{id,username,name}}"
    result = fetch(f"https://graph.facebook.com/v21.0/{ig_id}?fields={fields}&access_token={token}")
    if result.get("error"):
        return None
    return (result.get("business_discovery") or None)


def main() -> int:
    env = load_env()
    token = env.get("FACEBOOK_PAGE_ACCESS_TOKEN", "")
    page_id = env.get("FACEBOOK_PAGE_ID", PAGE_ID_DEFAULT)
    ig_id = env.get("INSTAGRAM_ACCOUNT_ID", "")
    handles = parse_handles(sys.argv)

    if not token:
        print("Manca FACEBOOK_PAGE_ACCESS_TOKEN in scripts/.env")
        return 1

    print("=== Collegamento multi-account Instagram ===\n")
    print(f"Facebook Page: {page_id}")
    print(f"Account da collegare: {', '.join('@' + h for h in handles)}\n")

    page = page_instagram_state(page_id, token)
    biz = (page.get("business") or {})
    biz_id = biz.get("id", "")
    if not biz_id:
        biz_probe = fetch(f"https://graph.facebook.com/v21.0/{page_id}?fields=business&access_token={token}")
        biz_id = (biz_probe.get("business") or {}).get("id", "")

    ig_business = page.get("instagram_business_account") or {}
    backed = (page.get("page_backed_instagram_accounts") or {}).get("data") or []

    print(f"Page: {page.get('name')}")
    if biz_id:
        owned = business_instagram_state(biz_id, token)
        owned_list = (owned.get("owned_instagram_accounts") or {}).get("data") or []
        print(f"Business: {owned.get('name', biz_id)} — IG owned: {len(owned_list)}")
        for item in owned_list:
            print(f"  ✓ @{item.get('username', '?')} (id={item.get('id')})")
    else:
        owned_list = []

    if ig_business.get("id"):
        print(f"\nPage collegata a: @{ig_business.get('username')} (instagram_business_account)")
    elif backed:
        print(f"\n⚠️  Solo page_backed id={backed[0].get('id')} — NON è un vero collegamento Business")
    else:
        print("\n⚠️  Nessun Instagram collegato alla Page")

    print("\n--- Verifica account richiesti ---")
    linked_usernames = {str(x.get("username", "")).lower() for x in owned_list if x.get("username")}
    if ig_business.get("username"):
        linked_usernames.add(str(ig_business["username"]).lower())

    for handle in handles:
        h = handle.lower()
        print(f"\n@{handle}")
        print(f"  URL: https://www.instagram.com/{handle}/")

        if h in linked_usernames:
            print("  Stato: GIÀ COLLEGATO al Business/Page")
            continue

        discovered = try_business_discovery(ig_id, handle, token) if ig_id else None
        if discovered:
            print(f"  Trovato via API: id={discovered.get('id')} name={discovered.get('name')}")
        else:
            print("  API: non raggiungibile (serve instagram_business_account collegato prima)")

        print("  Azione manuale richiesta:")
        print("    1. Login su Instagram come @" + handle)
        print("    2. Impostazioni → Account → Passa a professionale → Business")
        print("    3. Collega alla Page 'Crypto Italia Facile'")
        print(f"    4. Meta App → aggiungi @{handle} come Instagram Tester")

    upsert_env("INSTAGRAM_ACCOUNTS", ",".join(handles))
    primary = env.get("INSTAGRAM_USERNAME") or handles[-1]
    if handles[0] not in (env.get("INSTAGRAM_USERNAME"), env.get("INSTAGRAM_ACCOUNTS", "")):
        print(f"\nNota: account primario per i post resta @{primary} finché non cambi INSTAGRAM_USERNAME in .env")

    print("\n--- Link rapidi ---")
    urls = [
        ("Collega IG al Business", "https://business.facebook.com/settings/instagram-accounts"),
        ("Impostazioni Page", f"https://www.facebook.com/{page_id}/settings"),
        ("Ruoli app (Tester)", f"https://developers.facebook.com/apps/{APP_ID}/roles/roles/"),
        ("Graph API Explorer", f"https://developers.facebook.com/tools/explorer/{APP_ID}/"),
    ]
    for label, url in urls:
        print(f"  → {label}: {url}")
    for handle in handles:
        print(f"  → @{handle}: https://www.instagram.com/{handle}/")

    if "--open" in sys.argv:
        for _, url in urls[:2]:
            webbrowser.open(url)
        print("\nAperti Business Suite e impostazioni Page nel browser.")

    if "--discover" in sys.argv:
        discover = Path(__file__).resolve().parent / "discover-instagram-id.py"
        if discover.exists():
            subprocess.call([sys.executable, str(discover)])

    ok = bool(ig_business.get("id")) and any(h.lower() in linked_usernames for h in handles)
    if not ok:
        print("\n❌ Collegamento API non completato — serve azione manuale sui 2 account.")
        print("Dopo il collegamento:")
        print("  python scripts/aggiorna-token-facebook.py <USER_TOKEN>")
        print("  python scripts/link-instagram-accounts.py --discover")
        return 3

    print("\n✓ Almeno un account richiesto risulta collegato.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
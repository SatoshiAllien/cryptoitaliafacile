#!/usr/bin/env python3
"""Verifica token e permessi Facebook."""

import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent / ".env"
REQUIRED_SCOPES = {
    "pages_manage_posts",
    "pages_read_engagement",
    "pages_show_list",
}


def load_env() -> dict[str, str]:
    env = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def fetch(url: str, method: str = "GET", data: dict | None = None) -> dict:
    body = None
    if data is not None:
        body = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=body, method=method)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode("utf-8", errors="replace")
        try:
            return json.loads(payload)
        except json.JSONDecodeError:
            return {"error": {"message": payload, "code": exc.code}}


def main() -> None:
    env = load_env()
    token = env.get("FACEBOOK_PAGE_ACCESS_TOKEN", "")
    page_id = env.get("FACEBOOK_PAGE_ID", "")
    if not token:
        print("Manca FACEBOOK_PAGE_ACCESS_TOKEN in scripts/.env")
        sys.exit(1)

    debug = fetch(f"https://graph.facebook.com/v21.0/debug_token?input_token={token}&access_token={token}")
    data = debug.get("data", {})
    scopes = set(data.get("scopes") or [])
    token_type = data.get("type", "")
    print("App:", data.get("application"))
    print("Tipo token:", token_type)
    print("Valido:", data.get("is_valid"))
    print("Permessi attuali:", ", ".join(sorted(scopes)) or "(nessuno)")

    missing = sorted(REQUIRED_SCOPES - scopes)
    if missing:
        print("\nMANCANO permessi:", ", ".join(missing))
        print("Aggiungili qui: https://developers.facebook.com/apps/1058281383830078/use_cases/")
        print("Poi rigenera il token nel Graph API Explorer.")
    else:
        print("\nPermessi OK a livello app.")

    if token_type == "USER":
        print(
            "\nATTENZIONE: questo e' un token UTENTE, non della PAGINA."
            "\nPer pubblicare serve il token Pagina dal Graph API Explorer:"
            "\n  1. https://developers.facebook.com/tools/explorer/1058281383830078/"
            "\n  2. Generate Access Token -> spunta pages_manage_posts"
            "\n  3. Nella finestra Facebook seleziona la pagina The Little Satoshi News"
            "\n  4. Sotto il campo token, menu 'User or Page' -> scegli la PAGINA (non User Token)"
            "\n  5. Copia quel token e riesegui aggiorna-token-facebook.py"
        )

    me = fetch(f"https://graph.facebook.com/v21.0/me?fields=id,name&access_token={token}")
    if "error" not in me:
        print("Account:", me.get("name"), f"({me.get('id')})")

    accounts = fetch(
        "https://graph.facebook.com/v21.0/me/accounts"
        "?fields=id,name,access_token,tasks&access_token=" + token
    )
    pages = accounts.get("data") or []
    if pages:
        print("\nPagine trovate in me/accounts:")
        for page in pages:
            print(f"  - {page.get('name')} (id={page.get('id')})")
    else:
        print("\nme/accounts vuoto: probabilmente usi il nuovo modello Pagina=Profilo.")
        if page_id:
            print(f"Usero FACEBOOK_PAGE_ID={page_id} dal file .env")

    target_id = page_id or me.get("id", "")
    if target_id:
        post = fetch(
            f"https://graph.facebook.com/v21.0/{target_id}/feed",
            method="POST",
            data={"message": "Test API The Little Satoshi News", "access_token": token},
        )
        if post.get("id"):
            print("\nPOST TEST OK — id:", post["id"])
            sys.exit(0)
        err = post.get("error", {})
        print("\nPOST TEST FALLITO:", err.get("message", post))

    sys.exit(2 if missing else 1)


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""Converte un token USER in Page Access Token permanente (non scade)."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent / ".env"
VERIFY = Path(__file__).resolve().parent / "verify-facebook-token.py"
APP_ID = "1058281383830078"
GRAPH = "https://graph.facebook.com/v21.0"


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
        with urllib.request.urlopen(url, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            return json.loads(body)
        except json.JSONDecodeError:
            return {"error": {"message": body, "code": exc.code}}


def debug_token(token: str, *, access_token: str | None = None) -> dict:
    probe = access_token or token
    data = fetch(f"{GRAPH}/debug_token?input_token={urllib.parse.quote(token)}&access_token={urllib.parse.quote(probe)}")
    return data.get("data") or {}


def exchange_long_lived(user_token: str, app_secret: str) -> str:
    qs = urllib.parse.urlencode(
        {
            "grant_type": "fb_exchange_token",
            "client_id": APP_ID,
            "client_secret": app_secret,
            "fb_exchange_token": user_token,
        }
    )
    data = fetch(f"{GRAPH}/oauth/access_token?{qs}")
    if data.get("error"):
        raise RuntimeError(data["error"].get("message", str(data)))
    long_token = data.get("access_token", "")
    if not long_token:
        raise RuntimeError("Scambio long-lived fallito: risposta vuota")
    return long_token


def resolve_page_token(user_token: str, page_id: str) -> tuple[str, str]:
    accounts = fetch(
        f"{GRAPH}/me/accounts?fields=id,name,access_token&access_token={urllib.parse.quote(user_token)}"
    )
    for page in accounts.get("data") or []:
        if str(page.get("id")) == str(page_id):
            token = page.get("access_token") or ""
            if token:
                return token, str(page.get("name") or page_id)

    page = fetch(
        f"{GRAPH}/{page_id}?fields=id,name,access_token&access_token={urllib.parse.quote(user_token)}"
    )
    if page.get("error"):
        raise RuntimeError(page["error"].get("message", str(page)))
    token = page.get("access_token") or ""
    if not token:
        raise RuntimeError(
            "Impossibile ottenere access_token della Page. "
            "Nel Graph API Explorer seleziona User Token (non Page) e rigenera."
        )
    return token, str(page.get("name") or page_id)


def main() -> int:
    env = load_env()
    page_id = env.get("FACEBOOK_PAGE_ID", "")
    app_secret = env.get("FACEBOOK_APP_SECRET", "")

    args = sys.argv[1:]
    if args and args[0] == "--app-secret":
        if len(args) < 2:
            print("Uso: python token-permanente.py --app-secret SECRET [USER_TOKEN]")
            return 1
        app_secret = re.sub(r"\s+", "", args[1])
        user_token = re.sub(r"\s+", "", args[2]) if len(args) >= 3 else ""
    else:
        user_token = re.sub(r"\s+", "", " ".join(args))

    if not user_token:
        user_token = env.get("FACEBOOK_USER_ACCESS_TOKEN", env.get("FACEBOOK_PAGE_ACCESS_TOKEN", ""))
    user_token = re.sub(r"\s+", "", user_token)

    if not user_token.startswith("EAA"):
        print("Serve un token USER da Graph API Explorer (inizia con EAA...).")
        print("https://developers.facebook.com/tools/explorer/1058281383830078/")
        return 1

    if not app_secret:
        print("Manca FACEBOOK_APP_SECRET in scripts/.env")
        print("Trovalo qui: https://developers.facebook.com/apps/1058281383830078/settings/basic/")
        print("Oppure guida senza secret: facebook-token-permanente.html")
        print("Aggiungi: FACEBOOK_APP_SECRET=...  oppure incollalo ora: ", end="", flush=True)
        app_secret = sys.stdin.readline().strip()
    if not app_secret:
        return 1

    if not page_id:
        print("Manca FACEBOOK_PAGE_ID in scripts/.env")
        return 1

    upsert_env("FACEBOOK_APP_SECRET", app_secret)

    info = debug_token(user_token)
    token_type = info.get("type", "?")
    print(f"Token in ingresso: tipo={token_type}, valido={info.get('is_valid')}")
    if token_type == "PAGE":
        print(
            "\nATTENZIONE: hai un token PAGINA (scade). "
            "Per il permanente serve un token USER dal Graph API Explorer."
        )
        print("1. Generate Access Token → permessi pages + instagram")
        print("2. Menu 'User or Page' → scegli USER (non la pagina)")
        print("3. python scripts/token-permanente.py EAA...")
        return 2

    print("Scambio token USER → long-lived (60 giorni)...")
    try:
        long_lived = exchange_long_lived(user_token, app_secret)
    except RuntimeError as exc:
        print("ERRORE scambio:", exc)
        return 2

    print("Estraggo Page Access Token permanente...")
    try:
        page_token, page_name = resolve_page_token(long_lived, page_id)
    except RuntimeError as exc:
        print("ERRORE page token:", exc)
        return 2

    page_info = debug_token(page_token, access_token=long_lived)
    expires = page_info.get("expires_at")
    if expires in (0, None):
        print(f"OK — token Page permanente per: {page_name} ({page_id})")
    else:
        import datetime

        exp = datetime.datetime.fromtimestamp(int(expires), tz=datetime.timezone.utc)
        print(f"Token Page ottenuto, scade: {exp.strftime('%Y-%m-%d %H:%M UTC')}")

    upsert_env("FACEBOOK_PAGE_ACCESS_TOKEN", page_token)
    upsert_env("FACEBOOK_USER_ACCESS_TOKEN", long_lived)
    print(f"Salvato in {ENV_PATH}")

    if VERIFY.exists():
        return subprocess.call([sys.executable, str(VERIFY)])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
#!/usr/bin/env python3
"""Verify X API credentials for @TheRiser100x."""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import secrets
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent / ".env"
REQUIRED = ["X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"]


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def oauth1_signature(method: str, url: str, params: dict, consumer_secret: str, token_secret: str) -> str:
    encoded = "&".join(
        f"{urllib.parse.quote(k, safe='')}={urllib.parse.quote(str(v), safe='')}"
        for k, v in sorted(params.items())
    )
    base = f"{method.upper()}&{urllib.parse.quote(url, safe='')}&{urllib.parse.quote(encoded, safe='')}"
    key = f"{urllib.parse.quote(consumer_secret, safe='')}&{urllib.parse.quote(token_secret, safe='')}"
    digest = hmac.new(key.encode(), base.encode(), hashlib.sha1).digest()
    return base64.b64encode(digest).decode()


def oauth1_header(method: str, url: str, env: dict[str, str]) -> str:
    oauth = {
        "oauth_consumer_key": env["X_API_KEY"],
        "oauth_nonce": secrets.token_hex(16),
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(int(datetime.now().timestamp())),
        "oauth_token": env["X_ACCESS_TOKEN"],
        "oauth_version": "1.0",
    }
    oauth["oauth_signature"] = oauth1_signature(
        method, url, oauth, env["X_API_SECRET"], env["X_ACCESS_TOKEN_SECRET"]
    )
    parts = [f'{urllib.parse.quote(k, safe="")}="{urllib.parse.quote(str(v), safe="")}"' for k, v in sorted(oauth.items())]
    return "OAuth " + ", ".join(parts)


def main() -> None:
    env = load_env()
    missing = [k for k in REQUIRED if not env.get(k)]
    if missing:
        print("Missing X API credentials in scripts/.env:")
        for key in missing:
            print(f"  - {key}")
        print("\nGuide: x-auto-setup.html")
        print("Get keys: https://developer.x.com/")
        sys.exit(1)

    url = "https://api.twitter.com/2/users/me?user.fields=username,name"
    req = urllib.request.Request(url, method="GET", headers={
        "Authorization": oauth1_header("GET", url, env),
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        err = exc.read().decode("utf-8", errors="replace")
        print(f"X API error {exc.code}: {err}")
        sys.exit(1)

    user = data.get("data") or {}
    username = user.get("username", "?")
    name = user.get("name", "?")
    print(f"OK — authenticated as @{username} ({name})")
    if username.lower() != "theriser100x":
        print("Warning: expected @TheRiser100x — generate tokens while logged into that account.")
    print("Ready for automatic posting (5 posts/day, English, with images).")


if __name__ == "__main__":
    main()
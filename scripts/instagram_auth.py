"""Credenziali Instagram: Facebook Login (EAA) o Instagram Login (IGAA)."""

from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

FB_GRAPH = "https://graph.facebook.com/v21.0"
IG_GRAPH = "https://graph.instagram.com/v21.0"
ENV_PATH = Path(__file__).resolve().parent / ".env"


def is_instagram_login_token(token: str) -> bool:
    return token.startswith("IG")


def graph_base(token: str) -> str:
    return IG_GRAPH if is_instagram_login_token(token) else FB_GRAPH


def graph_url(path: str, token: str) -> str:
    if path.startswith("http"):
        return path
    if not path.startswith("/"):
        path = "/" + path
    return f"{graph_base(token)}{path}"


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


def fetch_json(url: str, timeout: int = 30) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "CryptoFacile/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            return json.loads(body)
        except json.JSONDecodeError:
            return {"error": {"message": body, "code": exc.code}}


def discover_instagram_login_profile(token: str) -> dict | None:
    """Profilo @krown.82 da token IGAA (Instagram Login)."""
    data = fetch_json(
        f"{IG_GRAPH}/me?fields=id,username,user_id,name&access_token={urllib.parse.quote(token)}"
    )
    if data.get("error"):
        return None
    user_id = data.get("user_id") or data.get("id")
    if not user_id:
        return None
    return {
        "id": str(user_id),
        "username": data.get("username", ""),
        "name": data.get("name", ""),
        "app_scoped_id": str(data.get("id", "")),
    }


def resolve_credentials(env: dict | None = None) -> tuple[str, str, str]:
    """Ritorna (ig_id, token, mode) con mode 'instagram' o 'facebook'."""
    env = env or load_env()
    ig_token = env.get("INSTAGRAM_ACCESS_TOKEN", "")
    page_token = env.get("FACEBOOK_PAGE_ACCESS_TOKEN", "")
    ig_id = env.get("INSTAGRAM_ACCOUNT_ID", "")

    if ig_token:
        if not ig_id:
            profile = discover_instagram_login_profile(ig_token)
            if profile:
                ig_id = profile["id"]
        return ig_id, ig_token, "instagram"

    return ig_id, page_token, "facebook"


def save_instagram_login_token(token: str) -> dict:
    profile = discover_instagram_login_profile(token)
    if not profile:
        raise ValueError("Token IGAA non valido o scaduto")

    upsert_env("INSTAGRAM_ACCESS_TOKEN", token)
    upsert_env("INSTAGRAM_ACCOUNT_ID", profile["id"])
    upsert_env("INSTAGRAM_USERNAME", profile.get("username", "krown.82"))
    return profile
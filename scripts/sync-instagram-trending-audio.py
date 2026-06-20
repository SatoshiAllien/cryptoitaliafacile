#!/usr/bin/env python3
"""Sincronizza tracce trending da Instagram Audio API nella playlist virale."""

from __future__ import annotations

import json
import re
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = Path(__file__).resolve().parent / ".env"
PLAYLIST_PATH = ROOT / "data" / "viral-story-playlist.json"
AUDIO_DIR = ROOT / "assets" / "audio" / "viral-stories" / "trending"
GRAPH = "https://graph.facebook.com/v21.0"
MAX_TRENDING = 6


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:40] or "trending-track"


def fetch_trending(ig_id: str, token: str) -> list[dict]:
    url = f"{GRAPH}/ig_audio?audio_type=music&user_id={ig_id}&access_token={token}"
    try:
        with urllib.request.urlopen(url, timeout=45) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print("API trending non disponibile:", body[:300])
        return []
    return (data.get("audio") or [])[:MAX_TRENDING]


def download_mp3(url: str, dest: Path) -> bool:
    if not url:
        return False
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "CryptoFacile/1.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            dest.write_bytes(resp.read())
        return dest.stat().st_size > 1000
    except Exception as exc:
        print("Download fallito:", dest.name, exc)
        return False


def main() -> int:
    env = load_env()
    token = env.get("FACEBOOK_PAGE_ACCESS_TOKEN", "")
    ig_id = env.get("INSTAGRAM_ACCOUNT_ID", "")
    if not token or not ig_id:
        print("Servono FACEBOOK_PAGE_ACCESS_TOKEN e INSTAGRAM_ACCOUNT_ID")
        return 1

    trending = fetch_trending(ig_id, token)
    if not trending:
        print("Nessun audio trending da Meta — usa tracce generate localmente.")
        return 0

    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    playlist = json.loads(PLAYLIST_PATH.read_text(encoding="utf-8"))
    base_tracks = [t for t in playlist.get("tracks", []) if not t.get("from_meta")]
    meta_tracks: list[dict] = []

    for item in trending:
        title = item.get("title") or "Trending"
        artist = item.get("display_artist") or "Trending Now"
        audio_id = item.get("audio_id", "")
        slug = slugify(f"{title}-{artist}")
        filename = f"meta-{slug}.mp3"
        dest = AUDIO_DIR / filename
        if not download_mp3(item.get("download_url", ""), dest):
            continue
        meta_tracks.append({
            "id": f"meta-{slug}",
            "title": title[:60],
            "artist": artist[:40],
            "file": f"trending/{filename}",
            "mood": "trending Instagram",
            "viral_tag": "#TrendingNow",
            "audio_id": audio_id,
            "from_meta": True,
        })
        print("OK trending", title, "—", artist)

    if not meta_tracks:
        print("Download trending fallito — restano tracce generate.")
        return 0

    playlist["tracks"] = meta_tracks + base_tracks
    playlist["updated"] = date.today().isoformat()
    playlist["source"] = "instagram-trending-sync + generated-viral"
    PLAYLIST_PATH.write_text(json.dumps(playlist, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Aggiornata playlist: {len(meta_tracks)} trending + {len(base_tracks)} generate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
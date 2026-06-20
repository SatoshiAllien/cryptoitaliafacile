#!/usr/bin/env python3
"""Scarica musica pop/EDM royalty-free da Mixkit per le Stories."""

from __future__ import annotations

import json
import re
import subprocess
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

try:
    import imageio_ffmpeg
except ImportError:
    imageio_ffmpeg = None  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
PLAYLIST_PATH = ROOT / "data" / "viral-story-playlist.json"
OUT_DIR = ROOT / "assets" / "audio" / "viral-stories" / "mixkit"
MANIFEST_PATH = ROOT / "data" / "mixkit-tracks.json"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) CryptoFacile/1.0"

MIXKIT_PAGES = [
    "https://mixkit.co/free-stock-music/edm/",
    "https://mixkit.co/free-stock-music/dance-pop/",
    "https://mixkit.co/free-stock-music/electropop/",
    "https://mixkit.co/free-stock-music/house/",
    "https://mixkit.co/free-stock-music/future-bass/",
    "https://mixkit.co/free-stock-music/electro-house/",
    "https://mixkit.co/free-stock-music/pop/",
]

PREFERRED_GENRES = {
    "edm", "house", "dance-pop", "electropop", "future bass", "electro house",
    "pop", "trance", "techno", "electronic", "disco",
}

MAX_TRACKS = 20
CLIP_SECONDS = 18


def ffmpeg_exe() -> str:
    if imageio_ffmpeg is None:
        raise SystemExit("Installa imageio-ffmpeg: pip install imageio-ffmpeg")
    return imageio_ffmpeg.get_ffmpeg_exe()


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", errors="replace")


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:50] or "track"


def parse_music_recordings(html: str) -> list[dict]:
    tracks: list[dict] = []
    seen: set[str] = set()
    pattern = re.compile(
        r'"@type":"MusicRecording"'
        r',"name":"([^"]+)"'
        r',"genre":"([^"]*)"'
        r',"byArtist":"([^"]+)"'
        r',"duration":"[^"]*"'
        r',"url":"(https://assets\.mixkit\.co/music/\d+/\d+\.mp3)"'
    )
    for name, genre, artist, url in pattern.findall(html):
        if url in seen:
            continue
        seen.add(url)
        tracks.append({
            "title": name,
            "artist": artist,
            "genre": genre.lower(),
            "download_url": url,
        })
    return tracks


def discover_tracks() -> list[dict]:
    all_tracks: list[dict] = []
    seen_urls: set[str] = set()

    for page in MIXKIT_PAGES:
        try:
            html = fetch(page)
        except urllib.error.HTTPError as exc:
            print("SKIP", page, exc.code)
            continue
        for track in parse_music_recordings(html):
            if track["download_url"] in seen_urls:
                continue
            seen_urls.add(track["download_url"])
            all_tracks.append(track)

    preferred = [t for t in all_tracks if any(g in t["genre"] for g in PREFERRED_GENRES)]
    pool = preferred if len(preferred) >= MAX_TRACKS else all_tracks
    return pool[:MAX_TRACKS]


def download_mp3(url: str, dest: Path) -> bool:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
        if len(data) < 10000:
            return False
        dest.write_bytes(data)
        return True
    except Exception as exc:
        print("Download fallito:", dest.name, exc)
        return False


def trim_mp3(src: Path, dest: Path, seconds: int = CLIP_SECONDS) -> None:
    subprocess.run(
        [
            ffmpeg_exe(), "-y", "-i", str(src),
            "-t", str(seconds),
            "-af", "afade=t=out:st=14:d=3,loudnorm=I=-14:TP=-1.5:LRA=11",
            "-codec:a", "libmp3lame", "-b:a", "192k",
            str(dest),
        ],
        check=True,
        capture_output=True,
    )


def main() -> int:
    print("Ricerca tracce Mixkit pop/EDM (audio reale)...")
    tracks = discover_tracks()
    print(f"Trovate {len(tracks)} tracce")

    if not tracks:
        print("Nessuna traccia trovata.")
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    playlist_tracks: list[dict] = []

    for meta in tracks:
        track_id = f"mixkit-{slugify(meta['title'])}"
        filename = f"{track_id}.mp3"
        raw_path = OUT_DIR / f"{track_id}-full.mp3"
        clip_path = OUT_DIR / filename

        if not raw_path.exists():
            print(f"  Scarico: {meta['title']} — {meta['artist']}")
            if not download_mp3(meta["download_url"], raw_path):
                continue
        try:
            trim_mp3(raw_path, clip_path)
        except subprocess.CalledProcessError as exc:
            print("Trim fallito:", filename, exc.stderr.decode(errors="replace")[:200])
            continue

        tag = "#EDM" if "edm" in meta["genre"] else "#PopEDM"
        playlist_tracks.append({
            "id": track_id,
            "title": meta["title"],
            "artist": meta["artist"],
            "file": f"mixkit/{filename}",
            "mood": meta["genre"] or "pop/EDM",
            "viral_tag": tag,
            "source": "mixkit",
            "license": "Mixkit Free License",
        })
        print("OK", clip_path.relative_to(ROOT))

    if not playlist_tracks:
        print("Nessun file audio valido.")
        return 1

    manifest = {
        "updated": date.today().isoformat(),
        "license": "https://mixkit.co/license/",
        "tracks": playlist_tracks,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    playlist = json.loads(PLAYLIST_PATH.read_text(encoding="utf-8"))
    playlist["name"] = "Pop EDM Viral · Mixkit Real Audio"
    playlist["description"] = "Musica pop/EDM reale royalty-free (Mixkit) — strumenti veri, non sintesi a bip"
    playlist["updated"] = date.today().isoformat()
    playlist["source"] = "mixkit-royalty-free"
    playlist["tracks"] = playlist_tracks
    PLAYLIST_PATH.write_text(json.dumps(playlist, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nPlaylist aggiornata: {len(playlist_tracks)} tracce reali")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
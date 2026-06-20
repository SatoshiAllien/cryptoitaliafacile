#!/usr/bin/env python3
"""Playlist musica Stories — virale trending, rotazione per slot."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAYLIST_PATH = ROOT / "data" / "viral-story-playlist.json"
AUDIO_DIR = ROOT / "assets" / "audio" / "viral-stories"


def load_playlist() -> dict:
    if not PLAYLIST_PATH.exists():
        fallback = ROOT / "data" / "chill-cyber-playlist.json"
        return json.loads(fallback.read_text(encoding="utf-8"))
    return json.loads(PLAYLIST_PATH.read_text(encoding="utf-8"))


def track_for_slot(slot: int, day_index: int = 0, posts_per_day: int = 20) -> dict:
    tracks = load_playlist()["tracks"]
    if not tracks:
        raise ValueError("Playlist vuota")
    idx = (max(0, day_index) * posts_per_day + slot) % len(tracks)
    track = dict(tracks[idx])
    track["index"] = idx
    track["path"] = str(AUDIO_DIR / track["file"])
    return track


def playlist_label() -> str:
    return load_playlist().get("name", "Pop EDM Viral · Stories 2026")


def viral_tag_for_slot(slot: int, day_index: int = 0, posts_per_day: int = 20) -> str:
    track = track_for_slot(slot, day_index, posts_per_day)
    return track.get("viral_tag", "#TrendingNow")
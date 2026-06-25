#!/usr/bin/env python3
"""Config condivisa per post feed + story (20/giorno)."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "data" / "social-post-config.json"


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        return {"stories_enabled": False, "mode": "feed_only"}
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def stories_enabled() -> bool:
    cfg = load_config()
    return bool(cfg.get("stories_enabled")) or cfg.get("mode") == "feed_and_stories"


def apply_story_args(args) -> None:
    """Abilita story da config se non disabilitate esplicitamente."""
    if getattr(args, "no_story", False):
        args.with_story = False
    elif not getattr(args, "with_story", False) and stories_enabled():
        args.with_story = True
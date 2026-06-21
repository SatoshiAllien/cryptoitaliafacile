#!/usr/bin/env python3
"""Pubblica MP4 story su URL accessibile (GitHub) per Instagram video_url."""

from __future__ import annotations

import os
import shutil
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLISHED_DIR = ROOT / "assets" / "video" / "stories" / "published"
SITE_URL = "https://satoshiallien.github.io/cryptoitaliafacile/"
GITHUB_RAW = os.environ.get(
    "GITHUB_RAW_BASE",
    "https://raw.githubusercontent.com/SatoshiAllien/cryptoitaliafacile/main",
)


def _url_reachable(url: str, timeout: int = 15) -> bool:
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "CryptoFacile/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return 200 <= resp.status < 400
    except urllib.error.HTTPError as exc:
        return exc.code == 403 and url.endswith(".mp4")
    except Exception:
        return False


def _git_push_file(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    subprocess.run(["git", "add", rel], cwd=ROOT, check=False, capture_output=True)
    status = subprocess.run(["git", "status", "--porcelain", rel], cwd=ROOT, capture_output=True, text=True)
    if not status.stdout.strip():
        return True
    msg = f"chore: story video {path.name}"
    commit = subprocess.run(["git", "commit", "-m", msg], cwd=ROOT, capture_output=True, text=True)
    if commit.returncode != 0:
        return False
    push = subprocess.run(
        ["git", "push", "origin", "main"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=90,
    )
    return push.returncode == 0


def wait_public_url(candidates: list[str], *, attempts: int = 8, delay: int = 5) -> str:
    for attempt in range(attempts):
        for url in candidates:
            if _url_reachable(url):
                return url
        if attempt < attempts - 1:
            print(f"Attendo URL pubblico story video ({attempt + 1}/{attempts})...")
            time.sleep(delay)
    return candidates[0]


def stage_story_video(video_path: Path, platform: str, *, push_git: bool = True) -> tuple[Path, str]:
    """Copia MP4 in assets pubblicati e restituisce URL per Instagram video_url."""
    if not video_path.exists():
        raise FileNotFoundError(f"Video story non trovato: {video_path}")

    dest = PUBLISHED_DIR / platform / video_path.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists() or dest.stat().st_size != video_path.stat().st_size:
        shutil.copy2(video_path, dest)

    rel = dest.relative_to(ROOT).as_posix()
    raw_url = f"{GITHUB_RAW}/{rel}"
    pages_url = f"{SITE_URL}{rel}"

    if push_git:
        pushed = _git_push_file(dest)
        if pushed:
            print(f"Video story su GitHub: {rel}")
        else:
            print("AVVISO: git push video non riuscito — uso URL se già online")

    public_url = wait_public_url([raw_url, pages_url])
    print(f"URL story video: {public_url}")
    return dest, public_url
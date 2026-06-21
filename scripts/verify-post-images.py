#!/usr/bin/env python3
"""Verifica che ogni articolo abbia immagini social integrate."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_PATH = ROOT / "data" / "articles.json"
SITE_URL = "https://satoshiallien.github.io/cryptoitaliafacile/"
FB_POSTS = ROOT / "assets" / "img" / "facebook" / "posts"
FB_STORIES = ROOT / "assets" / "img" / "facebook" / "stories"
IG_POSTS = ROOT / "assets" / "img" / "instagram" / "posts"
IG_STORIES = ROOT / "assets" / "img" / "instagram" / "stories"


def check_url(url: str) -> bool:
    req = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return 200 <= resp.status < 400
    except urllib.error.HTTPError as exc:
        return 200 <= exc.code < 400
    except Exception:
        return False


def main() -> int:
    data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
    missing_local: list[str] = []
    missing_meta: list[str] = []
    ok = 0

    for article in data["articles"]:
        slug = article["slug"]
        fb = article.get("fbImage")
        ig = article.get("igImage")
        if not fb or not ig:
            missing_meta.append(slug)
            continue
        paths = [
            FB_POSTS / fb,
            FB_STORIES / article.get("fbStoryImage", fb),
            IG_POSTS / ig,
            IG_STORIES / article.get("igStoryImage", ig),
        ]
        if all(p.exists() for p in paths):
            ok += 1
        else:
            missing_local.append(slug)

    print(f"Articoli OK (locale): {ok}/{len(data['articles'])}")
    if missing_meta:
        print(f"Mancano fbImage/igImage: {len(missing_meta)}")
        for s in missing_meta[:5]:
            print(f"  - {s}")
    if missing_local:
        print(f"File mancanti su disco: {len(missing_local)}")
        for s in missing_local[:5]:
            print(f"  - {s}")

    # Campione URL live (dopo deploy)
    sample = data["articles"][0]
    fb_url = SITE_URL + "assets/img/facebook/posts/" + sample["fbImage"]
    live = check_url(fb_url)
    print(f"\nURL live campione ({sample['slug']}): {'OK' if live else 'NON ANCORA ONLINE (deploy pending)'}")

    return 0 if ok == len(data["articles"]) and not missing_meta else 1


if __name__ == "__main__":
    raise SystemExit(main())
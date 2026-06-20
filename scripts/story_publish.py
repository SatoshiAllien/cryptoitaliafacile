#!/usr/bin/env python3
"""Pubblica Stories Facebook Page e Instagram via Graph API."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request

GRAPH = "https://graph.facebook.com/v21.0"


def graph_request(url: str, data: dict | None = None, method: str = "POST", dry_run: bool = False, label: str = "") -> dict:
    if dry_run:
        print(f"[DRY RUN] {method} {label or url}")
        if data:
            for k, v in data.items():
                if k != "access_token":
                    print(f"  {k}: {v}")
        return {"dry_run": True, "id": "dry-run-story"}

    body = None
    if data is not None:
        body = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=body, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode("utf-8", errors="replace")
        try:
            err = json.loads(payload)
        except json.JSONDecodeError:
            err = {"error": {"message": payload, "code": exc.code}}
        err.setdefault("error", {})["http_status"] = exc.code
        return err


def wait_instagram_media(creation_id: str, token: str, *, max_attempts: int = 8) -> dict | None:
    for attempt in range(max_attempts):
        time.sleep(3 if attempt == 0 else 5)
        status = graph_request(
            f"{GRAPH}/{creation_id}?fields=status_code&access_token={urllib.parse.quote(token)}",
            method="GET",
        )
        code = (status.get("status_code") or "").upper()
        if code in ("FINISHED", ""):
            return None
        if code == "ERROR":
            return status
        print(f"Story media status: {code or 'processing'}...")
    return None


def publish_facebook_story(page_id: str, image_url: str, token: str, dry_run: bool = False) -> dict:
    """Carica foto non pubblicata e la pubblica come Story sulla Page."""
    if dry_run:
        graph_request(
            f"{GRAPH}/{page_id}/photos",
            {"url": image_url, "published": "false", "access_token": token},
            dry_run=True,
            label="FB photo (unpublished)",
        )
        graph_request(
            f"{GRAPH}/{page_id}/photo_stories",
            {"photo_id": "dry-run-photo", "access_token": token},
            dry_run=True,
            label="FB photo_stories",
        )
        return {"dry_run": True, "id": "dry-run-fb-story", "post_id": "dry-run-fb-story"}

    photo_url = f"{GRAPH}/{page_id}/photos"
    photo_data = {
        "url": image_url,
        "published": "false",
        "access_token": token,
    }
    photo = graph_request(photo_url, photo_data, label="FB photo (unpublished)")
    if photo.get("error"):
        return photo

    photo_id = photo.get("id")
    if not photo_id:
        return {"error": {"message": f"No photo id: {photo}"}}

    story_url = f"{GRAPH}/{page_id}/photo_stories"
    story = graph_request(story_url, {"photo_id": photo_id, "access_token": token}, label="FB photo_stories")
    if story.get("error"):
        return story
    story.setdefault("photo_id", photo_id)
    return story


def publish_instagram_story(ig_id: str, image_url: str, token: str, dry_run: bool = False) -> dict:
    """Pubblica immagine 9:16 come Story Instagram."""
    if dry_run:
        graph_request(
            f"{GRAPH}/{ig_id}/media",
            {"image_url": image_url, "media_type": "STORIES", "access_token": token},
            dry_run=True,
            label="IG story container",
        )
        graph_request(
            f"{GRAPH}/{ig_id}/media_publish",
            {"creation_id": "dry-run", "access_token": token},
            dry_run=True,
            label="IG story publish",
        )
        return {"dry_run": True, "id": "dry-run-ig-story"}

    create_url = f"{GRAPH}/{ig_id}/media"
    container = graph_request(create_url, {
        "image_url": image_url,
        "media_type": "STORIES",
        "access_token": token,
    }, label="IG story container")
    if container.get("error"):
        return container

    creation_id = container.get("id")
    if not creation_id:
        return {"error": {"message": f"No creation_id: {container}"}}

    processing_err = wait_instagram_media(creation_id, token)
    if processing_err:
        return {"error": {"message": f"Story processing failed: {processing_err}"}}

    publish_url = f"{GRAPH}/{ig_id}/media_publish"
    return graph_request(publish_url, {
        "creation_id": creation_id,
        "access_token": token,
    }, label="IG story publish")
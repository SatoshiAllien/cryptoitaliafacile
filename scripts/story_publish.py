#!/usr/bin/env python3
"""Pubblica Stories Facebook Page e Instagram via Graph API (foto o video con musica)."""

from __future__ import annotations

import json
import mimetypes
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

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
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode("utf-8", errors="replace")
        try:
            err = json.loads(payload)
        except json.JSONDecodeError:
            err = {"error": {"message": payload, "code": exc.code}}
        err.setdefault("error", {})["http_status"] = exc.code
        return err


def multipart_upload(url: str, fields: dict, file_field: str, file_path: Path, token: str, dry_run: bool = False, label: str = "") -> dict:
    if dry_run:
        print(f"[DRY RUN] MULTIPART {label or url}")
        print(f"  {file_field}: {file_path}")
        for k, v in fields.items():
            if k != "access_token":
                print(f"  {k}: {v}")
        return {"dry_run": True, "id": "dry-run-upload"}

    boundary = f"----StoryBoundary{int(time.time() * 1000)}"
    body = bytearray()
    payload = {**fields, "access_token": token}
    for key, value in payload.items():
        body.extend(f"--{boundary}\r\n".encode())
        body.extend(f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode())
        body.extend(f"{value}\r\n".encode())

    mime = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    body.extend(f"--{boundary}\r\n".encode())
    body.extend(
        f'Content-Disposition: form-data; name="{file_field}"; filename="{file_path.name}"\r\n'.encode()
    )
    body.extend(f"Content-Type: {mime}\r\n\r\n".encode())
    body.extend(file_path.read_bytes())
    body.extend(f"\r\n--{boundary}--\r\n".encode())

    req = urllib.request.Request(
        url,
        data=bytes(body),
        method="POST",
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode("utf-8", errors="replace")
        try:
            err = json.loads(payload)
        except json.JSONDecodeError:
            err = {"error": {"message": payload, "code": exc.code}}
        err.setdefault("error", {})["http_status"] = exc.code
        return err


def _rupload_binary(upload_url: str, file_path: Path, token: str) -> dict:
    file_bytes = file_path.read_bytes()
    req = urllib.request.Request(upload_url, data=file_bytes, method="POST")
    req.add_header("Authorization", f"OAuth {token}")
    req.add_header("offset", "0")
    req.add_header("file_size", str(len(file_bytes)))
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode("utf-8", errors="replace")
        try:
            err = json.loads(payload)
        except json.JSONDecodeError:
            err = {"error": {"message": payload, "code": exc.code}}
        err.setdefault("error", {})["http_status"] = exc.code
        return err


def upload_facebook_video_story(page_id: str, video_path: Path, token: str, dry_run: bool = False) -> dict:
    """Upload e pubblica video Story sulla Page (rupload API su /video_stories)."""
    endpoint = f"{GRAPH}/{page_id}/video_stories"
    if dry_run:
        graph_request(
            endpoint,
            {"upload_phase": "start", "file_size": "0", "access_token": token},
            dry_run=True,
            label="FB video_stories start",
        )
        print(f"[DRY RUN] RUPLOAD {video_path}")
        return {"dry_run": True, "post_id": "dry-run-fb-video-story"}

    file_size = video_path.stat().st_size
    started = graph_request(
        endpoint,
        {"upload_phase": "start", "file_size": str(file_size), "access_token": token},
        label="FB video_stories start",
    )
    if started.get("error"):
        return started

    upload_url = started.get("upload_url")
    video_id = started.get("video_id")
    if not upload_url or not video_id:
        return {"error": {"message": f"Upload session story invalida: {started}"}}

    uploaded = _rupload_binary(upload_url, video_path, token)
    if uploaded.get("error"):
        return uploaded

    finished = graph_request(
        endpoint,
        {
            "upload_phase": "finish",
            "video_id": video_id,
            "access_token": token,
        },
        label="FB video_stories finish",
    )
    if finished.get("error"):
        return finished
    finished.setdefault("video_id", video_id)
    return finished


def wait_instagram_media(creation_id: str, token: str, *, max_attempts: int = 10) -> dict | None:
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


def _upload_instagram_resumable(ig_id: str, video_path: Path, token: str, dry_run: bool) -> dict:
    if dry_run:
        graph_request(
            f"{GRAPH}/{ig_id}/media",
            {"upload_type": "resumable", "media_type": "STORIES", "access_token": token},
            dry_run=True,
            label="IG resumable story container",
        )
        print(f"[DRY RUN] UPLOAD bytes {video_path}")
        return {"dry_run": True, "id": "dry-run-ig-story"}

    container = graph_request(
        f"{GRAPH}/{ig_id}/media",
        {"upload_type": "resumable", "media_type": "STORIES", "access_token": token},
        label="IG resumable story container",
    )
    if container.get("error"):
        return container

    creation_id = container.get("id")
    upload_uri = container.get("uri")
    if not creation_id or not upload_uri:
        return {"error": {"message": f"Resumable container invalido: {container}"}}

    file_bytes = video_path.read_bytes()
    req = urllib.request.Request(upload_uri, data=file_bytes, method="POST")
    req.add_header("Authorization", f"OAuth {token}")
    req.add_header("offset", "0")
    req.add_header("file_size", str(len(file_bytes)))
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            upload_result = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode("utf-8", errors="replace")
        return {"error": {"message": payload, "code": exc.code}}

    if upload_result.get("error"):
        return upload_result

    processing_err = wait_instagram_media(creation_id, token)
    if processing_err:
        return {"error": {"message": f"Story processing failed: {processing_err}"}}

    published = graph_request(
        f"{GRAPH}/{ig_id}/media_publish",
        {"creation_id": creation_id, "access_token": token},
        label="IG story publish",
    )
    published.setdefault("creation_id", creation_id)
    return published


def publish_facebook_story(
    page_id: str,
    image_url: str,
    token: str,
    dry_run: bool = False,
    *,
    video_path: Path | None = None,
    use_video: bool = False,
) -> dict:
    """Pubblica Story: video con musica se video_path, altrimenti foto."""
    wants_video = use_video or (video_path is not None and video_path.exists())
    if wants_video:
        if dry_run:
            return upload_facebook_video_story(page_id, video_path or Path("story.mp4"), token, dry_run=True)

        if not video_path or not video_path.exists():
            return {"error": {"message": f"Video story non trovato: {video_path}"}}

        return upload_facebook_video_story(page_id, video_path, token)

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

    photo = graph_request(
        f"{GRAPH}/{page_id}/photos",
        {"url": image_url, "published": "false", "access_token": token},
        label="FB photo (unpublished)",
    )
    if photo.get("error"):
        return photo

    photo_id = photo.get("id")
    if not photo_id:
        return {"error": {"message": f"No photo id: {photo}"}}

    story = graph_request(
        f"{GRAPH}/{page_id}/photo_stories",
        {"photo_id": photo_id, "access_token": token},
        label="FB photo_stories",
    )
    if story.get("error"):
        return story
    story.setdefault("photo_id", photo_id)
    return story


def publish_instagram_story(
    ig_id: str,
    image_url: str,
    token: str,
    dry_run: bool = False,
    *,
    video_path: Path | None = None,
    use_video: bool = False,
) -> dict:
    """Pubblica Story Instagram: video con musica o immagine statica."""
    wants_video = use_video or (video_path is not None and video_path.exists())
    if wants_video:
        result = _upload_instagram_resumable(ig_id, video_path or Path("story.mp4"), token, dry_run)
        if not result.get("error"):
            return result
        print(f"Resumable IG fallito, fallback image_url: {result.get('error')}", flush=True)

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

    container = graph_request(
        f"{GRAPH}/{ig_id}/media",
        {"image_url": image_url, "media_type": "STORIES", "access_token": token},
        label="IG story container",
    )
    if container.get("error"):
        return container

    creation_id = container.get("id")
    if not creation_id:
        return {"error": {"message": f"No creation_id: {container}"}}

    processing_err = wait_instagram_media(creation_id, token)
    if processing_err:
        return {"error": {"message": f"Story processing failed: {processing_err}"}}

    return graph_request(
        f"{GRAPH}/{ig_id}/media_publish",
        {"creation_id": creation_id, "access_token": token},
        label="IG story publish",
    )
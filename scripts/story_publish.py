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

from instagram_auth import graph_url, is_instagram_login_token
from story_video_host import stage_story_video

GRAPH = "https://graph.facebook.com/v21.0"


def _with_story_link(params: dict, link_url: str | None, *, platform: str = "instagram") -> dict:
    if not link_url:
        return params
    params["link"] = link_url
    if platform == "facebook":
        params["cta"] = json.dumps({"type": "SEE_MORE", "value": {"link": link_url}})
    return params


def _link_api_error(result: dict) -> bool:
    err = result.get("error") or {}
    blob = f"{err.get('message', '')} {err.get('error_user_msg', '')}".lower()
    return any(token in blob for token in ("link", "sticker", "invalid parameter", "not supported"))


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


def upload_facebook_video_story(
    page_id: str,
    video_path: Path,
    token: str,
    dry_run: bool = False,
    *,
    link_url: str | None = None,
) -> dict:
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

    finish_params = _with_story_link(
        {
            "upload_phase": "finish",
            "video_id": video_id,
            "access_token": token,
        },
        link_url,
        platform="facebook",
    )
    finished = graph_request(endpoint, finish_params, label="FB video_stories finish")
    if finished.get("error") and link_url and _link_api_error(finished):
        print("Link FB story non supportato via API — overlay visivo attivo, retry senza link.", flush=True)
        finished = graph_request(
            endpoint,
            {"upload_phase": "finish", "video_id": video_id, "access_token": token},
            label="FB video_stories finish (no link)",
        )
    if finished.get("error"):
        return finished
    finished.setdefault("video_id", video_id)
    return finished


def wait_instagram_media(creation_id: str, token: str, *, max_attempts: int = 10) -> dict | None:
    status_url = (
        f"{graph_url(f'/{creation_id}', token)}?fields=status_code&access_token={urllib.parse.quote(token)}"
    )
    for attempt in range(max_attempts):
        time.sleep(3 if attempt == 0 else 5)
        status = graph_request(status_url, method="GET")
        code = (status.get("status_code") or "").upper()
        if code in ("FINISHED", ""):
            return None
        if code == "ERROR":
            return status
        print(f"Story media status: {code or 'processing'}...")
    return None


def _upload_instagram_video_url(
    ig_id: str,
    video_url: str,
    token: str,
    dry_run: bool,
    *,
    link_url: str | None = None,
) -> dict:
    media_url = graph_url(f"/{ig_id}/media", token)
    publish_url = graph_url(f"/{ig_id}/media_publish", token)
    media_params = _with_story_link(
        {"video_url": video_url, "media_type": "STORIES", "access_token": token},
        link_url,
    )
    if dry_run:
        graph_request(media_url, media_params, dry_run=True, label="IG story video_url")
        return {"dry_run": True, "id": "dry-run-ig-story-video"}

    container = graph_request(media_url, media_params, label="IG story video_url")
    if container.get("error") and link_url and _link_api_error(container):
        print("Link IG non supportato via API — usa QR nella story, retry senza link.", flush=True)
        base_params = {"video_url": video_url, "media_type": "STORIES", "access_token": token}
        container = graph_request(media_url, base_params, label="IG story video_url (no link)")
    if container.get("error"):
        return container

    creation_id = container.get("id")
    if not creation_id:
        return {"error": {"message": f"No creation_id: {container}"}}

    processing_err = wait_instagram_media(creation_id, token)
    if processing_err:
        return {"error": {"message": f"Story video processing failed: {processing_err}"}}

    published = graph_request(
        publish_url,
        {"creation_id": creation_id, "access_token": token},
        label="IG story video publish",
    )
    published.setdefault("creation_id", creation_id)
    published.setdefault("video_url", video_url)
    if link_url:
        published["link_requested"] = link_url
        published["link_note"] = "IG API non supporta link cliccabili — QR nella story"
    return published


def _upload_instagram_resumable(
    ig_id: str,
    video_path: Path,
    token: str,
    dry_run: bool,
    *,
    link_url: str | None = None,
) -> dict:
    media_url = graph_url(f"/{ig_id}/media", token)
    media_params = _with_story_link(
        {"upload_type": "resumable", "media_type": "STORIES", "access_token": token},
        link_url,
    )
    if dry_run:
        graph_request(media_url, media_params, dry_run=True, label="IG resumable story container")
        print(f"[DRY RUN] UPLOAD bytes {video_path}")
        return {"dry_run": True, "id": "dry-run-ig-story"}

    container = graph_request(media_url, media_params, label="IG resumable story container")
    if container.get("error") and link_url and _link_api_error(container):
        print("Link sticker IG non supportato via API — overlay visivo attivo, retry senza link.", flush=True)
        base_params = {"upload_type": "resumable", "media_type": "STORIES", "access_token": token}
        container = graph_request(media_url, base_params, label="IG resumable story container (no link)")
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
        graph_url(f"/{ig_id}/media_publish", token),
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
    link_url: str | None = None,
) -> dict:
    """Pubblica Story: video con musica se video_path, altrimenti foto."""
    wants_video = use_video or (video_path is not None and video_path.exists())
    if wants_video:
        if dry_run:
            return upload_facebook_video_story(
                page_id, video_path or Path("story.mp4"), token, dry_run=True, link_url=link_url
            )

        if not video_path or not video_path.exists():
            return {"error": {"message": f"Video story non trovato: {video_path}"}}

        return upload_facebook_video_story(page_id, video_path, token, link_url=link_url)

    if dry_run:
        graph_request(
            f"{GRAPH}/{page_id}/photos",
            {"url": image_url, "published": "false", "access_token": token},
            dry_run=True,
            label="FB photo (unpublished)",
        )
        graph_request(
            f"{GRAPH}/{page_id}/photo_stories",
            _with_story_link({"photo_id": "dry-run-photo", "access_token": token}, link_url, platform="facebook"),
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

    story_params = _with_story_link({"photo_id": photo_id, "access_token": token}, link_url, platform="facebook")
    story = graph_request(f"{GRAPH}/{page_id}/photo_stories", story_params, label="FB photo_stories")
    if story.get("error") and link_url and _link_api_error(story):
        print("Link FB story non supportato via API — overlay visivo attivo, retry senza link.", flush=True)
        story = graph_request(
            f"{GRAPH}/{page_id}/photo_stories",
            {"photo_id": photo_id, "access_token": token},
            label="FB photo_stories (no link)",
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
    link_url: str | None = None,
) -> dict:
    """Pubblica Story Instagram: video con musica o immagine statica."""
    wants_video = use_video or (video_path is not None and video_path.exists())
    if wants_video:
        local_video = video_path or Path("story.mp4")
        if dry_run:
            return _upload_instagram_video_url(
                ig_id, "https://example.com/story.mp4", token, dry_run=True, link_url=link_url
            )

        if local_video.exists():
            try:
                _, public_url = stage_story_video(local_video, "instagram", push_git=True)
                result = _upload_instagram_video_url(
                    ig_id, public_url, token, dry_run=False, link_url=link_url
                )
                if not result.get("error"):
                    return result
                print(f"video_url IG fallito: {result.get('error')}", flush=True)
            except Exception as exc:
                print(f"Hosting video story fallito: {exc}", flush=True)

        if not is_instagram_login_token(token):
            result = _upload_instagram_resumable(ig_id, local_video, token, dry_run, link_url=link_url)
            if not result.get("error"):
                return result
            print(f"Resumable IG fallito: {result.get('error')}", flush=True)

    media_url = graph_url(f"/{ig_id}/media", token)
    publish_url = graph_url(f"/{ig_id}/media_publish", token)
    image_params = _with_story_link(
        {"image_url": image_url, "media_type": "STORIES", "access_token": token},
        link_url,
    )
    if dry_run:
        graph_request(media_url, image_params, dry_run=True, label="IG story container")
        graph_request(
            publish_url,
            {"creation_id": "dry-run", "access_token": token},
            dry_run=True,
            label="IG story publish",
        )
        return {"dry_run": True, "id": "dry-run-ig-story"}

    container = graph_request(media_url, image_params, label="IG story container")
    if container.get("error") and link_url and _link_api_error(container):
        print("Link sticker IG non supportato via API — overlay visivo attivo, retry senza link.", flush=True)
        base_params = {"image_url": image_url, "media_type": "STORIES", "access_token": token}
        container = graph_request(media_url, base_params, label="IG story container (no link)")
    if container.get("error"):
        return container

    creation_id = container.get("id")
    if not creation_id:
        return {"error": {"message": f"No creation_id: {container}"}}

    processing_err = wait_instagram_media(creation_id, token)
    if processing_err:
        return {"error": {"message": f"Story processing failed: {processing_err}"}}

    return graph_request(
        publish_url,
        {"creation_id": creation_id, "access_token": token},
        label="IG story publish",
    )
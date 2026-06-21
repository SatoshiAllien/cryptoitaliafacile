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
from story_links import SATOSHI_AI_STORY_LINK, SATOSHI_STORY_STICKER
from story_video_host import stage_story_video

GRAPH = "https://graph.facebook.com/v21.0"


def _cta_json(cta_type: str, link_url: str) -> str:
    return json.dumps({"type": cta_type, "value": {"link": link_url}}, separators=(",", ":"))


def _fb_link_cta_payloads(link_url: str) -> list[dict]:
    return [
        {"link": link_url, "cta": _cta_json("OPEN_LINK", link_url)},
        {"link": link_url, "cta": _cta_json("VIEW_WEBSITE", link_url)},
        {"link": link_url, "cta": _cta_json("SEE_MORE", link_url)},
        {"link": link_url, "cta": _cta_json("LEARN_MORE", link_url)},
        {"link": link_url},
    ]


def _ig_link_payloads(link_url: str) -> list[dict]:
    """Varianti parametro link per Story Instagram."""
    sticker = SATOSHI_STORY_STICKER
    return [
        {"link": link_url},
        {"link": link_url, "link_text": sticker},
        {"link": link_url, "link_text": "Parla con Satoshi AI"},
        {"website_url": link_url},
    ]


def _with_story_link(
    params: dict,
    link_url: str | None,
    *,
    platform: str = "instagram",
    ig_variant: int = 0,
) -> dict:
    if not link_url:
        return params
    out = dict(params)
    if platform == "facebook":
        payload = _fb_link_cta_payloads(link_url)[0]
        out.update(payload)
        return out
    ig_payload = _ig_link_payloads(link_url)[min(ig_variant, len(_ig_link_payloads(link_url)) - 1)]
    out.update(ig_payload)
    return out


def _fb_finish_attempts(video_id: str, link_url: str | None, token: str) -> list[dict]:
    base = {"upload_phase": "finish", "video_id": video_id, "access_token": token}
    if not link_url:
        return [base]
    return [{**base, **payload} for payload in _fb_link_cta_payloads(link_url)]


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

    finished: dict = {}
    for i, finish_params in enumerate(_fb_finish_attempts(video_id, link_url, token)):
        label = "FB video_stories finish" if i == 0 else f"FB video_stories finish try {i + 1}"
        finished = graph_request(endpoint, finish_params, label=label)
        if not finished.get("error"):
            if link_url and i > 0:
                print(f"Link FB story OK (strategia {i + 1})", flush=True)
            break
        if link_url:
            err = finished.get("error", {})
            print(f"Link FB tentativo {i + 1} fallito: {err.get('message', err)}", flush=True)
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

    container = _ig_story_container(
        media_url,
        {"video_url": video_url, "media_type": "STORIES", "access_token": token},
        link_url,
        label="IG story video_url",
    )
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
        if not published.get("link_attached"):
            published["link_note"] = "Link API IG non disponibile — usa QR Parla con Satoshi AI nella story"
    return published


def _ig_story_container(
    media_url: str,
    base_params: dict,
    link_url: str | None,
    *,
    label: str,
) -> dict:
    if not link_url:
        return graph_request(media_url, base_params, label=label)
    last: dict = {}
    variants = _ig_link_payloads(link_url)
    for i, extra in enumerate(variants):
        params = {**base_params, **extra}
        attempt_label = label if i == 0 else f"{label} link try {i + 1}"
        last = graph_request(media_url, params, label=attempt_label)
        if not last.get("error"):
            if i > 0:
                print(f"Link IG story OK (variante {i + 1})", flush=True)
            last["link_attached"] = True
            return last
        if not _link_api_error(last):
            return last
        err = last.get("error", {})
        print(f"Link IG tentativo {i + 1} fallito: {err.get('message', err)}", flush=True)
    print("Link sticker IG non supportato via API — QR Satoshi AI attivo nella story.", flush=True)
    return graph_request(media_url, base_params, label=f"{label} (no link)")


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

    container = _ig_story_container(
        media_url,
        {"upload_type": "resumable", "media_type": "STORIES", "access_token": token},
        link_url,
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

    story: dict = {}
    if link_url:
        for i, payload in enumerate(_fb_link_cta_payloads(link_url)):
            params = {"photo_id": photo_id, "access_token": token, **payload}
            lbl = "FB photo_stories" if i == 0 else f"FB photo_stories link try {i + 1}"
            story = graph_request(f"{GRAPH}/{page_id}/photo_stories", params, label=lbl)
            if not story.get("error"):
                if i > 0:
                    print(f"Link FB photo story OK (strategia {i + 1})", flush=True)
                break
            err = story.get("error", {})
            print(f"Link FB photo tentativo {i + 1} fallito: {err.get('message', err)}", flush=True)
    else:
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

    container = _ig_story_container(
        media_url,
        {"image_url": image_url, "media_type": "STORIES", "access_token": token},
        link_url,
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
        publish_url,
        {"creation_id": creation_id, "access_token": token},
        label="IG story publish",
    )
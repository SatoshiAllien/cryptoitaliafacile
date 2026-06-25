#!/usr/bin/env python3
"""Classificazione errori Meta Graph API per retry e circuit breaker."""

from __future__ import annotations


def extract_error(result: dict) -> dict:
    err = result.get("error") or {}
    if isinstance(err, dict):
        return err
    return {"message": str(err)}


def is_quota_error(result: dict) -> bool:
    err = extract_error(result)
    if err.get("code") == 9 and err.get("error_subcode") == 2207042:
        return True
    msg = str(err.get("message", "")).lower()
    return "too many actions" in msg or "maximum number of post" in msg


def is_token_error(result: dict) -> bool:
    err = extract_error(result)
    if err.get("code") in (190, 102):
        return True
    msg = str(err.get("message", "")).lower()
    return "expired" in msg or "invalid oauth" in msg or "session has expired" in msg


def is_permission_error(result: dict) -> bool:
    err = extract_error(result)
    if err.get("code") in (10, 200, 294):
        return True
    msg = str(err.get("message", "")).lower()
    return "permission" in msg or "does not have permission" in msg


def is_retryable(result: dict, *, http_status: int | None = None) -> bool:
    if is_token_error(result) or is_permission_error(result):
        return False
    if is_quota_error(result):
        return True
    err = extract_error(result)
    code = err.get("code")
    if http_status and http_status >= 500:
        return True
    if http_status == 429:
        return True
    if code in (1, 2, 4, 17, 32, 613):
        return True
    msg = str(err.get("message", "")).lower()
    if "temporarily unavailable" in msg or "please retry" in msg:
        return True
    if "media" in msg and ("processing" in msg or "not ready" in msg):
        return True
    return False


def error_summary(result: dict, *, http_status: int | None = None) -> str:
    err = extract_error(result)
    parts = [str(err.get("message") or "unknown error")]
    if err.get("code"):
        parts.append(f"code={err['code']}")
    if err.get("error_subcode"):
        parts.append(f"subcode={err['error_subcode']}")
    if http_status:
        parts.append(f"http={http_status}")
    return " | ".join(parts)
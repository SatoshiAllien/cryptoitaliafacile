#!/usr/bin/env python3
"""Crea video Story 9:16 (immagine + musica playlist) per FB/IG."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

try:
    import imageio_ffmpeg
except ImportError:
    imageio_ffmpeg = None  # type: ignore

from chill_cyber_playlist import load_playlist, playlist_label, track_for_slot

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / "assets" / "video" / "stories" / "cache"
FB_STORY_IMG = ROOT / "assets" / "img" / "facebook" / "stories"
IG_STORY_IMG = ROOT / "assets" / "img" / "instagram" / "stories"
STORY_DURATION = 15


def ffmpeg_exe() -> str:
    if imageio_ffmpeg is None:
        raise RuntimeError("Installa imageio-ffmpeg: pip install imageio-ffmpeg")
    return imageio_ffmpeg.get_ffmpeg_exe()


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def overlay_music_badge(
    image_path: Path,
    *,
    playlist_name: str,
    track_title: str,
    track_artist: str,
    viral_tag: str = "#TrendingNow",
    accent: str = "#FF2A6D",
) -> Path:
    img = Image.open(image_path).convert("RGBA")
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    box = (72, 1290, 1008, 1540)
    draw.rounded_rectangle(box, radius=28, fill=(15, 23, 42, 225), outline=accent, width=4)
    tag = viral_tag if viral_tag.startswith("#") else f"#{viral_tag}"
    draw.rounded_rectangle((108, 1310, 380, 1368), radius=18, fill=accent)
    draw.text((128, 1324), f"🔥 {tag}", fill=(15, 23, 42), font=_font(24, bold=True))
    draw.text((108, 1385), "🎵 " + playlist_name, fill="#E2E8F0", font=_font(28, bold=True))
    draw.text((108, 1435), f"▶ {track_title}", fill="#FFFFFF", font=_font(40, bold=True))
    draw.text((108, 1495), track_artist, fill="#94A3B8", font=_font(26))

    out = Image.alpha_composite(img, layer).convert("RGB")
    tmp = Path(tempfile.gettempdir()) / f"story-badge-{image_path.stem}.jpg"
    out.save(tmp, "JPEG", quality=92)
    return tmp


def build_story_video(
    image_path: Path,
    audio_path: Path,
    *,
    playlist_name: str,
    track_title: str,
    track_artist: str,
    viral_tag: str = "#TrendingNow",
    out_path: Path | None = None,
    accent: str = "#FF2A6D",
) -> Path:
    if not image_path.exists():
        raise FileNotFoundError(f"Immagine story non trovata: {image_path}")
    if not audio_path.exists():
        raise FileNotFoundError(f"Traccia audio non trovata: {audio_path}")

    framed = overlay_music_badge(
        image_path,
        playlist_name=playlist_name,
        track_title=track_title,
        track_artist=track_artist,
        viral_tag=viral_tag,
        accent=accent,
    )

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    if out_path is None:
        out_path = CACHE_DIR / f"{image_path.stem}-{Path(audio_path).stem}.mp4"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        ffmpeg_exe(),
        "-y",
        "-loop", "1",
        "-i", str(framed),
        "-i", str(audio_path),
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "128k",
        "-shortest",
        "-t", str(STORY_DURATION),
        "-movflags", "+faststart",
        str(out_path),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    framed.unlink(missing_ok=True)
    return out_path


def prepare_story_video(
    platform: str,
    image_file: str,
    slot: int,
    day_index: int = 0,
    posts_per_day: int = 20,
) -> tuple[Path, dict]:
    """Genera MP4 story con musica virale trending per topic e slot."""
    stem = Path(image_file).stem
    img_dir = FB_STORY_IMG if platform == "facebook" else IG_STORY_IMG
    image_path = img_dir / f"{stem}.jpg"
    track = track_for_slot(slot, day_index, posts_per_day)
    audio_path = Path(track["path"])
    out_path = CACHE_DIR / platform / f"{stem}-{track['id']}.mp4"
    video = build_story_video(
        image_path,
        audio_path,
        playlist_name=playlist_label(),
        track_title=track["title"],
        track_artist=track["artist"],
        viral_tag=track.get("viral_tag", "#TrendingNow"),
        out_path=out_path,
    )
    return video, track
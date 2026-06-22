#!/usr/bin/env python3
"""Crea video Story (immagine + musica) senza link, QR o sticker."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

try:
    import imageio_ffmpeg
except ImportError:
    imageio_ffmpeg = None  # type: ignore

from chill_cyber_playlist import playlist_label, track_for_slot
from story_links import SATOSHI_STORY_CTA, SATOSHI_STORY_SUBTITLE, SATOSHI_STORY_TITLE

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / "assets" / "video" / "stories" / "cache"
FB_STORY_IMG = ROOT / "assets" / "img" / "facebook" / "stories"
IG_STORY_IMG = ROOT / "assets" / "img" / "instagram" / "stories"
STORY_DURATION = 15
STORY_VARIANT_SUFFIXES = ("abstract", "thematic", "minimal")
STORY_OVERLAY_REV = "story-clean-v6"

THEME = {
    "instagram": {
        "accent": "#F7931A",
        "accent2": "#F4C430",
        "title": SATOSHI_STORY_TITLE,
        "subtitle": SATOSHI_STORY_SUBTITLE,
        "cta": SATOSHI_STORY_CTA,
        "tag": "✨ EDUCAZIONE",
    },
    "facebook": {
        "accent": "#F7931A",
        "accent2": "#F4C430",
        "title": SATOSHI_STORY_TITLE,
        "subtitle": SATOSHI_STORY_SUBTITLE,
        "cta": SATOSHI_STORY_CTA,
        "tag": "✨ EDUCAZIONE",
    },
}


def ffmpeg_exe() -> str:
    if imageio_ffmpeg is None:
        raise RuntimeError("Installa imageio-ffmpeg: pip install imageio-ffmpeg")
    return imageio_ffmpeg.get_ffmpeg_exe()


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def _hex_to_rgb(color: str) -> tuple[int, int, int]:
    color = color.lstrip("#")
    return tuple(int(color[i : i + 2], 16) for i in (0, 2, 4))


def story_image_file(article: dict, slot: int = 0) -> str:
    slug = article["slug"]
    suffix = STORY_VARIANT_SUFFIXES[slot % len(STORY_VARIANT_SUFFIXES)]
    fname = f"{slug}-{suffix}.jpg"
    for img_dir in (FB_STORY_IMG, IG_STORY_IMG):
        if (img_dir / fname).exists():
            return fname
    return article.get("fbStoryImage") or article.get("igStoryImage") or f"{slug}.jpg"


def _enhance_base(img: Image.Image) -> Image.Image:
    rgb = img.convert("RGB")
    rgb = ImageEnhance.Color(rgb).enhance(1.12)
    rgb = ImageEnhance.Contrast(rgb).enhance(1.06)
    rgb = ImageEnhance.Brightness(rgb).enhance(1.03)
    return rgb


def overlay_music_badge(
    image_source: Path | Image.Image,
    *,
    playlist_name: str,
    track_title: str,
    track_artist: str,
    viral_tag: str = "#TrendingNow",
    platform: str = "instagram",
) -> Path:
    """Badge musica in basso — nessun link o URL."""
    theme = THEME.get(platform, THEME["instagram"])
    accent = theme["accent"]
    accent2 = theme["accent2"]
    accent_rgb = _hex_to_rgb(accent)
    accent2_rgb = _hex_to_rgb(accent2)

    if isinstance(image_source, Path):
        img = Image.open(image_source).convert("RGBA")
    else:
        img = image_source.convert("RGBA")
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    h = img.height
    box = (56, h - 300, 1024, h - 80)
    draw.rounded_rectangle(box, radius=32, fill=(10, 15, 32, 240), outline=accent_rgb + (255,), width=4)
    tag = viral_tag if viral_tag.startswith("#") else f"#{viral_tag}"
    draw.rounded_rectangle((88, h - 280, 380, h - 220), radius=20, fill=accent2_rgb + (255,))
    draw.text((108, h - 266), f"🔥 {tag}", fill=(15, 23, 42), font=_font(24, bold=True))
    draw.text((88, h - 200), f"🎧 {playlist_name}", fill="#E2E8F0", font=_font(28, bold=True))
    draw.text((88, h - 155), f"▶️ {track_title}", fill="#FFFFFF", font=_font(36, bold=True))
    draw.text((88, h - 110), f"🎤 {track_artist}", fill="#94A3B8", font=_font(24))

    out = Image.alpha_composite(img, layer).convert("RGB")
    stem = image_source.stem if isinstance(image_source, Path) else "story"
    tmp = Path(tempfile.gettempdir()) / f"story-badge-{stem}.jpg"
    out.save(tmp, "JPEG", quality=94)
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
    platform: str = "instagram",
) -> Path:
    if not image_path.exists():
        raise FileNotFoundError(f"Immagine story non trovata: {image_path}")
    if not audio_path.exists():
        raise FileNotFoundError(f"Traccia audio non trovata: {audio_path}")

    base = _enhance_base(Image.open(image_path))
    framed = overlay_music_badge(
        base,
        playlist_name=playlist_name,
        track_title=track_title,
        track_artist=track_artist,
        viral_tag=viral_tag,
        platform=platform,
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
    *,
    link_url: str = "",
) -> tuple[Path, dict]:
    """Genera MP4 story con musica — senza overlay link."""
    _ = link_url
    stem = Path(image_file).stem
    img_dir = FB_STORY_IMG if platform == "facebook" else IG_STORY_IMG
    image_path = img_dir / f"{stem}.jpg"
    track = track_for_slot(slot, day_index, posts_per_day)
    audio_path = Path(track["path"])
    out_path = CACHE_DIR / platform / f"{stem}-{track['id']}-{STORY_OVERLAY_REV}.mp4"
    if (
        out_path.exists()
        and image_path.exists()
        and out_path.stat().st_mtime >= image_path.stat().st_mtime
    ):
        return out_path, track

    video = build_story_video(
        image_path,
        audio_path,
        playlist_name=playlist_label(),
        track_title=track["title"],
        track_artist=track["artist"],
        viral_tag=track.get("viral_tag", "#TrendingNow"),
        out_path=out_path,
        platform=platform,
    )
    return video, track
#!/usr/bin/env python3
"""Crea video Story 9:16 (immagine + musica + QR link) per FB/IG."""

from __future__ import annotations

import subprocess
import tempfile
import urllib.parse
from pathlib import Path

import qrcode
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

try:
    import imageio_ffmpeg
except ImportError:
    imageio_ffmpeg = None  # type: ignore

from chill_cyber_playlist import playlist_label, track_for_slot

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / "assets" / "video" / "stories" / "cache"
FB_STORY_IMG = ROOT / "assets" / "img" / "facebook" / "stories"
IG_STORY_IMG = ROOT / "assets" / "img" / "instagram" / "stories"
SITE_URL = "https://satoshiallien.github.io/cryptoitaliafacile/"
SITE_LABEL = "cryptoitaliafacile.com"
STORY_DURATION = 15

THEME = {
    "instagram": {
        "accent": "#00F0FF",
        "accent2": "#FF2A6D",
        "gold": "#FDE047",
        "cta": "👆 TAP HERE",
        "scan": "📱 Scan QR with camera",
        "hint": "👉 Opens cryptoitaliafacile.com",
        "free": "✨ FREE",
    },
    "facebook": {
        "accent": "#34D399",
        "accent2": "#FDE047",
        "gold": "#00F0FF",
        "cta": "👉 CLICCA QUI",
        "scan": "📱 Scansiona il QR",
        "hint": "👆 Si apre nel browser",
        "free": "✨ GRATIS",
    },
}


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


def _hex_to_rgb(color: str) -> tuple[int, int, int]:
    color = color.lstrip("#")
    return tuple(int(color[i : i + 2], 16) for i in (0, 2, 4))


def short_link_label(link_url: str) -> str:
    parsed = urllib.parse.urlparse(link_url)
    if parsed.netloc.endswith("github.io") and "cryptoitaliafacile" in parsed.path:
        return SITE_LABEL
    host = parsed.netloc.removeprefix("www.")
    if parsed.path.strip("/").startswith("articolo.html"):
        return f"{SITE_LABEL}/guide"
    return host or SITE_LABEL


def make_qr_image(link_url: str, size: int = 220) -> Image.Image:
    qr = qrcode.QRCode(version=None, box_size=8, border=1)
    qr.add_data(link_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0F172A", back_color="#FFFFFF")
    return img.resize((size, size), Image.Resampling.NEAREST).convert("RGB")


def _enhance_base(img: Image.Image) -> Image.Image:
    rgb = img.convert("RGB")
    rgb = ImageEnhance.Color(rgb).enhance(1.18)
    rgb = ImageEnhance.Contrast(rgb).enhance(1.08)
    rgb = ImageEnhance.Brightness(rgb).enhance(1.04)
    return rgb


def overlay_link_panel(
    image_path: Path,
    *,
    link_url: str,
    platform: str = "instagram",
) -> Path:
    """Pannello QR + CTA: l'unico modo affidabile per aprire il sito da Story IG."""
    theme = THEME.get(platform, THEME["instagram"])
    accent = theme["accent"]
    accent2 = theme["accent2"]
    accent_rgb = _hex_to_rgb(accent)
    accent2_rgb = _hex_to_rgb(accent2)

    img = _enhance_base(Image.open(image_path))
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    # Vignetta soft in basso per leggibilità
    for y in range(900, 1920):
        alpha = int(min(180, (y - 900) * 0.22))
        draw.line([(0, y), (1080, y)], fill=(8, 12, 28, alpha))

    box = (56, 980, 1024, 1260)
    draw.rounded_rectangle(box, radius=36, fill=(12, 18, 38, 235), outline=accent_rgb + (255,), width=4)
    draw.rounded_rectangle((56, 980, 1024, 1048), radius=36, fill=accent2_rgb + (220,))

    draw.text((88, 996), theme["cta"], fill=(15, 23, 42), font=_font(30, bold=True))
    draw.text((780, 996), theme["free"], fill=(15, 23, 42), font=_font(24, bold=True))

    qr = make_qr_image(link_url, size=200)
    qr_rgba = qr.convert("RGBA")
    layer.paste(qr_rgba, (88, 1068), qr_rgba)
    draw.rounded_rectangle((80, 1060, 296, 1276), radius=16, outline=accent_rgb + (255,), width=3)

    label = short_link_label(link_url)
    draw.text((330, 1080), f"🌐 {label}", fill="#FFFFFF", font=_font(40, bold=True))
    draw.text((330, 1140), theme["scan"], fill=accent, font=_font(28, bold=True))
    draw.text((330, 1190), theme["hint"], fill="#CBD5E1", font=_font(26))
    draw.rounded_rectangle((330, 1220, 990, 1250), radius=12, fill=accent_rgb + (60,))
    draw.text((350, 1224), f"🔗 {link_url[:52]}{'…' if len(link_url) > 52 else ''}", fill="#E2E8F0", font=_font(20))

    out = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
    tmp = Path(tempfile.gettempdir()) / f"story-link-{image_path.stem}.jpg"
    out.save(tmp, "JPEG", quality=94)
    return tmp


def overlay_music_badge(
    image_path: Path,
    *,
    playlist_name: str,
    track_title: str,
    track_artist: str,
    viral_tag: str = "#TrendingNow",
    platform: str = "instagram",
) -> Path:
    theme = THEME.get(platform, THEME["instagram"])
    accent = theme["accent"]
    accent2 = theme["accent2"]
    accent_rgb = _hex_to_rgb(accent)
    accent2_rgb = _hex_to_rgb(accent2)

    img = Image.open(image_path).convert("RGBA")
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    box = (56, 1290, 1024, 1560)
    draw.rounded_rectangle(box, radius=32, fill=(10, 15, 32, 240), outline=accent_rgb + (255,), width=4)
    tag = viral_tag if viral_tag.startswith("#") else f"#{viral_tag}"
    draw.rounded_rectangle((88, 1310, 400, 1370), radius=20, fill=accent2_rgb + (255,))
    draw.text((108, 1324), f"🔥 {tag}", fill=(15, 23, 42), font=_font(26, bold=True))
    draw.text((88, 1390), f"🎧 {playlist_name}", fill="#E2E8F0", font=_font(30, bold=True))
    draw.text((88, 1440), f"▶️ {track_title}", fill="#FFFFFF", font=_font(42, bold=True))
    draw.text((88, 1500), f"🎤 {track_artist}", fill="#94A3B8", font=_font(28))
    draw.text((720, 1505), "🎵", fill=accent, font=_font(36, bold=True))

    out = Image.alpha_composite(img, layer).convert("RGB")
    tmp = Path(tempfile.gettempdir()) / f"story-badge-{image_path.stem}.jpg"
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
    link_url: str = "",
    platform: str = "instagram",
) -> Path:
    if not image_path.exists():
        raise FileNotFoundError(f"Immagine story non trovata: {image_path}")
    if not audio_path.exists():
        raise FileNotFoundError(f"Traccia audio non trovata: {audio_path}")

    base = image_path
    link_tmp: Path | None = None
    if link_url:
        link_tmp = overlay_link_panel(base, link_url=link_url, platform=platform)
        base = link_tmp

    framed = overlay_music_badge(
        base,
        playlist_name=playlist_name,
        track_title=track_title,
        track_artist=track_artist,
        viral_tag=viral_tag,
        platform=platform,
    )
    if link_tmp:
        link_tmp.unlink(missing_ok=True)

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
    """Genera MP4 story con musica virale + QR verso articolo/sito."""
    stem = Path(image_file).stem
    img_dir = FB_STORY_IMG if platform == "facebook" else IG_STORY_IMG
    image_path = img_dir / f"{stem}.jpg"
    track = track_for_slot(slot, day_index, posts_per_day)
    audio_path = Path(track["path"])
    out_path = CACHE_DIR / platform / f"{stem}-{track['id']}.mp4"
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
        link_url=link_url or SITE_URL,
        platform=platform,
    )
    return video, track
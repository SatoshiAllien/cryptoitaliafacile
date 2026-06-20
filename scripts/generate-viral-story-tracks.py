#!/usr/bin/env python3
"""Genera tracce virali royalty-free per Stories (hook, phonk, reel energy)."""

from __future__ import annotations

import json
import math
import subprocess
import wave
from pathlib import Path

import numpy as np

try:
    import imageio_ffmpeg
except ImportError:
    imageio_ffmpeg = None  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
PLAYLIST_PATH = ROOT / "data" / "viral-story-playlist.json"
OUT_DIR = ROOT / "assets" / "audio" / "viral-stories"
SAMPLE_RATE = 44100
DURATION = 18.0


def ffmpeg_exe() -> str:
    if imageio_ffmpeg is None:
        raise SystemExit("Installa imageio-ffmpeg: pip install imageio-ffmpeg")
    return imageio_ffmpeg.get_ffmpeg_exe()


def _t() -> np.ndarray:
    return np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)


def _env(signal: np.ndarray, attack: float = 0.05, release: float = 0.8) -> np.ndarray:
    n = len(signal)
    env = np.ones(n)
    a = int(attack * SAMPLE_RATE)
    r = int(release * SAMPLE_RATE)
    if a > 0:
        env[:a] = np.linspace(0.0, 1.0, a)
    if r > 0:
        env[-r:] = np.linspace(1.0, 0.0, r)
    return signal * env


def _mix(*parts: np.ndarray, gain: float = 0.78) -> np.ndarray:
    sig = sum(parts)
    peak = np.max(np.abs(sig)) or 1.0
    return (sig / peak * gain).astype(np.float32)


def _kick(t: np.ndarray, bpm: float, amp: float = 0.22) -> np.ndarray:
    beat = 60.0 / bpm
    out = np.zeros_like(t)
    for hit in np.arange(0, DURATION, beat):
        mask = (t >= hit) & (t < hit + 0.08)
        env = np.exp(-80 * (t[mask] - hit))
        out[mask] = amp * np.sin(2 * math.pi * 55 * t[mask]) * env
    return out


def _sidechain(sig: np.ndarray, t: np.ndarray, bpm: float, depth: float = 0.45) -> np.ndarray:
    beat = 60.0 / bpm
    pump = 1.0 - depth * (np.sin(2 * math.pi * (1 / beat) * t) > 0.85)
    return sig * pump


def _hook_chords(t: np.ndarray, freqs: list[float], bpm: float, amp: float = 0.09) -> np.ndarray:
    bar = 4 * (60.0 / bpm)
    out = np.zeros_like(t)
    for i, f in enumerate(freqs * 4):
        start = (i % len(freqs)) * (bar / len(freqs))
        mask = (t % bar >= start) & (t % bar < start + bar / len(freqs))
        out[mask] += amp * np.sin(2 * math.pi * f * t[mask])
    return out


def track_fyp_energy(t: np.ndarray) -> np.ndarray:
    bpm = 128.0
    kick = _kick(t, bpm, 0.24)
    hook = _hook_chords(t, [220, 277.18, 329.63, 415.3], bpm)
    lead = 0.07 * np.sin(2 * math.pi * 880 * t) * (np.sin(2 * math.pi * 2 * (60 / bpm) * t) > 0)
    sig = _sidechain(_mix(kick, hook, lead), t, bpm)
    return _env(sig, 0.02, 0.6)


def track_scroll_stopper(t: np.ndarray) -> np.ndarray:
    bpm = 120.0
    hit = _kick(t, bpm, 0.26)
    stab = 0.12 * np.sin(2 * math.pi * 196 * t) * (np.sin(2 * math.pi * (60 / bpm) * t) > 0.92)
    riser = 0.05 * np.sin(2 * math.pi * (200 + 400 * (t / DURATION)) * t)
    return _env(_mix(hit, stab, riser), 0.01, 0.5)


def track_phonk_midnight(t: np.ndarray) -> np.ndarray:
    bpm = 110.0
    kick = _kick(t, bpm, 0.28)
    cowbell = 0.08 * np.sin(2 * math.pi * 800 * (t % 0.25)) * (t % 0.25 < 0.03)
    bass = 0.14 * np.sin(2 * math.pi * 49 * t)
    return _env(_sidechain(_mix(kick, cowbell, bass), t, bpm, 0.55), 0.02, 0.7)


def track_algo_boost(t: np.ndarray) -> np.ndarray:
    bpm = 125.0
    kick = _kick(t, bpm)
    synth = _hook_chords(t, [174.61, 220, 261.63, 349.23], bpm, 0.1)
    clap = 0.06 * np.sin(2 * math.pi * 1200 * (t % (60 / bpm))) * (t % (60 / bpm) > 0.5)
    return _env(_mix(kick, synth, clap), 0.02, 0.55)


def track_reel_hook(t: np.ndarray) -> np.ndarray:
    bpm = 130.0
    kick = _kick(t, bpm, 0.25)
    pluck = 0.1 * np.sin(2 * math.pi * 523.25 * (t % 0.5)) * (t % 0.5 < 0.12)
    sub = 0.12 * np.sin(2 * math.pi * 65.41 * t)
    return _env(_sidechain(_mix(kick, pluck, sub), t, bpm), 0.01, 0.5)


def track_crypto_hype(t: np.ndarray) -> np.ndarray:
    bpm = 118.0
    kick = _kick(t, bpm)
    arp = np.zeros_like(t)
    notes = [392, 440, 523.25, 587.33]
    step = 60 / bpm / 2
    for i, n in enumerate(notes * 6):
        m = (t >= i * step) & (t < (i + 1) * step)
        arp[m] = 0.09 * np.sin(2 * math.pi * n * t[m])
    return _env(_mix(kick, arp), 0.02, 0.6)


def track_bass_viral(t: np.ndarray) -> np.ndarray:
    bpm = 132.0
    kick = _kick(t, bpm, 0.3)
    bass = 0.16 * np.sin(2 * math.pi * 41.2 * t) * (1 + 0.3 * np.sin(2 * math.pi * 0.5 * t))
    hat = 0.04 * np.random.default_rng(7).standard_normal(len(t)) * (t % (60 / bpm / 2) < 0.01)
    return _env(_sidechain(_mix(kick, bass, hat), t, bpm, 0.5), 0.01, 0.45)


def track_story_fire(t: np.ndarray) -> np.ndarray:
    bpm = 122.0
    kick = _kick(t, bpm, 0.27)
    hook = _hook_chords(t, [246.94, 311.13, 369.99, 493.88], bpm, 0.11)
    return _env(_mix(kick, hook), 0.02, 0.55)


def track_trending_now(t: np.ndarray) -> np.ndarray:
    bpm = 126.0
    kick = _kick(t, bpm)
    vocal_chop = 0.07 * np.sin(2 * math.pi * 659.25 * t) * np.sin(2 * math.pi * 8 * t)
    pad = 0.06 * np.sin(2 * math.pi * 130.81 * t)
    return _env(_sidechain(_mix(kick, vocal_chop, pad), t, bpm), 0.02, 0.6)


def track_viral_loop(t: np.ndarray) -> np.ndarray:
    bpm = 115.0
    loop_len = 4 * (60 / bpm)
    phase = (t % loop_len) / loop_len
    kick = _kick(t, bpm, 0.24)
    melody = 0.1 * np.sin(2 * math.pi * 329.63 * t) * (phase < 0.5)
    return _env(_mix(kick, melody), 0.02, 0.65)


def track_hype_builder(t: np.ndarray) -> np.ndarray:
    bpm = 120.0
    kick = _kick(t, bpm, 0.24)
    rise = 0.08 * np.sin(2 * math.pi * (150 + 350 * (t / DURATION)) * t)
    drop = 0.14 * np.sin(2 * math.pi * 98 * t) * (t > DURATION * 0.55)
    build = kick * (0.85 + 0.15 * (t / DURATION))
    return _env(_mix(build, rise, drop), 0.02, 0.5)


def track_moment_heat(t: np.ndarray) -> np.ndarray:
    bpm = 134.0
    kick = _kick(t, bpm, 0.29)
    snap = 0.09 * np.sin(2 * math.pi * 700 * (t % (60 / bpm))) * (t % (60 / bpm) < 0.04)
    synth = _hook_chords(t, [207.65, 261.63, 311.13, 415.3], bpm, 0.08)
    return _env(_sidechain(_mix(kick, snap, synth), t, bpm), 0.01, 0.45)


def track_tiktok_dance(t: np.ndarray) -> np.ndarray:
    bpm = 124.0
    kick = _kick(t, bpm, 0.26)
    clap = 0.08 * np.sin(2 * math.pi * 900 * (t % (60 / bpm))) * (t % (60 / bpm) > 0.5)
    pop = 0.1 * np.sin(2 * math.pi * 440 * (t % 0.25)) * (t % 0.25 < 0.08)
    return _env(_sidechain(_mix(kick, clap, pop), t, bpm), 0.02, 0.55)


def track_jersey_club(t: np.ndarray) -> np.ndarray:
    bpm = 135.0
    beat = 60.0 / bpm
    kick = _kick(t, bpm, 0.3)
    bounce = 0.12 * np.sin(2 * math.pi * 73.42 * t) * (np.sin(2 * math.pi * 4 * t) > 0)
    bed = 0.06 * np.sin(2 * math.pi * 110 * (t % beat)) * (t % beat < 0.06)
    return _env(_sidechain(_mix(kick, bounce, bed), t, bpm, 0.6), 0.01, 0.45)


def track_drill_energy(t: np.ndarray) -> np.ndarray:
    bpm = 140.0
    kick = _kick(t, bpm, 0.32)
    slide = 0.14 * np.sin(2 * math.pi * (55 + 30 * np.sin(2 * math.pi * 0.25 * t)) * t)
    hat = 0.05 * np.random.default_rng(42).standard_normal(len(t)) * (t % (60 / bpm / 4) < 0.008)
    return _env(_mix(kick, slide, hat), 0.01, 0.4)


def track_afro_viral(t: np.ndarray) -> np.ndarray:
    bpm = 108.0
    kick = _kick(t, bpm, 0.25)
    shaker = 0.05 * np.sin(2 * math.pi * 3000 * (t % 0.125)) * (t % 0.125 < 0.02)
    melody = _hook_chords(t, [196, 246.94, 293.66, 349.23], bpm, 0.09)
    return _env(_mix(kick, shaker, melody), 0.03, 0.65)


def track_miami_bass(t: np.ndarray) -> np.ndarray:
    bpm = 128.0
    kick = _kick(t, bpm, 0.34)
    bass = 0.18 * np.sin(2 * math.pi * 36.71 * t) * (1 + 0.5 * np.sin(2 * math.pi * 2 * t))
    squeal = 0.06 * np.sin(2 * math.pi * 1200 * (t % 0.5)) * (t % 0.5 < 0.05)
    return _env(_sidechain(_mix(kick, bass, squeal), t, bpm, 0.55), 0.01, 0.4)


def track_funk_brasil(t: np.ndarray) -> np.ndarray:
    bpm = 130.0
    kick = _kick(t, bpm, 0.28)
    cuica = 0.07 * np.sin(2 * math.pi * (400 + 600 * (t % 0.2) / 0.2) * t) * (t % 0.2 < 0.15)
    bass = 0.13 * np.sin(2 * math.pi * 49 * t) * (np.sin(2 * math.pi * 2 * (60 / bpm) * t) > 0)
    return _env(_mix(kick, cuica, bass), 0.02, 0.5)


def track_remix_drop(t: np.ndarray) -> np.ndarray:
    bpm = 128.0
    kick = _kick(t, bpm, 0.27)
    build = 0.06 * np.sin(2 * math.pi * (180 + 500 * (t / DURATION)) * t)
    drop = 0.15 * np.sin(2 * math.pi * 87.31 * t) * (t > DURATION * 0.6)
    stab = 0.1 * np.sin(2 * math.pi * 523.25 * t) * (t > DURATION * 0.6) * (t % (60 / bpm) < 0.1)
    return _env(_mix(kick, build, drop, stab), 0.02, 0.5)


def track_nightcore_boost(t: np.ndarray) -> np.ndarray:
    bpm = 148.0
    kick = _kick(t, bpm, 0.24)
    lead = 0.09 * np.sin(2 * math.pi * 659.25 * t) * (np.sin(2 * math.pi * 4 * (60 / bpm) * t) > 0)
    arp = np.zeros_like(t)
    notes = [523.25, 659.25, 783.99, 987.77]
    step = 60 / bpm / 4
    for i, n in enumerate(notes * 8):
        m = (t >= i * step) & (t < (i + 1) * step)
        arp[m] = 0.07 * np.sin(2 * math.pi * n * t[m])
    return _env(_sidechain(_mix(kick, lead, arp), t, bpm), 0.01, 0.45)


GENERATORS = {
    "fyp-energy": track_fyp_energy,
    "scroll-stopper": track_scroll_stopper,
    "phonk-midnight": track_phonk_midnight,
    "algo-boost": track_algo_boost,
    "reel-hook": track_reel_hook,
    "crypto-hype": track_crypto_hype,
    "bass-viral": track_bass_viral,
    "story-fire": track_story_fire,
    "trending-now": track_trending_now,
    "viral-loop": track_viral_loop,
    "hype-builder": track_hype_builder,
    "moment-heat": track_moment_heat,
    "tiktok-dance": track_tiktok_dance,
    "jersey-club": track_jersey_club,
    "drill-energy": track_drill_energy,
    "afro-viral": track_afro_viral,
    "miami-bass": track_miami_bass,
    "funk-brasil": track_funk_brasil,
    "remix-drop": track_remix_drop,
    "nightcore-boost": track_nightcore_boost,
}


def write_wav(path: Path, signal: np.ndarray) -> None:
    pcm = np.int16(np.clip(signal, -1.0, 1.0) * 32767)
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(pcm.tobytes())


def wav_to_mp3(wav_path: Path, mp3_path: Path) -> None:
    subprocess.run(
        [ffmpeg_exe(), "-y", "-i", str(wav_path), "-codec:a", "libmp3lame", "-b:a", "192k", str(mp3_path)],
        check=True,
        capture_output=True,
    )
    wav_path.unlink(missing_ok=True)


def main() -> None:
    playlist = json.loads(PLAYLIST_PATH.read_text(encoding="utf-8"))
    t = _t()
    for track in playlist["tracks"]:
        gen = GENERATORS.get(track["id"])
        if not gen:
            print("SKIP", track["id"])
            continue
        wav_path = OUT_DIR / track["file"].replace(".mp3", ".wav")
        mp3_path = OUT_DIR / track["file"]
        write_wav(wav_path, gen(t))
        wav_to_mp3(wav_path, mp3_path)
        print("OK", mp3_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
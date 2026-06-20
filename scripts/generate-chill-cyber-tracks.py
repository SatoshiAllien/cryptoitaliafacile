#!/usr/bin/env python3
"""Genera tracce originali royalty-free per la playlist Chill Cyber Coding."""

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
PLAYLIST_PATH = ROOT / "data" / "chill-cyber-playlist.json"
OUT_DIR = ROOT / "assets" / "audio" / "chill-cyber-coding"
SAMPLE_RATE = 44100
DURATION = 18.0


def ffmpeg_exe() -> str:
    if imageio_ffmpeg is None:
        raise SystemExit("Installa imageio-ffmpeg: pip install imageio-ffmpeg")
    return imageio_ffmpeg.get_ffmpeg_exe()


def _env(signal: np.ndarray, attack: float = 0.4, release: float = 1.2) -> np.ndarray:
    n = len(signal)
    env = np.ones(n)
    a = int(attack * SAMPLE_RATE)
    r = int(release * SAMPLE_RATE)
    if a > 0:
        env[:a] = np.linspace(0.0, 1.0, a)
    if r > 0:
        env[-r:] = np.linspace(1.0, 0.0, r)
    return signal * env


def _lowpass(signal: np.ndarray, cutoff: float = 2200.0) -> np.ndarray:
    dt = 1.0 / SAMPLE_RATE
    rc = 1.0 / (2 * math.pi * cutoff)
    alpha = dt / (rc + dt)
    out = np.zeros_like(signal)
    prev = 0.0
    for i, x in enumerate(signal):
        prev = prev + alpha * (x - prev)
        out[i] = prev
    return out


def _mix(*parts: np.ndarray) -> np.ndarray:
    sig = sum(parts)
    peak = np.max(np.abs(sig)) or 1.0
    return (sig / peak * 0.82).astype(np.float32)


def _t() -> np.ndarray:
    return np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)


def track_neon_compiler(t: np.ndarray) -> np.ndarray:
    pad = 0.14 * np.sin(2 * math.pi * 110 * t)
    pad += 0.1 * np.sin(2 * math.pi * 164.81 * t)
    pad += 0.08 * np.sin(2 * math.pi * 220 * t)
    arp = 0.05 * np.sin(2 * math.pi * 440 * (t % 0.72))
    noise = 0.012 * np.random.default_rng(1).standard_normal(len(t))
    return _env(_lowpass(_mix(pad, arp, noise)))


def track_midnight_hash(t: np.ndarray) -> np.ndarray:
    bass = 0.16 * np.sin(2 * math.pi * 55 * t) * (0.6 + 0.4 * np.sin(2 * math.pi * 0.25 * t))
    pad = 0.09 * np.sin(2 * math.pi * 130.81 * t)
    hat = 0.03 * np.sin(2 * math.pi * 8000 * (t % 0.5)) * (t % 0.5 < 0.02)
    return _env(_lowpass(_mix(bass, pad, hat), 1800))


def track_synth_stack(t: np.ndarray) -> np.ndarray:
    notes = [220, 261.63, 329.63, 392]
    arp = np.zeros_like(t)
    step = 0.45
    for i, f in enumerate(notes * 3):
        mask = (t >= i * step) & (t < (i + 1) * step)
        arp[mask] = 0.11 * np.sin(2 * math.pi * f * t[mask])
    pad = 0.07 * np.sin(2 * math.pi * 98 * t)
    return _env(_lowpass(_mix(arp, pad), 2400))


def track_lofi_ledger(t: np.ndarray) -> np.ndarray:
    pad = 0.12 * np.sin(2 * math.pi * 87.31 * t)
    pad += 0.08 * np.sin(2 * math.pi * 103.83 * t)
    wobble = 1 + 0.015 * np.sin(2 * math.pi * 0.18 * t)
    crackle = 0.01 * np.random.default_rng(2).standard_normal(len(t))
    return _env(_lowpass(_mix(pad * wobble, crackle), 1600))


def track_cyber_chill_room(t: np.ndarray) -> np.ndarray:
    room = 0.1 * np.sin(2 * math.pi * 73.42 * t)
    room += 0.08 * np.sin(2 * math.pi * 146.83 * t)
    shimmer = 0.04 * np.sin(2 * math.pi * 587 * t) * np.sin(2 * math.pi * 0.08 * t)
    return _env(_lowpass(_mix(room, shimmer), 2000))


def track_block_by_block(t: np.ndarray) -> np.ndarray:
    pulse = 0.13 * np.sin(2 * math.pi * 65.41 * t) * (0.5 + 0.5 * np.sin(2 * math.pi * 1.1 * t))
    lead = 0.06 * np.sin(2 * math.pi * 196 * t) * (0.5 + 0.5 * np.sin(2 * math.pi * 0.35 * t))
    return _env(_lowpass(_mix(pulse, lead), 1900))


def track_terminal_dreams(t: np.ndarray) -> np.ndarray:
    dream = 0.11 * np.sin(2 * math.pi * 123.47 * t)
    dream += 0.07 * np.sin(2 * math.pi * 185.22 * t)
    delay = 0.05 * np.sin(2 * math.pi * 246.94 * (t - 0.18))
    return _env(_lowpass(_mix(dream, delay), 2100))


def track_node_runner(t: np.ndarray) -> np.ndarray:
    bpm = 92 / 60
    kick = 0.14 * np.sin(2 * math.pi * 60 * t) * (np.sin(2 * math.pi * bpm * t) > 0.92)
    synth = 0.08 * np.sin(2 * math.pi * 174.61 * t)
    arp = 0.05 * np.sin(2 * math.pi * 349.23 * (t % 0.35))
    return _env(_lowpass(_mix(kick, synth, arp), 2300))


GENERATORS = {
    "neon-compiler": track_neon_compiler,
    "midnight-hash": track_midnight_hash,
    "synth-stack": track_synth_stack,
    "lofi-ledger": track_lofi_ledger,
    "cyber-chill-room": track_cyber_chill_room,
    "block-by-block": track_block_by_block,
    "terminal-dreams": track_terminal_dreams,
    "node-runner": track_node_runner,
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
        [
            ffmpeg_exe(), "-y", "-i", str(wav_path),
            "-codec:a", "libmp3lame", "-b:a", "160k", str(mp3_path),
        ],
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
        signal = gen(t)
        write_wav(wav_path, signal)
        wav_to_mp3(wav_path, mp3_path)
        print("OK", mp3_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
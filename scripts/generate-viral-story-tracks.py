#!/usr/bin/env python3
"""Genera tracce pop/EDM virali royalty-free per Stories."""

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


def _arp(t: np.ndarray, notes: list[float], bpm: float, step_div: float = 2.0, amp: float = 0.08) -> np.ndarray:
    out = np.zeros_like(t)
    step = 60 / bpm / step_div
    for i, n in enumerate(notes * 12):
        m = (t >= i * step) & (t < (i + 1) * step)
        out[m] = amp * np.sin(2 * math.pi * n * t[m])
    return out


def _saw_lead(t: np.ndarray, freq: float, amp: float = 0.06) -> np.ndarray:
    return amp * (2 * (t * freq % 1.0) - 1.0)


def track_mainstage_drop(t: np.ndarray) -> np.ndarray:
    bpm = 128.0
    kick = _kick(t, bpm, 0.28)
    hook = _hook_chords(t, [220, 277.18, 329.63, 440], bpm, 0.1)
    lead = 0.08 * np.sin(2 * math.pi * 880 * t) * (t > DURATION * 0.5)
    return _env(_sidechain(_mix(kick, hook, lead), t, bpm), 0.02, 0.55)


def track_festival_pop(t: np.ndarray) -> np.ndarray:
    bpm = 126.0
    kick = _kick(t, bpm, 0.26)
    chorus = _hook_chords(t, [261.63, 329.63, 392, 523.25], bpm, 0.11)
    clap = 0.07 * np.sin(2 * math.pi * 1000 * (t % (60 / bpm))) * (t % (60 / bpm) > 0.48)
    return _env(_sidechain(_mix(kick, chorus, clap), t, bpm), 0.02, 0.55)


def track_future_bass_glow(t: np.ndarray) -> np.ndarray:
    bpm = 140.0
    kick = _kick(t, bpm, 0.24)
    wobble = 0.1 * np.sin(2 * math.pi * (180 + 120 * np.sin(2 * math.pi * 2 * t)) * t)
    pad = 0.06 * np.sin(2 * math.pi * 523.25 * t)
    return _env(_sidechain(_mix(kick, wobble, pad), t, bpm, 0.5), 0.02, 0.5)


def track_house_pop_banger(t: np.ndarray) -> np.ndarray:
    bpm = 124.0
    kick = _kick(t, bpm, 0.27)
    bass = 0.12 * np.sin(2 * math.pi * 55 * t)
    stab = 0.09 * np.sin(2 * math.pi * 440 * (t % 0.5)) * (t % 0.5 < 0.1)
    return _env(_sidechain(_mix(kick, bass, stab), t, bpm), 0.02, 0.55)


def track_summer_vibes_pop(t: np.ndarray) -> np.ndarray:
    bpm = 118.0
    kick = _kick(t, bpm, 0.22)
    guitar = 0.09 * np.sin(2 * math.pi * 329.63 * (t % 0.5)) * (t % 0.5 < 0.2)
    bright = 0.07 * np.sin(2 * math.pi * 659.25 * t) * (np.sin(2 * math.pi * 1 * t) > 0)
    return _env(_mix(kick, guitar, bright), 0.03, 0.65)


def track_game_time_energy(t: np.ndarray) -> np.ndarray:
    bpm = 132.0
    kick = _kick(t, bpm, 0.3)
    rise = 0.07 * np.sin(2 * math.pi * (200 + 600 * (t / DURATION)) * t)
    drop = 0.15 * np.sin(2 * math.pi * 73.42 * t) * (t > DURATION * 0.58)
    return _env(_mix(kick, rise, drop), 0.01, 0.45)


def track_sax_pop_fusion(t: np.ndarray) -> np.ndarray:
    bpm = 122.0
    kick = _kick(t, bpm, 0.25)
    sax = 0.1 * np.sin(2 * math.pi * (350 + 200 * np.sin(2 * math.pi * 0.5 * t)) * t)
    bass = 0.11 * np.sin(2 * math.pi * 49 * t)
    return _env(_sidechain(_mix(kick, sax, bass), t, bpm), 0.02, 0.55)


def track_melodic_edm_rise(t: np.ndarray) -> np.ndarray:
    bpm = 128.0
    kick = _kick(t, bpm, 0.24)
    build = 0.08 * np.sin(2 * math.pi * (150 + 400 * (t / DURATION)) * t)
    melody = _hook_chords(t, [196, 246.94, 293.66, 369.99], bpm, 0.08)
    return _env(_mix(kick, build, melody), 0.02, 0.55)


def track_synth_pop_viral(t: np.ndarray) -> np.ndarray:
    bpm = 120.0
    kick = _kick(t, bpm, 0.24)
    synth = _hook_chords(t, [261.63, 329.63, 392, 493.88], bpm, 0.1)
    lead = 0.07 * np.sin(2 * math.pi * 784 * t) * (np.sin(2 * math.pi * 2 * (60 / bpm) * t) > 0)
    return _env(_sidechain(_mix(kick, synth, lead), t, bpm), 0.02, 0.6)


def track_drop_zone_128(t: np.ndarray) -> np.ndarray:
    bpm = 128.0
    kick = _kick(t, bpm, 0.29)
    sub = 0.14 * np.sin(2 * math.pi * 65.41 * t) * (t > DURATION * 0.55)
    stab = 0.1 * np.sin(2 * math.pi * 523.25 * t) * (t > DURATION * 0.55) * (t % (60 / bpm) < 0.08)
    return _env(_mix(kick, sub, stab), 0.01, 0.45)


def track_eurodance_revival(t: np.ndarray) -> np.ndarray:
    bpm = 130.0
    kick = _kick(t, bpm, 0.26)
    lead = _arp(t, [392, 440, 523.25, 587.33], bpm, 2.0, 0.09)
    bass = 0.1 * np.sin(2 * math.pi * 49 * t)
    return _env(_sidechain(_mix(kick, lead, bass), t, bpm), 0.02, 0.55)


def track_tropical_pop_house(t: np.ndarray) -> np.ndarray:
    bpm = 110.0
    kick = _kick(t, bpm, 0.23)
    marimba = 0.09 * np.sin(2 * math.pi * 523.25 * (t % 0.25)) * (t % 0.25 < 0.08)
    pad = 0.06 * np.sin(2 * math.pi * 196 * t)
    return _env(_mix(kick, marimba, pad), 0.03, 0.65)


def track_electro_pop_rush(t: np.ndarray) -> np.ndarray:
    bpm = 128.0
    kick = _kick(t, bpm, 0.27)
    electro = _saw_lead(t, 220, 0.05) * (np.sin(2 * math.pi * 4 * (60 / bpm) * t) > 0)
    pop = 0.08 * np.sin(2 * math.pi * 440 * (t % 0.5)) * (t % 0.5 < 0.12)
    return _env(_sidechain(_mix(kick, electro, pop), t, bpm), 0.02, 0.5)


def track_club_pop_anthem(t: np.ndarray) -> np.ndarray:
    bpm = 125.0
    kick = _kick(t, bpm, 0.28)
    hook = _hook_chords(t, [246.94, 311.13, 369.99, 466.16], bpm, 0.11)
    hat = 0.04 * np.random.default_rng(3).standard_normal(len(t)) * (t % (60 / bpm / 2) < 0.01)
    return _env(_mix(kick, hook, hat), 0.02, 0.55)


def track_progressive_pop_drop(t: np.ndarray) -> np.ndarray:
    bpm = 128.0
    kick = _kick(t, bpm, 0.25)
    prog = 0.07 * np.sin(2 * math.pi * (130 + 350 * (t / DURATION)) * t)
    drop = 0.13 * np.sin(2 * math.pi * 87.31 * t) * (t > DURATION * 0.62)
    return _env(_mix(kick, prog, drop), 0.02, 0.5)


def track_dance_pop_fyp(t: np.ndarray) -> np.ndarray:
    bpm = 124.0
    kick = _kick(t, bpm, 0.26)
    pop = 0.1 * np.sin(2 * math.pi * 523.25 * (t % 0.25)) * (t % 0.25 < 0.1)
    clap = 0.07 * np.sin(2 * math.pi * 900 * (t % (60 / bpm))) * (t % (60 / bpm) > 0.5)
    return _env(_sidechain(_mix(kick, pop, clap), t, bpm), 0.02, 0.55)


def track_big_room_energy(t: np.ndarray) -> np.ndarray:
    bpm = 128.0
    kick = _kick(t, bpm, 0.32)
    slam = 0.12 * np.sin(2 * math.pi * 55 * t) * (t > DURATION * 0.5)
    riser = 0.06 * np.sin(2 * math.pi * (300 + 500 * (t / DURATION)) * t) * (t < DURATION * 0.5)
    return _env(_mix(kick, slam, riser), 0.01, 0.42)


def track_pop_hook_drop(t: np.ndarray) -> np.ndarray:
    bpm = 126.0
    kick = _kick(t, bpm, 0.26)
    hook = 0.11 * np.sin(2 * math.pi * 440 * t) * (np.sin(2 * math.pi * 2 * (60 / bpm) * t) > 0)
    bass = 0.1 * np.sin(2 * math.pi * 55 * t)
    return _env(_sidechain(_mix(kick, hook, bass), t, bpm), 0.02, 0.55)


def track_life_feels_good(t: np.ndarray) -> np.ndarray:
    bpm = 116.0
    kick = _kick(t, bpm, 0.22)
    uplift = _hook_chords(t, [196, 246.94, 293.66, 349.23], bpm, 0.09)
    sparkle = 0.06 * np.sin(2 * math.pi * 783.99 * t) * (np.sin(2 * math.pi * 0.5 * t) > 0)
    return _env(_mix(kick, uplift, sparkle), 0.03, 0.65)


def track_sun_on_me_pop(t: np.ndarray) -> np.ndarray:
    bpm = 105.0
    kick = _kick(t, bpm, 0.2)
    dreamy = 0.08 * np.sin(2 * math.pi * 329.63 * t) * (1 + 0.2 * np.sin(2 * math.pi * 0.25 * t))
    pad = 0.06 * np.sin(2 * math.pi * 130.81 * t)
    return _env(_mix(kick, dreamy, pad), 0.04, 0.7)


GENERATORS = {
    "mainstage-drop": track_mainstage_drop,
    "festival-pop": track_festival_pop,
    "future-bass-glow": track_future_bass_glow,
    "house-pop-banger": track_house_pop_banger,
    "summer-vibes-pop": track_summer_vibes_pop,
    "game-time-energy": track_game_time_energy,
    "sax-pop-fusion": track_sax_pop_fusion,
    "melodic-edm-rise": track_melodic_edm_rise,
    "synth-pop-viral": track_synth_pop_viral,
    "drop-zone-128": track_drop_zone_128,
    "eurodance-revival": track_eurodance_revival,
    "tropical-pop-house": track_tropical_pop_house,
    "electro-pop-rush": track_electro_pop_rush,
    "club-pop-anthem": track_club_pop_anthem,
    "progressive-pop-drop": track_progressive_pop_drop,
    "dance-pop-fyp": track_dance_pop_fyp,
    "big-room-energy": track_big_room_energy,
    "pop-hook-drop": track_pop_hook_drop,
    "life-feels-good": track_life_feels_good,
    "sun-on-me-pop": track_sun_on_me_pop,
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
#!/usr/bin/env python3
"""
update-bitcoin-rainbow-chart.py
================================
Fetches live Bitcoin Rainbow Chart data from BlockchainCenter,
computes Original + Dynamic (Power Law) band models, and regenerates:

  - assets/rainbow-chart.png
  - data/bitcoin-rainbow-chart.json
  - sections/bitcoin-rainbow-chart.md

Re-run this script whenever the agent (or a cron job) should refresh
the homepage chart. No financial advice: educational visualization only.

Source: https://www.blockchaincenter.net/bitcoin-rainbow-chart/
"""

from __future__ import annotations

import json
import math
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = ROOT / "assets"
DATA_DIR = ROOT / "data"
SECTIONS_DIR = ROOT / "sections"
PNG_PATH = ASSETS_DIR / "rainbow-chart.png"
JSON_PATH = DATA_DIR / "bitcoin-rainbow-chart.json"
MD_PATH = SECTIONS_DIR / "bitcoin-rainbow-chart.md"

CHART_API = "https://www.blockchaincenter.net/api/coin/chartdata/?crypto=BTC"
RATES_API = "https://www.blockchaincenter.net/api/coin/rates/?crypto=BTC"
SOURCE_URL = "https://www.blockchaincenter.net/bitcoin-rainbow-chart/"
GENESIS = datetime(2009, 1, 3)  # Bitcoin genesis (days base for power law)
CHART_START = datetime(2012, 1, 1)
CHART_END = datetime(2032, 12, 31)
USER_AGENT = "CryptoItaliaFacile-RainbowAgent/1.0 (+https://github.com/SatoshiAllien/cryptoitaliafacile)"

# Classic BlockchainCenter rainbow legend (top → bottom).
# Colors and labels reverse-engineered from their live JS bundle.
BANDS_TOP_TO_BOTTOM: list[dict[str, Any]] = [
    {"id": 0, "label": "Maximum Bubble Territory", "color": "#c00000"},
    {"id": 1, "label": "Sell. Seriously, SELL!", "color": "#d64018"},
    {"id": 2, "label": "FOMO intensifies", "color": "#ed7d31"},
    {"id": 3, "label": "Is this a bubble?", "color": "#f6b45a"},
    {"id": 4, "label": "HODL!", "color": "#ffeb84"},
    {"id": 5, "label": "Still cheap", "color": "#b1d580"},
    {"id": 6, "label": "Accumulate", "color": "#63be7b"},
    {"id": 7, "label": "BUY!", "color": "#54989f"},
    {"id": 8, "label": "Basically a Fire Sale", "color": "#4472c4"},
    {"id": 9, "label": "Bitcoin is dead", "color": "#9568db"},
]

# Original logarithmic regression band coefficients (natural log).
# price_bound = 10 ** (coeff * ln(n + offset) - 19.463)
# n = days since 2012-01-01 (0-based index used by BlockchainCenter).
ORIGINAL_BAND_COEFFS = [
    (2.9000, 1400),  # Maximum Bubble Territory (upper edge)
    (2.8860, 1375),  # Sell
    (2.8720, 1350),  # FOMO
    (2.8590, 1320),  # Bubble?
    (2.8450, 1293),  # HODL!
    (2.8295, 1275),  # Still cheap
    (2.8150, 1250),  # Accumulate
    (2.8010, 1225),  # BUY!
    (2.7880, 1200),  # Fire Sale
    (2.7750, 1175),  # Bitcoin is dead
]


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------
def http_get_json(url: str) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def days_between(a: datetime, b: datetime) -> int:
    return int(round((a - b).total_seconds() / 86400.0))


def parse_day(s: str) -> datetime:
    return datetime.strptime(s[:10], "%Y-%m-%d")


# ---------------------------------------------------------------------------
# Data fetch
# ---------------------------------------------------------------------------
def fetch_live_data() -> tuple[list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    """Return (daily_prices_usd, rates, feed_meta) from BlockchainCenter.

    The chartdata feed often tracks EUR levels while the public chart is labeled
    in USD. We detect that (last close ≈ price_eur) and convert to USD with the
    live FX implied by rates so bands stay comparable to the classic model.
    """
    chart = http_get_json(CHART_API)
    rates = http_get_json(RATES_API)
    if not isinstance(chart, list) or not chart:
        raise RuntimeError("chartdata API returned empty/invalid payload")
    if not isinstance(rates, dict) or "price_usd" not in rates:
        raise RuntimeError("rates API returned invalid payload")

    raw: list[dict[str, Any]] = []
    for row in chart:
        try:
            price = float(row["price"])
            if price <= 0:
                continue
            raw.append({"time": row["time"][:10], "price": price})
        except (KeyError, TypeError, ValueError):
            continue
    if not raw:
        raise RuntimeError("No valid price points in chartdata")

    last = float(raw[-1]["price"])
    price_usd = float(rates["price_usd"])
    price_eur = float(rates.get("price_eur") or 0)
    fx = 1.0
    unit = "usd"
    # If last chart close is within 2% of EUR quote, treat series as EUR → USD
    if price_eur > 0 and abs(last - price_eur) / price_eur < 0.02:
        fx = price_usd / price_eur
        unit = "eur_converted_to_usd"
    elif price_usd > 0 and abs(last - price_usd) / price_usd < 0.02:
        unit = "usd"
        fx = 1.0
    else:
        # Prefer aligning the last point to live USD scale
        fx = price_usd / last if last else 1.0
        unit = "scaled_to_live_usd"

    series = [{"time": r["time"], "price": round(float(r["price"]) * fx, 4)} for r in raw]
    # Pin latest close to the live USD tick for band position
    series[-1] = {"time": series[-1]["time"], "price": price_usd}

    meta = {
        "feed_unit_detected": unit,
        "fx_used": round(fx, 6),
        "raw_last_close": last,
        "points": len(series),
    }
    return series, rates, meta


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------
@dataclass
class OriginalModel:
    """Static rainbow bands (original logarithmic regression)."""

    day_index: int
    bounds_usd: list[float]  # 10 upper edges top→bottom
    band_index: int
    band: dict[str, str]


def original_band_price(day_index: int, coeff: float, offset: int) -> float:
    return 10 ** (coeff * math.log(day_index + offset) - 19.463)


def compute_original_model(price: float, as_of: datetime) -> OriginalModel:
    day_index = max(0, days_between(as_of, CHART_START))
    bounds = [original_band_price(day_index, c, o) for c, o in ORIGINAL_BAND_COEFFS]
    # Band i if lower_bound <= price < upper_bound (upper = bounds[i], lower = bounds[i+1] or 0)
    band_index = len(bounds) - 1
    for i in range(len(bounds) - 1):
        upper = bounds[i]
        lower = bounds[i + 1]
        if price >= lower:
            band_index = i
            break
    if price >= bounds[0]:
        band_index = 0
    return OriginalModel(
        day_index=day_index,
        bounds_usd=bounds,
        band_index=band_index,
        band=BANDS_TOP_TO_BOTTOM[band_index],
    )


@dataclass
class DynamicModel:
    """Dynamic Power Law fit on 180-day local bottoms (BlockchainCenter method)."""

    slope: float
    intercept: float
    r2: float
    formula: str
    fit_price: float  # k(days) at as_of
    band_edges: list[float]  # C[0]..C[9] at as_of: t * 1.3^(8-e)
    band_index: int
    band: dict[str, str]
    deviation_pct: float  # vs HODL-ish center (1.3^3.5 * k)
    bottoms_used: int
    tops_used: int


def find_cycle_extremes(series: list[dict[str, Any]], window: int = 180) -> tuple[list[dict], list[dict]]:
    """Local tops/bottoms within ±window days (same idea as BlockchainCenter)."""
    prices = [float(p["price"]) for p in series]
    tops: list[dict] = []
    bottoms: list[dict] = []
    n = len(prices)
    for i, row in enumerate(series):
        lo = max(0, i - window)
        hi = min(n - 1, i + window)
        p = prices[i]
        is_top = all(prices[j] <= p for j in range(lo, hi + 1) if j != i)
        is_bot = all(prices[j] >= p for j in range(lo, hi + 1) if j != i)
        if is_top:
            tops.append(row)
        if is_bot:
            bottoms.append(row)
    return tops, bottoms


def compute_dynamic_model(series: list[dict[str, Any]], price: float, as_of: datetime) -> DynamicModel:
    _, bottoms = find_cycle_extremes(series, window=180)
    xs: list[float] = []
    ys: list[float] = []
    for row in bottoms:
        d = days_between(parse_day(row["time"]), GENESIS)
        if d > 0 and row["price"] > 0:
            xs.append(math.log10(d))
            ys.append(math.log10(float(row["price"])))

    if len(xs) < 2:
        # Fallback: fit all daily points since 2012
        for row in series:
            t = parse_day(row["time"])
            if t < CHART_START:
                continue
            d = days_between(t, GENESIS)
            if d > 0 and row["price"] > 0:
                xs.append(math.log10(d))
                ys.append(math.log10(float(row["price"])))

    n = len(xs)
    sx = sum(xs)
    sy = sum(ys)
    sxy = sum(x * y for x, y in zip(xs, ys))
    sxx = sum(x * x for x in xs)
    den = n * sxx - sx * sx
    slope = 0.0 if den == 0 else (n * sxy - sx * sy) / den
    intercept = (sy - slope * sx) / n if n else 0.0

    mean_y = sy / n if n else 0.0
    ss_tot = sum((y - mean_y) ** 2 for y in ys)
    ss_res = sum((y - (slope * x + intercept)) ** 2 for x, y in zip(xs, ys))
    r2 = 1.0 if ss_tot == 0 else 1.0 - ss_res / ss_tot

    formula = f"Price = 10^({slope:.4f} * log10(days) + {intercept:.4f})"

    def k(days: float) -> float:
        if days <= 0:
            return float("nan")
        return 10 ** (slope * math.log10(days) + intercept)

    days_now = max(1, days_between(as_of, GENESIS))
    fit = k(days_now)
    # C[e] = fit * 1.3^(8-e) for e in 0..9  (BlockchainCenter dynamic bands)
    edges = [fit * (1.3 ** (8 - e)) for e in range(10)]

    # Band index: price > C[r] → r-1 for r=1..8 else 8  (maps to labels 0..8)
    band_index = 8
    for r in range(1, 9):
        if price > edges[r]:
            band_index = r - 1
            break

    center = (1.3 ** 3.5) * fit  # ≈ 2.504965... * k
    deviation_pct = ((price - center) / center * 100.0) if center else 0.0

    tops, bottoms_all = find_cycle_extremes(series, window=180)

    return DynamicModel(
        slope=slope,
        intercept=intercept,
        r2=r2,
        formula=formula,
        fit_price=fit,
        band_edges=edges,
        band_index=band_index,
        band=BANDS_TOP_TO_BOTTOM[band_index],
        deviation_pct=deviation_pct,
        bottoms_used=len(bottoms_all),
        tops_used=len(tops),
    )


def interpretation_en(band: dict[str, Any], model: str) -> str:
    """Non-advisory trend reading of the current band (English)."""
    key = band["label"]
    texts = {
        "Maximum Bubble Territory": (
            "The highest band of the historical model. In past cycles it often aligned with extreme "
            "euphoria and cycle tops. This is relative valuation context, not a price forecast."
        ),
        "Sell. Seriously, SELL!": (
            "A zone historically linked to late-stage euphoria. The meme chart invites caution; "
            "it remains a descriptive model, not a trading signal."
        ),
        "FOMO intensifies": (
            "A band where past cycles often saw heavy retail inflows (FOMO). Useful as a sentiment "
            "thermometer, not as precise market timing."
        ),
        "Is this a bubble?": (
            "Upper-mid area: price sits above the model’s long-term trend. Markets have debated "
            "“bubble” narratives here without implying a certain outcome."
        ),
        "HODL!": (
            "Near the center of the model’s long-term trend. Often read as roughly “fair” relative "
            "to history — not a recommendation to hold or sell."
        ),
        "Still cheap": (
            "Below the log-trend center. In past cycles this was often consolidation or gradual "
            "recovery territory; it does not mean price is absolutely “cheap.”"
        ),
        "Accumulate": (
            "Lower-mid rainbow band. Historically associated with long-horizon accumulation stories, "
            "with the usual caveat that past performance is not predictive."
        ),
        "BUY!": (
            "A lower zone of the original/dynamic model. Past cycles sometimes saw strong relative "
            "undervaluation vs the trend here — not an invitation to buy."
        ),
        "Basically a Fire Sale": (
            "Among the lowest bands: historically linked to panic or late bear-market phases. "
            "The label is a meme; it is not financial advice."
        ),
        "Bitcoin is dead": (
            "Purple band added in later chart versions when price fell below the classic rainbow. "
            "It marks an extreme downside gap vs the original model."
        ),
    }
    base = texts.get(key, "Position within the long-term rainbow valuation model.")
    return f"[{model}] {base}"


# ---------------------------------------------------------------------------
# Chart rendering (Pillow, log-scale)
# ---------------------------------------------------------------------------
def _font(size: int) -> ImageFont.ImageFont:
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _font_bold(size: int) -> ImageFont.ImageFont:
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return _font(size)


def render_chart_png(
    series: list[dict[str, Any]],
    dynamic: DynamicModel,
    original: OriginalModel,
    live_price: float,
    as_of: datetime,
    out_path: Path,
) -> None:
    """Draw a log-scale rainbow chart PNG with dynamic power-law bands."""
    W, H = 1400, 820
    left, right, top, bottom = 80, 220, 70, 70
    plot_w = W - left - right
    plot_h = H - top - bottom

    # Sample weekly for drawing performance
    pts = [p for p in series if parse_day(p["time"]) >= CHART_START]
    if len(pts) > 900:
        step = max(1, len(pts) // 900)
        pts = pts[::step] + ([pts[-1]] if pts[-1] not in pts[::step] else [])

    t0 = CHART_START.timestamp()
    t1 = CHART_END.timestamp()
    y_min, y_max = 1.0, 2_000_000.0  # log domain

    def x_of(ts: float) -> float:
        return left + (ts - t0) / (t1 - t0) * plot_w

    def y_of(price: float) -> float:
        p = max(y_min, min(y_max, price))
        return top + (math.log10(y_max) - math.log10(p)) / (math.log10(y_max) - math.log10(y_min)) * plot_h

    img = Image.new("RGB", (W, H), "#0a0a12")
    draw = ImageDraw.Draw(img, "RGBA")
    font_title = _font_bold(28)
    font_sub = _font(16)
    font_small = _font(13)
    font_tiny = _font(11)

    # Background plot area
    draw.rectangle([left, top, left + plot_w, top + plot_h], fill="#12121c")

    # Precompute band edges across time for filled rainbow (dynamic model)
    # Use monthly samples for band fills
    band_times: list[datetime] = []
    cur = CHART_START
    while cur <= CHART_END:
        band_times.append(cur)
        # advance ~30 days
        cur = datetime.fromtimestamp(cur.timestamp() + 30 * 86400)

    def band_edge_at(day: datetime, e: int) -> float:
        d = max(1, days_between(day, GENESIS))
        fit = 10 ** (dynamic.slope * math.log10(d) + dynamic.intercept)
        return fit * (1.3 ** (8 - e))

    # Draw bands from top (e=0) to bottom as filled polygons between edges
    # labels map to edges C[1]..C[9]; fill between C[e] and C[e+1]
    for e, band in enumerate(BANDS_TOP_TO_BOTTOM[:9]):
        upper = []
        lower = []
        for day in band_times:
            xu = x_of(day.timestamp())
            upper.append((xu, y_of(band_edge_at(day, e))))
            lower.append((xu, y_of(band_edge_at(day, e + 1))))
        poly = upper + list(reversed(lower))
        # Convert hex to RGBA with alpha
        hex_c = band["color"].lstrip("#")
        r, g, b = int(hex_c[0:2], 16), int(hex_c[2:4], 16), int(hex_c[4:6], 16)
        draw.polygon(poly, fill=(r, g, b, 160))

    # Gridlines (log prices)
    for price in [10, 100, 1_000, 10_000, 100_000, 1_000_000]:
        y = y_of(price)
        draw.line([(left, y), (left + plot_w, y)], fill=(255, 255, 255, 25), width=1)
        label = f"${price:,.0f}"
        draw.text((left + plot_w + 8, y - 7), label, fill="#8b8b9a", font=font_tiny)

    # Year ticks
    for year in range(2012, 2033, 2):
        dt = datetime(year, 1, 1)
        x = x_of(dt.timestamp())
        if left <= x <= left + plot_w:
            draw.line([(x, top), (x, top + plot_h)], fill=(255, 255, 255, 18), width=1)
            draw.text((x - 14, top + plot_h + 10), str(year), fill="#8b8b9a", font=font_tiny)

    # Price line
    price_xy = []
    for row in pts:
        ts = parse_day(row["time"]).timestamp()
        price_xy.append((x_of(ts), y_of(float(row["price"]))))
    if len(price_xy) >= 2:
        draw.line(price_xy, fill="#f8fafc", width=2)

    # Live price marker
    as_ts = as_of.timestamp()
    px, py = x_of(as_ts), y_of(live_price)
    if left <= px <= left + plot_w:
        draw.ellipse([px - 6, py - 6, px + 6, py + 6], fill="#00f0ff", outline="#ffffff")
        draw.line([(px, top), (px, top + plot_h)], fill=(0, 240, 255, 40), width=1)

    # Title / subtitle
    draw.text((left, 18), "Bitcoin Rainbow Chart — Dynamic Power Law", fill="#f8fafc", font=font_title)
    sub = (
        f"Live price: ${live_price:,.0f}  ·  Band: {dynamic.band['label']}  ·  "
        f"R²={dynamic.r2 * 100:.1f}%  ·  {as_of.strftime('%Y-%m-%d')}"
    )
    draw.text((left, 48), sub, fill="#a0a0b0", font=font_sub)

    # Legend (right side under axis labels area — draw left of plot bottom-right stack)
    legend_x = left + 12
    legend_y = top + 12
    draw.rounded_rectangle(
        [legend_x - 6, legend_y - 6, legend_x + 250, legend_y + 9 * 18 + 10],
        radius=8,
        fill=(10, 10, 18, 200),
        outline=(255, 255, 255, 30),
    )
    for i, band in enumerate(BANDS_TOP_TO_BOTTOM[:9]):
        y = legend_y + i * 18
        hex_c = band["color"].lstrip("#")
        r, g, b = int(hex_c[0:2], 16), int(hex_c[2:4], 16), int(hex_c[4:6], 16)
        active = i == dynamic.band_index
        draw.rectangle([legend_x, y, legend_x + 14, y + 12], fill=(r, g, b))
        color = "#00f0ff" if active else "#d0d0d8"
        prefix = "▶ " if active else "  "
        draw.text((legend_x + 20, y - 1), f"{prefix}{band['label']}", fill=color, font=font_tiny)

    # Footer
    footer = (
        f"Source: BlockchainCenter · Power Law fit on 180d local bottoms · "
        f"Not financial advice · {SOURCE_URL}"
    )
    draw.text((left, H - 28), footer, fill="#666677", font=font_tiny)

    # Border
    draw.rectangle([left, top, left + plot_w, top + plot_h], outline=(255, 255, 255, 40), width=1)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(out_path, "PNG", optimize=True)
    print(f"Wrote {out_path} ({out_path.stat().st_size} bytes)")


# ---------------------------------------------------------------------------
# Markdown + JSON writers
# ---------------------------------------------------------------------------
def build_payload(
    series: list[dict[str, Any]],
    rates: dict[str, Any],
    original: OriginalModel,
    dynamic: DynamicModel,
    live_price: float,
    as_of: datetime,
    feed_meta: dict[str, Any] | None = None,
) -> dict[str, Any]:
    # Downsample historical dataset for the JSON block (weekly + last point)
    hist = []
    for i, row in enumerate(series):
        t = parse_day(row["time"])
        if t < CHART_START:
            continue
        if i % 7 == 0 or i == len(series) - 1:
            day_index = days_between(t, CHART_START)
            hist.append(
                {
                    "date": row["time"],
                    "price": round(float(row["price"]), 2),
                    "original_band_bounds": [
                        round(original_band_price(day_index, c, o), 2) for c, o in ORIGINAL_BAND_COEFFS
                    ],
                }
            )

    return {
        "meta": {
            "title": "Bitcoin Rainbow Chart – Dynamic Analysis",
            "source": SOURCE_URL,
            "source_apis": {"chartdata": CHART_API, "rates": RATES_API},
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "as_of": as_of.strftime("%Y-%m-%d"),
            "disclaimer": (
                "The Rainbow Chart is not financial advice. "
                "Past performance is not an indication of future results. "
                "It is a fun, visual way to look at long-term price movements."
            ),
            "agent": "Grok Agent · CryptoItaliaFacile",
            "language": "en",
            "feed": feed_meta or {},
        },
        "live": {
            "price_usd": live_price,
            "price_eur": rates.get("price_eur"),
            "market_cap_usd": rates.get("market_cap_usd"),
            "percent_change_24h": rates.get("percent_change_24h"),
            "percent_change_7d": rates.get("percent_change_7d"),
            "ath": rates.get("ath"),
            "ath_date": rates.get("ath_date"),
            "symbol": rates.get("symbol", "BTC"),
            "name": rates.get("name", "Bitcoin"),
        },
        "legend": BANDS_TOP_TO_BOTTOM,
        "original_model": {
            "type": "static_log_regression",
            "day_index_since_2012": original.day_index,
            "band_index": original.band_index,
            "band": original.band,
            "bounds_usd": [round(b, 2) for b in original.bounds_usd],
            "interpretation": interpretation_en(original.band, "Original model"),
        },
        "dynamic_model": {
            "type": "power_law_bottoms_180d",
            "formula": dynamic.formula,
            "slope": dynamic.slope,
            "intercept": dynamic.intercept,
            "r2": round(dynamic.r2, 4),
            "r2_percent": round(dynamic.r2 * 100, 1),
            "fit_price_usd": round(dynamic.fit_price, 2),
            "band_index": dynamic.band_index,
            "band": dynamic.band,
            "band_edges_usd": [round(e, 2) for e in dynamic.band_edges],
            "deviation_percent_vs_center": round(dynamic.deviation_pct, 2),
            "bottoms_used": dynamic.bottoms_used,
            "tops_used": dynamic.tops_used,
            "interpretation": interpretation_en(dynamic.band, "Dynamic model"),
        },
        "historical": {
            "points": len(hist),
            "from": hist[0]["date"] if hist else None,
            "to": hist[-1]["date"] if hist else None,
            "dataset": hist,
        },
    }


def write_markdown(payload: dict[str, Any], out_path: Path) -> None:
    live = payload["live"]
    dyn = payload["dynamic_model"]
    orig = payload["original_model"]
    meta = payload["meta"]
    band = dyn["band"]

    legend_rows = "\n".join(
        f"| `{b['color']}` | **{b['label']}** |" for b in payload["legend"]
    )

    # Compact JSON (full dataset stays in data/*.json)
    compact = {
        "meta": meta,
        "live": live,
        "legend": payload["legend"],
        "original_model": {k: v for k, v in orig.items() if k != "bounds_usd"}
        | {"bounds_usd_sample": orig["bounds_usd"]},
        "dynamic_model": {k: v for k, v in dyn.items() if k != "band_edges_usd"}
        | {"band_edges_usd": dyn["band_edges_usd"]},
        "historical_summary": {
            "points": payload["historical"]["points"],
            "from": payload["historical"]["from"],
            "to": payload["historical"]["to"],
            "note": "Full weekly dataset in /data/bitcoin-rainbow-chart.json",
        },
    }

    md = f"""# Bitcoin Rainbow Chart – Dynamic Analysis

> Auto-updated by **Grok Agent** · {meta["generated_at"]}  
> Source: [{SOURCE_URL}]({SOURCE_URL})

## What is the Bitcoin Rainbow Chart?

The **Bitcoin Rainbow Chart** is a logarithmic chart of Bitcoin’s full price history,
overlaid with colored bands (the “rainbow”) that mark relative valuation zones along
a long-term growth curve.

It began as a Reddit meme (2014, user *azop*) and was turned into a live tool by
[BlockchainCenter]({SOURCE_URL}). It is **not a scientific forecasting model** and
**not financial advice**. It helps zoom out from daily volatility and place the current
price in multi-year cycle context.

The **Dynamic** version fits a **Power Law** regression in real time on price history
(using 180-day local bottoms), with fit strength commonly reported around **94%+ R²**
on the source site.

---

## Live data (from BlockchainCenter)

| Field | Value |
|-------|--------|
| BTC price (USD) | **${live["price_usd"]:,.2f}** |
| BTC price (EUR) | {f'€{live["price_eur"]:,.2f}' if live.get("price_eur") else "n/a"} |
| Change 24h | {live.get("percent_change_24h", 0):+.2f}% |
| Change 7d | {live.get("percent_change_7d", 0):+.2f}% |
| Market cap (USD) | ${live.get("market_cap_usd") or 0:,.0f} |
| ATH | ${live.get("ath") or 0:,.0f} ({(live.get("ath_date") or "")[:10]}) |
| As of | {meta["as_of"]} |

### Current band position

| Model | Current band |
|-------|--------------|
| **Dynamic Power Law** | **{band["label"]}** |
| Original (log regression) | {orig["band"]["label"]} |

- Dynamic formula: `{dyn["formula"]}`
- Fit R²: **{dyn["r2_percent"]}%**
- Deviation vs model center: **{dyn["deviation_percent_vs_center"]:+.1f}%**

---

## Generated chart

![Bitcoin Rainbow Chart](../assets/rainbow-chart.png)

*Image regenerated on every run of `scripts/update-bitcoin-rainbow-chart.py`.*

---

## Color bands & legend

| Color | Label |
|-------|--------|
{legend_rows}

Bands run from the top (euphoria / relative overvaluation) to the bottom
(panic / relative undervaluation vs the model’s long-term trend).

---

## Interpretation of the current band

### Dynamic model — {band["label"]}

{dyn["interpretation"]}

### Original model — {orig["band"]["label"]}

{orig["interpretation"]}

### How to read this (not financial advice)

- The chart describes **long-term history and sentiment**, not entry/exit timing.
- Labels (BUY, SELL, FOMO, HODL…) are **educational memes**, not trading orders.
- A low band does not guarantee rallies; a high band does not guarantee drawdowns.
- Use the rainbow as **context**, alongside risk management, time horizon, and
  understanding of the Bitcoin protocol.

---

## Dynamic JSON dataset

The block below is a compact extract of the generated payload. The full weekly
historical dataset is in [`/data/bitcoin-rainbow-chart.json`](../data/bitcoin-rainbow-chart.json).

```json
{json.dumps(compact, indent=2, ensure_ascii=False)}
```

---

## How to refresh

```bash
python3 scripts/update-bitcoin-rainbow-chart.py
```

The script:

1. Fetches historical and live prices from BlockchainCenter  
2. Recomputes Original + Dynamic bands  
3. Regenerates PNG, JSON, and this markdown  

---

## Disclaimer

{meta["disclaimer"]}

Project: **CryptoItaliaFacile / The Little Satoshi News** · Agent: Grok
"""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")
    print(f"Wrote {out_path}")


def main() -> int:
    print("Fetching BlockchainCenter rainbow data…")
    series, rates, feed_meta = fetch_live_data()
    live_price = float(rates["price_usd"])
    last_chart = series[-1]
    as_of = parse_day(last_chart["time"])

    print(
        f"Series points: {len(series)} · as_of={as_of.date()} · live=${live_price:,.2f} "
        f"· feed={feed_meta.get('feed_unit_detected')} fx={feed_meta.get('fx_used')}"
    )

    original = compute_original_model(live_price, as_of)
    dynamic = compute_dynamic_model(series, live_price, as_of)

    print(f"Original band: {original.band['label']} (#{original.band_index})")
    print(f"Dynamic  band: {dynamic.band['label']} (#{dynamic.band_index}) R²={dynamic.r2:.4f}")
    print(f"Dynamic formula: {dynamic.formula}")

    payload = build_payload(series, rates, original, dynamic, live_price, as_of, feed_meta)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    SECTIONS_DIR.mkdir(parents=True, exist_ok=True)

    JSON_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {JSON_PATH} ({JSON_PATH.stat().st_size} bytes)")

    render_chart_png(series, dynamic, original, live_price, as_of, PNG_PATH)
    write_markdown(payload, MD_PATH)

    # Sidecar snapshot for the homepage #rainbow-data injector
    snapshot = {
        "updated_at": payload["meta"]["generated_at"],
        "as_of": payload["meta"]["as_of"],
        "price_usd": live_price,
        "band": dynamic.band,
        "band_original": original.band,
        "r2_percent": payload["dynamic_model"]["r2_percent"],
        "formula": dynamic.formula,
        "interpretation": payload["dynamic_model"]["interpretation"],
        "source": SOURCE_URL,
        "chart_image": "assets/rainbow-chart.png",
        "section_md": "sections/bitcoin-rainbow-chart.md",
        "disclaimer": payload["meta"]["disclaimer"],
    }
    snap_path = DATA_DIR / "bitcoin-rainbow-live.json"
    snap_path.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {snap_path}")
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

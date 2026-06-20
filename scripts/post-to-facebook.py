#!/usr/bin/env python3
"""Pubblica articoli The Little Satoshi News su Facebook via Graph API.

Setup: scripts/.env oppure variabili d'ambiente FACEBOOK_*
Guida: facebook-auto-setup.html

Uso manuale:
  python post-to-facebook.py --slug iniziare-exchange-revolut-kraken
  python post-to-facebook.py --dry-run --today --per-day 3

Automazione (20 post/giorno, 07:00–22:00 Roma):
  python post-to-facebook.py --auto --now        # rileva slot dall'orario
  python post-to-facebook.py --auto --slot 0     # post 1 (07:00)
  python post-to-facebook.py --auto --slot 19    # post 20 (22:00)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime
from pathlib import Path
try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_PATH = ROOT / "data" / "articles.json"
SCHEDULE_PATH = ROOT / "data" / "facebook-schedule.json"
SITE_URL = "https://satoshiallien.github.io/cryptoitaliafacile/"
IMAGE_BASE = f"{SITE_URL}assets/img/facebook/posts/"
ENV_PATH = Path(__file__).resolve().parent / ".env"

EMOJI = {
    "guide": "📖", "tip": "💡", "trend": "📈", "tutorial": "🎓",
    "cardano": "🔷", "sicurezza": "🔒",
}
LABELS = {
    "guide": "Guida", "tip": "Crypto Tip", "trend": "Trend", "tutorial": "Tutorial",
    "cardano": "Cardano", "sicurezza": "Sicurezza",
}
HOOKS = {
    "guide": "🔥 GUIDA GRATIS — Non saltare questo:",
    "tip": "⚡ TIP DA APPLICARE SUBITO:",
    "trend": "📈 TREND HOT — Cosa devi sapere:",
    "tutorial": "🎓 TUTORIAL PASSO-PASSO:",
    "cardano": "🔷 CARDANO — Lo spieghiamo facile:",
    "sicurezza": "🚨 ATTENZIONE — Evita questo errore:",
}
IMAGE_DEFAULTS = {
    "guide": "guide.jpg", "tip": "tip.jpg", "trend": "trend.jpg", "tutorial": "guide.jpg",
    "cardano": "cardano.jpg", "sicurezza": "sicurezza.jpg",
}
IMAGE_BY_TAG = {
    "bitcoin": "bitcoin.jpg", "btc": "bitcoin.jpg", "exchange": "exchange.jpg",
    "revolut": "exchange.jpg", "kraken": "exchange.jpg", "wallet": "wallet.jpg",
    "seed phrase": "sicurezza.jpg", "sicurezza": "sicurezza.jpg", "phishing": "sicurezza.jpg",
    "truffe": "sicurezza.jpg", "cardano": "cardano.jpg", "ada": "cardano.jpg",
    "ethereum": "ethereum.jpg", "eth": "ethereum.jpg", "defi": "defi.jpg",
    "uniswap": "defi.jpg", "staking": "ethereum.jpg", "ledger": "wallet.jpg",
    "metamask": "wallet.jpg", "#bitcoin": "bitcoin.jpg", "#ethereum": "ethereum.jpg",
    "#defi": "defi.jpg", "#etf": "bitcoin.jpg", "#layer2": "ethereum.jpg",
}
FB_POSTS_PER_DAY = 20


def generate_slot_times(per_day: int = FB_POSTS_PER_DAY, start_h: int = 7, end_h: int = 22) -> list[str]:
    start_m = start_h * 60
    end_m = end_h * 60
    times: list[str] = []
    for i in range(per_day):
        if per_day == 1:
            mins = start_m
        else:
            mins = round(start_m + (end_m - start_m) * i / (per_day - 1))
        times.append(f"{mins // 60:02d}:{mins % 60:02d}")
    return times


def slot_label(index: int, per_day: int = FB_POSTS_PER_DAY) -> str:
    times = generate_slot_times(per_day)
    if 0 <= index < len(times):
        return f"Post {index + 1} ({times[index]})"
    return f"Post {index + 1}"


def current_slot_index(per_day: int = FB_POSTS_PER_DAY, tz_name: str = "Europe/Rome", tolerance: int = 22) -> int | None:
    if ZoneInfo is None:
        return None
    try:
        now = datetime.now(ZoneInfo(tz_name))
    except Exception:
        return None
    now_mins = now.hour * 60 + now.minute
    for i, t in enumerate(generate_slot_times(per_day)):
        h, m = map(int, t.split(":"))
        slot_mins = h * 60 + m
        if abs(now_mins - slot_mins) <= tolerance:
            return i
    return None


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    env.update({k: v for k, v in os.environ.items() if k.startswith("FACEBOOK_")})
    return env


def load_schedule() -> dict:
    default = {
        "startDate": date.today().isoformat(),
        "postsPerDay": FB_POSTS_PER_DAY,
        "timezone": "Europe/Rome",
        "posted": [],
    }
    if not SCHEDULE_PATH.exists():
        return default
    data = json.loads(SCHEDULE_PATH.read_text(encoding="utf-8"))
    return {**default, **data}


def save_schedule(schedule: dict) -> None:
    SCHEDULE_PATH.write_text(
        json.dumps(schedule, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def article_url(slug: str) -> str:
    return f"{SITE_URL}articolo.html?slug={urllib.parse.quote(slug)}"


def facebook_image_file(article: dict) -> str:
    if article.get("fbImage"):
        return article["fbImage"]
    for raw in article.get("tags") or []:
        tag = str(raw).lower().lstrip("#").strip()
        if tag in IMAGE_BY_TAG:
            return IMAGE_BY_TAG[tag]
        if f"#{tag}" in IMAGE_BY_TAG:
            return IMAGE_BY_TAG[f"#{tag}"]
    title = (article.get("title") or "").lower()
    slug = (article.get("slug") or "").lower()
    if "bitcoin" in title or "bitcoin" in slug:
        return "bitcoin.jpg"
    if "ethereum" in title or "ethereum" in slug:
        return "ethereum.jpg"
    if "cardano" in title or "cardano" in slug or "ada" in slug:
        return "cardano.jpg"
    if "exchange" in title or "exchange" in slug or "revolut" in slug or "kraken" in slug:
        return "exchange.jpg"
    if "wallet" in title or "wallet" in slug or "seed" in slug:
        return "wallet.jpg"
    if "sicurezz" in title or "sicurezz" in slug or "phishing" in slug:
        return "sicurezza.jpg"
    if "defi" in title or "defi" in slug or "uniswap" in slug:
        return "defi.jpg"
    cat = article.get("category", "guide")
    return IMAGE_DEFAULTS.get(cat, "guide.jpg")


def facebook_image_url(article: dict) -> str:
    return IMAGE_BASE + facebook_image_file(article)


def build_post(article: dict) -> str:
    cat = article.get("category", "guide")
    emoji = EMOJI.get(cat, "📖")
    label = LABELS.get(cat, "Guida")
    hook = HOOKS.get(cat, "🔥 Non perdere questa guida:")
    raw_tags = []
    for t in (article.get("tags") or [])[:4]:
        clean = t.lstrip("#").strip()
        if clean:
            raw_tags.append(f"#{clean}")
    tags = " ".join(raw_tags)
    base_tags = "#crypto #The Little Satoshi News #educazione"
    return (
        f"{hook}\n\n"
        f"{emoji} {label}: {article['title']}\n\n"
        f"{article['excerpt']}\n\n"
        f"👉 Leggi la guida completa:\n{article_url(article['slug'])}\n\n"
        f"{tags} {base_tags}".strip()
    )


def graph_post(url: str, data: dict, dry_run: bool, label: str) -> dict:
    if dry_run:
        print(f"[DRY RUN] POST {label}", url)
        for k, v in data.items():
            if k != "access_token":
                print(f"  {k}: {v}")
        return {"dry_run": True, "id": "dry-run"}
    body = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        return {"error": {"code": e.code, "message": err_body}}


def post_to_facebook(message: str, link: str, image_url: str, page_id: str, token: str, dry_run: bool) -> dict:
    photo_url = f"https://graph.facebook.com/v21.0/{page_id}/photos"
    photo_data = {
        "url": image_url,
        "message": message,
        "access_token": token,
        "published": "true",
    }
    if dry_run:
        print("[DRY RUN] POST photo", photo_url)
        print(message)
        print("IMAGE:", image_url)
        print("LINK:", link)
        return {"dry_run": True, "id": "dry-run"}

    result = graph_post(photo_url, photo_data, dry_run=False, label="photo")
    if not result.get("error"):
        return result

    err = result["error"]
    print(f"Photo post failed ({err.get('code')}): trying feed+link fallback...", file=sys.stderr)
    feed_url = f"https://graph.facebook.com/v21.0/{page_id}/feed"
    feed_data = {
        "message": message,
        "link": link,
        "picture": image_url,
        "access_token": token,
    }
    fallback = graph_post(feed_url, feed_data, dry_run=False, label="feed")
    if fallback.get("error"):
        fb_err = fallback["error"]
        hint = ""
        if "expired" in str(fb_err.get("message", "")).lower():
            hint = "\nToken scaduto → facebook-fix.html"
        raise SystemExit(f"Facebook API error {fb_err.get('code')}: {fb_err.get('message')}{hint}") from None
    return fallback


def article_score(article: dict) -> int:
    return (4 if article.get("featured") else 0) + (2 if article.get("popular") else 0)


def balanced_queue(articles: list[dict]) -> list[dict]:
    buckets: dict[str, list[dict]] = {
        "guide": sorted(
            [a for a in articles if a.get("category") in ("guide", "tutorial")],
            key=article_score, reverse=True,
        ),
        "tip": sorted([a for a in articles if a.get("category") == "tip"], key=article_score, reverse=True),
        "trend": sorted([a for a in articles if a.get("category") == "trend"], key=article_score, reverse=True),
        "other": sorted(
            [a for a in articles if a.get("category") in ("cardano", "sicurezza")],
            key=article_score, reverse=True,
        ),
    }
    queue: list[dict] = []
    max_len = max((len(v) for v in buckets.values()), default=0)
    for i in range(max_len):
        for key in ("guide", "tip", "trend", "other"):
            if i < len(buckets[key]):
                queue.append(buckets[key][i])
    seen: set[str] = set()
    unique: list[dict] = []
    for item in queue:
        slug = item["slug"]
        if slug in seen:
            continue
        seen.add(slug)
        unique.append(item)
    return unique


def daily_plan(articles: list[dict], per_day: int) -> list[list[dict]]:
    queue = balanced_queue(articles)
    if not queue:
        return []
    min_days = max((len(queue) + per_day - 1) // per_day, 30)
    days: list[list[dict]] = []
    cursor = 0
    for _ in range(min_days):
        day_posts = [queue[cursor % len(queue)] for _ in range(per_day)]
        cursor += per_day
        days.append(day_posts)
    return days


def parse_date(value: str) -> date:
    return date.fromisoformat(value[:10])


def today_in_timezone(tz_name: str = "Europe/Rome") -> date:
    if ZoneInfo is not None:
        try:
            return datetime.now(ZoneInfo(tz_name)).date()
        except Exception:
            pass
    return date.today()


def now_in_timezone_iso(tz_name: str = "Europe/Rome") -> str:
    if ZoneInfo is not None:
        try:
            return datetime.now(ZoneInfo(tz_name)).isoformat()
        except Exception:
            pass
    return datetime.now().isoformat()


def day_index_from_start(start_date: str, today: date | None = None) -> int:
    start = parse_date(start_date)
    current = today or date.today()
    return (current - start).days


def already_posted(schedule: dict, date_str: str, slot: int) -> bool:
    return any(
        p.get("date") == date_str and p.get("slot") == slot
        for p in schedule.get("posted", [])
    )


def record_post(schedule: dict, date_str: str, slot: int, slug: str, post_id: str) -> None:
    schedule.setdefault("posted", []).append({
        "date": date_str,
        "slot": slot,
        "slug": slug,
        "postId": post_id,
        "publishedAt": now_in_timezone_iso(schedule.get("timezone", "Europe/Rome")),
    })


def get_auto_article(articles: list[dict], schedule: dict, slot: int, env: dict) -> tuple[dict | None, int, str]:
    per_day = int(env.get("FACEBOOK_POSTS_PER_DAY") or schedule.get("postsPerDay") or FB_POSTS_PER_DAY)
    start_date = env.get("FACEBOOK_SCHEDULE_START") or schedule.get("startDate")
    tz_name = schedule.get("timezone", "Europe/Rome")
    today = today_in_timezone(tz_name)
    today_str = today.isoformat()

    if slot >= per_day:
        print(f"Slot {slot} disattivato (postsPerDay={per_day})")
        return None, day_index_from_start(start_date, today), today_str

    if already_posted(schedule, today_str, slot):
        print(f"Già pubblicato oggi slot {slot} ({slot_label(slot, per_day)})")
        return None, day_index_from_start(start_date, today), today_str

    day_idx = day_index_from_start(start_date, today)
    if day_idx < 0:
        print(f"Piano non ancora iniziato (startDate={start_date})")
        return None, day_idx, today_str

    days = daily_plan(articles, per_day)
    if not days:
        print("Nessun articolo nel piano")
        return None, day_idx, today_str

    effective_day = day_idx % len(days)
    day_posts = days[effective_day]
    if slot >= len(day_posts):
        print(f"Nessun articolo per slot {slot} nel giorno {day_idx + 1}")
        return None, day_idx, today_str

    return day_posts[slot], day_idx, today_str


def select_articles(data: dict, args: argparse.Namespace) -> list[dict]:
    articles = data["articles"]
    if args.slug:
        found = [a for a in articles if a["slug"] == args.slug]
        if not found:
            raise SystemExit(f"Articolo non trovato: {args.slug}")
        return found

    schedule = load_schedule()
    per_day = args.per_day

    if args.auto:
        env = load_env()
        article, day_idx, today_str = get_auto_article(articles, schedule, args.slot, env)
        if not article:
            return []
        auto_per_day = int(env.get("FACEBOOK_POSTS_PER_DAY") or schedule.get("postsPerDay") or FB_POSTS_PER_DAY)
        print(f"Auto post — giorno {day_idx + 1}, slot {args.slot} ({slot_label(args.slot, auto_per_day)}), data {today_str}")
        return [article]

    if args.day is not None or args.today:
        days = daily_plan(articles, per_day)
        if args.today:
            start = schedule.get("startDate", date.today().isoformat())
            day_index = max(0, day_index_from_start(start))
        else:
            day_index = max(0, args.day - 1)
        if day_index >= len(days):
            raise SystemExit(f"Giorno {day_index + 1} non disponibile (piano: {len(days)} giorni)")
        return days[day_index]

    if args.all:
        return balanced_queue(articles)

    if args.featured:
        articles = [a for a in articles if a.get("featured") or a.get("popular")]
    elif args.popular:
        articles = [a for a in articles if a.get("popular")]
    articles = sorted(articles, key=article_score, reverse=True)
    return articles[: args.limit]


def main() -> None:
    parser = argparse.ArgumentParser(description="Pubblica articoli su Facebook")
    parser.add_argument("--slug", help="Slug di un singolo articolo")
    parser.add_argument("--featured", action="store_true", help="Solo articoli in evidenza")
    parser.add_argument("--popular", action="store_true", help="Solo articoli popolari")
    parser.add_argument("--limit", type=int, default=1, help="Numero massimo di post")
    parser.add_argument("--per-day", type=int, default=FB_POSTS_PER_DAY, help="Post per giorno nel piano (default: 20)")
    parser.add_argument("--day", type=int, help="Pubblica il piano del giorno N (1 = primo giorno)")
    parser.add_argument("--today", action="store_true", help="Pubblica tutti i post del giorno corrente del piano")
    parser.add_argument("--auto", action="store_true", help="Modalità automatica (un post per slot)")
    parser.add_argument("--now", action="store_true", help="Con --auto: rileva lo slot dall'orario di Roma")
    parser.add_argument("--slot", type=int, default=0, help="Slot orario 0–19 (20 post/giorno, 07:00–22:00 Roma)")
    parser.add_argument("--dry-run", action="store_true", help="Mostra senza pubblicare")
    parser.add_argument("--all", action="store_true", help="Pubblica tutti gli articoli del sito")
    parser.add_argument("--delay", type=int, default=18, help="Secondi di pausa tra i post (con --all)")
    args = parser.parse_args()

    env = load_env()
    page_id = env.get("FACEBOOK_PAGE_ID", "")
    token = env.get("FACEBOOK_PAGE_ACCESS_TOKEN", "")

    if not args.dry_run and (not page_id or not token):
        print("Mancano FACEBOOK_PAGE_ID e FACEBOOK_PAGE_ACCESS_TOKEN.", file=sys.stderr)
        print(f"Crea il file: {ENV_PATH}", file=sys.stderr)
        print("Guida: facebook-auto-setup.html", file=sys.stderr)
        sys.exit(1)

    data = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
    schedule = load_schedule()
    per_day = int(schedule.get("postsPerDay") or FB_POSTS_PER_DAY)

    if args.auto and args.now:
        tz_name = schedule.get("timezone", "Europe/Rome")
        detected = current_slot_index(per_day, tz_name)
        if detected is None:
            print(f"Nessuno slot attivo ora ({tz_name}). Orari: {', '.join(generate_slot_times(per_day))}")
            return
        args.slot = detected
        print(f"Slot rilevato: {detected} — {slot_label(detected, per_day)}")

    if args.slot < 0 or args.slot >= per_day:
        raise SystemExit(f"Slot {args.slot} non valido. Usa 0–{per_day - 1}.")

    selected = select_articles(data, args)

    if not selected:
        print("Nessun post da pubblicare.")
        return

    posted_slugs = {p.get("slug") for p in schedule.get("posted", []) if p.get("slug")}
    ok = 0
    fail = 0

    for i, article in enumerate(selected):
        if args.all and article["slug"] in posted_slugs and not args.dry_run:
            print(f"\n[SKIP] Già pubblicato: {article['slug']}")
            continue

        message = build_post(article)
        link = article_url(article["slug"])
        image_url = facebook_image_url(article)
        print(f"\n--- [{i + 1}/{len(selected)}] {article['title']} ---")
        print(f"IMAGE: {image_url}")
        try:
            result = post_to_facebook(message, link, image_url, page_id, token, args.dry_run)
            print(json.dumps(result, indent=2))
            ok += 1
        except SystemExit as exc:
            print(f"ERRORE: {exc}")
            fail += 1
            if args.all:
                print("Attendo 60s prima di riprovare il prossimo...")
                time.sleep(60)
                continue
            raise

        if not args.dry_run and result.get("id"):
            today_str = today_in_timezone(schedule.get("timezone", "Europe/Rome")).isoformat()
            if args.auto:
                record_post(schedule, today_str, args.slot, article["slug"], result.get("id", ""))
            elif args.all:
                schedule.setdefault("posted", []).append({
                    "date": today_str,
                    "slot": -1,
                    "slug": article["slug"],
                    "postId": result.get("id", ""),
                    "publishedAt": now_in_timezone_iso(schedule.get("timezone", "Europe/Rome")),
                    "bulk": True,
                })
                posted_slugs.add(article["slug"])
            if args.auto or args.all:
                save_schedule(schedule)

        if args.all and i < len(selected) - 1 and not args.dry_run:
            print(f"Pausa {args.delay}s...")
            time.sleep(args.delay)

    if args.all:
        print(f"\nCompletato: {ok} pubblicati, {fail} errori, {len(selected)} totali nel piano.")


if __name__ == "__main__":
    main()
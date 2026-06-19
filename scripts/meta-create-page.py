#!/usr/bin/env python3
"""Crea la Pagina Facebook The Little Satoshi News via browser automatizzato."""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path

PAGE_NAME = "The Little Satoshi News"
CATEGORIES = ("Sito web educativo", "Istruzione", "Education website", "Education")
PAGE_BIO = "Notizie crypto, chiare e semplici. Guide passo-passo, tips e sicurezza. 100% educativo, zero hype."
PAGE_URL = "https://satoshiallien.github.io/cryptoitaliafacile/"
CREATE_URL = "https://www.facebook.com/pages/create/"
SHOTS = Path(__file__).resolve().parent / "meta-screenshots"


def click_first(page, labels: tuple[str, ...]) -> str | None:
    for label in labels:
        for getter in (
            lambda l=label: page.get_by_role("button", name=l),
            lambda l=label: page.get_by_text(l, exact=False),
        ):
            loc = getter()
            if loc.count() > 0:
                try:
                    loc.first.click(timeout=3000)
                    page.wait_for_timeout(1200)
                    return label
                except Exception:
                    pass
    return None


def fill_first(page, selectors: tuple[str, ...], value: str) -> bool:
    for sel in selectors:
        loc = page.locator(sel)
        if loc.count() > 0:
            try:
                loc.first.click(timeout=2000)
                loc.first.fill(value, timeout=2000)
                page.wait_for_timeout(800)
                return True
            except Exception:
                pass
    return False


def wait_login(page) -> None:
    if "login" not in page.url.lower() and page.locator('input[name="email"]').count() == 0:
        return
    print("Serve login Facebook. Accedi nella finestra del browser (max 3 min)...")
    deadline = time.time() + 180
    while time.time() < deadline:
        page.wait_for_timeout(2000)
        if "login" not in page.url.lower():
            dialogs = page.locator('input[name="email"]')
            if dialogs.count() == 0:
                print("Login rilevato.")
                return
    print("Timeout login — continuo comunque...")


def main() -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Esegui: pip install playwright && python -m playwright install chromium")
        return 1

    SHOTS.mkdir(exist_ok=True)
    edge = Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "Edge" / "User Data"

    with sync_playwright() as p:
        context = None
        browser = None
        if edge.exists():
            try:
                context = p.chromium.launch_persistent_context(
                    user_data_dir=str(edge),
                    channel="msedge",
                    headless=False,
                    slow_mo=250,
                    args=["--profile-directory=Default"],
                    locale="it-IT",
                    viewport={"width": 1280, "height": 900},
                )
                page = context.pages[0] if context.pages else context.new_page()
                print("Uso sessione Edge (login salvato).")
            except Exception as exc:
                print("Edge occupato, uso Chromium:", exc)
                context = None

        if context is None:
            browser = p.chromium.launch(headless=False, slow_mo=250)
            context = browser.new_context(locale="it-IT", viewport={"width": 1280, "height": 900})
            page = context.new_page()

        print("Apro creazione pagina...")
        page.goto(CREATE_URL, wait_until="domcontentloaded", timeout=90000)
        page.wait_for_timeout(4000)
        wait_login(page)
        page.screenshot(path=str(SHOTS / "retry-01.png"), full_page=True)

        clicked = click_first(
            page,
            ("Inizia", "Get Started", "Azienda o brand", "Azienda o marchio", "Business or Brand"),
        )
        if clicked:
            print("Cliccato:", clicked)

        fill_first(
            page,
            (
                'input[aria-label*="Nome della Pagina"]',
                'input[aria-label*="Page name" i]',
                'input[placeholder*="Nome"]',
                'label:has-text("Nome della Pagina") + input',
                'input[type="text"]',
            ),
            PAGE_NAME,
        )
        print("Nome:", PAGE_NAME)

        # Categoria
        cat_clicked = click_first(page, ("Aggiungi una categoria", "Add a category", "Categoria"))
        if cat_clicked:
            print("Aperto campo categoria")
        for cat in CATEGORIES:
            loc = page.get_by_text(cat, exact=False)
            if loc.count() > 0:
                try:
                    loc.first.click(timeout=2500)
                    print("Categoria:", cat)
                    page.wait_for_timeout(1000)
                    break
                except Exception:
                    pass
        else:
            fill_first(page, ('input[aria-label*="Categoria"]', 'input[placeholder*="categoria" i]'), CATEGORIES[0])

        page.screenshot(path=str(SHOTS / "retry-02-filled.png"), full_page=True)

        clicked = click_first(page, ("Continua", "Continue", "Crea", "Create", "Avanti", "Next"))
        if clicked:
            print("Cliccato:", clicked)
        page.wait_for_timeout(3000)
        page.screenshot(path=str(SHOTS / "retry-03-after-continue.png"), full_page=True)

        # Passi successivi se compaiono
        for _ in range(3):
            click_first(page, ("Salta", "Skip", "Fine", "Done", "Continua", "Continue", "Avanti", "Next"))
            page.wait_for_timeout(2000)

        page.screenshot(path=str(SHOTS / "retry-04-final.png"), full_page=True)
        final_url = page.url
        print("\nURL attuale:", final_url)

        if "facebook.com/" in final_url and "create" not in final_url and "login" not in final_url:
            print("\nPAGINA PROBABILMENTE CREATA!")
            print("URL da usare:", final_url)
        else:
            print("\nCompleta manualmente se serve (categoria + Continua).")
            print("Bio:", PAGE_BIO)
            print("Sito:", PAGE_URL)

        print("\nAttendo 90 secondi per completamento manuale...")
        page.wait_for_timeout(90000)
        print("URL finale:", page.url)

        if browser:
            browser.close()
        else:
            context.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
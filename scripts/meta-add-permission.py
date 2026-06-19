#!/usr/bin/env python3
"""Apre Meta Developer Console e tenta di aggiungere pages_manage_posts.

Richiede login Facebook attivo nel browser. Se non sei loggato, accedi manualmente
quando si apre la finestra, poi lo script continua.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

APP_ID = "1058281383830078"
USE_CASES_URL = f"https://developers.facebook.com/apps/{APP_ID}/use_cases/"
EXPLORER_URL = "https://developers.facebook.com/tools/explorer/"


def main() -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Installa Playwright: pip install playwright && python -m playwright install chromium")
        return 1

    shots = Path(__file__).resolve().parent / "meta-screenshots"
    shots.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        context = browser.new_context(locale="it-IT")
        page = context.new_page()

        print("Apro Casi d'uso Meta...")
        page.goto(USE_CASES_URL, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(4000)
        page.screenshot(path=str(shots / "01-use-cases.png"), full_page=True)

        if "login" in page.url.lower():
            print("Serve login Facebook. Accedi nella finestra del browser...")
            try:
                page.wait_for_url("**/apps/**", timeout=180000)
            except Exception:
                page.screenshot(path=str(shots / "02-login-timeout.png"), full_page=True)
                print("Timeout login. Riprova dopo aver effettuato l'accesso.")
                browser.close()
                return 2

        print("Cerco il caso d'uso Pagina...")
        page.wait_for_timeout(2000)

        candidates = [
            "text=Gestisci tutto sulla tua Pagina",
            "text=Manage everything on your Page",
            "text=Personalizza",
            "text=Customize",
        ]
        clicked = False
        for sel in candidates:
            loc = page.locator(sel)
            if loc.count() > 0:
                try:
                    loc.first.click(timeout=3000)
                    clicked = True
                    print(f"Cliccato: {sel}")
                    break
                except Exception:
                    pass

        page.wait_for_timeout(2000)
        page.screenshot(path=str(shots / "03-after-click.png"), full_page=True)

        for sel in ("text=pages_manage_posts", "text=Aggiungi", "text=Add"):
            loc = page.locator(sel)
            if loc.count() > 0:
                try:
                    loc.first.click(timeout=3000)
                    print(f"Cliccato: {sel}")
                    page.wait_for_timeout(1500)
                except Exception:
                    pass

        page.screenshot(path=str(shots / "04-permissions.png"), full_page=True)

        print("Apro Graph API Explorer per rigenerare il token...")
        page.goto(EXPLORER_URL, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(3000)
        page.screenshot(path=str(shots / "05-explorer.png"), full_page=True)

        print("\nScreenshot salvati in:", shots)
        print("Se il permesso non e' stato aggiunto automaticamente, completalo manualmente")
        print("nella finestra del browser (UI Meta cambia spesso).")
        print("\nPremi INVIO qui quando hai rigenerato il token...")
        try:
            input()
        except EOFError:
            time.sleep(30)

        browser.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
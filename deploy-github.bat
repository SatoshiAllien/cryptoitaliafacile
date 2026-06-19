@echo off
cd /d C:\SitoGrok

echo === CryptoItaliaFacile - Deploy su GitHub ===
echo.

where gh >nul 2>&1
if errorlevel 1 (
  echo GitHub CLI non trovato. Installalo da: https://cli.github.com/
  pause
  exit /b 1
)

gh auth status >nul 2>&1
if errorlevel 1 (
  echo Login GitHub richiesto. Segui le istruzioni a schermo...
  gh auth login -h github.com -p https -w
)

echo.
echo Creazione repository se non esiste...
gh repo view SatoshiAllien/cryptoitaliafacile >nul 2>&1
if errorlevel 1 (
  gh repo create SatoshiAllien/cryptoitaliafacile --public --source=. --remote=origin --push
) else (
  echo Repository gia esistente, eseguo push...
  git push -u origin main
)

echo.
echo === Fatto! ===
echo Sito: https://satoshiallien.github.io/cryptoitaliafacile/
echo Repo: https://github.com/SatoshiAllien/cryptoitaliafacile
echo.
echo GitHub Pages si attiva automaticamente dopo il primo push.
echo Se non vedi il sito, vai su Settings ^> Pages e scegli Source: GitHub Actions
echo.
pause
#!/usr/bin/env bash
# Avvio automato post — configura cron WSL + GitHub Actions + coda 14gg
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPTS="$ROOT/scripts"
MARKER="# cryptoitaliafacile-auto-post"
CRON_LINE="*/30 7-22 * * * TZ=Europe/Rome cd $SCRIPTS && /usr/bin/python3 publish_orchestrator.py --auto --limit 2 >> $ROOT/data/auto-post-cron.log 2>&1"

echo ""
echo "  CryptoItaliaFacile — Avvio automato post"
echo "  ========================================="
echo ""

cd "$SCRIPTS"

echo "→ Genera coda 14 giorni..."
python3 publish_orchestrator.py --generate --days 14

echo "→ Reset circuit breaker..."
python3 publish_orchestrator.py --reset-circuit

echo "→ Verifica credenziali..."
python3 verify-facebook-token.py 2>&1 | tail -3
python3 verify-instagram.py 2>&1 | tail -3

if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
  echo "→ Aggiorna GitHub Secrets..."
  bash "$SCRIPTS/setup-social-github-secrets.sh"
else
  echo "⚠ gh non autenticato — salto GitHub Secrets (esegui setup-social-github-secrets.sh dopo)"
fi

echo "→ Installa cron (ogni 30 min, 07:00–22:00 Roma)..."
TMP="$(mktemp)"
(crontab -l 2>/dev/null | grep -v "$MARKER" | grep -v "publish_orchestrator.py --auto" || true) > "$TMP"
echo "$CRON_LINE $MARKER" >> "$TMP"
crontab "$TMP"
rm -f "$TMP"

echo ""
echo "  ✅ Automazione attiva"
echo "  • Cron locale: ogni 30 min (07:00–22:00 Europe/Rome)"
echo "  • GitHub Actions: social-auto-post.yml (stesso orario)"
echo "  • Log cron: $ROOT/data/auto-post-cron.log"
echo ""
python3 publish_orchestrator.py --status
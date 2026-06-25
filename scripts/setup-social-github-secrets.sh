#!/usr/bin/env bash
# Push credenziali social da scripts/.env → GitHub Actions secrets
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="$ROOT/scripts/.env"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "ERRORE: $ENV_FILE non trovato" >&2
  exit 1
fi

declare -A vars=()
while IFS= read -r line; do
  line="${line%%#*}"
  line="$(echo "$line" | xargs)"
  [[ -z "$line" || "$line" != *"="* ]] && continue
  key="${line%%=*}"
  val="${line#*=}"
  val="${val%\"}"; val="${val#\"}"
  val="${val%\'}"; val="${val#\'}"
  vars["$key"]="$val"
done < "$ENV_FILE"

required=(FACEBOOK_PAGE_ID FACEBOOK_PAGE_ACCESS_TOKEN INSTAGRAM_ACCOUNT_ID)
for key in "${required[@]}"; do
  if [[ -z "${vars[$key]:-}" ]]; then
    echo "ERRORE: manca $key in scripts/.env" >&2
    exit 1
  fi
done

cd "$ROOT"
for key in "${required[@]}"; do
  echo "Setting GitHub secret: $key"
  printf '%s' "${vars[$key]}" | gh secret set "$key" --repo SatoshiAllien/cryptoitaliafacile
done

# Instagram workflow accetta anche token pagina Facebook
ig_token="${vars[INSTAGRAM_ACCESS_TOKEN]:-${vars[FACEBOOK_PAGE_ACCESS_TOKEN]}}"
echo "Setting GitHub secret: INSTAGRAM_ACCESS_TOKEN"
printf '%s' "$ig_token" | gh secret set INSTAGRAM_ACCESS_TOKEN --repo SatoshiAllien/cryptoitaliafacile

echo "GitHub workflow social-auto-post.yml pronto (20 post+story/giorno IG+FB)."
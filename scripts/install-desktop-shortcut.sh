#!/usr/bin/env bash
# Copia launcher sul Desktop Windows (WSL)
set -euo pipefail
DESKTOP="/mnt/c/Users/krown/Desktop"
SRC="$(cd "$(dirname "$0")/.." && pwd)/desktop"
ICO="$SRC/../assets/img/CryptoItaliaFacile.ico"

cp "$SRC/CryptoItaliaFacile.ps1" "$DESKTOP/CryptoItaliaFacile.ps1"
cp "$SRC/CryptoItaliaFacile-Pubblica.bat" "$DESKTOP/CryptoItaliaFacile-Pubblica.bat"

if [ -f "$ICO" ]; then
  cp "$ICO" "$DESKTOP/CryptoItaliaFacile.ico"
fi

cat > "$DESKTOP/CryptoItaliaFacile-Pubblica.vbs" <<'VBS'
Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "C:\Users\krown"
WshShell.Run "cmd /c ""C:\Users\krown\Desktop\CryptoItaliaFacile-Pubblica.bat""", 1, True
VBS

echo "Desktop shortcut aggiornato:"
echo "  $DESKTOP/CryptoItaliaFacile-Pubblica.bat"
echo "  $DESKTOP/CryptoItaliaFacile.ps1"
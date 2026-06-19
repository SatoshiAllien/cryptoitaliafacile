@echo off
echo Avvio server CryptoFacile su http://localhost:8080
echo Premi Ctrl+C per fermare
cd /d "%~dp0"
python -m http.server 8080
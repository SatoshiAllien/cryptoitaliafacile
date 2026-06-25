@echo off
cd /d "C:\Users\krown"
title CryptoItaliaFacile - Auto Post
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Users\krown\Desktop\CryptoItaliaFacile.ps1"
if errorlevel 1 (
  echo.
  echo ERRORE avvio launcher.
  echo Verifica che WSL "NVIDIA-Workbench" sia attivo.
  pause
)
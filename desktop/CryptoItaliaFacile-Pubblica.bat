@echo off
title CryptoItaliaFacile - Pubblica
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0CryptoItaliaFacile.ps1"
if errorlevel 1 (
  echo.
  echo ERRORE avvio launcher.
  echo Verifica che WSL "NVIDIA-Workbench" sia attivo.
  pause
)
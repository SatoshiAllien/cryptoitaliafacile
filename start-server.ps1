Set-Location $PSScriptRoot
Write-Host "Avvio server CryptoFacile su http://localhost:8080"
Write-Host "Premi Ctrl+C per fermare"
python -m http.server 8080
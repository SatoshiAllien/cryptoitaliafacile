Set-Location $PSScriptRoot
Write-Host "Avvio server The Little Satoshi News su http://localhost:8080"
Write-Host "Premi Ctrl+C per fermare"
python -m http.server 8080
# One-click setup for automatic X posts on @TheRiser100x
# Run: powershell -ExecutionPolicy Bypass -File scripts\setup-x-auto.ps1

$Project = "C:\Users\krown\cryptofacile"
Set-Location $Project

Write-Host "=== X Auto Post Setup (@TheRiser100x) ===" -ForegroundColor Cyan

$envFile = Join-Path $Project "scripts\.env"
$required = @("X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET")
$hasAll = $true
if (Test-Path $envFile) {
  $content = Get-Content $envFile -Raw
  foreach ($key in $required) {
    if ($content -notmatch "$key=.+") { $hasAll = $false }
  }
} else {
  $hasAll = $false
}

if (-not $hasAll) {
  Write-Host ""
  Write-Host "X API keys missing in scripts\.env" -ForegroundColor Yellow
  Write-Host "1. Open https://developer.x.com/"
  Write-Host "2. Create app with Read + Write for @TheRiser100x"
  Write-Host "3. Add to scripts\.env:"
  Write-Host ""
  Write-Host "X_API_KEY=..."
  Write-Host "X_API_SECRET=..."
  Write-Host "X_ACCESS_TOKEN=..."
  Write-Host "X_ACCESS_TOKEN_SECRET=..."
  Write-Host ""
  Start-Process "https://developer.x.com/en/portal/dashboard"
  exit 1
}

Write-Host "Verifying credentials..." -ForegroundColor Green
python scripts\verify-x-credentials.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host ""
Write-Host "Dry-run test (slot 0)..." -ForegroundColor Green
python scripts\fetch-crypto-news.py
python scripts\post-to-x.py --auto --slot 0 --dry-run
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host ""
Write-Host "Registering Windows scheduled tasks..." -ForegroundColor Green
& "$Project\scripts\register-x-tasks.ps1"

Write-Host ""
Write-Host "Done! Automatic posts active on this PC." -ForegroundColor Green
Write-Host "Cloud backup: add same keys to GitHub Secrets (see x-auto-setup.html)"
Write-Host "Preview: https://satoshiallien.github.io/cryptoitaliafacile/x-posts.html"
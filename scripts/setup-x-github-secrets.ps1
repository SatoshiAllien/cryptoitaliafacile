# Push X API keys from scripts\.env to GitHub Actions secrets
# Run: powershell -ExecutionPolicy Bypass -File scripts\setup-x-github-secrets.ps1

$Project = "C:\Users\krown\cryptofacile"
$envFile = Join-Path $Project "scripts\.env"
if (-not (Test-Path $envFile)) { Write-Error "scripts\.env not found"; exit 1 }

$vars = @{}
Get-Content $envFile | ForEach-Object {
  $line = $_.Trim()
  if ($line -and -not $line.StartsWith("#") -and $line.Contains("=")) {
    $parts = $line.Split("=", 2)
    $vars[$parts[0].Trim()] = $parts[1].Trim().Trim('"').Trim("'")
  }
}

$keys = @("X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET")
foreach ($key in $keys) {
  if (-not $vars[$key]) {
    Write-Error "Missing $key in scripts\.env"
    exit 1
  }
}

Set-Location $Project
foreach ($key in $keys) {
  Write-Host "Setting GitHub secret: $key"
  $vars[$key] | gh secret set $key
}

Write-Host "GitHub Actions workflow will post 5x/day even when PC is off."
Write-Host "Test: gh workflow run `"X Auto Post (TheRiser100x)`" -f dry_run=true"
# Push Instagram credentials from scripts\.env to GitHub Actions
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

$keys = @("INSTAGRAM_ACCOUNT_ID", "INSTAGRAM_ACCESS_TOKEN", "FACEBOOK_PAGE_ACCESS_TOKEN")
foreach ($key in $keys) {
  if (-not $vars[$key]) { Write-Error "Missing $key in scripts\.env"; exit 1 }
}

Set-Location $Project
foreach ($key in $keys) {
  Write-Host "Setting GitHub secret: $key"
  $vars[$key] | gh secret set $key
}
Write-Host "GitHub workflow instagram-auto-post.yml — 20 post + story/giorno su @krown.82."
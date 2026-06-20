# Register Windows scheduled task for 5 X posts/day (@TheRiser100x)
# Run: powershell -ExecutionPolicy Bypass -File scripts\register-x-tasks.ps1

$Project = "C:\Users\krown\cryptofacile"
$Python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $Python) { Write-Error "Python not found"; exit 1 }

@("TheRiser100x-X-Auto") | ForEach-Object {
  Unregister-ScheduledTask -TaskName $_ -Confirm:$false -ErrorAction SilentlyContinue
}

$fetch = New-ScheduledTaskAction -Execute $Python -Argument "scripts\fetch-crypto-news.py" -WorkingDirectory $Project
$post = New-ScheduledTaskAction -Execute $Python -Argument "scripts\post-to-x.py --auto --now" -WorkingDirectory $Project

# Fetch news every hour (07:00–22:00)
$fetchTrigger = New-ScheduledTaskTrigger -Once -At "07:00" -RepetitionInterval (New-TimeSpan -Hours 1) -RepetitionDuration (New-TimeSpan -Hours 16)
$fetchSettings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
Register-ScheduledTask -TaskName "TheRiser100x-X-Fetch" -Action $fetch -Trigger $fetchTrigger -Settings $fetchSettings -Force | Out-Null

# Post every 30 min (07:00–22:00) — detects slot automatically
$postTrigger = New-ScheduledTaskTrigger -Once -At "07:00" -RepetitionInterval (New-TimeSpan -Minutes 30) -RepetitionDuration (New-TimeSpan -Hours 16)
$postSettings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
Register-ScheduledTask -TaskName "TheRiser100x-X-Auto" -Action $post -Trigger $postTrigger -Settings $postSettings -Force | Out-Null

Write-Host "Registered:"
Write-Host "  TheRiser100x-X-Fetch  (hourly news refresh)"
Write-Host "  TheRiser100x-X-Auto   (every 30 min, 5 posts/day)"
Write-Host "Requires scripts\.env with X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET"
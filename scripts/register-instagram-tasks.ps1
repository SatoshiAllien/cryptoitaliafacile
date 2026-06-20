# Registra attività Windows per 20 post/giorno su Instagram
$Project = "C:\Users\krown\cryptofacile"
$Python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $Python) { Write-Error "Python non trovato"; exit 1 }

$action = New-ScheduledTaskAction -Execute $Python -Argument "scripts\post-to-instagram.py --auto --now" -WorkingDirectory $Project
$trigger = New-ScheduledTaskTrigger -Once -At "07:00" -RepetitionInterval (New-TimeSpan -Minutes 30) -RepetitionDuration (New-TimeSpan -Hours 15)
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
Register-ScheduledTask -TaskName "BitcoinIsHope-IG-20post" -Action $action -Trigger $trigger -Settings $settings -Force | Out-Null

Write-Host "Registrato: BitcoinIsHope-IG-20post (ogni 30 min, 07:00-22:00, 20 post/giorno)"
Write-Host "Richiede INSTAGRAM_ACCOUNT_ID + FACEBOOK_PAGE_ACCESS_TOKEN in scripts\.env"
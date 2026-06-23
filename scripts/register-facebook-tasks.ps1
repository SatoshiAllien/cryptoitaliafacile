# Registra attività Windows per 20 post/giorno su Facebook (locale)
# Esegui: powershell -ExecutionPolicy Bypass -File register-facebook-tasks.ps1

$Project = "C:\Users\krown\cryptofacile"
$Python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $Python) { Write-Error "Python non trovato"; exit 1 }

# Rimuovi vecchie attività (3 slot)
@("The Little Satoshi News-FB-Mattina", "The Little Satoshi News-FB-Pranzo", "The Little Satoshi News-FB-Sera") | ForEach-Object {
  Unregister-ScheduledTask -TaskName $_ -Confirm:$false -ErrorAction SilentlyContinue
}

# Una attività ogni 30 minuti (07:00–22:00) che rileva lo slot con --now
$action = New-ScheduledTaskAction -Execute $Python -Argument "scripts\post-to-facebook.py --auto --now --with-story" -WorkingDirectory $Project
$trigger = New-ScheduledTaskTrigger -Once -At "07:00" -RepetitionInterval (New-TimeSpan -Minutes 30) -RepetitionDuration (New-TimeSpan -Hours 15)
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
Register-ScheduledTask -TaskName "The Little Satoshi News-FB-20post" -Action $action -Trigger $trigger -Settings $settings -Force | Out-Null

Write-Host "Registrato: The Little Satoshi News-FB-20post (ogni 30 min, 07:00–22:00, 20 post+story/giorno)"
Write-Host "Richiede scripts\.env con FACEBOOK_PAGE_ID e FACEBOOK_PAGE_ACCESS_TOKEN"
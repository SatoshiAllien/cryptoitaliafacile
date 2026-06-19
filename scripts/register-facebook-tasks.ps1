# Registra 3 attività Windows per post automatici su Facebook (locale)
# Esegui come amministratore: powershell -ExecutionPolicy Bypass -File register-facebook-tasks.ps1

$Project = "C:\Users\krown\cryptofacile"
$Python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $Python) { Write-Error "Python non trovato"; exit 1 }

$slots = @(
  @{ Name = "The Little Satoshi News-FB-Mattina";  Slot = 0; Time = "09:00" },
  @{ Name = "The Little Satoshi News-FB-Pranzo";   Slot = 1; Time = "13:00" },
  @{ Name = "The Little Satoshi News-FB-Sera";     Slot = 2; Time = "19:00" }
)

foreach ($s in $slots) {
  $action = New-ScheduledTaskAction -Execute $Python -Argument "scripts\post-to-facebook.py --auto --slot $($s.Slot)" -WorkingDirectory $Project
  $trigger = New-ScheduledTaskTrigger -Daily -At $s.Time
  $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
  Register-ScheduledTask -TaskName $s.Name -Action $action -Trigger $trigger -Settings $settings -Force | Out-Null
  Write-Host "Registrato: $($s.Name) alle $($s.Time)"
}

Write-Host "`nFatto. Verifica in Utilità di pianificazione > The Little Satoshi News-FB-*"
Write-Host "Richiede scripts\.env con FACEBOOK_PAGE_ID e FACEBOOK_PAGE_ACCESS_TOKEN"
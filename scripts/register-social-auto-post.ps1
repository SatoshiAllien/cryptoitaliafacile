# Registra attività Windows per auto-post unificato (WSL orchestrator)
# Esegui: powershell -ExecutionPolicy Bypass -File scripts\register-social-auto-post.ps1

$Wsl = "C:\Windows\System32\wsl.exe"
$Distro = "NVIDIA-Workbench"
$Scripts = "/home/workbench/cryptoitaliafacile/scripts"
$TaskName = "CryptoItaliaFacile-AutoPost"

Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue

$action = New-ScheduledTaskAction -Execute $Wsl -Argument "-d $Distro bash -lc `"cd $Scripts && python3 publish_orchestrator.py --auto --limit 2`""
$trigger = New-ScheduledTaskTrigger -Once -At "07:00" -RepetitionInterval (New-TimeSpan -Minutes 30) -RepetitionDuration (New-TimeSpan -Hours 15)
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Minutes 25)
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Force | Out-Null

Write-Host "Registrato: $TaskName"
Write-Host "  Ogni 30 min, 07:00-22:00 — publish_orchestrator.py --auto --limit 2"
Write-Host "  WSL: $Distro"
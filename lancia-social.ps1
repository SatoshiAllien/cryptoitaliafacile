# CryptoItaliaFacile — launcher (stesso menu del Desktop)
Set-Location "C:\Users\krown"
$Wsl = "C:\Windows\System32\wsl.exe"
$Distro = "NVIDIA-Workbench"
$Scripts = "/home/workbench/cryptoitaliafacile/scripts"

function Run-Wsl([string]$Cmd) {
    & $Wsl -d $Distro bash -lc $Cmd
    return $LASTEXITCODE
}

function Test-Credentials {
    Write-Host "`n  Verifica credenziali da scripts/.env ..." -ForegroundColor DarkCyan
    Run-Wsl "cd $Scripts && python3 verify-facebook-token.py 2>&1 | tail -6"
    Run-Wsl "cd $Scripts && python3 verify-instagram.py 2>&1 | tail -5"
}

function Show-Menu {
    Clear-Host
    Write-Host "`n  CryptoItaliaFacile - Social Launch`n" -ForegroundColor Yellow
    Write-Host "  [1] Pubblica ORA (coda unificata)" -ForegroundColor Green
    Write-Host "  [2] Test dry-run" -ForegroundColor Cyan
    Write-Host "  [3] Stato coda" -ForegroundColor Magenta
    Write-Host "  [4] Aggiorna token" -ForegroundColor Yellow
    Write-Host "  [5] Server :8080" -ForegroundColor White
    Write-Host "  [6] Rigenera immagini" -ForegroundColor DarkYellow
    Write-Host "  [9] Avvio automato post (cron + GitHub)" -ForegroundColor Green
    Write-Host "  [0] Esci`n" -ForegroundColor DarkGray
}

Test-Credentials

do {
    Show-Menu
    $c = Read-Host "  Scegli"
    switch ($c) {
        "1" {
            Run-Wsl "cd $Scripts && python3 publish_orchestrator.py --auto --limit 2"
            Read-Host "Invio"
        }
        "2" {
            Run-Wsl "cd $Scripts && python3 publish_orchestrator.py --auto --dry-run --limit 2"
            Read-Host "Invio"
        }
        "3" {
            Run-Wsl "cd $Scripts && python3 publish_orchestrator.py --status"
            Read-Host "Invio"
        }
        "4" {
            $tok = Read-Host "Incolla token EAA/IG"
            if ($tok) {
                $escaped = $tok.Trim() -replace '\s+', '' -replace "'", "'\''"
                Run-Wsl "cd $Scripts && python3 aggiorna-token-facebook.py '$escaped'"
            }
            Read-Host "Invio"
        }
        "5" { Run-Wsl "cd /home/workbench/cryptoitaliafacile && python3 -m http.server 8080" }
        "6" {
            Run-Wsl "cd $Scripts && python3 regenerate-all-images.py"
            Read-Host "Invio"
        }
        "9" {
            Run-Wsl "cd $Scripts && bash avvio-automato-post.sh"
            Read-Host "Invio"
        }
        "0" { break }
    }
} while ($c -ne "0")
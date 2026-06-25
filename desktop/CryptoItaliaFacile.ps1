# CryptoItaliaFacile - Auto Post Launcher (desktop shortcut)
Set-Location "C:\Users\krown"
$Wsl = "C:\Windows\System32\wsl.exe"
$Distro = "NVIDIA-Workbench"
$Scripts = "/home/workbench/cryptoitaliafacile/scripts"
$Site = "/home/workbench/cryptoitaliafacile"

function Run-Wsl {
    param([string]$Command)
    & $Wsl -d $Distro bash -lc $Command
    return $LASTEXITCODE
}

function Test-Credentials {
    Write-Host ""
    Write-Host "  Credenziali API (scripts/.env)" -ForegroundColor DarkCyan
    Write-Host "  ----------------------------------------" -ForegroundColor DarkGray
    Run-Wsl "cd $Scripts; python3 verify-facebook-token.py 2>&1 | tail -5"
    Run-Wsl "cd $Scripts; python3 verify-instagram.py 2>&1 | tail -4"
    Write-Host "  ----------------------------------------" -ForegroundColor DarkGray
}

function Update-Token {
    Write-Host ""
    Write-Host "  Incolla il nuovo token Meta (EAA... o IG...)" -ForegroundColor Yellow
    $tok = Read-Host "  Token"
    $tok = $tok.Trim() -replace '\s+', ''
    if (-not $tok) {
        Write-Host "  Nessun token inserito." -ForegroundColor Red
        return
    }
    $cmd = "cd $Scripts; python3 aggiorna-token-facebook.py " + $tok
    Run-Wsl $cmd
    Read-Host "`nInvio per continuare"
}

function Show-Menu {
    Clear-Host
    Write-Host ""
    Write-Host "  ========================================" -ForegroundColor DarkYellow
    Write-Host "    CryptoItaliaFacile - Auto Post" -ForegroundColor Yellow
    Write-Host "  ========================================" -ForegroundColor DarkYellow
    Write-Host ""
    Write-Host "  IG @krown.82  |  FB The Little Satoshi News" -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "  [1] Pubblica ORA     (coda unificata IG+FB)" -ForegroundColor Green
    Write-Host "  [2] Test dry-run" -ForegroundColor Cyan
    Write-Host "  [3] Stato coda" -ForegroundColor Magenta
    Write-Host "  [4] Genera coda 14gg" -ForegroundColor White
    Write-Host "  [5] Verifica API" -ForegroundColor DarkCyan
    Write-Host "  [6] Aggiorna token" -ForegroundColor Yellow
    Write-Host "  [7] Reset circuit breaker" -ForegroundColor DarkYellow
    Write-Host "  [8] Avvia server :8080" -ForegroundColor Gray
    Write-Host "  [0] Esci" -ForegroundColor DarkGray
    Write-Host ""
}

Test-Credentials

do {
    Show-Menu
    $c = Read-Host "  Scegli"
    switch ($c) {
        "1" {
            Run-Wsl "cd $Scripts; python3 publish_orchestrator.py --auto --limit 2"
            Read-Host "`nInvio per continuare"
        }
        "2" {
            Run-Wsl "cd $Scripts; python3 publish_orchestrator.py --auto --dry-run --limit 2"
            Read-Host "`nInvio per continuare"
        }
        "3" {
            Run-Wsl "cd $Scripts; python3 publish_orchestrator.py --status"
            Read-Host "`nInvio per continuare"
        }
        "4" {
            Run-Wsl "cd $Scripts; python3 publish_orchestrator.py --generate --days 14"
            Read-Host "`nInvio per continuare"
        }
        "5" {
            Run-Wsl "cd $Scripts; python3 verify-facebook-token.py"
            Write-Host ""
            Run-Wsl "cd $Scripts; python3 verify-instagram.py"
            Read-Host "`nInvio per continuare"
        }
        "6" { Update-Token }
        "7" {
            Run-Wsl "cd $Scripts; python3 publish_orchestrator.py --reset-circuit"
            Read-Host "`nInvio per continuare"
        }
        "8" {
            Run-Wsl "cd $Site; python3 -m http.server 8080"
        }
        "0" { break }
        default { Start-Sleep -Seconds 1 }
    }
} while ($c -ne "0")
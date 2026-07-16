# 🚀 ONE-COMMAND DEPLOYMENT
# Run this in PowerShell to set up entire Engineering Division

Write-Host "`n╔═══════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                                                                   ║" -ForegroundColor Cyan
Write-Host "║            🤖 ENGINEERING DIVISION QUICK DEPLOY                   ║" -ForegroundColor Cyan
Write-Host "║                                                                   ║" -ForegroundColor Cyan
Write-Host "║  One command to rule them all                                    ║" -ForegroundColor Cyan
Write-Host "║  Time: 5 minutes | Cost: $0                                      ║" -ForegroundColor Cyan
Write-Host "║                                                                   ║" -ForegroundColor Cyan
Write-Host "╚═══════════════════════════════════════════════════════════════════╝`n" -ForegroundColor Cyan

# Navigate to MircoHydro
Set-Location C:\MircoHydro

# Activate venv
Write-Host "🐍 Activating Python environment..." -ForegroundColor Yellow
& .\.venv\Scripts\Activate.ps1

# Run deployment script
Write-Host "`n📦 Running automated deployment...`n" -ForegroundColor Yellow
python Engineering\deploy.py

# Check if .env needs editing
if (Test-Path "Engineering\.env") {
    Write-Host "`n⚠️  IMPORTANT: Edit Engineering\.env with your API keys!" -ForegroundColor Red
    Write-Host "Opening .env file in VS Code...`n" -ForegroundColor Yellow
    Start-Sleep -Seconds 2
    code Engineering\.env
}

# Open browser tabs for API keys
Write-Host "`n🔑 Opening API key registration pages..." -ForegroundColor Yellow
Start-Sleep -Seconds 1

Write-Host "  📖 Gemini (FREE 1500 req/day)..." -ForegroundColor Green
Start-Process "https://aistudio.google.com/app/apikey"
Start-Sleep -Seconds 2

Write-Host "  ⚡ Groq (FREE 14,400 req/day)..." -ForegroundColor Green
Start-Process "https://console.groq.com/keys"

Write-Host "`n✅ DEPLOYMENT COMPLETE!" -ForegroundColor Green
Write-Host "`n📋 NEXT:" -ForegroundColor Yellow
Write-Host "  1. Copy API keys from browser tabs" -ForegroundColor White
Write-Host "  2. Paste into .env file (now open)" -ForegroundColor White
Write-Host "  3. Save .env file" -ForegroundColor White
Write-Host "  4. Run: python Agents\chief_agent.py briefing" -ForegroundColor White
Write-Host "`n⏱️  Total time: 5 minutes" -ForegroundColor Cyan
Write-Host "💰 Total cost: $0" -ForegroundColor Cyan
Write-Host "🚀 Let's build!`n" -ForegroundColor Cyan

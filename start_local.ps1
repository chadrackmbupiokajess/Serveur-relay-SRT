# Script pour tester l'application localement (Windows)
# IMPORTANT: Nécessite ffmpeg installé sur votre système

Write-Host "🧪 Démarrage du serveur SRT Relay en mode local" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Vérifier que Python est installé
Write-Host "🔍 Vérification de Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python installé: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python n'est pas installé!" -ForegroundColor Red
    Write-Host "Téléchargez Python depuis: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

# Vérifier que ffmpeg est installé
Write-Host ""
Write-Host "🔍 Vérification de ffmpeg..." -ForegroundColor Yellow
try {
    $ffmpegVersion = ffmpeg -version 2>&1 | Select-Object -First 1
    Write-Host "✅ ffmpeg installé: $ffmpegVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ ffmpeg n'est pas installé!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Installation de ffmpeg:" -ForegroundColor Yellow
    Write-Host "1. Avec Chocolatey: choco install ffmpeg" -ForegroundColor White
    Write-Host "2. Ou téléchargez depuis: https://ffmpeg.org/download.html" -ForegroundColor White
    Write-Host ""
    exit 1
}

# Créer l'environnement virtuel si nécessaire
Write-Host ""
Write-Host "📦 Configuration de l'environnement Python..." -ForegroundColor Yellow

if (-not (Test-Path "venv")) {
    Write-Host "Création de l'environnement virtuel..." -ForegroundColor Cyan
    python -m venv venv
}

# Activer l'environnement virtuel
Write-Host "Activation de l'environnement virtuel..." -ForegroundColor Cyan
& ".\venv\Scripts\Activate.ps1"

# Installer les dépendances
Write-Host ""
Write-Host "📥 Installation des dépendances..." -ForegroundColor Yellow
pip install -q -r requirements.txt

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Échec de l'installation des dépendances" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Dépendances installées" -ForegroundColor Green

# Démarrer l'application
Write-Host ""
Write-Host "=========================================" -ForegroundColor Green
Write-Host "🚀 DÉMARRAGE DU SERVEUR LOCAL" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Green
Write-Host ""
Write-Host "🌐 Interface web : http://localhost:8080" -ForegroundColor Cyan
Write-Host "📡 Port SRT      : 9000" -ForegroundColor Cyan
Write-Host ""
Write-Host "⚠️  MODE LOCAL:" -ForegroundColor Yellow
Write-Host "   - OBS URL    : srt://localhost:9000?streamid=publish/live" -ForegroundColor White
Write-Host "   - vMix URL   : srt://localhost:9000?streamid=play/live" -ForegroundColor White
Write-Host ""
Write-Host "Appuyez sur Ctrl+C pour arrêter le serveur" -ForegroundColor Gray
Write-Host ""

# Définir les variables d'environnement
$env:PORT = "8080"
$env:SRT_PORT = "9000"
$env:FLY_APP_NAME = "localhost"

# Lancer l'application
python app.py

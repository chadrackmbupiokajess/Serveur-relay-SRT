# SWEEP.md - Configuration et commandes du projet

## 📁 Structure du projet

```
OBS_VMIX/
├── app.py              # Serveur relay SRT + interface web Flask
├── requirements.txt    # Dépendances Python
├── Dockerfile         # Configuration Docker pour Fly.io
├── fly.toml           # Configuration Fly.io
├── README.md          # Documentation complète
├── GUIDE_RAPIDE.md    # Guide de démarrage rapide
└── .gitignore         # Fichiers à ignorer par Git
```

## 🚀 Commandes principales

### Déploiement sur Railway

```powershell
# Pousser les modifications sur GitHub
git add .
git commit -m "Description des changements"
git push

# Railway redéploie automatiquement !
```

### Git / GitHub

```powershell
# Premier push
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/VOTRE-USERNAME/mon-relay-srt.git
git push -u origin main

# Mises à jour
git add .
git commit -m "Mise à jour"
git push
```

### Test local (optionnel)

```powershell
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement
.\venv\Scripts\Activate.ps1

# Installer les dépendances
pip install -r requirements.txt

# Lancer localement (nécessite ffmpeg installé)
python app.py
```

## 🏗️ Architecture technique

### Protocole
- **SRT (Secure Reliable Transport)** sur port UDP 9000
- Interface web HTTP sur port 8080

### Stack
- **Backend** : Python 3.11 + Flask
- **Relay** : FFmpeg avec support SRT
- **Hébergement** : Fly.io (Docker container)
- **Frontend** : HTML/CSS/JavaScript (template Flask)

### Flux de données

```
OBS (Site A)
    ↓ SRT Publish (port 9000)
Fly.io Relay Server (RAM uniquement)
    ↓ SRT Play (port 9000)
vMix (Site B)
```

## 🔧 Configuration

### URLs SRT
- **OBS (publish)** : `srt://votre-app.fly.dev:9000?streamid=publish/live`
- **vMix (play)** : `srt://votre-app.fly.dev:9000?streamid=play/live`

### Variables d'environnement (fly.toml)
- `PORT=8080` - Port interface web
- `SRT_PORT=9000` - Port SRT
- `FLY_APP_NAME` - Nom de l'application (auto-généré)

### Régions Fly.io recommandées pour RDC 🇨🇩
- `jnb` - Johannesburg (Afrique du Sud) ⭐ OPTIMAL
- `cdg` - Paris (France) - Bon choix francophone
- `ams` - Amsterdam (Pays-Bas)
- `lhr` - Londres (Royaume-Uni)

## 📝 Notes de style de code

- **Français** pour les commentaires et messages utilisateur
- **Anglais** pour les noms de variables/fonctions
- **PEP 8** pour le style Python
- **Logging** avec module `logging` (pas de prints)

## 🔒 Sécurité

- Aucun stockage sur disque (relay en RAM uniquement)
- Pas de logs du contenu vidéo
- SRT avec correction d'erreurs intégrée
- HTTPS forcé pour l'interface web

## 💰 Limites Fly.io gratuit

- 160 GB de transfert/mois
- 1 machine virtuelle
- 256 MB RAM
- Pas de mise en veille (toujours actif)

## 🎯 Usage typique

1. Déployer une fois sur Fly.io
2. Configurer OBS avec l'URL publish
3. Configurer vMix avec l'URL play
4. OBS démarre le stream → vMix reçoit automatiquement
5. Monitoring via interface web
tif)

## 🎯 Usage typique

1. Déployer une fois sur Fly.io
2. Configurer OBS avec l'URL publish
3. Configurer vMix avec l'URL play
4. OBS démarre le stream → vMix reçoit automatiquement
5. Monitoring via interface web

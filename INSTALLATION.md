# 🎯 INSTALLATION - Étape par étape

## ✅ CE QUI A ÉTÉ CRÉÉ

Votre projet contient maintenant :

```
OBS_VMIX/
├── app.py                 # ✅ Serveur relay SRT + interface web
├── requirements.txt       # ✅ Dépendances Python (Flask)
├── Dockerfile            # ✅ Configuration Docker
├── fly.toml              # ✅ Configuration Fly.io
├── deploy.ps1            # ✅ Script déploiement automatique
├── start_local.ps1       # ✅ Test local (optionnel)
├── config_generator.py   # ✅ Générateur URLs OBS/vMix
├── README.md             # ✅ Documentation complète
├── GUIDE_RAPIDE.md       # ✅ Guide rapide
└── .gitignore            # ✅ Configuration Git
```

---

## 🚀 DÉPLOIEMENT EN 3 ÉTAPES

### ✨ MÉTHODE AUTOMATIQUE (RECOMMANDÉE)

**1️⃣ Ouvrez PowerShell dans ce dossier**
```powershell
cd "C:\Users\chadr\Videos\Projet\OBS_VMIX"
```

**2️⃣ Lancez le script de déploiement**
```powershell
.\deploy.ps1
```

**3️⃣ Suivez les instructions à l'écran**
- Le script vérifie tout automatiquement
- Installe flyctl si nécessaire
- Vous connecte à Fly.io
- Déploie l'application
- Ouvre l'interface web

**C'est tout ! 🎉**

---

### 🔧 MÉTHODE MANUELLE

Si vous préférez le faire manuellement :

**1. Installer Fly.io CLI**
```powershell
iwr https://fly.io/install.ps1 -useb | iex
```
Redémarrez PowerShell après.

**2. Se connecter**
```powershell
flyctl auth login
```

**3. Déployer**
```powershell
cd "C:\Users\chadr\Videos\Projet\OBS_VMIX"
flyctl launch
```

Répondez aux questions :
- App name : (Entrée pour auto)
- Region : `jnb` (Johannesburg - optimal pour RDC 🇨🇩) ou `cdg` (Paris)
- PostgreSQL : `n`
- Redis : `n`
- Deploy now : `y`

---

## 🎥 CONFIGURATION OBS/vMix

### Option 1 : Via l'interface web (facile)

Après le déploiement, ouvrez l'URL de votre app :
```
https://votre-app.fly.dev
```

➡️ Copiez les URLs directement depuis la page web !

### Option 2 : Générateur de config (ligne de commande)

```powershell
python config_generator.py votre-app.fly.dev
```

Cela générera un fichier `config_urls.txt` avec toutes les infos.

---

## ✅ VÉRIFICATION

**Après le déploiement, vérifiez :**

```powershell
# Voir le statut
flyctl status

# Voir les logs
flyctl logs

# Ouvrir l'interface web
flyctl open
```

L'interface web doit afficher :
- ✅ "Serveur actif"
- ✅ URLs de configuration OBS
- ✅ URLs de configuration vMix

---

## 🧪 TEST LOCAL (Optionnel)

Pour tester en local AVANT de déployer :

```powershell
.\start_local.ps1
```

**Note :** Nécessite ffmpeg installé sur votre PC.

---

## 🎬 UTILISATION

### Workflow complet :

**1. OBS (Site A) :**
- Ouvrir OBS Studio
- Paramètres → Diffusion
- Service : Personnalisé
- Serveur : (URL depuis l'interface web)
- Clé : (vide)
- Démarrer la diffusion

**2. vMix (Site B) :**
- Add Input → Stream/SRT
- URL : (URL depuis l'interface web)
- OK
- Le flux apparaît automatiquement !

**3. Monitoring :**
- Ouvrez `https://votre-app.fly.dev`
- Voyez le statut en temps réel

---

## 🆘 PROBLÈMES COURANTS

### Le déploiement échoue ?

```powershell
# Vérifier l'authentification
flyctl auth whoami

# Se reconnecter si nécessaire
flyctl auth login

# Réessayer le déploiement
flyctl deploy
```

### Le stream ne fonctionne pas ?

1. **Vérifiez que le serveur est actif :**
   ```powershell
   flyctl status
   ```

2. **Regardez les logs :**
   ```powershell
   flyctl logs
   ```

3. **OBS doit diffuser AVANT vMix**
   - Lancez OBS d'abord
   - Puis vMix se connecte

### Erreur de région ?

Changez la région dans `fly.toml` ligne 3 :
```toml
primary_region = "jnb"  # Johannesburg - optimal pour RDC
```

Régions disponibles pour la RDC 🇨🇩 :
- `jnb` - Johannesburg 🇿🇦 ⭐ **MEILLEUR** (Afrique)
- `cdg` - Paris 🇫🇷 ✅ Bon (francophone)
- `ams` - Amsterdam 🇳🇱 ✅ Bon
- `lhr` - Londres 🇬🇧 ⚠️ Plus loin

Puis redéployez :
```powershell
flyctl deploy
```

---

## 📊 COMMANDES UTILES

```powershell
# Statut de l'application
flyctl status

# Logs en temps réel
flyctl logs

# Redémarrer l'application
flyctl apps restart

# Ouvrir l'interface web
flyctl open

# Informations de l'application
flyctl info

# Liste de toutes vos apps
flyctl apps list

# Supprimer l'application
flyctl apps destroy nom-app
```

---

## 🔒 SÉCURITÉ

### Rappel important :
- ✅ **Aucun enregistrement** du flux vidéo
- ✅ Tout passe en **mémoire RAM uniquement**
- ✅ Aucun fichier créé sur le disque
- ✅ Quand le stream s'arrête → tout disparaît

Le serveur est un **relay pur** (relais transparent).

---

## 💰 COÛTS

**Fly.io gratuit :**
- ✅ 160 GB transfert/mois
- ✅ 1 machine virtuelle
- ✅ ~50-80 heures de stream HD/mois

**Largement suffisant pour un usage normal !**

Si vous dépassez, Fly.io vous notifiera. Pas de frais surprise.

---

## 📚 RESSOURCES

- **Documentation complète** : `README.md`
- **Guide rapide** : `GUIDE_RAPIDE.md`
- **Commandes projet** : `SWEEP.md`
- **Aide Fly.io** : https://fly.io/docs/

---

## 🎉 C'EST PRÊT !

Votre système de relay SRT est maintenant configuré et prêt à l'emploi !

**Prochaine étape :**
```powershell
.\deploy.ps1
```

**Bon streaming ! 🎬🚀**

# 🚀 DÉPLOYER VOTRE APPLICATION RELAY SRT

**Votre propre serveur relay - Indépendant et sous votre contrôle**

---

## 🎯 CE QUE VOUS ALLEZ AVOIR

```
Site A (OBS)  ──→  VOTRE Serveur Relay  ──→  Site B (vMix)
                   (100% vous, 100% contrôle)
```

**Caractéristiques :**
- ✅ Votre propre application (pas Tailscale, pas de dépendance)
- ✅ Interface web personnalisée
- ✅ URLs de configuration automatiques
- ✅ Monitoring en temps réel
- ✅ Code modifiable à volonté

---

## 📋 SOLUTION : RAILWAY (Recommandé pour RDC)

**Pourquoi Railway ?**
- ✅ $5 crédit gratuit/mois (~500h streaming)
- ✅ Fonctionne depuis la RDC
- ✅ Support SRT/UDP complet
- ✅ Déploiement ultra-simple depuis GitHub
- ✅ Pas de carte requise au début

---

## 🚀 ÉTAPE 1 : Préparer le code sur GitHub

### 1.1 Créer un compte GitHub (si pas déjà fait)

1. Allez sur https://github.com/signup
2. Créez un compte (gratuit)
3. Validez votre email

---

### 1.2 Créer un nouveau repository

1. Sur GitHub, cliquez **"New repository"** (bouton vert)
2. Nom : `mon-relay-srt`
3. Description : `Mon serveur relay SRT pour OBS vers vMix`
4. Sélectionnez **"Public"**
5. **NE cochez PAS** "Add a README"
6. Cliquez **"Create repository"**

---

### 1.3 Pousser votre code sur GitHub

**Ouvrez PowerShell dans votre dossier :**

```powershell
cd "C:\Users\chadr\Videos\Projet\OBS_VMIX"
```

**Configurez Git (si première fois) :**

```powershell
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"
```

**Initialisez et poussez :**

```powershell
# Initialiser Git
git init

# Ajouter tous les fichiers
git add app.py requirements.txt Dockerfile .dockerignore

# Premier commit
git commit -m "Mon serveur relay SRT"

# Connecter à GitHub (remplacez VOTRE-USERNAME)
git remote add origin https://github.com/VOTRE-USERNAME/mon-relay-srt.git
git branch -M main
git push -u origin main
```

**Entrez vos identifiants GitHub quand demandé.**

---

## 🚂 ÉTAPE 2 : Déployer sur Railway

### 2.1 Créer un compte Railway

1. Allez sur https://railway.app/
2. Cliquez **"Login"** ou **"Start a New Project"**
3. Connectez-vous avec **GitHub** (le plus simple)
4. Autorisez Railway à accéder à vos repos

---

### 2.2 Créer un nouveau projet

1. Dans Railway, cliquez **"New Project"**
2. Sélectionnez **"Deploy from GitHub repo"**
3. Cherchez votre repository : `mon-relay-srt`
4. Cliquez dessus pour le sélectionner

---

### 2.3 Configurer le déploiement

Railway va détecter automatiquement le `Dockerfile`.

**Ajoutez les variables d'environnement :**

1. Cliquez sur votre service déployé
2. Allez dans l'onglet **"Variables"**
3. Ajoutez :

| Variable | Valeur |
|----------|--------|
| `PORT` | `8080` |
| `SRT_PORT` | `9000` |

4. Cliquez **"Add"**

---

### 2.4 Configurer le domaine public

**Railway va générer une URL publique :**

1. Dans votre service, allez dans **"Settings"**
2. Section **"Networking"**
3. Cliquez **"Generate Domain"**
4. Vous aurez une URL comme : `mon-relay-srt.up.railway.app`

**Notez cette URL ! C'est votre serveur ! 🎉**

---

### 2.5 Déployer

Railway déploie automatiquement !

⏳ **Attendez 3-5 minutes...**

Une fois terminé, vous verrez **"Success"** en vert.

---

## 🌐 ÉTAPE 3 : Accéder à votre application

**Ouvrez votre navigateur et allez sur :**

```
https://mon-relay-srt.up.railway.app
```

**Vous devriez voir votre interface web ! 🎉**

Avec :
- ✅ Statut du serveur
- ✅ URL pour OBS
- ✅ URL pour vMix
- ✅ Instructions de configuration

---

## 🎥 ÉTAPE 4 : Configurer OBS et vMix

### Configuration OBS (Site A)

**Dans l'interface web, copiez l'URL OBS.**

**Dans OBS Studio :**
1. Paramètres → Diffusion
2. Service : **Personnalisé**
3. Serveur : `srt://mon-relay-srt.up.railway.app:9000?streamid=publish/live`
4. Clé : **(vide)**
5. OK

---

### Configuration vMix (Site B)

**Dans l'interface web, copiez l'URL vMix.**

**Dans vMix :**
1. Add Input → Stream / SRT
2. URL : `srt://mon-relay-srt.up.railway.app:9000?streamid=play/live`
3. OK

---

## ✅ ÉTAPE 5 : Tester

1. **OBS** : Cliquez "Démarrer la diffusion"
2. **vMix** : Le flux devrait apparaître automatiquement ! 🎬

---

## 🔄 METTRE À JOUR VOTRE APPLICATION

**Si vous modifiez le code :**

```powershell
cd "C:\Users\chadr\Videos\Projet\OBS_VMIX"

# Après modifications
git add .
git commit -m "Description de vos changements"
git push
```

**Railway redéploie automatiquement ! 🚀**

---

## 💰 COÛTS RAILWAY

**Plan gratuit :**
- ✅ $5 crédit/mois
- ✅ ~500 heures de streaming
- ✅ Largement suffisant !

**Si vous dépassez :**
- Vous pouvez ajouter une carte (vous ne payez que ce que vous utilisez)
- Ou attendre le mois suivant (crédit se renouvelle)

---

## 📊 MONITORING

### Voir les logs

**Dans Railway :**
1. Cliquez sur votre service
2. Onglet **"Logs"**
3. Vous voyez tout en temps réel !

---

### Vérifier l'utilisation

**Onglet "Metrics" :**
- CPU
- RAM
- Réseau
- Temps d'utilisation

---

## ⚙️ PERSONNALISER VOTRE APPLICATION

**Vous pouvez modifier `app.py` pour :**
- ✅ Changer l'interface web
- ✅ Ajouter des fonctionnalités
- ✅ Changer les ports
- ✅ Ajouter de l'authentification
- ✅ Logger les statistiques

**C'est VOTRE application ! Faites ce que vous voulez ! 😊**

---

## 🆘 DÉPANNAGE

### Le déploiement échoue ?

**Vérifiez les logs dans Railway.**

**Erreurs communes :**
- Dockerfile mal formaté
- requirements.txt manquant
- Port incorrect

---

### Le stream ne fonctionne pas ?

1. **Vérifiez que le service est actif** (Railway)
2. **Testez l'interface web** (https://votre-url.railway.app)
3. **Vérifiez les URLs dans OBS/vMix**
4. **Regardez les logs Railway**

---

## 🎯 RÉSUMÉ

**Votre système complet :**

```
1. Code sur GitHub (votre repository)
2. Déployé sur Railway (votre serveur)
3. Interface web accessible (votre URL)
4. OBS et vMix configurés
5. 100% VOUS, 0% dépendance externe
```

**Vous contrôlez tout ! 🎉**

---

## 📞 PROCHAINES ÉTAPES

1. ✅ Créer compte GitHub
2. ✅ Pousser le code
3. ✅ Créer compte Railway
4. ✅ Déployer
5. ✅ Configurer OBS/vMix
6. ✅ Streamer !

**Temps total : 15-20 minutes**

---

## 💡 ALTERNATIVES À RAILWAY

**Si Railway ne fonctionne pas depuis la RDC :**

### Contabo VPS (4€/mois)
- VPS complet sous votre contrôle
- Je peux vous guider pour l'installation

### DigitalOcean (6$/mois)
- Datacenter proche de l'Afrique
- Interface simple

### Hostinger VPS (5€/mois)
- Accepte paiement RDC
- Support francophone

**Dites-moi si vous voulez un guide pour une autre plateforme !**

---

**Commençons ! Dites-moi quand vous avez créé votre compte GitHub ! 🚀**

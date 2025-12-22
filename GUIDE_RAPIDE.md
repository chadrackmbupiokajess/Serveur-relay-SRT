# ⚡ GUIDE RAPIDE - Démarrage en 10 minutes

## 🎯 OBJECTIF
Faire fonctionner le streaming OBS → vMix via Internet RAPIDEMENT.

---

## ✅ CHECKLIST AVANT DE COMMENCER

- [ ] J'ai un compte Fly.io (gratuit) → [S'inscrire](https://fly.io/app/sign-up)
- [ ] J'ai Git installé → [Télécharger](https://git-scm.com/download/win)
- [ ] J'ai OBS Studio (Site A)
- [ ] J'ai vMix (Site B)

---

## 🚀 INSTALLATION (5 commandes seulement)

### 1️⃣ Installer Fly.io CLI

**PowerShell (Admin) :**
```powershell
iwr https://fly.io/install.ps1 -useb | iex
```

**Fermez et rouvrez PowerShell**

---

### 2️⃣ Se connecter

```powershell
flyctl auth login
```
→ Connectez-vous dans le navigateur

---

### 3️⃣ Aller dans le dossier

```powershell
cd "C:\Users\chadr\Videos\Projet\OBS_VMIX"
```

---

### 4️⃣ Déployer

```powershell
flyctl launch
```

**Réponses :**
- Nom : (Entrée pour auto)
- Région : `jnb` (Johannesburg 🇿🇦 - optimal pour RDC 🇨🇩)
- PostgreSQL : `n`
- Redis : `n`
- Deploy : `y`

⏳ Attendez 2-3 minutes...

---

### 5️⃣ Obtenir votre URL

```powershell
flyctl status
```

Notez votre URL : `https://votre-app.fly.dev`

---

## 🎥 CONFIGURER OBS (1 minute)

1. **Ouvrez `https://votre-app.fly.dev`**
2. **Copiez l'URL OBS** (bouton Copier)
3. **OBS** → Paramètres → Diffusion
   - Service : `Personnalisé`
   - Serveur : (Collez l'URL)
   - Clé : (vide)
4. **Démarrer la diffusion** ✅

---

## 📺 CONFIGURER vMix (30 secondes)

1. **Sur la même page web, copiez l'URL vMix**
2. **vMix** → Add Input → Stream/SRT
3. **Collez l'URL** → OK
4. **Le flux apparaît !** 🎉

---

## ✨ C'EST TOUT !

Votre système est opérationnel ! 🚀

### Commandes utiles :

**Voir les logs :**
```powershell
flyctl logs
```

**Redémarrer :**
```powershell
flyctl apps restart
```

**Ouvrir l'interface :**
```powershell
flyctl open
```

---

## 🆘 Problème ?

1. **Vérifiez que OBS diffuse** avant de lancer vMix
2. **Regardez les logs :** `flyctl logs`
3. **Redémarrez :** `flyctl apps restart`

---

**Bon streaming ! 🎬**

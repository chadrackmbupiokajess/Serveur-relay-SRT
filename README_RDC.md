# 🇨🇩 GUIDE SPÉCIAL RDC - Optimisations pour la République Démocratique du Congo

## 🌍 Configuration optimale pour la RDC

Votre projet est maintenant **optimisé pour la RDC** !

### ✅ Ce qui a été configuré automatiquement

- **Région serveur** : Johannesburg (Afrique du Sud) 🇿🇦
- **Distance** : ~2000 km (contre ~6000 km pour Paris)
- **Latence estimée** : 30-80ms (contre 150-250ms pour l'Europe)

---

## 🚀 Recommandations pour la RDC

### 📡 Connexion Internet

**Pour un streaming fluide, vous avez besoin de :**

| Qualité | Bitrate OBS | Upload min requis | Résolution |
|---------|-------------|-------------------|------------|
| **Basse** | 1500 kbps | 2 Mbps | 720p |
| **Moyenne** | 2500 kbps | 3.5 Mbps | 720p/1080p |
| **Haute** | 4000 kbps | 5.5 Mbps | 1080p |
| **Très haute** | 6000 kbps | 8 Mbps | 1080p |

**⚠️ IMPORTANT :** Testez votre connexion sur les deux sites :
- Site A (OBS) : Besoin d'upload stable
- Site B (vMix) : Besoin de download stable

**Test de vitesse recommandé :**
- Speedtest.net
- Fast.com
- nPerf.com

---

## ⚙️ Configuration OBS optimale pour la RDC

### Paramètres recommandés

**1. Paramètres de sortie (Output) :**
```
Sortie → Streaming
- Encodeur vidéo : x264
- Contrôle du débit : CBR (Constant Bitrate)
- Débit : 2500 kbps (ajustez selon votre connexion)
- Intervalle d'image-clé : 2
- Preset CPU : veryfast (ou faster si CPU faible)
```

**2. Paramètres vidéo :**
```
Vidéo
- Résolution de base : 1920x1080 (votre source)
- Résolution de sortie : 1280x720 (recommandé pour RDC)
- FPS : 25 ou 30
- Filtre d'échelle : Bicubique
```

**3. Paramètres audio :**
```
Audio
- Débit audio : 128 kbps (Bitrate)
- Fréquence d'échantillonnage : 44.1 kHz ou 48 kHz
```

### 🎯 Ajustements selon votre connexion

**Si vous avez une connexion instable :**
- Réduisez le bitrate à 1500-2000 kbps
- Passez en 720p (1280x720)
- Utilisez preset "ultrafast"
- Réduisez les FPS à 25

**Si vous avez une bonne connexion (5+ Mbps upload) :**
- Bitrate 3500-4000 kbps
- 1080p possible
- Preset "fast" ou "medium"
- 30 FPS

---

## 🌐 Fournisseurs Internet RDC

### Optimisations par opérateur

**Vodacom 🇨🇩**
- Généralement stable pour streaming
- Privilégiez heures creuses (6h-9h, 14h-17h)
- 4G+ recommandé si disponible

**Orange RDC 🇨🇩**
- Bonne couverture urbaine
- Testez en heures creuses d'abord

**Airtel RDC 🇨🇩**
- Variable selon les zones
- Commencez avec bitrate conservateur (2000 kbps)

**Connexion par satellite**
- Latence plus élevée (200-600ms)
- Réduisez le bitrate (1500-2000 kbps)
- 720p maximum recommandé

---

## 🔧 Test et validation

### Avant de streamer en production

**1. Test de connexion (5 min) :**
```powershell
# Après déploiement, testez avec OBS
# Commencez par un bitrate de 2000 kbps
# Observez les indicateurs OBS :
# - Vert = Excellent
# - Jaune = Acceptable
# - Rouge = Réduisez le bitrate
```

**2. Test progressif :**
- Jour 1 : Test 5 minutes à 1500 kbps
- Jour 2 : Test 10 minutes à 2000 kbps
- Jour 3 : Test 15 minutes à 2500 kbps
- Augmentez progressivement selon stabilité

**3. Vérification vMix :**
- Le flux doit être fluide sans saccades
- Pas de buffering visible
- Qualité d'image acceptable

---

## ⚡ Optimisations réseau RDC

### Améliorez votre streaming

**1. Connexion câblée (Ethernet) :**
- ✅ TOUJOURS préférable au WiFi
- Câble CAT5e ou CAT6 recommandé
- Évitez les adaptateurs WiFi-USB si possible

**2. Priorité réseau (QoS) :**
- Configurez votre routeur pour prioriser OBS
- Fermez autres applications gourmandes :
  - Téléchargements
  - Updates Windows
  - Cloud sync (OneDrive, Dropbox, etc.)

**3. Heures optimales :**
- **Meilleur** : 6h-9h, 14h-17h (heures creuses)
- **Bon** : 10h-12h
- **À éviter** : 18h-22h (heures de pointe)

**4. Coupures électriques (délestage) :**
- ✅ UPS/Onduleur OBLIGATOIRE
- Minimum 1000VA recommandé
- Protège contre coupures courtes
- Plan B : Générateur si streaming critique

---

## 🌍 Régions Fly.io pour RDC

**Ordre de préférence :**

1. **`jnb` - Johannesburg 🇿🇦** ⭐ **DÉJÀ CONFIGURÉ**
   - Distance : ~2000 km
   - Latence : 30-80ms
   - **OPTIMAL pour RDC**

2. **`cdg` - Paris 🇫🇷**
   - Distance : ~6000 km
   - Latence : 150-250ms
   - Bon si problème avec jnb

3. **`ams` - Amsterdam 🇳🇱**
   - Distance : ~6500 km
   - Latence : 150-250ms
   - Alternative européenne

---

## 💡 Astuces spécifiques RDC

### Gestion de la bande passante

**Économisez la bande passante :**
- Utilisez 720p au lieu de 1080p (économie 40%)
- 25 FPS au lieu de 30 (économie 15%)
- Bitrate audio 96 kbps au lieu de 128 (si acceptable)

**Bundle data mobile :**
- Calculez la consommation : `Bitrate × Durée`
- Ex: 2500 kbps × 1 heure = ~1.1 GB
- Prévoyez 20% de marge (overhead)

### Solutions de secours

**Si connexion principale échoue :**
1. **4G/5G de secours** (smartphone hotspot)
2. **Cyber café** avec bonne connexion
3. **Coworking space** avec Internet stable
4. **Hôtels** avec connexion professionnelle

---

## 📊 Monitoring et diagnostics

### Indicateurs à surveiller (OBS)

**Pendant le streaming :**
- **🟢 Vert** : Connexion excellente (0-5% dropped frames)
- **🟡 Jaune** : Connexion acceptable (5-10% dropped frames)
- **🔴 Rouge** : Problème (>10% dropped frames)

**Actions correctives :**
- Dropped frames > 5% → Réduisez bitrate de 500 kbps
- Dropped frames > 15% → Réduisez bitrate de 1000 kbps + résolution

### Commandes de diagnostic

```powershell
# Voir les logs du serveur
flyctl logs

# Vérifier le statut
flyctl status

# Tester la latence vers Johannesburg
ping jnb.fly.dev
```

---

## 🔒 Considérations légales RDC

### Conformité

- ✅ Pas d'enregistrement (conforme RGPD africain)
- ✅ Données en transit uniquement
- ✅ Serveur basé en Afrique du Sud (juridiction stable)

### Recommandations

- Informez vos utilisateurs du relay
- Pas de contenu illégal ou protégé
- Respectez les lois RDC sur la diffusion

---

## 💰 Coûts et budget

### Fly.io gratuit

**160 GB/mois gratuit = environ :**
- 2500 kbps → ~55 heures/mois
- 2000 kbps → ~70 heures/mois
- 1500 kbps → ~90 heures/mois

**Largement suffisant pour :**
- ✅ Événements hebdomadaires
- ✅ Streaming régulier (2-3h/jour)
- ✅ Tests et production

**Si vous dépassez :**
- Fly.io vous notifie
- Pas de frais surprise
- Upgrade optionnel (~5-10$/mois)

---

## 🆘 Support local RDC

### Communautés tech RDC

- **Facebook** : Groupes "Développeurs RDC"
- **WhatsApp** : Groupes tech Kinshasa/Lubumbashi
- **Discord** : Communautés tech africaines

### Assistance technique

**Problèmes de connexion :**
1. Contactez votre FAI
2. Testez à différentes heures
3. Envisagez changement FAI si persistant

**Problèmes techniques :**
1. Vérifiez `README.md`
2. Consultez logs : `flyctl logs`
3. Redémarrez : `flyctl apps restart`

---

## ✅ Checklist avant streaming RDC

**Avant CHAQUE session :**

- [ ] Connexion Internet stable testée
- [ ] UPS/Onduleur chargé et connecté
- [ ] OBS configuré (bitrate adapté)
- [ ] Test 5 min avec vMix avant production
- [ ] Heure optimale (éviter 18h-22h)
- [ ] Applications gourmandes fermées
- [ ] Câble Ethernet connecté (pas WiFi)
- [ ] Serveur Fly.io actif (flyctl status)

---

## 🎯 Résumé RDC

**Votre configuration optimale :**

✅ Serveur : Johannesburg (jnb)
✅ Bitrate recommandé : 2000-2500 kbps
✅ Résolution : 720p (1280x720)
✅ FPS : 25-30
✅ Upload minimum : 3.5 Mbps
✅ Connexion : Câble Ethernet
✅ Protection : UPS/Onduleur

---

**Bon streaming depuis la RDC ! 🇨🇩🎬🚀**

---

## 📞 Questions ?

Consultez :
- `README.md` - Documentation complète
- `GUIDE_RAPIDE.md` - Démarrage rapide
- `INSTALLATION.md` - Installation détaillée

Ou ouvrez l'interface web après déploiement pour configuration automatique !

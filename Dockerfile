# Dockerfile pour SRT Video Relay Server
FROM python:3.11-slim

# Installation des outils SRT (qui incluent srt-live-transmit)
RUN apt-get update && apt-get install -y \
    srt-tools \
    && rm -rf /var/lib/apt/lists/*

# Créer le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Variables d'environnement par défaut
# Railway fournira le port HTTP via la variable $PORT
ENV SRT_PORT=9000

# Démarrer l'application
# Railway utilise la variable PORT pour le service web
CMD python app.py

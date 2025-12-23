# Dockerfile pour SRT Video Relay Server
FROM python:3.11-slim

# Installation de srt-live-transmit et ffmpeg
RUN apt-get update && apt-get install -y \
    ffmpeg \
    srt-tools \
    && rm -rf /var/lib/apt/lists/*

# Créer le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Exposer les ports
# Port 8080 pour l'interface web
EXPOSE 8080
# Port 9000 pour SRT (OBS)
EXPOSE 9000/udp
# Port 9001 pour SRT (vMix)
EXPOSE 9001/udp

# Variables d'environnement par défaut
ENV PORT=8080
ENV SRT_PORT=9000

# Démarrer l'application
CMD ["python", "app.py"]

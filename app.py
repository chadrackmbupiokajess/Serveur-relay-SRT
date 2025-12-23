"""
SRT Video Relay Server - Relais vidéo SRT entre OBS et vMix
Aucun enregistrement - Relay pur en mémoire RAM uniquement
"""

from flask import Flask, render_template_string, jsonify, request
import subprocess
import threading
import os
import time
from datetime import datetime
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
SRT_PORT = int(os.environ.get('SRT_PORT', '9000'))
HTTP_PORT = int(os.environ.get('PORT', '8080'))

# État du serveur
server_state = {
    'srt_process': None,
    'is_running': False,
    'start_time': None,
    'obs_connected': False,
    'vmix_connected': False,
    'obs_connection_time': None,
    'vmix_connection_time': None,
    'stats': {
        'total_bytes': 0,
        'current_bitrate': '0 kbits/s',
        'dropped_packets': 0
    }
}


def start_srt_relay():
    """Démarre le serveur relay SRT avec ffmpeg - Version corrigée"""
    global server_state

    try:
        logger.info(f"🚀 Démarrage du relay SRT sur le port {SRT_PORT}")

        # Commande ffmpeg CORRIGÉE pour relay SRT
        # OBS se connecte en mode caller, on écoute et on republie
        cmd = [
            'ffmpeg',
            '-loglevel', 'info',
            # Input: Écoute les connexions SRT entrantes (OBS)
            '-i', f'srt://0.0.0.0:{SRT_PORT}?mode=listener',
            # Output: Republie le flux pour vMix (mode listener aussi)
            '-c', 'copy',  # Copie sans réencodage (relay pur)
            '-f', 'mpegts',
            f'srt://0.0.0.0:{SRT_PORT + 1}?mode=listener'  # Port différent pour éviter conflit
        ]

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )

        server_state['srt_process'] = process
        server_state['is_running'] = True
        server_state['start_time'] = datetime.now()

        logger.info("✅ Relay SRT démarré avec succès")
        logger.info(f"📥 OBS: Connectez-vous sur port {SRT_PORT}")
        logger.info(f"📺 vMix: Connectez-vous sur port {SRT_PORT + 1}")

        # Thread pour lire les logs ffmpeg
        threading.Thread(target=monitor_ffmpeg_output, args=(process,), daemon=True).start()

    except Exception as e:
        logger.error(f"❌ Erreur démarrage SRT relay: {e}")
        server_state['is_running'] = False


def monitor_ffmpeg_output(process):
    """Monitore la sortie de ffmpeg pour extraire les stats et détecter connexions"""
    global server_state

    for line in iter(process.stderr.readline, ''):
        if not line:
            break

        line_lower = line.lower()

        # Détection connexion OBS
        if 'srt' in line_lower and 'accepted' in line_lower:
            logger.info("📥 OBS connecté!")
            server_state['obs_connected'] = True
            server_state['obs_connection_time'] = datetime.now()

        # Détection connexion vMix
        if 'output' in line_lower and 'srt' in line_lower:
            logger.info("📺 vMix connecté!")
            server_state['vmix_connected'] = True
            server_state['vmix_connection_time'] = datetime.now()

        # Log pour debug
        if 'bitrate=' in line_lower or 'speed=' in line_lower:
            logger.debug(f"FFmpeg: {line.strip()}")

        # Extraction stats
        if 'bitrate=' in line:
            try:
                parts = line.split('bitrate=')
                if len(parts) > 1:
                    bitrate_str = parts[1].split()[0]
                    server_state['stats']['current_bitrate'] = bitrate_str
            except:
                pass

        # Détection déconnexion
        if 'connection closed' in line_lower or 'end of file' in line_lower:
            logger.warning("⚠️ Déconnexion détectée")
            server_state['obs_connected'] = False
            server_state['vmix_connected'] = False

    logger.warning("⚠️ Processus ffmpeg terminé")
    server_state['is_running'] = False
    server_state['obs_connected'] = False
    server_state['vmix_connected'] = False


# HTML Template pour l'interface web
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SRT Video Relay - OBS → vMix</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            padding: 20px;
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }

        .card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        .status {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .status-indicator {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1.2em;
            font-weight: bold;
        }

        .status-dot {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }

        .status-dot.active {
            background: #4CAF50;
        }

        .status-dot.inactive {
            background: #f44336;
            animation: none;
        }

        .connection-status {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin: 20px 0;
        }

        .connection-box {
            background: #f5f5f5;
            padding: 15px;
            border-radius: 10px;
            border-left: 4px solid #ccc;
        }

        .connection-box.connected {
            border-left-color: #4CAF50;
            background: #e8f5e9;
        }

        .connection-box.disconnected {
            border-left-color: #f44336;
            background: #ffebee;
        }

        .connection-box h4 {
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .connection-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            display: inline-block;
        }

        .connection-indicator.on {
            background: #4CAF50;
            box-shadow: 0 0 10px #4CAF50;
        }

        .connection-indicator.off {
            background: #ccc;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        .config-section {
            margin-top: 20px;
        }

        .config-section h3 {
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.3em;
        }

        .config-box {
            background: #f5f5f5;
            border-left: 4px solid #667eea;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 15px;
        }

        .config-box h4 {
            color: #333;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .config-box code {
            display: block;
            background: white;
            padding: 12px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            font-size: 0.95em;
            color: #d63384;
            word-break: break-all;
            margin: 10px 0;
            border: 1px solid #ddd;
        }

        .copy-btn {
            background: #667eea;
            color: white;
            border: none;
            padding: 8px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.9em;
            transition: all 0.3s;
        }

        .copy-btn:hover {
            background: #5568d3;
            transform: translateY(-2px);
        }

        .copy-btn:active {
            transform: translateY(0);
        }

        .instructions {
            background: #e3f2fd;
            border-left: 4px solid #2196F3;
            padding: 15px;
            border-radius: 5px;
            margin-top: 15px;
        }

        .instructions ol {
            margin-left: 20px;
            margin-top: 10px;
        }

        .instructions li {
            margin: 8px 0;
            line-height: 1.6;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }

        .stat-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }

        .stat-box h4 {
            font-size: 0.9em;
            opacity: 0.9;
            margin-bottom: 10px;
        }

        .stat-box .value {
            font-size: 1.8em;
            font-weight: bold;
        }

        .emoji {
            font-size: 1.5em;
            margin-right: 5px;
        }

        .warning {
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            border-radius: 5px;
            margin-top: 15px;
        }

        .success {
            background: #d4edda;
            border-left: 4px solid #28a745;
            padding: 15px;
            border-radius: 5px;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎬 SRT Video Relay Server</h1>
            <p>Relais vidéo OBS → vMix via Internet</p>
        </div>

        <div class="card">
            <div class="status">
                <div class="status-indicator">
                    <div class="status-dot {{ 'active' if is_running else 'inactive' }}"></div>
                    <span>{{ 'Serveur actif' if is_running else 'Serveur arrêté' }}</span>
                </div>
                <div>
                    {% if start_time %}
                    <small>Démarré: {{ start_time }}</small>
                    {% endif %}
                </div>
            </div>

            {% if is_running %}
            <div class="success">
                <strong>✅ Le serveur relay est opérationnel !</strong>
                <p>Vous pouvez maintenant configurer OBS et vMix avec les URLs ci-dessous.</p>
            </div>

            <div class="connection-status">
                <div class="connection-box {{ 'connected' if obs_connected else 'disconnected' }}">
                    <h4>
                        <span class="connection-indicator {{ 'on' if obs_connected else 'off' }}"></span>
                        OBS (Site A)
                    </h4>
                    {% if obs_connected %}
                        <p>✅ <strong>Connecté</strong></p>
                        {% if obs_time %}
                        <small>Depuis: {{ obs_time }}</small>
                        {% endif %}
                    {% else %}
                        <p>❌ Déconnecté</p>
                        <small>En attente de connexion...</small>
                    {% endif %}
                </div>

                <div class="connection-box {{ 'connected' if vmix_connected else 'disconnected' }}">
                    <h4>
                        <span class="connection-indicator {{ 'on' if vmix_connected else 'off' }}"></span>
                        vMix (Site B)
                    </h4>
                    {% if vmix_connected %}
                        <p>✅ <strong>Connecté</strong></p>
                        {% if vmix_time %}
                        <small>Depuis: {{ vmix_time }}</small>
                        {% endif %}
                    {% else %}
                        <p>❌ Déconnecté</p>
                        <small>En attente de connexion...</small>
                    {% endif %}
                </div>
            </div>
            {% else %}
            <div class="warning">
                <strong>⚠️ Le serveur démarre...</strong>
                <p>Rafraîchissez la page dans quelques secondes.</p>
            </div>
            {% endif %}
        </div>

        <div class="card">
            <div class="config-section">
                <h3>🎥 Configuration OBS (Site A - Émetteur)</h3>

                <div class="config-box">
                    <h4><span class="emoji">📡</span>URL du serveur SRT (Mode: Caller automatique)</h4>
                    <code id="obs-url">{{ srt_url_publish }}</code>
                    <button class="copy-btn" onclick="copyToClipboard('obs-url')">📋 Copier</button>

                    <div class="instructions">
                        <strong>Instructions OBS :</strong>
                        <ol>
                            <li>Ouvrez <strong>OBS Studio</strong></li>
                            <li>Allez dans <strong>Paramètres → Diffusion</strong></li>
                            <li>Service: Sélectionnez <strong>"Personnalisé"</strong></li>
                            <li>Serveur: <strong>Collez l'URL ci-dessus</strong></li>
                            <li>Clé de diffusion: Laissez <strong>VIDE</strong></li>
                            <li>Cliquez <strong>OK</strong></li>
                            <li>Cliquez <strong>"Démarrer la diffusion"</strong></li>
                        </ol>
                        <p style="margin-top: 10px;"><strong>Note:</strong> OBS se connecte automatiquement en mode Caller</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="card">
            <div class="config-section">
                <h3>📺 Configuration vMix (Site B - Récepteur)</h3>

                <div class="config-box">
                    <h4><span class="emoji">📥</span>URL de réception SRT (Mode: Caller automatique)</h4>
                    <code id="vmix-url">{{ srt_url_play }}</code>
                    <button class="copy-btn" onclick="copyToClipboard('vmix-url')">📋 Copier</button>

                    <div class="instructions">
                        <strong>Instructions vMix :</strong>
                        <ol>
                            <li>Ouvrez <strong>vMix</strong></li>
                            <li>Cliquez sur <strong>"Add Input"</strong> (Ajouter une entrée)</li>
                            <li>Sélectionnez <strong>"Stream / SRT"</strong></li>
                            <li><strong>Collez l'URL ci-dessus</strong> dans le champ URL</li>
                            <li><strong>NE changez PAS le mode</strong> (Caller par défaut)</li>
                            <li>Cliquez <strong>"OK"</strong></li>
                            <li><strong>IMPORTANT:</strong> OBS doit diffuser AVANT de configurer vMix</li>
                        </ol>
                        <p style="margin-top: 10px;"><strong>Note:</strong> vMix se connecte en mode Caller (pas Listener!)</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="card">
            <h3>📊 Statistiques du relay</h3>
            <div class="stats-grid">
                <div class="stat-box">
                    <h4>Débit actuel</h4>
                    <div class="value">{{ current_bitrate }}</div>
                </div>
                <div class="stat-box">
                    <h4>Port SRT</h4>
                    <div class="value">{{ srt_port }}</div>
                </div>
                <div class="stat-box">
                    <h4>Statut</h4>
                    <div class="value">{{ 'ON' if is_running else 'OFF' }}</div>
                </div>
            </div>

            <div class="warning" style="margin-top: 20px;">
                <strong>🔒 Confidentialité garantie</strong>
                <p>Votre flux vidéo passe uniquement en mémoire RAM et n'est JAMAIS enregistré sur le disque.
                Le serveur agit comme un simple relais (tuyau) sans aucun stockage.</p>
            </div>
        </div>
    </div>

    <script>
        function copyToClipboard(elementId) {
            const element = document.getElementById(elementId);
            const text = element.textContent;

            navigator.clipboard.writeText(text).then(() => {
                const btn = event.target;
                const originalText = btn.textContent;
                btn.textContent = '✅ Copié !';
                btn.style.background = '#4CAF50';

                setTimeout(() => {
                    btn.textContent = originalText;
                    btn.style.background = '#667eea';
                }, 2000);
            });
        }

        // Auto-refresh every 10 seconds
        setTimeout(() => {
            location.reload();
        }, 10000);
    </script>
</body>
</html>
"""


@app.route('/')
def index():
    """Page principale avec la configuration"""

    # Récupère l'URL de l'application (Railway, Fly.io, ou autre)
    # Essaie plusieurs variables d'environnement
    app_url = os.environ.get('RAILWAY_STATIC_URL',
                             os.environ.get('FLY_APP_NAME', 'localhost'))

    # Nettoie l'URL si nécessaire
    if app_url.startswith('https://'):
        app_url = app_url.replace('https://', '')
    if app_url.startswith('http://'):
        app_url = app_url.replace('http://', '')

    # Si c'est Fly.io, ajoute .fly.dev
    if not '.' in app_url and app_url != 'localhost':
        full_url = f"{app_url}.fly.dev"
    else:
        full_url = app_url

    # Format temps de connexion
    obs_time = server_state['obs_connection_time'].strftime('%H:%M:%S') if server_state.get('obs_connection_time') else None
    vmix_time = server_state['vmix_connection_time'].strftime('%H:%M:%S') if server_state.get('vmix_connection_time') else None

    return render_template_string(
        HTML_TEMPLATE,
        is_running=server_state['is_running'],
        start_time=server_state['start_time'].strftime('%Y-%m-%d %H:%M:%S') if server_state['start_time'] else None,
        srt_url_publish=f"srt://{full_url}:{SRT_PORT}",
        srt_url_play=f"srt://{full_url}:{SRT_PORT + 1}",
        srt_port=SRT_PORT,
        current_bitrate=server_state['stats'].get('current_bitrate', '0 kbits/s'),
        obs_connected=server_state.get('obs_connected', False),
        vmix_connected=server_state.get('vmix_connected', False),
        obs_time=obs_time,
        vmix_time=vmix_time
    )


@app.route('/api/status')
def api_status():
    """API pour récupérer le statut"""
    return jsonify({
        'is_running': server_state['is_running'],
        'start_time': server_state['start_time'].isoformat() if server_state['start_time'] else None,
        'stats': server_state['stats']
    })


@app.route('/health')
def health():
    """Health check pour Fly.io"""
    return jsonify({'status': 'healthy', 'srt_running': server_state['is_running']})


if __name__ == '__main__':
    # Démarre le relay SRT dans un thread séparé
    threading.Thread(target=start_srt_relay, daemon=True).start()

    # Démarre le serveur web Flask
    logger.info(f"🌐 Démarrage serveur web sur le port {HTTP_PORT}")
    app.run(host='0.0.0.0', port=HTTP_PORT, debug=False)

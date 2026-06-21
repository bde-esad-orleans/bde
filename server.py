#!/usr/bin/env python3
"""
Serveur local BDE — sert le site statique + API pour manage.html
Usage : python3 server.py
"""

import base64
import hashlib
import json
import os
import re
import secrets
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = 4242

# ── Chargement du mot de passe depuis .env ───────────────────────────

def load_env():
    env_path = os.path.join(ROOT, '.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    os.environ.setdefault(k.strip(), v.strip())

load_env()

PASSWORD = os.environ.get('BDE_PASSWORD', '')
if not PASSWORD:
    raise SystemExit("❌  Mot de passe manquant. Créer un fichier .env avec :\n   BDE_PASSWORD=votre_mot_de_passe")

# Token de session en mémoire (valide jusqu'au redémarrage du serveur)
SESSION_TOKEN = secrets.token_hex(32)

# Routes qui nécessitent une authentification
PROTECTED_PATHS = {'/manage.html', '/api/events', '/api/archive',
                   '/api/save', '/api/archive-event', '/api/delete', '/api/commit'}

# Page de login HTML
LOGIN_PAGE = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BDE — Connexion</title>
    <link rel="stylesheet" href="/style.css">
    <style>
        body { display: flex; align-items: center; justify-content: center; min-height: 100vh; }
        .login-box {
            width: 100%; max-width: 360px; padding: 2.5rem;
            border: 1px solid var(--border); border-radius: 10px;
            background: var(--white); text-align: center;
        }
        .login-box h1 {
            font-family: 'Playfair Display', serif;
            font-style: italic; font-size: 2rem; font-weight: 400;
            margin-bottom: 0.25rem;
        }
        .login-box p { font-size: 0.82rem; color: var(--muted); margin-bottom: 2rem; }
        .login-box input[type=password] {
            width: 100%; padding: 0.7rem 1rem; margin-bottom: 1rem;
            border: 1px solid var(--border); border-radius: 6px;
            font-family: inherit; font-size: 1rem;
            background: var(--cream); color: var(--ink);
            outline: none; text-align: center; letter-spacing: 0.1em;
        }
        .login-box input[type=password]:focus { border-color: var(--ink); }
        .login-box button {
            width: 100%; padding: 0.7rem;
            background: var(--ink); color: var(--cream);
            border: none; border-radius: 6px;
            font-family: inherit; font-size: 0.82rem; font-weight: 500;
            letter-spacing: 0.08em; text-transform: uppercase;
            cursor: pointer;
        }
        .login-box button:hover { opacity: 0.85; }
        .error { color: #c0392b; font-size: 0.82rem; margin-top: 0.75rem; }
    </style>
</head>
<body>
    <div class="login-box">
        <h1>BDE</h1>
        <p>Accès à l'espace de gestion</p>
        <form method="POST" action="/api/login">
            <input type="password" name="password" placeholder="Mot de passe" autofocus />
            <button type="submit">Entrer</button>
            {error}
        </form>
    </div>
</body>
</html>"""


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def log_message(self, fmt, *args):
        pass

    # ── Auth ─────────────────────────────────────────────────────────

    def is_authenticated(self):
        cookie_header = self.headers.get('Cookie', '')
        for part in cookie_header.split(';'):
            part = part.strip()
            if part.startswith('bde_session='):
                token = part[len('bde_session='):]
                return secrets.compare_digest(token, SESSION_TOKEN)
        return False

    def requires_auth(self, path):
        return path in PROTECTED_PATHS or path.startswith('/api/')

    def redirect_to_login(self):
        self.send_response(302)
        self.send_header('Location', '/login')
        self.end_headers()

    # ── HTTP verbs ────────────────────────────────────────────────────

    def do_GET(self):
        path = urlparse(self.path).path

        if path in ('/', ''):
            path = '/index.html'

        if path == '/login':
            self.serve_login()
            return

        if self.requires_auth(path) and not self.is_authenticated():
            self.redirect_to_login()
            return

        if path.startswith('/api/'):
            self.handle_api_get(path)
        else:
            super().do_GET()

    def do_POST(self):
        path = urlparse(self.path).path
        length = int(self.headers.get('Content-Length', 0))
        raw = self.rfile.read(length) if length else b''

        if path == '/api/login':
            self.handle_login(raw)
            return

        if self.requires_auth(path) and not self.is_authenticated():
            self.json_response({'error': 'Non autorisé'}, 401)
            return

        body = json.loads(raw) if raw else {}
        if path.startswith('/api/'):
            self.handle_api_post(path, body)
        else:
            self.send_error(404)

    def do_DELETE(self):
        path = urlparse(self.path).path
        if self.requires_auth(path) and not self.is_authenticated():
            self.json_response({'error': 'Non autorisé'}, 401)
            return
        length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(length)) if length else {}
        if path.startswith('/api/'):
            self.handle_api_delete(path, body)
        else:
            self.send_error(404)

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    # ── Login ─────────────────────────────────────────────────────────

    def serve_login(self, error=False):
        error_html = '<p class="error">Mot de passe incorrect.</p>' if error else ''
        html = LOGIN_PAGE.replace('{error}', error_html).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', len(html))
        self.end_headers()
        self.wfile.write(html)

    def handle_login(self, raw):
        params = parse_qs(raw.decode('utf-8'))
        submitted = params.get('password', [''])[0]
        if secrets.compare_digest(submitted, PASSWORD):
            self.send_response(302)
            self.send_header('Set-Cookie',
                f'bde_session={SESSION_TOKEN}; HttpOnly; SameSite=Strict; Path=/')
            self.send_header('Location', '/manage.html')
            self.end_headers()
        else:
            self.serve_login(error=True)

    # ── API GET ──────────────────────────────────────────────────────

    def handle_api_get(self, path):
        if path == '/api/events':
            self.json_response(self.read_json('data/events.json') or [])
        elif path == '/api/archive':
            self.json_response(self.read_json('data/archive.json') or [])
        else:
            self.send_error(404)

    # ── API POST ─────────────────────────────────────────────────────

    def handle_api_post(self, path, body):
        if path == '/api/save':
            self.api_save(body)
        elif path == '/api/archive-event':
            self.api_archive_event(body)
        elif path == '/api/commit':
            self.api_commit(body)
        else:
            self.send_error(404)

    # ── API DELETE ───────────────────────────────────────────────────

    def handle_api_delete(self, path, body):
        if path == '/api/delete':
            self.api_delete(body)
        else:
            self.send_error(404)

    # ── Handlers ─────────────────────────────────────────────────────

    def api_save(self, body):
        try:
            titre    = body.get('titre', '').strip()
            date     = body.get('date', '').strip()
            heure    = body.get('heure', '').strip()
            lieu     = body.get('lieu', '').strip()
            desc     = body.get('desc', '').strip()
            old_file = body.get('old_file', '')

            if not titre or not date:
                return self.json_response({'error': 'titre et date requis'}, 400)

            from datetime import date as dt
            today = dt.today().isoformat()
            is_archive = date < today
            folder = '_archive' if is_archive else '_events'
            slug = slugify(titre)
            file_name = f"{date}-{slug}.md"
            file_path = f"{folder}/{file_name}"

            fm = f'---\ntitre: "{titre}"\ndate: {date}\n'
            if heure: fm += f'heure: "{heure}"\n'
            if lieu:  fm += f'lieu: "{lieu}"\n'
            fm += '---\n\n'
            if desc:  fm += desc + '\n'

            poster_data = body.get('poster_data', '')
            poster_name = body.get('poster_name', '')
            poster_path = ''

            if not poster_data and old_file:
                old_abs = os.path.join(ROOT, old_file)
                if os.path.exists(old_abs):
                    with open(old_abs, encoding='utf-8') as f:
                        old_text = f.read()
                    m = re.search(r'^poster:\s*"?([^"\n]+)"?', old_text, re.MULTILINE)
                    if m:
                        poster_path = m.group(1).strip()

            if poster_data and poster_name:
                ext = os.path.splitext(poster_name)[1].lower()
                poster_path = f"assets/images/posters/{slug}{ext}"
                abs_poster = os.path.join(ROOT, poster_path)
                os.makedirs(os.path.dirname(abs_poster), exist_ok=True)
                b64 = poster_data.split(',', 1)[1] if ',' in poster_data else poster_data
                with open(abs_poster, 'wb') as pf:
                    pf.write(base64.b64decode(b64))

            if poster_path:
                fm = fm.replace('---\n\n', f'poster: "{poster_path}"\n---\n\n', 1)

            if old_file and old_file != file_path:
                old_abs = os.path.join(ROOT, old_file)
                if os.path.exists(old_abs):
                    os.remove(old_abs)

            abs_path = os.path.join(ROOT, file_path)
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)
            with open(abs_path, 'w', encoding='utf-8') as f:
                f.write(fm)

            entry = {'titre': titre, 'date': date, 'file': file_path}
            if heure: entry['heure'] = heure
            if lieu:  entry['lieu'] = lieu
            if poster_path: entry['poster'] = poster_path

            if is_archive:
                data = self.read_json('data/archive.json') or []
                if old_file:
                    data = [e for e in data if e.get('file') != old_file]
                data.append(entry)
                data.sort(key=lambda e: e['date'], reverse=True)
                self.write_json('data/archive.json', data)
                events = self.read_json('data/events.json') or []
                events = [e for e in events if e.get('file') != old_file]
                self.write_json('data/events.json', events)
            else:
                data = self.read_json('data/events.json') or []
                if old_file:
                    data = [e for e in data if e.get('file') != old_file]
                data.append(entry)
                data.sort(key=lambda e: e['date'])
                self.write_json('data/events.json', data)
                archive = self.read_json('data/archive.json') or []
                archive = [e for e in archive if e.get('file') != old_file]
                self.write_json('data/archive.json', archive)

            self.json_response({'ok': True, 'file': file_path})
        except Exception as e:
            self.json_response({'error': str(e)}, 500)

    def api_archive_event(self, body):
        try:
            file_path = body.get('file', '')
            new_path = file_path.replace('_events/', '_archive/')
            os.makedirs(os.path.join(ROOT, '_archive'), exist_ok=True)
            os.rename(os.path.join(ROOT, file_path), os.path.join(ROOT, new_path))

            events = self.read_json('data/events.json') or []
            archive = self.read_json('data/archive.json') or []
            moved = next((e for e in events if e['file'] == file_path), None)
            if moved:
                events = [e for e in events if e['file'] != file_path]
                moved['file'] = new_path
                archive.append(moved)
                archive.sort(key=lambda e: e['date'], reverse=True)
            self.write_json('data/events.json', events)
            self.write_json('data/archive.json', archive)
            self.json_response({'ok': True})
        except Exception as e:
            self.json_response({'error': str(e)}, 500)

    def api_delete(self, body):
        try:
            file_path = body.get('file', '')
            source = body.get('source', '')
            abs_path = os.path.join(ROOT, file_path)
            if os.path.exists(abs_path):
                os.remove(abs_path)
            json_file = 'data/events.json' if source == 'upcoming' else 'data/archive.json'
            data = self.read_json(json_file) or []
            data = [e for e in data if e.get('file') != file_path]
            self.write_json(json_file, data)
            self.json_response({'ok': True})
        except Exception as e:
            self.json_response({'error': str(e)}, 500)

    def api_commit(self, body):
        try:
            titre = body.get('titre', 'mise à jour')
            subprocess.run(['git', 'add', '-A'], cwd=ROOT, check=True)
            result = subprocess.run(
                ['git', 'commit', '-m', f'Événement : {titre}'],
                cwd=ROOT, capture_output=True, text=True
            )
            self.json_response({'ok': True, 'message': result.stdout.strip() or result.stderr.strip()})
        except Exception as e:
            self.json_response({'error': str(e)}, 500)

    # ── Utils ────────────────────────────────────────────────────────

    def read_json(self, rel_path):
        abs_path = os.path.join(ROOT, rel_path)
        if not os.path.exists(abs_path):
            return None
        with open(abs_path, encoding='utf-8') as f:
            return json.load(f)

    def write_json(self, rel_path, data):
        abs_path = os.path.join(ROOT, rel_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')

    def json_response(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self._cors()
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)

    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')


def slugify(s):
    s = s.lower()
    for src, dst in [('àâä','a'),('éèêë','e'),('îï','i'),('ôö','o'),('ùûü','u'),('ç','c')]:
        for c in src:
            s = s.replace(c, dst)
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


MONTHS_FR = ['janvier','février','mars','avril','mai','juin',
             'juillet','août','septembre','octobre','novembre','décembre']

def format_date_fr(date_str):
    try:
        y, m, d = date_str.split('-')
        return f"{int(d)} {MONTHS_FR[int(m)-1]} {y}"
    except Exception:
        return date_str


if __name__ == '__main__':
    os.chdir(ROOT)
    server = HTTPServer(('localhost', PORT), Handler)
    print(f"  BDE      → http://localhost:{PORT}")
    print(f"  Manage   → http://localhost:{PORT}/manage.html")
    print(f"  Ctrl+C pour arrêter\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServeur arrêté.")

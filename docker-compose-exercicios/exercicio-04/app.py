#!/usr/bin/env python3
import os
from flask import Flask

app = Flask(__name__)

# Lendo variáveis de ambiente
APP_NAME = os.getenv('APP_NAME', 'App Sem Nome')
APP_PORT = os.getenv('APP_PORT', '5000')
APP_ENV = os.getenv('APP_ENV', 'production')
HOST_VAR = os.getenv('MY_HOST_VAR', 'Nenhum')

@app.route('/')
def home():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{APP_NAME}</title>
        <style>
            body {{ font-family: Arial; max-width: 800px; margin: 50px auto; padding: 20px; }}
            .card {{ background: #e3f2fd; padding: 20px; margin: 10px 0; border-radius: 8px; }}
            var {{ background: #fff3cd; padding: 2px 6px; border-radius: 4px; }}
        </style>
    </head>
    <body>
        <h1>🎉 {APP_NAME}</h1>

        <div class="card">
            <h3>🔧 Configurações:</h3>
            <ul>
                <li>Nome: <var>{APP_NAME}</var></li>
                <li>Porta: <var>{APP_PORT}</var></li>
                <li>Ambiente: <var>{APP_ENV}</var></li>
                <li>Host Var: <var>{HOST_VAR}</var></li>
            </ul>
        </div>

        <div class="card">
            <h3>📝 Variáveis do Container:</h3>
            <ul>
    """

    for key, value in os.environ.items():
        if not key.startswith(('PATH', 'PYTHON', 'HOME')):
            html += f"                <li>{key} = <var>{value}</var></li>\n"

    html += """
            </ul>
        </div>

        <div class="card">
            <h3>🎯 Exercício:</h3>
            <p>Edite o <code>docker-compose.yml</code> e altere as variáveis.</p>
            <p>Depois: <code>docker-compose up -d --force-recreate</code></p>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    print(f"Iniciando {APP_NAME} na porta {APP_PORT}...")
    app.run(host='0.0.0.0', port=int(APP_PORT))

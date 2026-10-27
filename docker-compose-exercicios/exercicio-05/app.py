#!/usr/bin/env python3
import os
import pymysql
from flask import Flask, g

app = Flask(__name__)

# Configuração do banco
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASS', ''),
    'database': os.getenv('DB_NAME', 'test'),
    'cursorclass': pymysql.cursors.DictCursor
}

def get_db():
    """Conexão com o banco de dados."""
    if 'db' not in g:
        g.db = pymysql.connect(**DB_CONFIG)
    return g.db

@app.route('/')
def home():
    """Página inicial."""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Senac - Exercício 5</title>
        <style>
            body { font-family: Arial; max-width: 900px; margin: 50px auto; padding: 20px; }
            .card { background: #e3f2fd; padding: 20px; margin: 10px 0; border-radius: 8px; }
            .success { background: #d4edda; }
            table { width: 100%; border-collapse: collapse; margin-top: 10px; }
            th, td { padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }
            th { background: #1976d2; color: white; }
        </style>
    </head>
    <body>
        <h1>🐳 Docker Compose - Exercício 5</h1>
        <h2>📦 Build Customizado + Banco de Dados</h2>

        <div class="card success">
            <h3>✅ Container rodando!</h3>
            <p>Este container foi construído com um Dockerfile customizado.</p>
            <p>Conectado ao banco: <strong>{db_host}</strong></p>
        </div>

        <div class="card">
            <h3>📊 Dados do Banco:</h3>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Email</th>
                    <th>Status</th>
                </tr>
                {dados}
            </table>
        </div>

        <div class="card">
            <h3>🔧 Como Funciona:</h3>
            <ul>
                <li><code>build:</code> constrói imagem do Dockerfile</li>
                <li><code>context:</code> diretório com os arquivos</li>
                <li><code>depends_on:</code> banco sobe primeiro</li>
                <li><code>volumes:</code> código em desenvolvimento</li>
            </ul>
        </div>

        <div class="card">
            <h3>🎯 Exercícios:</h3>
            <ul>
                <li>Edite o <code>app.py</code> e atualize o navegador</li>
                <li>Veja os logs: <code>docker-compose logs -f app</code></li>
                <li>Entre no banco: <code>docker-compose exec database mysql -uroot -proot123 senac_db</code></li>
            </ul>
        </div>
    </body>
    </html>
    """

    try:
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios")
            rows = cursor.fetchall()

            dados_html = ""
            for row in rows:
                dados_html += f"<tr><td>{row['id']}</td><td>{row['nome']}</td><td>{row['email']}</td><td>{row['status']}</td></tr>"

            return html.format(
                db_host=DB_CONFIG['host'],
                dados=dados_html or "<tr><td colspan='4'>Nenhum dado encontrado</td></tr>"
            )
    except Exception as e:
        return html.format(db_host=f"{DB_CONFIG['host']} (erro: {str(e)})", dados="<tr><td colspan='4'>Erro ao conectar</td></tr>")

@app.route('/health')
def health():
    """Health check."""
    try:
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute("SELECT 1")
            return {'status': 'healthy', 'db': 'connected'}, 200
    except:
        return {'status': 'unhealthy', 'db': 'disconnected'}, 503

if __name__ == '__main__':
    print("Iniciando aplicação...")
    print(f"Banco: {DB_CONFIG['host']}")
    app.run(host='0.0.0.0', port=5000)

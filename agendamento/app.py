from flask import Flask, render_template
from flask_cors import CORS
from route.agendamento_routes import agendamento_routes

app = Flask(__name__)
CORS(app) 

app.secret_key = "senha_super_secreta"

# Registrando rotas da API
app.register_blueprint(agendamento_routes, url_prefix='/api')

# Rota principal para servir o Frontend
@app.route('/')
def principal():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
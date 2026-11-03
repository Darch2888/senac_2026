from flask import Flask, Blueprint, jsonify, render_template, request
from flask_cors import CORS
from services.usuario_service import usuario_alterar, usuario_alterar_senha, usuario_aprovar
from routes.usuario_routes import usuario_routes
from routes.filme_routes import filme_routes
from routes.avaliacao_routes import avaliacao_routes
from auth.middleware import register_middlewares
# construindo a aplicação flask
app = Flask(__name__)
CORS(app) 

app.secret_key = "senha_super_secreta"

app.register_blueprint(usuario_routes, url_prefix='/usuario')
app.register_blueprint(filme_routes, url_prefix='/filme')
app.register_blueprint(avaliacao_routes, url_prefix='/avaliacao')

#Para criar a primeira camada de segurança (rotas)
#register_middlewares(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    usuario_alterar(1, "Administrador", "admin@email.com", "ADMIN")
    usuario_alterar_senha(1, "123456")
    usuario_aprovar(1)
    app.run(debug=True)
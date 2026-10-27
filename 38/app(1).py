from flask import Flask, Blueprint
from flask_cors import CORS
from routes.tarefa_route import tarefa_route

app = Flask(__name__)
CORS(app)

# registrando as rotas na aplicação
app.register_blueprint(tarefa_route)

if __name__ == '__main__':
    app.run(debug=True)
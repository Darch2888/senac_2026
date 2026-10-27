from flask import Flask, Blueprint
from flask_cors import CORS
from routes.aluno_route import aluno_routes

app = Flask(__name__)
CORS(app)

# registrando as rotas na aplicação
app.register_blueprint(aluno_routes) 

if __name__ == '__main__':
    app.run(debug=True)
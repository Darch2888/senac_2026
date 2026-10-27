#importando as biblotecas
from flask import Flask, request, jsonify
from flask_cors import CORS

#criando a publicaçãobackend
app = Flask(__name__)
CORS(app)

#rita principal
@app.route('/')
def principal():
    return jsonify({"mensagem":"Servidor Funcionando"})

@app.route('/mensagem')
def cliente():
    lista = [{"mensagem":"Não deixe para amanhã o que você pode recusar hoje."}]
    return jsonify(lista)

if __name__ == "__main__":
    app.run(debug=True)
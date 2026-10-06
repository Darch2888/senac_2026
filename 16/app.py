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

@app.route('/cliente')
def cliente():
    lista = [{"id":1, "nome":"jesse"},
             {"id":2, "nome":"lucy"}]
    return jsonify(lista)

if __name__ == "__main__":
    app.run(debug=True)
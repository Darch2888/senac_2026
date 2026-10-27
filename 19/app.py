#importando as biblotecas
from flask import Flask, request, jsonify
from flask_cors import CORS

#criando a publicaçãobackend
app = Flask(__name__)
CORS(app)

lista = [{"id":1, "nome":"jesse"},
         {"id":2, "nome":"lucy"}]
#rita principal
@app.route('/')
def principal():
    return jsonify({"mensagem":"Servidor Funcionando"})

@app.route('/usuario')
def usuario():
    return jsonify(lista)

@app.route('/usuario/<int:id>')
def detalhe(id):
    usuario = []
    for item in lista:
        if item["id"] == id:
            usuario = item

    return jsonify(usuario)

if __name__ == "__main__":
    app.run(debug=True)
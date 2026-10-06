#importando as biblotecas
from flask import Flask, request, jsonify
from flask_cors import CORS

#criando a publicaçãobackend
app = Flask(__name__)
CORS(app)

lista = [{"id":1, "nome":"claiton", "disciplina":"filosofia", "av1": 7.0, "av2": 8.0, "media":7.50},
         {"id":2, "nome":"valentina", "disciplina":"literatura", "av1":5, "av2":8, "media":6.50},
         {"id":3, "nome":"enzo", "disciplina":"matematica", "av1":3, "av2":4, "media":6.50}
         ]
#rita principal 
@app.route('/')
def principal():
    return jsonify({"mensagem":"Servidor Funcionando"})

@app.route('/notas')
def notas():
    lista_notas = []
    for item in lista:
        resumo = {
            "nome": item["nome"],
            "disciplina": item["disciplina"],
            "media": item["media"]
        }
        lista_notas.append(resumo)
    return jsonify(lista_notas)


@app.route('/aluno/<int:id>')
def detalhe(id):
    aluno = []
    for item in lista:
        if item["id"] == id:
            aluno = item

    return jsonify(aluno)

if __name__ == "__main__":
    app.run(debug=True)
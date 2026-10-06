#importando as bibliotecas
from flask import Flask, request, jsonify
from flask_cors import CORS

#criando a aplicação backend
app = Flask(__name__)
CORS(app)

produtos = [{"nome": "Arroz", "preco": 5.50},
            {"nome": "Feijão", "preco": 7.20},
            {"nome": "Macarrão", "preco": 3.40},
            {"nome": "Óleo", "preco": 6.00}
            ]

#rota principal
@app.route('/')
def principal():
    return jsonify({"mensagem":"Backend funcionando"})

@app.route('/obtervalor', methods=["POST"])
def obtervalor():
    #verificando se na request é um json
    if request.is_json:
        dados = request.get_json(silent=True)

        resultado = []

        # verificando se é uma lista de valores
        if isinstance(dados, list):
            for linha in dados:
                # pegar o json e separar em variaveis
                nome = linha.get("nome")
                for produto in produtos:
                    if produto["nome"] == nome:
                       resultado.append(produto)
        else:
            # pegar o json e separar em variaveis
            nome = dados.get("nome")
            for produto in produtos:
                if produto["nome"] == nome:
                    resultado.append(produto)

        return jsonify(resultado)
    else:
        mensagem = "Você deve enviar um json valido"    
        return jsonify({"mensagem":mensagem})

@app.route('/consultar', methods=["GET"])
def consulta():
    return jsonify(produtos)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify, request
from flask_cors import CORS

# Criando o backend
app = Flask(__name__)
CORS(app)

produtos = []

@app.route('/')
def principal():
    return jsonify({'mensagem': 'Servidor Funcionando'})

@app.route('/produto', methods=['POST'])
def desconto():
        if request.is_json:
            dados = request.get_json(silent=True)
            nome = dados.get("nome")
            preco = float(dados.get("preco"))*0.9
            produtos.append({"nome":nome, "preco":preco})
            mensagem = "produto enviado com sucesso"
        else:
            mensagem = "Voce deve enviar um json valido"
        return jsonify({"Mensagem":mensagem})

@app.route("/listar", methods = ['GET'])
def listar():
    return jsonify(produtos)

if __name__ == '__main__':
    app.run(debug=True)

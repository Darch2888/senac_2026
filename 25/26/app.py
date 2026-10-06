from flask import Flask, jsonify, request
from flask_cors import CORS

# Criando o backend
app = Flask(__name__)
CORS(app)

pessoa = []

@app.route('/')
def principal():
    return jsonify({'mensagem': 'Servidor Funcionando'})

@app.route('/cadastro', methods={"POST"})
def cadastrar():
    #verificando se na requisição é um json
    if request.is_json:
        dados = request.get_json(silent=True)

        #verificando se é uma lista de valores
        if isinstance(dados, list):
            for linha in dados: 
                nome = linha.get("nome")
                email = linha.get("email")
                pessoa.append({"Nome":nome, "email":email})
                mensagem = "cadastro efetivado com sucesso"
        else: 
            nome = dados.get("nome")
            email = dados.get("email")
            pessoa.append({"Nome":nome, "email":email})
            mensagem = "cadastro efetivado com sucesso"
    else:
        mensagem = "Voce deve enviar um json valido"
    return jsonify({"Mensagem":mensagem})
    
@app.route("/listar", methods = ["GET"])
def listar():
    return jsonify(pessoa)
        


if __name__ == '__main__':
    app.run(debug=True)

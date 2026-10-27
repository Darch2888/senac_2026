from flask import Flask, jsonify, request
from flask_cors import CORS

# Criando o backend
app = Flask(__name__)
CORS(app)

pessoa = []

@app.route('/')
def principal():
    return jsonify({'mensagem': 'Servidor Funcionando'})

@app.route('/login', methods={"POST"})
def cadastrar():
    #verificando se na requisição é um json
    if request.is_json:
        dados = request.get_json(silent=True)

        #verificando se é uma lista de valores
        if isinstance(dados, list):
            for linha in dados: 
                nome = linha.get("nome")
                senha = linha.get("senha")
                pessoa.append({"Nome":nome, "senha":senha})
                mensagem = "cadastro enviado"
                if (nome=="admin" and senha=="123"):
                    pessoa.append({"Nome":nome, "senha":senha})
                    mensagem = "Login bem-sucedido"
                else:
                    pessoa.append({"Nome":nome, "senha":senha})
                    mensagem = "Usuário ou senha incorretos"                     
        else: 
            nome = dados.get("nome")
            senha = dados.get("senha")
            pessoa.append({"Nome":nome, "senha":senha})
            mensagem = "cadastro enviado"
            if (nome=="admin" and senha=="123"):
                pessoa.append({"Nome":nome, "senha":senha})
                mensagem = "Login bem-sucedido"
            else:
                pessoa.append({"Nome":nome, "senha":senha})
                mensagem = "Usuário ou senha incorretos"
    else:
        mensagem = "Voce deve enviar um json valido"
    return jsonify({"Mensagem":mensagem})
    
@app.route("/listar", methods = ["GET"])
def listar():
    return jsonify(pessoa)
        


if __name__ == '__main__':
    app.run(debug=True)

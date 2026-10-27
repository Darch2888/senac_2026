from flask import Flask, jsonify, request
from flask_cors import CORS

# Criando o backend
app = Flask(__name__)
CORS(app)

nota = []

@app.route('/')
def principal():
    return jsonify({'mensagem': 'Servidor Funcionando'})

@app.route('/notas', methods=['POST'])
def calculo():
        if request.is_json:
            dados = request.get_json(silent=True)
            nome = dados.get("nome")
            nota1 = float(dados.get("nota1"))
            nota2 = float(dados.get("nota2"))
            nota3 = float(dados.get("nota3"))
            media = float((nota1+nota2+nota3)/3)
            if (media >= 7):
                nota.append({"nome":nome, "media":media})
                mensagem = "aluno aprovado"
            else:
                nota.append({"nome":nome, "media":media})
                mensagem = "aluno reprodado"                 
        else:
            mensagem = "Voce deve enviar um json valido"
        return jsonify({"Mensagem":mensagem})

@app.route("/listar", methods = ['GET'])
def listar():
    return jsonify(nota)

if __name__ == '__main__':
    app.run(debug=True)

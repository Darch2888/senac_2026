from flask import Flask, jsonify
from flask_cors import CORS

# Criando o backend
app = Flask(__name__)
CORS(app)

@app.route('/')
def principal():
    return jsonify({'mensagem': 'Servidor Funcionando'})

@app.route('/aluno/<string:nome>/<int:idade>')
def aluno(nome, idade):
    return jsonify({'nome': nome, 'e tem ': idade "anos"})

if __name__ == '__main__':
    app.run(debug=True)

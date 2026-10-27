from flask import Flask, request, jsonify
from flask_cors import CORS

#criando a publicaçãobackend
app = Flask(__name__)
CORS(app)

@app.route('/')
def principal():
    return jsonify({"mensagem":"Servidor Funcionando"})

@app.route('/oi')
def oi():
    nome = str(request.args.get('name'))
    return jsonify([{"mensagem":f"Bem Vindo, {nome}"}])


if __name__ == "__main__":
    app.run(debug=True)
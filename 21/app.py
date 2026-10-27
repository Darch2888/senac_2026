from flask import Flask, request, jsonify
from flask_cors import CORS

#criando a publicaçãobackend
app = Flask(__name__)
CORS(app)

@app.route('/')
def principal():
    return jsonify({"mensagem":"Servidor Funcionando"})

@app.route('/soma')
def soma():
    numero_1 = int(request.args.get('num1'))
    numero_2 = int(request.args.get('num2'))
    resultado = numero_1 + numero_2
    return jsonify([{"mensagem":f"a soma de {numero_1} + {numero_2} = {resultado}"}])


if __name__ == "__main__":
    app.run(debug=True)
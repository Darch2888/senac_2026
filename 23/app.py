from flask import Flask, request, jsonify
from flask_cors import CORS

#criando a publicaçãobackend
app = Flask(__name__)
CORS(app)

@app.route('/')
def principal():
    return jsonify({"mensagem":"Servidor Funcionando"})

@app.route('/media')
def nota():
    nota1 = int(request.args.get('num1'))
    nota2 = int(request.args.get('num2'))
    nota3 = int(request.args.get('num3'))

    media = (nota1 + nota2 + nota3)/2
    return jsonify([{"mensagem":f"a media e {media}"}])


if __name__ == "__main__":
    app.run(debug=True)
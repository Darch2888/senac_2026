#importando as biblotecas
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

#criando a publicaçãobackend
app = Flask(__name__)
CORS(app)

#rita principal
@app.route('/')
def principal():
    return jsonify({"mensagem":"Servidor Funcionando"})

@app.route('/pagina')
def pagina():
    return render_template('index.html')

@app.route('/produto')
def produto():
    lista = [{"id":1, "nome":"esmalte", "preco":5},
             {"id":2, "nome":"chocolate", "preco":10},
             {"id":3, "nome":"ameixa", "preco":1}
             ]
    return jsonify(lista)

if __name__ == "__main__":
    app.run(debug=True)
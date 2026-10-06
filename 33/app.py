from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

#criando a aplicação backend
app = Flask(__name__)
CORS(app)

produtos = []

@app.route("/")
def inicio():
    return render_template("produtos.html", produtos=produtos)

@app.route("/produtos", methods=["POST"])
def cadastro():
    nome = (request.form["nome"])
    preco = float(request.form["preco"])
    categoria = request.form["categoria"]
    produto = {"nome":nome,"preco":preco,"categoria":categoria}    
    produtos.append(produto)
    return render_template("produtos.html", produtos=produtos)



if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

#criando a aplicação backend
app = Flask(__name__)
CORS(app)

lista_contatos = []

@app.route("/")
def inicio():
    return render_template("formulario.html")

@app.route("/contato", methods=["POST"])
def cadastro():
    nome = request.form["nome"]
    email = request.form["email"]
    contato = {"nome":nome,"email":email}
    lista_contatos.append(contato)
    return render_template("agradecimento.html", contato=contato)

if __name__ == "__main__":
    app.run(debug=True)
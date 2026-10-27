from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
usuarios = []
@app.route("/")
def inicio():
    return render_template("login.html")
 
@app.route("/registro", methods=["POST"])
def registro():
    nome = request.form["nome"]
    login = request.form["login"]
    senha = request.form["senha"]
    usuario = {"nome": nome,"login": login,"senha": senha}
    usuarios.append(usuario)
    mensagem = "Registro efetuado com sucesso"
    return render_template("login.html", mensagem=mensagem)
 
@app.route("/login", methods=["POST"])
def login():
    login = request.form["login"]
    senha = request.form["senha"]
    encontrado = False
    for usuario in usuarios:
        if (usuario["login"] == login) and (usuario["senha"] == senha):
            encontrado = True
    if encontrado:
        mensagem = "Login efetuado com sucesso"
        return render_template("login.html", mensagem=mensagem)
    else:
        mensagem = "Usuário e/ou senha inválidos"
        return render_template("login.html", mensagem=mensagem)
 
if __name__ == "__main__":
    app.run(debug=True)
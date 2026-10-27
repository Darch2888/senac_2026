from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

#criando a aplicação backend
app = Flask(__name__)
CORS(app)

produtos = []

@app.route("/")
def inicio():
    return render_template("notas.html", media=None)

@app.route("/media", methods=["POST"])
def CalculadoraMedia():
    nota1 = float(request.form["nota1"])
    nota2 = float(request.form["nota2"])
    nota3 = float(request.form["nota3"])
    media = (nota1 + nota2 + nota3)/3
    situacao = "aprovado" if media>= 7 else "reprova"



    return render_template("notas.html", media=media, situacao=situacao)



if __name__ == "__main__":
    app.run(debug=True)
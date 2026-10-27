from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

#criando a aplicação backend
app = Flask(__name__)
CORS(app)

lista_contatos = []

@app.route("/")
def inicio():
    return render_template("calculadora.html")

@app.route("/calculadora", methods=["POST"])
def calculadora():
    numero1 = float(request.form["numero1"])
    numero2 = float(request.form["numero2"])
    operacao = request.form["operacao"]

    if operacao =="+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1*numero2
    elif operacao == "/":
        resultado = numero1/numero2
    else: 
        resultado = "valor informado invalido"
    
    return render_template("calculadora.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
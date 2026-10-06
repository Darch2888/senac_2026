from flask import Flask, Blueprint, jsonify, render_template, request
from flask_cors import CORS
from services.usuario_service import usuario_alterar_senha, usuario_aprovar

# construindo a aplicação flask
app = Flask(__name__)
CORS(app) 

app.secret_key = "senha_super_secreta"

if __name__ == '__main__':
    usuario_alterar_senha(1, '123456')
    usuario_aprovar(1)
    app.run(debug=True)
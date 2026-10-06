from flask import Flask, request, render_template, Blueprint
from services.usuario_service import *

usuario_routes = Blueprint('usuarios_routes', __name__)

@usuario_routes.route('/')
def principal():
    return render_template('login.html')

@usuario_routes.route('/registro', methods=["POST"])
def registro():
    nome = request.form["nome"]
    login = request.form["login"]
    senha = request.form["senha"]

    resultado = usuario_registrar(nome, login, senha)
    if resultado:
        mensagem = "Usuário registrado com sucesso"
    else:
        mensagem = "Erro ao salvar o usuário"

    return render_template('login.html', mensagem=mensagem)


@usuario_routes.route('/login', methods=["POST"])
def login():
    login = request.form["login"]
    senha = request.form["senha"]

    resultado = usuario_login(login, senha)
    if resultado:
        mensagem = "Login efetuado com sucesso"
    else:
        mensagem = "Usuario e senha invalidos"

    return render_template('login.html', mensagem=mensagem)

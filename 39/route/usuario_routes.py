from flask import Flask, Blueprint, redirect, request, jsonify, render_template, url_for
from services.usuario_service import *
from auth.decorators import admin_required

usuario_routes = Blueprint('usuario_routes', __name__)

#rotass de tela
@usuario_routes.route('/')
def rote_usuario_principal():
    if session["usuario_perfil"] == "ADMIN":
        return render_template("usuario/gerenciar.html")
    else:
        return render_template("usuario/perfil.html")
    
@usuario_routes.route('/login')
def rota_usuario_login():
    return render_template("usuario/login.html")

@usuario_routes.route('/registrar', methods=['GET'])
def rota_usuario_registro():
    return render_template("usuario/registro.html")

@usuario_routes.route('/gerenciar', methods=['GET'])
def rota_usuario_gerenciar():
    return render_template("usuario/gerenciar.html")

@usuario_routes.route('/ver_perfil', methods=['GET'])
def rota_usuario_ver_perfil():
    return render_template("usuario/ver_perfil.html")

@usuario_routes.route('/novo', methods=['POST'])
def rota_usuario_novo():
    resultado = False
    mensagem = ""

    if request.is_json:
        data = request.get_json()
        nome = data.get("nome")
        login = data.get("login")
        senha = data.get("senha")

        resultado = usuario_novo(nome, login, senha)
        if resultado: 
            mensagem = "Usuário cadastrado com sucesso!"
            resultado = True
        else:
            mensagem = "Falha ao registrar usuário"
    else:
        mensagem = "Requisição inválida"

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@usuario_routes.route('/logon', methods=['POST'])
def rota_usuario_logon():
    resultado = False
    mensagem = ""

    if request.is_json:
        data = request.get_json()
        login = data.get("login")
        senha = data.get("senha")

        resultado, mensagem = usuario_logon(login, senha)
        return jsonify({"resultado": resultado, "mensagem": mensagem})
    else:
        mensagem = "Requisição inválida"
        return jsonify({"resultado": resultado, "mensagem": mensagem})

@usuario_routes.route('/logout', methods=['GET'])
def rota_usuario_logout():
    usuario_logout()
    return redirect(url_for('usuario_routes.rota_usuario_login'))

@usuario_routes.route('/alterar_senha', methods=['POST'])
def rota_usuario_alterar_senha():
    usuario_logout()
    resultado = False
    mensagem = ""

    if request.is_json:
        data = request.get_json()
        id = data.get("id")
        senha = data.get("senha")

        resultado = usuario_alterar_senha(id, senha)
        if resultado:
            resultado = True
            mensagem = "Senha alterada com sucesso!"
        else:
            resultado = False
            mensagem = "Falha ao alterar senha"
    else:
        resultado = False
        mensagem = "Requisição inválida"

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@usuario_routes.route('/listar', methods=['GET'])
def rota_usuario_listar():
    resultado = False
    mensagem = ""

    usuario = usuario_listar()
    if usuario:
        mensagem = "Usuários listados com sucesso!"
        resultado = True
    else:
        mensagem = "Nenhum usuário encontrado"
    return jsonify({"resultado": resultado, "mensagem": mensagem, "usuarios": usuario})

@usuario_routes.route('/aprovar/<int:id>', methods=['PUT'])
def rota_usuario_aprovar(id):
    resultado = False
    mensagem = ""

    usuario = usuario_aprovar(id)
    if usuario:
        mensagem = "Usuário aprovado com sucesso!"
        resultado = True
    else:
        mensagem = "Falha ao aprovar usuário"

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@usuario_routes.route('/bloquear/<int:id>', methods=['PUT'])
def rota_usuario_bloquear(id):
    resultado = False
    mensagem = ""

    usuario = usuario_bloquear(id)
    if usuario:
        mensagem = "Usuário bloqueado com sucesso!"
        resultado = True
    else:
        mensagem = "Falha ao bloquear usuário"

    return jsonify({"resultado": resultado, "mensagem": mensagem,})

@usuario_routes.route('/detalhe/<int:id>', methods=['GET'])
def rota_usuario_detalhe(id):
    resultado = False
    mensagem = ""

    usuario = usuario_detalhe(id)
    if usuario:
        resultado = True
        mensagem = "Detalhes do usuario obtidos com sucesso!"
    else:
        resultado = False
        mensagem = "Falha ao obter detalhes do usuário"

    return jsonify({"resultado": resultado, "mensagem": mensagem, "usuario": usuario})

@usuario_routes.route('/alterar', methods=['PUT'])
@admin_required
def rota_usuario_alterar():
    resultado = False
    mensagem = ""

    if request.is_json:
        data = request.get_json()
        id = data.get("id")
        nome = data.get("nome")
        login = data.get("login")
        perfil = data.get("perfil")

        resultado = usuario_alterar(id, nome, login, perfil)
        if resultado:
            resultado = True
            mensagem = "Usuário alterado com sucesso!"
        else:
            mensagem = "Falha ao alterar usuário"
    else:
        mensagem = "Requisição inválida"

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@usuario_routes.route('/excluir/<int:id>', methods=['DELETE'])
def rota_usuario_excluir(id):
    resultado = False
    mensagem = ""

    usuario = usuario_excluir(id)
    if resultado:
        resultado = True
        mensagem = "Usuário excluído com sucesso!"
    else:
        resultado = False
        mensagem = "Falha ao excluir usuário"

    return jsonify({"resultado": resultado, "mensagem": mensagem})

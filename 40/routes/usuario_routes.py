from flask import Flask, Blueprint, jsonify, redirect, request, render_template, url_for
from services.usuario_service import *
from auth.decorators import role_required

usuario_routes = Blueprint('usuario_routes', __name__)

#Rotas de tela
@usuario_routes.route('/')
def rota_usuario_principal():
    if session["usuario_perfil"] == "ADMIN":
        return render_template('usuario/gerenciar.html')
    else:
        return render_template('usuario/perfil.html')    

@usuario_routes.route('/login', methods=['GET'])
def rota_usuario_login():
    return render_template("usuario/login.html")

@usuario_routes.route('/registrar', methods=['GET'])
def rota_usuario_registro():
    return render_template("usuario/registro.html")

@usuario_routes.route('/gerenciar')
@role_required("ADMIN")
def rota_usuario_gerenciar():
    return render_template('usuario/gerenciar.html')

@usuario_routes.route('/ver_perfil')
def rota_usuario_ver_perfil():
    return render_template('usuario/perfil.html')

#Rotas de administracao
@usuario_routes.route('/listar', methods=['GET'])
@role_required("ADMIN")
def rota_usuario_listar():
    resultado = False
    mensagem = ""

    usuarios = usuario_listar()
    if usuarios:        
        mensagem = "Usuários listados com sucesso."
        resultado = True
    else:
        mensagem = "Nenhum usuário encontrado."

    return jsonify({"resultado": resultado, "mensagem": mensagem, "usuarios": usuarios})

@usuario_routes.route('/aprovar/<int:id>', methods=['PUT'])
@role_required("ADMIN")
def rota_usuario_aprovar(id):
    resultado = False
    mensagem = ""

    resultado = usuario_aprovar(id)
    if resultado:
        mensagem = "Usuário aprovado com sucesso."
    else:
        mensagem = "Falha ao aprovar usuário."

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@usuario_routes.route('/bloquear/<int:id>', methods=['PUT'])
@role_required("ADMIN")
def rota_usuario_bloquear(id):
    resultado = False
    mensagem = ""

    resultado = usuario_bloquear(id)
    if resultado:
        mensagem = "Usuário bloqueado com sucesso."
        resultado = True
    else:
        mensagem = "Falha ao bloquear usuário."

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@usuario_routes.route('/detalhe/<int:id>', methods=['GET'])
@role_required("ADMIN")
def rota_usuario_detalhe(id):
    resultado = False
    mensagem = ""

    usuario = usuario_detalhe(id)
    if usuario:
        resultado = True
        mensagem = "Detalhes do usuário obtidos com sucesso."
    else:
        resultado = False
        mensagem = "Falha ao obter detalhes do usuário."

    return jsonify({"resultado": resultado, "mensagem": mensagem, "usuario": usuario})

@usuario_routes.route('/excluir/<int:id>', methods=['DELETE'])
@role_required("ADMIN")
def rota_usuario_excluir(id):
    resultado = False
    mensagem = ""

    resultado = usuario_excluir(id)
    if resultado:
        resultado = True
        mensagem = "Usuário excluído com sucesso."
    else:
        resultado = False
        mensagem = "Falha ao excluir usuário."

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@usuario_routes.route('/alterar', methods=['PUT'])
@role_required("ADMIN")
def rota_usuario_alterar():
    resultado = False
    mensagem = ""

    if request.is_json:
        data = request.get_json()
        id = data.get('id')
        nome = data.get('nome')
        email = data.get('email')
        perfil = data.get('perfil')
        
        resultado = usuario_alterar(id, nome, email, perfil)
        if resultado:
            resultado = True
            mensagem = "Usuário alterado com sucesso!"
        else:
            resultado = False
            mensagem = "Falha ao alterar usuário."
    else:
        resultado = False
        mensagem = "Requisição inválida"

    return jsonify({"resultado": resultado, "mensagem": mensagem})

#Rotas específicas de usuario
@usuario_routes.route('/novo', methods=['POST'])
def rota_usuario_novo():
    resultado = False
    mensagem = ""

    if request.is_json:
        data = request.get_json()
        nome = data.get('nome')
        email = data.get('email')
        senha = data.get('senha')
        
        resultado = usuario_novo(nome, email, senha)
        if resultado:
            mensagem = "Usuário registrado com sucesso!"
            resultado = True
        else:
            mensagem = "Falha ao registrar usuário."
    else:
        mensagem = "Requisição inválida"

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@usuario_routes.route('/perfil', methods=['GET'])
def rota_usuario_detalhe_perfil():
    resultado = False
    mensagem = ""

    usuario = usuario_perfil()
    if usuario:
        resultado = True
        mensagem = "Detalhes do usuário obtidos com sucesso."
    else:
        resultado = False
        mensagem = "Falha ao obter detalhes do usuário."

    return jsonify({"resultado": resultado, "mensagem": mensagem, "usuario": usuario})

@usuario_routes.route('/alterar_senha', methods=['PUT'])
def rota_usuario_alterar_senha():
    resultado = False
    mensagem = ""

    if request.is_json:
        data = request.get_json()
        id = data.get('id')
        senha = data.get('senha')
        
        resultado = usuario_alterar_senha(id, senha)
        if resultado:
            resultado = True
            mensagem = "Senha alterada com sucesso!"
        else:
            resultado = False
            mensagem = "Falha ao alterar senha."
    else:
        resultado = False
        mensagem = "Requisição inválida"

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@usuario_routes.route('/logon', methods=['POST'])
def rota_usuario_logon():
    resultado = False
    mensagem = ""

    if request.is_json:
        data = request.get_json()
        email = data.get('email')
        senha = data.get('senha')
        
        resultado, mensagem = usuario_logon(email, senha)
        return jsonify({"resultado": resultado, "mensagem": mensagem})
            
    else:
        mensagem = "Requisição inválida"
        return jsonify({"resultado": resultado, "mensagem": mensagem})

@usuario_routes.route('/logout', methods=['GET'])
def rota_usuario_logout():
    usuario_logout()
    return redirect(url_for("usuario_routes.rota_usuario_login"))

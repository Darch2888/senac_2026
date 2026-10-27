from flask import Flask, Blueprint, jsonify, redirect, request, render_template, url_for
from auth.decorators import admin_required
from routes import usuario_routes
from services.avaliacao_service import *
from services.filme_service import filme_listar_id

avaliacao_routes = Blueprint('avaliacao_routes', __name__)

@avaliacao_routes.route('/alertas/')
def rota_avaliacao_alertas():
    return render_template('avaliar.html')

@avaliacao_routes.route('/ver/<int:id_filme>', methods=['GET'])
def rota_avaliacao_ver(id_filme):
    filme = filme_listar_id(id_filme)
    return render_template('avaliacao.html', filme=filme)

@avaliacao_routes.route('/listar/<int:id_filme>', methods=['GET'])
def rota_avaliacao_listar(id_filme):
    resultado = False
    mensagem = ""

    avaliacao = avaliacao_listar_filme(id_filme)
    if avaliacao:        
        mensagem = "Avaliações listadas com sucesso."
        resultado = True
    else:
        mensagem = "Nenhuma avaliação encontrada."

    return jsonify({"resultado": resultado, "mensagem": mensagem, "avaliacoes": avaliacao})

@avaliacao_routes.route('/avaliar/', methods=['GET'])
def rota_avaliacao_avaliar():
    resultado = False
    mensagem = ""

    avaliacoes = avaliacao_listar_alerta()
    if avaliacoes:        
        mensagem = "Avaliações listadas com sucesso."
        resultado = True
    else:
        mensagem = "Nenhuma avaliação encontrada."

    return jsonify({"resultado": resultado, "mensagem": mensagem, "avaliacoes": avaliacoes})

@avaliacao_routes.route('/denunciar/<int:id_avaliacao>', methods=['put'])
def rota_avaliacao_denunciar(id_avaliacao):
    resultado = False
    mensagem = ""

    resultado = avaliacao_alertar(id_avaliacao)
    if resultado:
        mensagem = "Avaliação denunciada com sucesso."
    else:
        mensagem = "Erro ao denunciar avaliação."

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@avaliacao_routes.route('/inofensivo/<int:id_avaliacao>', methods=['put'])
def rota_avaliacao_inofensivo(id_avaliacao):
    resultado = False
    mensagem = ""

    resultado = avaliacao_inofensiva(id_avaliacao)
    if resultado:
        mensagem = "Avaliação denunciada marcada como inofensiva com sucesso."
    else:
        mensagem = "Erro ao avaliar a denunciar."

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@avaliacao_routes.route('/ofensivo/<int:id_avaliacao>', methods=['put'])
def rota_avaliacao_ofensivo(id_avaliacao):
    resultado = False
    mensagem = ""

    resultado = avaliacao_ofensiva(id_avaliacao)
    if resultado:
        mensagem = "Avaliação denunciada marcada como ofensiva com sucesso."
    else:
        mensagem = "Erro ao avaliar a denunciar."

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@avaliacao_routes.route('/novo', methods=['POST'])
def rota_avaliacao_novo():
    resultado = False
    mensagem = ""

    if request.is_json:
        data = request.get_json()
        nota = int(data.get('nota'))
        filme_id = int(data.get('filme_id'))
        usuario_id = int(session.get('usuario_id'))
        comentario = data.get('comentario')
        
        resultado = avaliacao_nova(filme_id, usuario_id, comentario, nota)
        if resultado:
            mensagem = "Avaliação registrada com sucesso!"
            resultado = True
        else:
            mensagem = "Falha ao registrar avaliação."
    else:
        mensagem = "Requisição inválida"

    return jsonify({"resultado": resultado, "mensagem": mensagem})

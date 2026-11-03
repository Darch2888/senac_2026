from flask import Flask, Blueprint, jsonify, redirect, request, render_template, url_for
from auth.decorators import admin_required
from services.filme_service import *

filme_routes = Blueprint('filme_routes', __name__)

#Rotas de tela
@filme_routes.route('/listar', methods=['GET'])
def rota_filme_listar():
    resultado = False
    mensagem = ""

    filmes = filme_listar_todos()
    if filmes:        
        mensagem = "Filmes listados com sucesso."
        resultado = True
    else:
        mensagem = "Nenhum filme encontrado."

    return jsonify({"resultado": resultado, "mensagem": mensagem, "filmes": filmes})

@filme_routes.route('/pesquisar', methods=['POST'])
def rota_filme_pesquisar():
    resultado = False
    mensagem = ""
    filmes = []
    
    if request.is_json:
        data = request.get_json()
        titulo = data.get('titulo')

        filmes = filme_listar_pesquisa(titulo)
        if filmes:        
            mensagem = "Filmes listados com sucesso."
            resultado = True
        else:
            mensagem = "Nenhum filme encontrado."
    else:
        mensagem = "Pesquisa inválida."

    return jsonify({"resultado": resultado, "mensagem": mensagem, "filmes": filmes})

@filme_routes.route('/top5', methods=['GET'])
def rota_filme_listar_top5():
    resultado = False
    mensagem = ""

    filmes = filme_listar_top5()
    if filmes:        
        mensagem = "Filmes listados com sucesso."
        resultado = True
    else:
        mensagem = "Nenhum filme encontrado."

    return jsonify({"resultado": resultado, "mensagem": mensagem, "filmes": filmes})

@filme_routes.route('/atualizar_lista', methods=['GET'])
@admin_required
def rota_filme_atualizar_base():
    resultado = False
    mensagem = ""

    filme_atualizar_tabela()
    
    return redirect(url_for('index'))
from flask import Flask, Blueprint, jsonify, request, render_template
from services.tarefa_service import *

tarefa_routes = Blueprint('tarefa_routes', __name__)

@tarefa_routes.route('/')
def principal():
    return render_template('tarefa.html')

@tarefa_routes.route('/pendentes', methods=['GET'])
def rota_tarefa_pendentes():
    tarefas = listarTarefasPendentes()
    if tarefas:
        resultado = True
    else:
        resultado = False
    return jsonify({"resultado": resultado, "tarefas": tarefas})

@tarefa_routes.route('/finalizadas', methods=['GET'])
def rota_tarefa_finalizadas():
    tarefas = listarTarefasFinalizadas()
    if tarefas:
        resultado = True
    else:
        resultado = False
    return jsonify({"resultado": resultado, "tarefas": tarefas})

@tarefa_routes.route('/detalhe/<int:id>', methods=['GET'])
def rota_tarefa_detalhe(id):
    tarefa = detalharTarefa(id)
    if tarefa:
        resultado = True
    else:
        resultado = False
    return jsonify({"resultado": resultado, "tarefa": tarefa})

@tarefa_routes.route('/salvar', methods=['POST'])
def rota_tarefa_incluir():
    resultado = False
    mensagem = ""

    if request.is_json:
        dados = request.get_json(silent=True)
        nome = dados['nome']
        prioridade = dados['prioridade']
        finalizada = "N"
        resultado = incluirTarefa(nome, prioridade, finalizada)
        if resultado:
            mensagem = "Tarefa incluída com sucesso"
        else:
            mensagem = "Erro: Tarefa não incluída"
    else:
        mensagem = "Erro: Dados não recebidos no formato JSON"

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@tarefa_routes.route('/alterar', methods=['PUT'])
def rota_tarefa_alterar():
    resultado = False
    mensagem = ""

    if request.is_json:
        dados = request.get_json(silent=True)
        id = dados['id']
        nome = dados['nome']
        prioridade = dados['prioridade']
        resultado = alterarTarefa(id, nome, prioridade)
        if resultado:
            mensagem = "Tarefa alterada com sucesso"
        else:
            mensagem = "Erro: Tarefa não alterada"
    else:
        mensagem = "Erro: Dados não recebidos no formato JSON"

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@tarefa_routes.route('/excluir/<int:id>', methods=['DELETE'])
def rota_tarefa_excluir(id):
    resultado = False
    mensagem = ""

    resultado = excluirTarefa(id)
    if resultado:
        mensagem = "Tarefa excluída com sucesso"
    else:
        mensagem = "Erro: Tarefa não excluída"

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@tarefa_routes.route('/finalizar/<int:id>', methods=['PATCH'])
def rota_tarefa_finalizar(id):
    resultado = False
    mensagem = ""

    resultado = finalizarTarefa(id)
    if resultado:
        mensagem = "Tarefa finalizada com sucesso"
    else:
        mensagem = "Erro: Tarefa não finalizada"

    return jsonify({"resultado": resultado, "mensagem": mensagem})

@tarefa_routes.route('/reabrir/<int:id>', methods=['PATCH'])
def rota_tarefa_reabrir(id):
    resultado = False
    mensagem = ""

    resultado = reabrirTarefa(id)
    if resultado:
        mensagem = "Tarefa reaberta com sucesso"
    else:
        mensagem = "Erro: Tarefa não reaberta"

    return jsonify({"resultado": resultado, "mensagem": mensagem})

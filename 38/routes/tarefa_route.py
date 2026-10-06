from flask import Flask, request, render_template, Blueprint
from services.tarefa_service import *

tarefa_routes = Blueprint('tarefa_routes', __name__)

@tarefa_routes.route('/pendentes')
def principal():
    tarefas = listarTarefasPendentes()
    return render_template('tarefa.html', tarefas=tarefas, tarefa=None, mensagem="")

@tarefa_routes.route('/salvar', methods=["POST"])
def rota_aluno_novo():
    
    nome = request.form["nome"]
    matricula = request.form["matricula"]
    curso = request.form["curso"]

    aluno = aluno_incluir(nome, matricula, curso)
    if aluno:
        mensagem = 'tarefa incluido com sucesso'
    else:
        mensagem = 'Não foi possivel incluir a tarefa'

    tarefas = aluno_listar_todos()
    return render_template('tarefa.html', alunos=alunos, aluno=aluno, mensagem=mensagem)

@tarefa_routes.route('/alterar', methods=["POST"])
def rota_aluno_alterar():
    
    id = int(request.form["id"])
    nome = request.form["nome"]
    matricula = request.form["matricula"]
    curso = request.form["curso"]

    aluno = aluno_alterar(id, nome, matricula, curso)
    if aluno:
        mensagem = 'Aluno alterado com sucesso'
    else:
        mensagem = 'Não foi possivel alterado o aluno'

    alunos = aluno_listar_todos()
    return render_template('tarefa.html', alunos=alunos, aluno=aluno, mensagem=mensagem)


@tarefa_routes.route('/excluir', methods=["POST"])
def rota_tarefa_excluir():
    id = int(request.form["id"])
    resultado = tarefa_excluir_id(id)
    tarefas = tarefa_listar_todas()
    if resultado:
        mensagem = 'Tarefa excluida com sucesso'
    else:
        mensagem = 'Não foi possivel excluir o aluno'
    return render_template('tarefa.html', alunos=alunos, aluno=None, mensagem=mensagem)

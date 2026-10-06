from flask import Flask, request, render_template, Blueprint
from services.aluno_service import *

aluno_routes = Blueprint('aluno_routes', __name__)

@aluno_routes.route('/')
def principal():
    alunos = aluno_listar_todos()
    return render_template('alunos.html', alunos=alunos, aluno=None, mensagem="")

@aluno_routes.route('/detalhe', methods=["POST"])
def rota_aluno_detalhe():
    id = int(request.form["id"])
    aluno = aluno_listar_id(id)
    if aluno:
        mensagem = 'Aluno localizado com sucesso'
    else:
        mensagem = 'Não foi possivel localizar o aluno'

    alunos = aluno_listar_todos()
    return render_template('alunos.html', alunos=alunos, aluno=aluno, mensagem=mensagem)

@aluno_routes.route('/salvar', methods=["POST"])
def rota_aluno_novo():
    
    nome = request.form["nome"]
    matricula = request.form["matricula"]
    curso = request.form["curso"]

    aluno = aluno_incluir(nome, matricula, curso)
    if aluno:
        mensagem = 'Aluno incluido com sucesso'
    else:
        mensagem = 'Não foi possivel incluir o aluno'

    alunos = aluno_listar_todos()
    return render_template('alunos.html', alunos=alunos, aluno=aluno, mensagem=mensagem)

@aluno_routes.route('/alterar', methods=["POST"])
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
    return render_template('alunos.html', alunos=alunos, aluno=aluno, mensagem=mensagem)


@aluno_routes.route('/excluir', methods=["POST"])
def rota_aluno_excluir():
    id = int(request.form["id"])
    resultado = aluno_excluir_id(id)
    alunos = aluno_listar_todos()
    if resultado:
        mensagem = 'Aluno excluido com sucesso'
    else:
        mensagem = 'Não foi possivel excluir o aluno'
    return render_template('alunos.html', alunos=alunos, aluno=None, mensagem=mensagem)

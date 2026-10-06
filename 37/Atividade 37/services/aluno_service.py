from conn import SessionLocal
from models.aluno import Aluno

def aluno_listar_todos():
    alunos = []
    with SessionLocal() as sessao:
        dados = sessao.query(Aluno).all()
        if dados:
            alunos = [aluno.to_print() for aluno in dados]

    return alunos

def aluno_listar_id(id):
    aluno = None
    with SessionLocal() as sessao:
        aluno = sessao.query(Aluno).get(id)
        if aluno:
            aluno = aluno.to_print()

    return aluno

def aluno_incluir(nome, matricula, curso):
    resultado = False
    aluno = Aluno(nome=nome, matricula=matricula, curso=curso)
    with SessionLocal() as sessao:
        sessao.add(aluno)
        sessao.commit()
        resultado = True

    return resultado

def aluno_alterar(id, nome, matricula, curso):
    resultado = False
    with SessionLocal() as sessao:
        aluno = sessao.query(Aluno).get(id)
        if aluno:
            aluno.nome = nome
            aluno.matricula=matricula
            aluno.curso=curso
            sessao.commit()
            resultado = True

    return resultado

def aluno_excluir_id(id):
    resultado = False
    with SessionLocal() as sessao:
        aluno = sessao.query(Aluno).get(id)
        if aluno:
            sessao.delete(aluno)
            sessao.commit()
            resultado = True

    return resultado

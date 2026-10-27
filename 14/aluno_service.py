#import library
from conn import SessionLocal
from aluno import Aluno

#criando metodo para incluir o aluno
def incluir():
    #recebendo os dados para incluir
    nome = input("informe o nome: ")

    #abrindo a sessão com o bando e executando a operacao
    with SessionLocal() as sessao:
        aluno = Aluno(nome=nome)
        sessao.add(aluno)
        sessao.commit()

#criando metodo para listar os alunos
def listar():
    #abrindo sessao com o banco de dados e executando a operação
    with SessionLocal() as sessao: 
        lista_alunos = sessao.query(Aluno).all()
        #percorrendo a lista para imprimir
        for aluno in lista_alunos:
            aluno.to_print()

def alterar():
    #recebendo os dados para alterar
    id = int(input("informar o id que vai ser alterado: "))
    nome = input("Informe o novo nome: ")
    #colocar sessao do codifo que eu pule

    with SessionLocal() as sessao:
        #abrindo sessao com o bando de dados e executando a operacao
        aluno = sessao.get(Aluno, id)
        if aluno:
         #alterando os dados
         aluno.nome = nome
         sessao.commit()


#criando metodo para excluir os dados do aluno
def excluir():
    #recebendo os dados para alterar
    id = int(input("informe o id do aluno que será excluido: "))

    with SessionLocal() as sessao:
        #buscando o aluno pelo id
        aluno = sessao.get(Aluno, id)
        if aluno:
            #excluindo os dados
            sessao.delete(aluno)
            sessao.commit()
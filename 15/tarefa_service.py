from conn import SessionLocal
from tarefa import Tarefa

#metodo para incluir tarefa
def incluirTarefa():
    #coletando dado
    nome = input("Informe o nome da tarefa: ")
    prioridade = int(input("Informe a prioridade da tarefa (1-9):"))
    finalizada = "N"

    #obtendo a sessao e executando a acao
    with SessionLocal() as sessao: 
        tarefa = Tarefa(nome=nome, prioridade=prioridade, finalizada=finalizada)
        sessao.add(Tarefa)
        sessao.commit()

#metodo que lista todas as tarefas que estao pendente
def listarTarefasPendentes():
    #abrindo a sessao e executando a acao
    with SessionLocal() as sessao:
        listarTarefas = (sessao
                         .query(Tarefa)
                         .filter(Tarefa.finalizada == "N")
                         .order_by(Tarefa.prioridade.desc())
                         .all()
                        )
        for tarefa in listarTarefas:
            tarefa.to_print()

def listarTarefasFinalizadas():
    #abrindo a sessao e executando a acao
    with SessionLocal() as sessao:
        listarTarefas = (sessao
                         .query(Tarefa)
                         .filter(Tarefa.finalizada == "N")
                         .order_by(Tarefa.id)
                         .all()
                        )
        for tarefa in listarTarefas:
            tarefa.to_print()

#metodo para finalizar a tarefa
def finalizarTarefa():
    #obtendo dados para incuir a tarefa
    id = int(input("Informe o id da tarefa: "))

    #obtendo a sessao e executando a acao
    with SessionLocal() as sessao:
        tarefa = sessao.get(Tarefa, id)
        if tarefa: 
            tarefa.finalizada = "S"
            sessao.commit()


#metodo para finalizar a tarefa
def reabrirTarefa():
    #obtendo dados para incuir a tarefa
    id = int(input("Informe o id da tarefa: "))

    #obtendo a sessao e executando a acao
    with SessionLocal() as sessao:
        tarefa = sessao.get(Tarefa, id)
        if tarefa: 
            tarefa.finalizada = "N"
            sessao.commit()

def alterarTarefa(): 
    id = int(input("idtarefa", Integer, primary_key=True))
    nome = input("nome", String(100))
    prioridade = input("prioridade", Integer)

    with SessionLocal() as sessao:
        tarefa = sessao.get(Tarefa. id)
        if tarefa: 
            tarefa.nome = nome
            tarefa.prioridade = prioridade
            sessao.commit()

def excluirTarefa():
    #obtendo dados para incuir a tarefa
    id = int(input("Informe o id da tarefa: "))

    #obtendo a sessao e executando a acao
    with SessionLocal() as sessao:
        tarefa = sessao.get(Tarefa, id)
        if tarefa: 
            tarefa.finalizada = "S"
            sessao.commit()




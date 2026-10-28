<<<<<<< HEAD
from conn import SessionLocal
from model.tarefa import Tarefa

# metodo para listar as tarefas pendentes
def listarTarefasPendentes():
    tarefas = []

    with SessionLocal() as session:
        dados = session.query(Tarefa).filter(Tarefa.finalizada == "N").order_by(Tarefa.prioridade.desc()).all()
        if dados:
            tarefas = [tarefa.to_print() for tarefa in dados]
            
    return tarefas

# metodo para listar as tarefas finalizadas
def listarTarefasFinalizadas():
    tarefas = []

    with SessionLocal() as session:
        dados = session.query(Tarefa).filter(Tarefa.finalizada == "S").order_by(Tarefa.id).all()
        if dados:
            tarefas = [tarefa.to_print() for tarefa in dados]

    return tarefas

# metodo para listar tarefa pelo id
def detalharTarefa(id):
    tarefa = None
    with SessionLocal() as session:
        tarefa = session.get(Tarefa, id)        
        if tarefa:
            tarefa = tarefa.to_print()
    return tarefa

# metodo para incluir uma tarefa
def incluirTarefa(nome, prioridade, finalizada="N"):
    resultado = False

    with SessionLocal() as session:
        tarefa = Tarefa(nome=nome, prioridade=prioridade, finalizada=finalizada)
        session.add(tarefa)
        session.commit()
        resultado = True

    return resultado

# metado para alterar uma tarefa
def alterarTarefa(id, nome, prioridade):
    resultado = False

    with SessionLocal() as session:
        tarefa = session.get(Tarefa, id)
        if tarefa:
            tarefa.nome = nome
            tarefa.prioridade = prioridade
            session.commit()
            resultado = True

    return resultado

# metodo para excluir uma tarefa
def excluirTarefa(id):
    resultado = False

    with SessionLocal() as session:
        tarefa = session.get(Tarefa, id)
        if tarefa:
            session.delete(tarefa)
            session.commit()
            resultado = True

    return resultado

# metodo para finalizar uma tarefa
def finalizarTarefa(id):
    resultado = False

    with SessionLocal() as session:
        tarefa = session.get(Tarefa, id)
        if tarefa:
            tarefa.finalizada = "S"
            session.commit()
            resultado = True

    return resultado

# metodo para reabrir uma tarefa
def reabrirTarefa(id):
    resultado = False
    
    with SessionLocal() as session:
        tarefa = session.get(Tarefa, id)
        if tarefa:
            tarefa.finalizada = "N"
            session.commit()
            resultado = True

    return resultado

=======
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



>>>>>>> 0638b7055c0e3f84a609c43094336f17582d1c3e

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


#importar as bibliotecas
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

#criando o elemento que faz o mapeamento classe e tabela
base = declarative_base()

class Tarefa(base): 
    __tablename__ = "tarefa"

    id = Column("idtarefa", Integer, primary_key=True)
    nome = Column("nome", String(100))
    prioridade = Column("prioridade", Integer)
    finalizada = Column("finalizada", String(1))

    def to_print(self): 
        print(f"id:{self.id}, nome:{self.nome}, prioridade{self.prioridade}")
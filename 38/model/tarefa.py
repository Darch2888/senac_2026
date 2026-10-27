from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# criando o elemento que vai mapear a classe com a tabela do banco
Base = declarative_base()

class Tarefa(Base):

    __tablename__ = "TAREFA"

    id = Column("IDTAREFA", Integer, primary_key=True)
    nome = Column("NOME", String(100))
    prioridade = Column("PRIORIDADE", Integer)
    finalizada = Column("FINALIZADA", String(1))

    def to_print(self):
        return {"id": self.id
                , "nome": self.nome
                , "prioridade": self.prioridade
                , "finalizada": self.finalizada
                }
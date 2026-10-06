#importar as biblotecas
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

#criando o elemento que vai mapear este objeto com a tabela
base = declarative_base()

#criando o objeto que vai representar a tabela
class Aluno(base):
    __tablename__ = "ALUNO"

    id = Column("idaluno", Integer, primary_key=True)
    nome = Column("NOME", String(100))
    
    #metodo para imprimir dados do aluno
    def to_print(self):
        print(f"id:{self.id}, nome:{self.nome}")
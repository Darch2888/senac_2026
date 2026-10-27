from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "ALUNO"

    id = Column("IDALUNO", Integer, primary_key=True)
    nome = Column("NOME", String(100))
    matricula = Column("MATRICULA", String(100))
    curso = Column("CURSO", String(100))    

    def to_print(self):
        return {"id":self.id,
                "nome":self.nome,
                "matricula":self.matricula,
                "curso":self.curso
                }
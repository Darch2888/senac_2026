from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "USUARIO"

    id = Column("IDUSUARIO",Integer, primary_key=True, autoincrement=True)
    nome = Column("NOME", String(100))
    login = Column("LOGIN", String(100))
    senha = Column("SENHA", String(100))

    def to_print(self):
        return {"id":self.id,
                "nome":self.nome,
                "login":self.login,
                "senha":self.senha
                }
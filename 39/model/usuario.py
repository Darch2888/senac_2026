#importar as bibliotecas
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

#criando o elemento que faz o mapeamento classe e tabela
base = declarative_base()

class Usuario(base): 
    __tablename__ = "usuario"

    id = Column("idusuario", Integer, primary_key=True)
    nome = Column("nome", String(100))
    login = Column("login", String(100))
    senha = Column("senha", String(200))
    perfil = Column("perfil", String(10))
    bloqueado = Column("bloqueado", String(1))

#adicionar return e corrigir
    def to_print(self): 
        return {
            "id": self.id,
            "nome": self.nome,
            "login": self.login,
            "senha": self.senha,
            "perfil": self.perfil,
            "bloqueado": self.bloqueado
        }
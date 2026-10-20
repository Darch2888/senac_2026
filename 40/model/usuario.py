#importar as bibliotecas
from sqlalchemy import Column, Integer, String, Boolean, Null, Enum
from sqlalchemy.orm import declarative_base

#criando o elemento que faz o mapeamento classe e tabela
base = declarative_base()

class Usuario(base): 
    __tablename__ = "usuario"

    id = Column("idusuario", Integer, autoincrement=True, primary_key=True)
    nome = Column("nome", String(100))
    login = Column("email", String(150))
    senha = Column("senha", String(255))
    perfil = Column("perfil", Enum('ADMIN', 'COMUM'), not Null, default='COMUM')
    bloqueado = Column("bloqueado", Boolean, not Null, default=False)

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
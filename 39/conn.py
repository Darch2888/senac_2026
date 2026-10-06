#importando as bibliotecas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#criando a string de conexão com o banco de dados
URL_BANCO = "mysql+mysqlconnector://root:root@localhost:3306/DBEXERCICIO39"

#definindo a conexao com o banco
engine = create_engine(URL_BANCO, echo=False)

#criando a sessão com o banco de dados
DB_Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

<<<<<<< HEAD
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# criando a string utilizada para conexão com o banco de dados
URL_BANCO = "mysql+mysqlconnector://root:root123@localhost:3306/DBEXERCICIO38"

engine = create_engine(URL_BANCO, echo=False)

# criando o configuração da conexão
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
=======
#importando as bibliotecas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#criando a string de conexão com o banco de dados
URL_BANCO = "mysql+mysqlconnector://root:root@localhost:3306/DBEXERCICIO38"

#definindo a conexao com o banco
engine = create_engine(URL_BANCO, echo=False)

#criando a sessão com o banco de dados
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
>>>>>>> 0638b7055c0e3f84a609c43094336f17582d1c3e

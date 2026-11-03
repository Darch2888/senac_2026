from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# criando a string utilizada para conexão com o banco de dados
URL_BANCO = "mysql+mysqlconnector://root:root@localhost:3306/DBEXERCICIO40"

engine = create_engine(URL_BANCO, echo=False)

# criando o configuração da conexão
BD_Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

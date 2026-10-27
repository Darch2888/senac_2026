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

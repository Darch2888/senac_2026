from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#criando a string de conexão com o banco de dados
URL_BANCO = "mysql+mysqlconnector://root:root@localhost:3306/DBEXERCICIO37"

engine = create_engine(URL_BANCO, echo=False)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
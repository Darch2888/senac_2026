from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# criando a string utilizada para conexão com o banco de dados
URL_BANCO = "mysql+mysqlconnector://root:root@localhost:3306/DBEXERCICIO39"

engine = create_engine(URL_BANCO, echo=False)

# criando o configuração da conexão
DB_Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

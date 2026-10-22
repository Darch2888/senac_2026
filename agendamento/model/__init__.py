import mysql.connector
from mysql.connector import pooling

# Configuração centralizada do banco de dados para a camada model
db_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="clinica_pool",
    pool_size=5,
    pool_reset_session=True,
    host="localhost",
    user="root",
    password="root", # <-- Coloque a senha do seu MySQL aqui
    database="clinica_db"
)

def get_connection():
    return db_pool.get_connection()
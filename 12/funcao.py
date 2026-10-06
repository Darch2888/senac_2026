import mysql.connector

# criando metodo de conexao com o banco de dados
def conectar():
    con = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "DBEXERCICIO11"
    )
    return con

# metodo para incluir aluno
def incluir():
    #recebendo o valor do nome a ser incluido
    nome = input("Informe um nome: ")
    comandosql = "insert into aluno (nome) values(%s)"
    valores = (nome,)

    # obter a conexao
    conexao = conectar()
    # criar um cursor
    cursor = conexao.cursor()
    #executando o comando sql
    cursor.execute(comandosql, valores)
    # gravando no banco de dados
    conexao.commit()
    #fechando a conexao
    cursor.close()
    conexao.close()
    
    
def listar():
    comandosql = "select idaluno, nome from aluno"
   
    # obter a conexao
    conexao = conectar()
   
    # criar um cursor
    cursor = conexao.cursor()
   
    #executando o comando sql
    cursor.execute(comandosql)
   
    # pegando os dados
    dados = cursor.fetchall()
    for id, nome in dados:
        print(f"id: {id}, nome: {nome}")
   
    #fechando a conexao
    cursor.close()
    conexao.close()

def alterar():
    id = int(input("Informe o ID a ser alterado: "))
    nome = input("Informe o Nome a ser alterado: ")

    # criando o comando SQL
    comandosql = "Update aluno set nome = %s where idaluno = %s"
    valores = (nome,id)

     # obter a conexao
    conexao = conectar()
   
    # criar um cursor
    cursor = conexao.cursor()
   
    #executando o comando sql
    cursor.execute(comandosql, valores)
   
    # salvando os dados
    conexao.commit()
   
    #fechando a conexao
    cursor.close()
    conexao.close()

def excluir():
    id = int(input("Informe o id do ALUNO a ser EXCLUÍDO: "))

    # criando o comando sql
    comandosql = "delete from aluno where idaluno = %s"
    valores = (id,)
     
    # obter a conexao
    conexao = conectar()
   
    # criar um cursor
    cursor = conexao.cursor()
   
    #executando o comando sql
    cursor.execute(comandosql,valores)
   
    # salvando os dados
    conexao.commit()
   
    #fechando a conexao
    cursor.close()
    conexao.close()
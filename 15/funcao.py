import mysql.connector

# criando metodo de conexão com o banco de dados
def conectar():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="DBEXERCICIO13"
    )
    return con

# metodo para incluir um aluno
def incluirTarefa():
    # obtendo dados para incluir a tarefa
    nome = input("Informe o nome da tarefa: ")
    prioridade = int(input("Informe a prioridade da tarefa (1-9):"))
    finalizada = "N"

    #montando comando SQL
    comandoSQL = "INSERT INTO TAREFA (NOME, PRIORIDADE, FINALIZADA) VALUES (%s, %s, %s)"
    valoresSQL = (nome, prioridade, finalizada)

    # abrindo conexao com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    # executando o comando SQL
    cursor.execute(comandoSQL, valoresSQL)
    conexao.commit()
    # fechando a conexão com o banco de dados
    cursor.close()
    conexao.close()

def listarTarefasPendentes():
    #montando comando SQL
    comandoSQL = "SELECT IDTAREFA, NOME, PRIORIDADE FROM TAREFA WHERE FINALIZADA = 'N' ORDER BY PRIORIDADE DESC"

    # abrindo conexao com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    # executando o comando SQL
    cursor.execute(comandoSQL)
    dados = cursor.fetchall()
    
    for id, nome, prioridade in dados:
        print(f"id: {id}, nome: {nome}, prioridade: {prioridade}")

    # fechando a conexão com o banco de dados
    cursor.close()
    conexao.close()

def listarTarefasFinalizadas():
    #montando comando SQL
    comandoSQL = "SELECT IDTAREFA, NOME, PRIORIDADE FROM TAREFA WHERE FINALIZADA = 'S' ORDER BY IDTAREFA"

    # abrindo conexao com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    # executando o comando SQL
    cursor.execute(comandoSQL)
    dados = cursor.fetchall()
    
    for id, nome, prioridade in dados:
        print(f"id: {id}, nome: {nome}, prioridade: {prioridade}")

    # fechando a conexão com o banco de dados
    cursor.close()
    conexao.close()

def finalizarTarefa():
    # obtendo dados para incluir a tarefa
    id = int(input("Informe o id da tarefa:"))

    #montando comando SQL
    comandoSQL = "UPDATE TAREFA SET FINALIZADA = 'S' WHERE IDTAREFA = %s"
    valoresSQL = (id,)

    # abrindo conexao com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    # executando o comando SQL
    cursor.execute(comandoSQL, valoresSQL)
    conexao.commit()
    # fechando a conexão com o banco de dados
    cursor.close()
    conexao.close()

def reabrirTarefa():
    # obtendo dados para incluir a tarefa
    id = int(input("Informe o id da tarefa:"))

    #montando comando SQL
    comandoSQL = "UPDATE TAREFA SET FINALIZADA = 'N' WHERE IDTAREFA = %s"
    valoresSQL = (id,)

    # abrindo conexao com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    # executando o comando SQL
    cursor.execute(comandoSQL, valoresSQL)
    conexao.commit()
    # fechando a conexão com o banco de dados
    cursor.close()
    conexao.close()

def alterarTarefa():
    # obtendo dados para incluir a tarefa
    id = int(input("Informe o id da tarefa:"))
    nome = input("Informe o novo nome da tarefa:")
    prioridade = int(input("Informe a nova prioridade :"))

    #montando comando SQL
    comandoSQL = "UPDATE TAREFA SET NOME = %s, PRIORIDADE = %s WHERE IDTAREFA = %s"
    valoresSQL = (nome, prioridade, id)

    # abrindo conexao com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    # executando o comando SQL
    cursor.execute(comandoSQL, valoresSQL)
    conexao.commit()
    # fechando a conexão com o banco de dados
    cursor.close()
    conexao.close()

def excluirTarefa():
    # obtendo dados para incluir a tarefa
    id = int(input("Informe o id da tarefa:"))

    #montando comando SQL
    comandoSQL = "DELETE FROM TAREFA WHERE IDTAREFA = %s"
    valoresSQL = (id,)

    # abrindo conexao com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    # executando o comando SQL
    cursor.execute(comandoSQL, valoresSQL)
    conexao.commit()
    # fechando a conexão com o banco de dados
    cursor.close()
    conexao.close()
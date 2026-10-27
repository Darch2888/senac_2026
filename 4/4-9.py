# definindo a função inicio, que será responsável por executar o código principal do programa
def inicio():
    # entrada de dados
    data = input("Informe a data: ")

    # processamento
    data = data.replace("/01/", "/Janeiro/")
    data = data.replace("/02/", "/Fevereiro/")
    data = data.replace("/03/", "/Março/")
    data = data.replace("/04/", "/Abril/")
    data = data.replace("/05/", "/Maio/")
    data = data.replace("/06/", "/Junho/")
    data = data.replace("/07/", "/Julho/")
    data = data.replace("/08/", "/Agosto/")
    data = data.replace("/09/", "/Setembro/")
    data = data.replace("/10/", "/Outubro/")
    data = data.replace("/11/", "/Novembro/")
    data = data.replace("/12/", "/Dezembro/")

    # saida de dados
    print(data)

if __name__ == "__main__":
    inicio()

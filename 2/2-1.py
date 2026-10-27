
def inicio():
    # entrada de dados
    x = int(input("Informe X: "))
    y = int(input("Informe Y: "))
    z = int(input("Informe Z: "))
    cor = str(input("Informe a Cor: "))
    nome = str(input("Informe o Nome: "))

    #  item 1
    resultado = (x ** 2 + y) > y
    print("Resposta item 1: ", resultado)

    # respondendo item 2
    resultado = cor == "azul"
    print("Resposta item 2: ", resultado)

    # respondendo item 3
    resultado = nome != "joao"
    print("Resposta item 3: ", resultado)


if __name__ == "__main__":
    inicio()
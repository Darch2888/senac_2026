def inicio():
    # entrada de dados
    texto = str(input("Informe o texto: "))

    # processamento
    qtde = len(texto)

    # saida de dados
    print("O texto tem: ", qtde, " caracteres")

if __name__ == "__main__":
    inicio()
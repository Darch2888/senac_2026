def inicio():
    # entrada de dados
    texto = str(input("Informe o texto: "))

    # processamento
    texto = texto.upper()

    # saida de dados
    print("Novo texto é: ", texto)

if __name__ == "__main__":
    inicio()
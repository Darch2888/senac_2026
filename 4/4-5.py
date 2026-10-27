def inicio():
    # entrada de dados
    texto = str(input("Informe o texto: "))
    letra = str(input("Informe a letra: "))

    # processamento
    posicao = texto.find(letra, 0)
    posicao = posicao + 1

    # saida de dados
    print("A posicao da letra é ", posicao)

if __name__ == "__main__":
    inicio()
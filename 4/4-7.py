def inicio():
    # entrada de dados
    nome_completo = str(input("Informe o Nome Completo: "))

    # processamento
    posicao = nome_completo.find(" ", 0)
    nome = nome_completo[0:posicao]
    sobre_nome = nome_completo[posicao + 1:len(nome_completo)]

    sobre_nome = sobre_nome.upper()

    primeira_letra_nome = nome[0:1]
    primeira_letra_nome = primeira_letra_nome.upper()

    resto_nome = nome[1:len(nome)]
    resto_nome = resto_nome.lower()

    # saida de dados
    print("O nome informado é ", sobre_nome + ", " + primeira_letra_nome + resto_nome)

if __name__ == "__main__":
    inicio()

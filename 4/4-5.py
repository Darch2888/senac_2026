<<<<<<< HEAD
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
=======
#entrada de dados
texto = str(input("Informe o texto: "))
letra = str(input("Informe a letra: "))

#processamento
vPosicao = texto.find(letra)
vPosicao = vPosicao + 1

#saida de dados
print(f"A posicao da letra é ", vPosicao)
>>>>>>> 0638b7055c0e3f84a609c43094336f17582d1c3e

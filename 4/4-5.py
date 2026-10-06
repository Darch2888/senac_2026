#entrada de dados
texto = str(input("Informe o texto: "))
letra = str(input("Informe a letra: "))

#processamento
vPosicao = texto.find(letra)
vPosicao = vPosicao + 1

#saida de dados
print(f"A posicao da letra é ", vPosicao)

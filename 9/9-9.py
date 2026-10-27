def inicio():
	valor = []
	multiplicacao = []

	# recebendo valores
	for linha in range(0, 3):
		interno = []
		for coluna in range(0, 3):
			interno.append(int(input(f"Informe valor [{linha}][{coluna}]: ")))
		valor.append(interno) 

	# identificando o multiplicador para cada elemento da matriz
	for linha in range(0, 3):
		interno = [None, None, None]
		for coluna in range(0, 3):
			if linha > coluna:
				interno[coluna] = 1
			elif linha < coluna:
				interno[coluna] = -1
			else:
				interno[coluna] = 0
		multiplicacao.append(interno) 

	# impressao da matriz original
	print("MAtriz original")
	for linha in range(0, 3):
		print(valor[linha])

	# impressao da matriz de multiplicacao
	print("MAtriz multimplicacao")
	for linha in range(0, 3):
		print(multiplicacao[linha])

	# impressao da matriz resultado
	print("MAtriz resultado")
	for linha in range(0, 3):
		interno = []
		for coluna in range(0, 3):
			interno.append(valor[linha][coluna] * multiplicacao[linha][coluna])
		print(interno)


if __name__ == "__main__":
	inicio()
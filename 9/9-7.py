def inicio():

	valor = []

	# recebendo valores
	for linha in range(0, 3):
		interno = []
		for coluna in range(0, 3):
			interno.append(int(input(f"Informe valor [{linha}][{coluna}]: ")))
		valor.append(interno)

	#mostrando os valores em formato de matriz
	for linha in range(0, 3):
		print(valor[linha])

	#alterando a diagonal principal e mostrando valores
	for linha in range(0, 3):
		interno = valor[linha]
		for coluna in range(0, 3):
			if(linha == coluna):
				interno[coluna] = "*"
		print(interno)

if __name__ == "__main__":
	inicio()
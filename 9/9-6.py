def inicio():
	
	valor = []
	soma = []

	for linha in range(0, 3):
		interno = []
		for coluna in range(0, 3):
			interno.append(int(input(f"Informe valor [{linha}][{coluna}]: ")))
		valor.append(interno)

	#inicializando o total
	for coluna in range(0, 3):
		soma.append(0)

	# totalizando as colunas
	for linha in range(0, 3):
		for coluna in range(0, 3):
			soma[coluna] += valor[linha][coluna]

	print("Valores informado:")	
	for linha in range(0, 3):
		print(valor[linha])

	print("total:")	
	print(soma)

if __name__ == "__main__":
	inicio()
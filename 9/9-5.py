def inicio():

	valor = []
	
	for linha in range(0, 3):
		interno = []

		# laco de repetição para colunas
		for coluna in range(0, 3):
			interno.append(int(input(f"Informe o valor para [{linha}][{coluna}]: ")))

		#adicionando as colunas na linhas
		valor.append(interno)

	# laco de repetição para linhas
	for linha in range(0, 3):
		print(valor[linha])

if __name__ == "__main__":
	inicio()
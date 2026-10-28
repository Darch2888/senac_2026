def inicio():

	nome = []

	for indice in range(0, 4):
		nome.append(input(f"Informe o {indice + 1}º nome: "))

	print("")
	
	for indice in range(0, 4):
		print(nome[indice])

if __name__ == "__main__":
	inicio()
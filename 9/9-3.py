def inicio():
	nome = []
	altura = []

	for indice in range(0, 5):
		nome.append(input(f"Informe o {(indice + 1)}º nome: "))
		altura.append(float(input("Informe a Altura:")))

	for indice in range(0, 5):
		if(altura[indice] > 1.6):
			print(f" {nome[indice]} tem {altura[indice]}")

if __name__ == "__main__":
	inicio()
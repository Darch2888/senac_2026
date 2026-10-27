def inicio():
	vetor = []

	for indice in range(0, 5):
		vetor.append(int(input(f"Informe um numero {indice + 1}: ")))

	print("")
	for indice in range(0, 5):
		print(f"{indice + 1} x {vetor[indice]} = {(indice + 1) * vetor[indice]}")

if __name__ == "__main__":
	inicio()
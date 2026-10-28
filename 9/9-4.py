def inicio():
	numero = []
	soma = 0

	for indice in range(0, 10):
		numero.append(int(input(f"Informe o {indice + 1}º numero:")))

	for indice in range(0, 10):
		soma += numero[indice]

	print(f"A soma é {soma}")
	
if __name__ == "__main__":
	inicio()
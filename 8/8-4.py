def inicio():
	menor = 0
	contador = 1
	while True:
		numero = int(input(f"Informe um numero {contador}/20: "))
		if((contador == 1)or(menor > numero)):
			menor = numero
		contador += 1

		if contador > 20:
			# para encerrar o contador enquanto (while) use break
			break
	
	print(f"O menor numero informado é {menor}")

if __name__ == "__main__":
	inicio()
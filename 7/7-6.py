def inicio():
	#entrada de dados
	l1 = float(input("Informe o comprimento do lado 1: "))
	l2 = float(input("Informe o comprimento do lado 2: "))
	l3 = float(input("Informe o comprimento do lado 3: "))

	#processamento
	if(l1 == l2) and (l2 == l3):
		triangulo = "Equilátero"		
	elif(l1 == l2) or (l2 == l3) or (l1 == l3):
		triangulo = "Isósceles"			
	else:
		triangulo = "Escaleno"

	#saida de dados
	print(f"Para os valores informados o tipo de triangulo é {triangulo}")

if __name__ == "__main__":
	inicio()
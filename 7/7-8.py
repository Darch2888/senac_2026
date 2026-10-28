def inicio():
	#entrada de dados
	a = float(input("Informe o valor A: "))
	b = float(input("Informe o valor B: "))
	operacao = input("Informe a operação desejada (+, -, *, /): ")
	
	#processamento
	if (operacao == '+'):
		vOperador = "Adição"
		resultado = a + b
	elif (operacao == '-'):
		vOperador = "Subtração"
		resultado = a - b
	elif (operacao == '*'):
		vOperador = "Multiplicação"
		resultado = a * b
	elif (operacao == '/'):
		vOperador = "Divisão"
		resultado = a / b
	else:
		vOperador = "Inválido"
		resultado = 0.0
	
	#saida de dados
	print(f"{a:.2f} {operacao} {b:.2f} = {resultado:.2f}")
	
if __name__ == "__main__":
	inicio()
def Soma(pNumeroA, pNumeroB) -> float:
	return pNumeroA + pNumeroB	

def Subtracao(pNumeroA, pNumeroB) -> float:
	return pNumeroA - pNumeroB
	
def Multiplicacao(pNumeroA, pNumeroB) -> float:
	return pNumeroA * pNumeroB	
	
def Divisao(pNumeroA, pNumeroB) -> float:
	return pNumeroA / pNumeroB

def inicio():
	vNumeroA = float(input("Informe o número A: "))
	vNumeroB = float(input("Informe o número B: "))
	vOperador = input("Informe a operação desejada: ")

	vResultado = None

	if vOperador == "+":
		vResultado = Soma(vNumeroA, vNumeroB)
	elif vOperador == "-":
		vResultado = Subtracao(vNumeroA, vNumeroB)
	elif vOperador == "*":
		vResultado = Multiplicacao(vNumeroA, vNumeroB)
	elif vOperador == "/":
		vResultado = Divisao(vNumeroA, vNumeroB)
	else:
		print("Operador invalido")

	if vResultado:
		print(f"{vNumeroA} {vOperador} {vNumeroB} = {vResultado}")



if __name__ == "__main__":
	inicio()
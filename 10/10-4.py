def Fatorial(pNumero) -> int:
	if(pNumero > 1):
		vResultado = pNumero * Fatorial(pNumero - 1)
	else:
		vResultado = pNumero * 1	
	return vResultado

def inicio():
	vNumero = int(input("Informe um numero: "))
	print(f"O fatorial de {vNumero} é {Fatorial(vNumero)}")

if __name__ == "__main__":
	inicio()
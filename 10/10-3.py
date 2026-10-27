
def IniciarVetor():
	for vPos in range(0, 5):
		vVetor.append(0)

def PreencherVetor():
	for vPos in range(0, 5):
		vVetor[vPos] = (int(input(f"Escreva o valor para a posicao {vPos + 1}:")))

def OrdenarVetor():
	vTemporario = None
	vTeveTroca = True
	while(vTeveTroca):
		vTeveTroca = False
		for vPos in range(0, 4):
			if vVetor[vPos] >  vVetor[vPos + 1]:
				vTeveTroca = True
				vTemporario = vVetor[vPos]
				vVetor[vPos] = vVetor[vPos + 1]
				vVetor[vPos + 1] = vTemporario

def MostrarVetor():
	print(vVetor)

def MaiorValor():
	vMaior = vVetor[0]
	for vPos in range(0, 5):
		if(vMaior <  vVetor[vPos]):
			vMaior = vVetor[vPos]
	return vMaior

def MenorValor():
	vMenor = vVetor[0]
	for vPos in range(0, 5):
		if(vMenor >  vVetor[vPos]):
			vMenor = vVetor[vPos]
	return vMenor		

def MediaValores():
	return (SomaValores() / 5)


def SomaValores():
	vSoma = 0
	for vPos in range(0, 5):
		vSoma += vVetor[vPos]			
	return vSoma

vVetor = []

def inicio():
	print("1. Iniciar todos os elementos do vetor com valor 0")
	IniciarVetor()

	print("")
	print("2. Entrada de dados")
	PreencherVetor()

	print("")
	print("3. Ordenação")
	OrdenarVetor()

	print("")
	print("4. Mostrar os valores do vetor")
	MostrarVetor()

	print("")
	print("5. Maior valor")
	print(f"Maior Valor: {MaiorValor()}")

	print("")
	print("6. Menor valor")
	print(f"Menor Valor: {MenorValor()}")

	print("")
	print("7. Média dos Valores")
	print(f"Media Valor: {MediaValores()}")

	print("")
	print("8. Soma dos valores")
	print(f"Soma Valores: {SomaValores()}")

if __name__ == "__main__":
	inicio()

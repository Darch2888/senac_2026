def inicio():
	# entrada de dados
	velocidade = float(input("Informe a velocidade: "))

	#processamento
	if(velocidade <= 10):
		multa = 50
	elif(velocidade >= 11)and(velocidade <= 30 ):
		multa = 100
	else:
		multa = 200

	#saida de dados
	print(f"O valor da multa para a velocidade {velocidade} é R$ {multa:.2f}")

if __name__ == "__main__":
	inicio()
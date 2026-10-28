def inicio():
	#entrada de dados
	andar = int(input("Informe o andar desejado:"))

	#processamento
	if andar == 0:
		departamento = "Recepção, Manutenção"
	elif andar == 1:
		departamento = "Comercial"
	elif andar == 2: 
		departamento = "Cobrança"
	elif andar == 3: 
		departamento = "Financeiro"
	elif andar == 4: 
		departamento = "TI e Infraestrutura"
	elif andar == 5: 
		departamento = "Gerencia e Direção"
	else: 
		departamento = "não identificado"

	#saida de dados
	print(f"No andar {andar} tem o departamento {departamento}")

if __name__ == "__main__":
	inicio()
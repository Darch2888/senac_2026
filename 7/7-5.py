def inicio():
	#entrada de dados
	funcionario = input("Informe o nome do funcionário: ")
	salario_mensal = float(input("Informe o salário mensal: "))

	#processamento
	salario_anual = salario_mensal * 12
	
	if(salario_anual <= 22847.76):
		faixa = "1ª Faixa"
		aliquota = 0.0
		deducao = 0.0
	elif(salario_anual >= 22847.77)and(salario_anual <= 33919.80):
		faixa = "2ª Faixa"
		aliquota = 7.5
		deducao = 1713.58
	elif(salario_anual >= 33919.81)and(salario_anual <= 45012.60):
		faixa = "3ª Faixa"
		aliquota = 15.0
		deducao = 4257.57
	elif(salario_anual >= 45012.61)and(salario_anual <= 55976.16):
		faixa = "4ª Faixa"
		aliquota = 22.5
		deducao = 7633.51
	elif(salario_anual >= 55976.17):
		faixa = "5ª Faixa"
		aliquota = 27.5
		deducao = 10432.32
	else:
		faixa = "Inválido"
		aliquota = 0.0
		deducao = 0.0
		
	imposto_total = (salario_anual * aliquota) / 100
	imposto_pagar = imposto_total - deducao

	#saida de dados
	print(f"{'Nome do funcionário':<20}: {funcionario}")
	print(f"{'Salario mensal':<20}: R$ {salario_mensal:.2f}")
	print(f"{'Seu salario anual':<20}: R$ {salario_anual:.2f}")
	print(f"{'Sua faixa de IR':<20}: {faixa}")
	print(f"{'Seu imposto total':<20}: R$ {imposto_total:.2f}")
	print(f"{'Seu valor de deducao':<20}: R$ {deducao:.2f}")
	print(f"{'Seu imposta a pagar':<20}: R$ {imposto_pagar:.2f}")

if __name__ == "__main__":
	inicio()
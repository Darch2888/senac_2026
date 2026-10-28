def inicio():
	#entrada de dados
	categoria = int(input("Informe o código do produto: "))
	quantidade = int(input("Informe a quantidade comprada: "))
	valor_unitario = float(input("Informe o valor unitário: "))

	#processamento		
	valor_total = valor_unitario * quantidade

	if categoria == 0:
		regra = "Alimento não-perecível"
		desconto = 1.0
	elif categoria == 1:
		regra = "Alimento perecível"
		desconto = 2.0
	elif categoria == 2:
		regra = "Vestuário"
		desconto = 0.5
	elif categoria == 3:
		regra = "Higiene pessoal"
		desconto = 1.0
	elif categoria == 4:
		regra = "Limpeza e utensílios domésticos"
		desconto = 0.5
	else:	
		regra = "Inválido"
		desconto = 0.0

	valor_desconto = valor_total - ((valor_total - desconto) / 100)

	#saida de dados
	print(f"O código do produto: {categoria}")
	print(f"A quantidade comprada: {quantidade}")
	print(f"Tipo do produto: {regra}")
	print(f"Valor: {valor_total:.2f}")
	print(f"Desconto: {desconto:.2f} %")
	print(f"Valor total: {valor_desconto:.2f}")

if __name__ == "__main__":
	inicio()
def inicio():
	#entrada de dados
	nome = input("Informe o nome do aluno: ")
	media = float(input("Informe a media do aluno (0 a 100):"))

	#processamento
	if (media >= 0) and (media <= 49):
		situacao = "Insuficiente"
	elif (media >= 50) and (media <= 64):
		situacao = "Regular"
	elif (media >= 65) and (media <= 84):
		situacao = "Bom"
	elif(media >= 85) and (media <= 100):
		situacao = "Ótimo"
	else:
		situacao = "Valor inválido"

	#saida de dados
	print(f"Nome do aluno: ", nome)
	print(f"Média informada: ", media)
	print(f"Situacao calculada: ", situacao)

if __name__ == "__main__":
	inicio()
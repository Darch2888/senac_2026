def inicio():
	# entrada de dados
	nome = input("Informe o nome: ")
	n1 = float(input("Informe a nota 1: "))
	n2 = float(input("Informe a nota 2: "))

	#processamento
	media = (n1 + n2) / 2

	if(media >= 7):
		situacao = "Aprovado"
	else:
		situacao = "Reprovado"

	# saida de dados
	print("Nome: ", nome)
	print("Media: ", media)
	print("Situacao: ", situacao)

if __name__ == "__main__":
	inicio()

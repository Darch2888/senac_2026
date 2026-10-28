def inicio():
	#entrada de dados
	idade = int(input("informe a idade: "))

	#processamento
	if(idade >= 18 ):
		situacao = "Maior de idade"
	else:
		situacao = "Menor de idade"

	#Saidade de dados
	print(f"Para a idade {idade} a situacao é '{situacao}'")

if __name__ == "__main__":
	inicio()
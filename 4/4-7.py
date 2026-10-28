<<<<<<< HEAD
def inicio():
    # entrada de dados
    nome_completo = str(input("Informe o Nome Completo: "))

    # processamento
    posicao = nome_completo.find(" ", 0)
    nome = nome_completo[0:posicao]
    sobre_nome = nome_completo[posicao + 1:len(nome_completo)]

    sobre_nome = sobre_nome.upper()

    primeira_letra_nome = nome[0:1]
    primeira_letra_nome = primeira_letra_nome.upper()

    resto_nome = nome[1:len(nome)]
    resto_nome = resto_nome.lower()

    # saida de dados
    print("O nome informado é ", sobre_nome + ", " + primeira_letra_nome + resto_nome)

if __name__ == "__main__":
    inicio()
=======
#entrada de dados
nome_completo = str(input("Informe o nome completo: "))

#processamento
nome, sobrenome = nome_completo.split(" ", 1)
sobrenome = sobrenome.upper()
SobreNome = tex.caixa_alta(SobreNome)
		
PrimeiraLetraNome = tex.extrair_subtexto(Nome, 0, 1)
PrimeiraLetraNome = tex.caixa_alta(PrimeiraLetraNome)

RestoNome = tex.extrair_subtexto(Nome, 1, tex.numero_caracteres(Nome))
RestoNome = tex.caixa_baixa(RestoNome)
		
#saida de dados
		#escreva("\n O nome informado é ", vSobreNome, ", ", vPrimeiraLetraNome, vRestoNome)

>>>>>>> 0638b7055c0e3f84a609c43094336f17582d1c3e

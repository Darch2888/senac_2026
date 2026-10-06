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


programa
{
	inclua biblioteca Texto --> tex
	
	funcao inicio()
	{

		//declaracao de variavel
		cadeia vNomeCompleto, vNome, vSobreNome, vPrimeiraLetraNome, vRestoNome
		inteiro vPosicao

		//entrada de dados
		escreva("\n Informe o Nome Completo: ")
		leia(vNomeCompleto)

		//processamento
		vPosicao = tex.posicao_texto(" ", vNomeCompleto, 0)
		vNome = tex.extrair_subtexto(vNomeCompleto, 0, vPosicao)
		vSobreNome = tex.extrair_subtexto(vNomeCompleto, vPosicao + 1, tex.numero_caracteres(vNomeCompleto))

		vSobreNome = tex.caixa_alta(vSobreNome)
		
		vPrimeiraLetraNome = tex.extrair_subtexto(vNome, 0, 1)
		vPrimeiraLetraNome = tex.caixa_alta(vPrimeiraLetraNome)

		vRestoNome = tex.extrair_subtexto(vNome, 1, tex.numero_caracteres(vNome))
		vRestoNome = tex.caixa_baixa(vRestoNome)
		
		//saida de dados
		escreva("\n O nome informado é ", vSobreNome, ", ", vPrimeiraLetraNome, vRestoNome)

	}

}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 848; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
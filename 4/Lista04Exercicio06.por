programa
{
	inclua biblioteca Texto --> tex
	
	funcao inicio()
	{
		//declaracao variaveis
		cadeia vCidade, vPrimeiraLetra, vRestoLetras

		//entrada de dados
		escreva("\n Informe a Cidade: ")
		leia(vCidade)

		//processamento
		vPrimeiraLetra = tex.extrair_subtexto(vCidade, 0, 1)
		vRestoLetras = tex.extrair_subtexto(vCidade, 1, tex.numero_caracteres(vCidade))

		vPrimeiraLetra = tex.caixa_alta(vPrimeiraLetra)
		vRestoLetras = tex.caixa_baixa(vRestoLetras)

		//saida de dados
		escreva("A cidade informada é ", vPrimeiraLetra, vRestoLetras)

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 420; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
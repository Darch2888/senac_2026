programa
{
	inclua biblioteca Texto --> tex
	
	funcao inicio()
	{
		//declaracao de variavel
		cadeia vTexto

		//entrada de dados
		escreva("\n Informe o texto: ")
		leia(vTexto)

		//processamento 
		vTexto = tex.caixa_baixa(vTexto)

		//saida de dados
		escreva("\n Novo texto é ", vTexto)

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 296; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
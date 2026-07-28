programa
{
	inclua biblioteca Texto --> tex
	
	funcao inicio()
	{
		
		//declare variaveis
		cadeia vTexto, vLetra
		inteiro vPosicao

		//entrada de dados
		escreva("\n Informe o texto: ")
		leia(vTexto)

		escreva("\n Informe a letra: ")
		leia(vLetra)

		//processamento
		vPosicao = tex.posicao_texto(vLetra, vTexto, 0)
		vPosicao = vPosicao + 1

		//saida de dados
		escreva("\n A posicao da letra é ", vPosicao)

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 353; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
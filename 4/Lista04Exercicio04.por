programa
{
	inclua biblioteca Texto --> tex
	
	funcao inicio()
	{
		//declaracao variavel
		cadeia vTexto
		caracter vLetra

		//entrada de dados
		escreva("\n Informe o texto: ")
		leia(vTexto)
		
		//processamento
		vLetra = tex.obter_caracter(vTexto, 2)

		//saida de dados
		escreva("\n Na terceira posicao tem ", vLetra)

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 329; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
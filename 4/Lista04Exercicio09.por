programa
{
	inclua biblioteca Texto --> tex
	
	funcao inicio()
	{
		
		//declaracao variaveis
		cadeia vdata

		//entrada de dados
		escreva("\n Informe a data:")
		leia(vdata)

		//processamento
		vdata = tex.substituir(vdata, "/01/", "/Janeiro/")
		vdata = tex.substituir(vdata, "/02/", "/Fevereiro/")
		vdata = tex.substituir(vdata, "/03/", "/Marco/")
		//saida de dados
		escreva("\n", vdata)

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 358; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
programa
{
	inclua biblioteca Texto --> tex
	
	funcao inicio()
	{

		//declaracao de variavel
		cadeia vTexto
		inteiro vQtde

		//entrada de dados
		escreva("\n Informe o texto: ")
		leia(vTexto)

		//processamento
		vQtde = tex.numero_caracteres(vTexto)

		//saida de dados
		escreva("\n O texto tem: ", vQtde, " caracteres")

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 97; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
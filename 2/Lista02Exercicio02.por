programa
{
	
	inclua biblioteca Matematica --> mat
	
	funcao inicio()
	{
		// declaracao de variaveis
		real vA, vB, vC 
		logico vL, vResultado

		//entrada de dados
		escreva("digite o valor de A:") 
		leia(vA) 
		escreva("digite o valor de B:") 
		leia(vB) 
		escreva("digite o valor de C:") 
		leia(vC) 
		escreva("digite o valor de L:") 
		leia(vL) 
				
		// processamento
		vResultado = (vB==(vA*vC))e(vL)
		escreva("\n :", vResultado)

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 442; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
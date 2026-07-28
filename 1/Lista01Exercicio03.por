programa
{
	inclua biblioteca Matematica --> mat  // Inclui a biblioteca Matemática
	inclua biblioteca Tipos --> tip
	
	funcao inicio()
	{
		real vN, vResultado
		inteiro vNInteiro, vResultadoInteiro
		leia(vN)
	
		vResultado = mat.potencia(vN, 2.0)
		escreva (vResultado, "\n")
	
		vResultado = mat.raiz(vN, 2.0)
		escreva (vResultado, "\n")
	
		vResultado = vN / 2.0
		escreva (vResultado, "\n")

		vNInteiro = tip.real_para_inteiro(vN)
		vResultadoInteiro = vNInteiro / 2
		escreva (vResultadoInteiro, "\n")
	
		vResultadoInteiro = vNInteiro % 2
		escreva (vResultadoInteiro, "\n")

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 581; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
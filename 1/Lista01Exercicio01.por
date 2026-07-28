programa
{
	inclua biblioteca Matematica --> mat  // Inclui a biblioteca Matemática
	
	funcao inicio()
	{
		

		real vA, vB, vC, vResultado
		
		leia(vA)
		leia(vB)
		leia(vC)

		// respondendo item 1
		vResultado = mat.potencia(vA + vB, 2.0) 
		escreva("\n", vResultado)	
		
		// respondendo item 2
		vResultado = (mat.potencia(vA, 2.0) + (2 * vA * vC) + mat.potencia(vB, 2.0))
		escreva("\n", vResultado)
	
		// respondendo item 3
		vResultado = (mat.potencia(vA, 2.0) - mat.potencia(vB, 2.0))
		escreva("\n", vResultado)
	
		// respondendo item 4
		vResultado = ((vA + vB) * (vA - vB))
		escreva("\n", vResultado)	

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 174; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
programa
{
	
	inclua biblioteca Matematica --> mat
	
	funcao inicio()
	{
		// declaracao de variaveis
		inteiro vX, vY, vZ
		cadeia vCor, vNome
		logico vResultado

		//entrada de dados
		escreva("\n Informe X:")
		leia(vX)
		escreva("\n Informe Y:")
		leia(vY)
		escreva("\n Informe Z:")
		leia(vZ)
		escreva("\n Informe a Cor:")
		leia(vCor)
		escreva("\n Informe o NOMe:")
		leia(vNome)

		
		// respondendo item 1
		vResultado = (mat.potencia(vX, 2.0) + vY) > vZ
		escreva("\n Resposta item 1:")
		escreva(vResultado)

		// respondendo item 2
		vResultado = vCor == "azul"
		escreva("\n Resposta item 2:")
		escreva(vResultado)

		// respondendo item 3
		vResultado = vNome != "joao"
		escreva("\n Resposta item 3:")
		escreva(vResultado)


	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 692; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
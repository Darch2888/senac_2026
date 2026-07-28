programa
{
	
	funcao inicio()
	{
		//declaracao de variaveis
		real vTempo, vVelocidade, vConsumo, vDistancia, vLitros

		//entrada de dados
		escreva("\n Informe o tempo gasto: ")
		leia(vTempo)

		escreva("\n Informe a velocidade media: ")
		leia(vVelocidade)

		vConsumo = 7

		//processamento
		vDistancia = vTempo * vVelocidade
		vLitros = vDistancia / vConsumo

		
		//saida de dados
		escreva("\n A distancia percorrida é: ", vDistancia)
		escreva("\n A qtde de litros consumido é: ", vLitros)	

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 505; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
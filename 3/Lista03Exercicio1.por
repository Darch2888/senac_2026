programa
{

	funcao inicio()
	{
		
		real vSaldo, vCredito, vDebito, vSaldoAtual
		
		escreva("\n Informe o saldo:")
		leia(vSaldo)
		escreva("\n Informe o credito:")
		leia(vCredito)
		escreva("\n Informe o debito:")
		leia(vDebito)
		
		vSaldoAtual = vSaldo + vCredito - vDebito

		escreva("\n Seu saldo atual é", vSaldoAtual);

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 573; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
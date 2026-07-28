programa
{
	
	funcao inicio()
	{
		//declaracao de variavel
		real vValorHora, vQtdeHora, vPercDesc, vSalarioBruto, vValorINSS, vSalarioLiquido

		//entrada de dados
		escreva("\n Informe o Valor por hora:")
		leia(vValorHora)

		escreva("\n Informe a qtde de horas trabalhadas: ")
		leia(vQtdeHora)

		escreva("\n Informe o percentual do INSS: ")
		leia(vPercDesc)

		//processamento
		vSalarioBruto = vValorHora * vQtdeHora
		vValorINSS = (vPercDesc * vSalarioBruto)/100
		vSalarioLiquido = vSalarioBruto - vValorINSS

		//saida de dados
		escreva("\n Salario bruto: ", vSalarioBruto)
		escreva("\n Desconto INSS: ", vValorINSS)
		escreva("\n Salario liquido: ", vSalarioLiquido)
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 690; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
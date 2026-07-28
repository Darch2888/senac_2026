programa
{
	
	funcao inicio()
	{
		//DECLARACAO DE VARIAVEIS
		cadeia vNOME
		real vQTDE_HORAS, vQTDE_DEPENDENTES
		real vVALOR_HORA, vVALOR_AUX_EDU, vVALOR_AUX_REF, vVALOR_AUX_ALI, vVALOR_AUX_TRA
		real vPERC_INSS, vVALOR_INSS, vPERC_IR, vVALOR_IR, vPERC_SIND, vVALOR_SIND
		real vSALARIO_BRUTO, vSALARIO_LIQUIDO, vSALARIO_B_ANUAL, vSALARIO_L_ANUAL

		//ENTRADA DE DADOS
		escreva("\n INFORME O NOME DO FUNCIONARIO: ")
		leia(vNOME)
		escreva("\n INFORME A QTDE HORAS: ")
		leia(vQTDE_HORAS)
		escreva("\n INFORME O NUMERO DE DEPENDENTES: ")
		leia(vQTDE_DEPENDENTES)

		//PROCESSAMENTO
		vVALOR_HORA = 48
		vVALOR_AUX_EDU = 340
		vVALOR_AUX_REF = 550
		vVALOR_AUX_ALI = 550
		vVALOR_AUX_TRA = 300

		vPERC_INSS = 8.5 / 100
		vPERC_IR = 5.0 / 100
		vPERC_SIND = 2.0 / 100

		vSALARIO_BRUTO = (vVALOR_HORA * vQTDE_HORAS) + (vVALOR_AUX_EDU * vQTDE_DEPENDENTES) + vVALOR_AUX_REF + vVALOR_AUX_ALI + vVALOR_AUX_TRA

		vVALOR_INSS = vSALARIO_BRUTO * vPERC_INSS
		vVALOR_IR = vSALARIO_BRUTO * vPERC_IR
		vVALOR_SIND = vSALARIO_BRUTO * vPERC_SIND

		vSALARIO_LIQUIDO = vSALARIO_BRUTO - (vVALOR_INSS + vVALOR_IR + vVALOR_SIND)
 	
		vSALARIO_B_ANUAL = vSALARIO_BRUTO * 12
		vSALARIO_L_ANUAL = vSALARIO_LIQUIDO * 12


		//SAIDA DE DADOS
		escreva("\n Nome do funcionário: ", vNOME)
		escreva("\n Salário bruto: ", vSALARIO_BRUTO)
		escreva("\n valores descontados:")
		escreva("\n      INSS:", vVALOR_INSS)
		escreva("\n      IR:", vVALOR_IR)
		escreva("\n      SINDICATO:", vVALOR_SIND)
		escreva("\n Salário líquido: ", vSALARIO_LIQUIDO)
		escreva("\n Salário Bruto Anual: ", vSALARIO_B_ANUAL)
		escreva("\n Salário Liquido Anual: ", vSALARIO_L_ANUAL )


	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1649; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
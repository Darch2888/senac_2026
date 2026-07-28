programa
{
	inclua biblioteca Texto --> tex
	
	funcao inicio()
	{

		//declaracao
		cadeia vAutor, vTitulo, vEditora, vLocaPublicacao, vNome, vSobreNome, vPrimeiraLetra, vResto
		inteiro vAno, vPosicaoEspaco, vPosicaoFinal

		escreva("\n Informe o nome: ")
		leia(vAutor)
		
		escreva("\n Informe o Titulo: ")
		leia(vTitulo)
		
		escreva("\n Informe o Editora: ")
		leia(vEditora)
		
		escreva("\n Informe o Local de Publicação: ")
		leia(vLocaPublicacao)
	
		escreva("\n Informe o Ano de Publicação: ")
		leia(vAno)
						
		//processando o nome
		//Localizando o espaco entre o nome e o sobrenome
		vPosicaoEspaco = tex.posicao_texto(" ", vAutor, 0)
		vPosicaoFinal = tex.numero_caracteres(vAutor)
		vNome = tex.extrair_subtexto(vAutor, 0, vPosicaoEspaco)
		vSobreNome = tex.extrair_subtexto(vAutor, vPosicaoEspaco + 1, vPosicaoFinal)

		vAutor = tex.caixa_alta(vSobreNome) + ", " + tex.caixa_baixa(vNome)

		//processando o titulo
		vPrimeiraLetra = tex.extrair_subtexto(vTitulo, 0, 1)
		vPrimeiraLetra = tex.caixa_alta(vPrimeiraLetra)
		vPosicaoFinal = tex.numero_caracteres(vTitulo)
		vResto = tex.extrair_subtexto(vTitulo, 1, vPosicaoFinal)
		vResto = tex.caixa_baixa(vResto)

		vTitulo = vPrimeiraLetra + vResto
		
		//processando o editora
		vPrimeiraLetra = tex.extrair_subtexto(vEditora, 0, 1)
		vPrimeiraLetra = tex.caixa_alta(vPrimeiraLetra)
		vPosicaoFinal = tex.numero_caracteres(vEditora)
		vResto = tex.extrair_subtexto(vEditora, 1, vPosicaoFinal)
		vResto = tex.caixa_baixa(vResto)

		vEditora = vPrimeiraLetra + vResto
		
		//processando o local de publicacao
		vPrimeiraLetra = tex.extrair_subtexto(vLocaPublicacao, 0, 1)
		vPrimeiraLetra = tex.caixa_alta(vPrimeiraLetra)
		vPosicaoFinal = tex.numero_caracteres(vLocaPublicacao)
		vResto = tex.extrair_subtexto(vLocaPublicacao, 1, vPosicaoFinal)
		vResto = tex.caixa_baixa(vResto)

		vLocaPublicacao = vPrimeiraLetra + vResto		
		
		// saida de dados
		escreva("\n \n", vAutor, ". ", vTitulo, ". ", vEditora, ": ", vLocaPublicacao, ", ", vAno)
	
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1935; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
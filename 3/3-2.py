tempo = float(input("Informe o seu tempo gasto: "))
velocidade = float(input("Informe a velocidade média: "))
consumo = 7

#processamento
distancia = tempo * velocidade
litros = distancia / consumo
		
#saida de dados
print(f"A distância percorrida é: ", distancia)
print(f"A qtde de litros consumido é: ", litros)	

<<<<<<< HEAD
def inicio():
    # entrada de dados
    tempo = float(input("Informe o tempo gasto: "))
    velocidade = float(input("Informe a velocidade media: "))
    consumo = 7

    # processamento
    distancia = tempo * velocidade
    litros = distancia / consumo

    # saida de dados
    print("A distancia percorrida é: ", distancia)
    print("A qtde de litros consumido é: ", litros)

if __name__ == "__main__":
    inicio()
=======
tempo = float(input("Informe o seu tempo gasto: "))
velocidade = float(input("Informe a velocidade média: "))
consumo = 7

#processamento
distancia = tempo * velocidade
litros = distancia / consumo
		
#saida de dados
print(f"A distância percorrida é: ", distancia)
print(f"A qtde de litros consumido é: ", litros)	
>>>>>>> 0638b7055c0e3f84a609c43094336f17582d1c3e

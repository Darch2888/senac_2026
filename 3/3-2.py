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
def inicio():
    # entrada de dados
    cidade = str(input("Informe a Cidade: "))

    # processamento
    PrimeiraLetra = cidade[0:1]
    RestoLetras = cidade[1:len(cidade)]

    PrimeiraLetra = PrimeiraLetra.upper()
    RestoLetras = RestoLetras.lower()

    # saida de dados
    print("A cidade informada é ", PrimeiraLetra + RestoLetras)

if __name__ == "__main__":
    inicio()
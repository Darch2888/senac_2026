<<<<<<< HEAD
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
=======
#entrada de dados
cidade = str(input("Informe a cidade"))

#processamento
PrimeiraLetra = cidade[:1]
RestoLetras = cidade[1:]

PrimeiraLetra = PrimeiraLetra.upper()
RestoLetras = RestoLetras.lower()

#saida de dados
print(f"A cidade informada é ", PrimeiraLetra, RestoLetras)
>>>>>>> 0638b7055c0e3f84a609c43094336f17582d1c3e

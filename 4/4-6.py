#entrada de dados
cidade = str(input("Informe a cidade"))

#processamento
PrimeiraLetra = cidade[:1]
RestoLetras = cidade[1:]

PrimeiraLetra = PrimeiraLetra.upper()
RestoLetras = RestoLetras.lower()

#saida de dados
print(f"A cidade informada é ", PrimeiraLetra, RestoLetras)
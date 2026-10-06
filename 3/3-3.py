#entrada de dados
valorHora = float(input("Informe o valor por hora: "))
qhora = float(input("Informe a quantidade de horas trabalhadas: "))
perDesc = float(input("Informe o percentual do INSS: "))

#processamento
salarioBruto = valorHora * qhora
valorINSS = (perDesc * salarioBruto)/100
salarioLiquido = salarioBruto - valorINSS

#saida de dados
print(f"Salário bruto: ", salarioBruto)
print(f"Desconto INSS: ", valorINSS)
print(f"Salario liquido: ", salarioLiquido)
		

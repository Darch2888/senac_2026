<<<<<<< HEAD
def inicio():
    # entrada de dados
    valor_hora = float(input("Informe o Valor por hora: "))
    qtde_horas = float(input("Informe a qtde de horas trabalhadas: "))
    perc_inss = float(input("Informe o percentual do INSS: "))
    # processamento
    salario_bruto = valor_hora * qtde_horas
    valorINSS = (perc_inss * salario_bruto) / 100
    salarioLiquido = salario_bruto - valorINSS

    # saida de dados
    print("Salario bruto: ", salario_bruto)
    print("Desconto INSS: ", valorINSS)
    print("Salario liquido: ", salarioLiquido)

if __name__ == "__main__":
    inicio()
=======
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
		
>>>>>>> 0638b7055c0e3f84a609c43094336f17582d1c3e

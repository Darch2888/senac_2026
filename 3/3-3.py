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
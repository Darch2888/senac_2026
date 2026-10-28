
def inicio():
    # ENTRADA DE DADOS
    nome = str(input("Informe o nome do funcionário: "))
    qtde_hora = float(input("Informe a quantidade de horas: "))
    qtde_dependente = float(input("Informe o número de dependentes: "))

    # PROCESSAMENTO
    valor_hora = 48
    valor_aux_edu = 340
    valor_aux_ref = 550
    valor_aux_ali = 550
    valor_aux_tra = 300

    per_inss = 8.5 / 100
    per_ir = 5.0 / 100
    per_sind = 2.0 / 100

    salario_bruto = (valor_hora * qtde_hora) + (valor_aux_edu * qtde_dependente) + valor_aux_ref + valor_aux_ali + valor_aux_tra

    valor_inss = salario_bruto * per_inss
    valor_ir = salario_bruto * per_ir
    valor_sind = salario_bruto * per_sind

    salario_liquido = salario_bruto - (valor_inss + valor_ir + valor_sind)

    salario_b_anual = salario_bruto * 12
    salario_l_anual = salario_liquido * 12

    # SAIDA DE DADOS
    print("Nome do funcionário: ", nome)
    print("Salário bruto: ", salario_bruto)
    print("valores descontados:")
    print("      INSS:", valor_inss)
    print("      IR:", valor_ir)
    print("      SINDICATO:", valor_sind)
    print("Salário líquido: ", salario_liquido)
    print("Salário Bruto Anual: ", salario_b_anual)
    print("Salário Liquido Anual: ", salario_l_anual)

if __name__ == "__main__":
    inicio()

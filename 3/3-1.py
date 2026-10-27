def inicio():
    # entrada de dados
    saldo = float(input("Informe o saldo: "))
    credito = float(input("Informe o credito: "))
    debito = float(input("Informe o debito: "))

    # processamento
    saldoAtual = saldo + credito - debito

    # saida de dados
    print("Seu saldo atual é ", saldoAtual)

if __name__ == "__main__":
    inicio()
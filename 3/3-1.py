<<<<<<< HEAD
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
=======
saldo = float(input("Informe seu saldo: "))		
credito = float(input("Informe seu crédito: "))
debito = float(input("Informe seu débito: "))

saldoAtual = saldo + credito - debito

print(f"Seu saldo atual é: ", saldoAtual)
>>>>>>> 0638b7055c0e3f84a609c43094336f17582d1c3e

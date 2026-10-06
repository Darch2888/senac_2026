saldo = float(input("Informe seu saldo: "))		
credito = float(input("Informe seu crédito: "))
debito = float(input("Informe seu débito: "))

saldoAtual = saldo + credito - debito

print(f"Seu saldo atual é: ", saldoAtual)
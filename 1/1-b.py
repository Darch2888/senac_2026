#resposta questão 1-b referente ao pdf "Atividade 01 - Expressões Aritméticas" - ok
import math

def inicio():
    a = float(input("Digite um número corespondente ao valor de a:"))
    b = float(input("Digite o valor corespondete ao valor de b: "))
    c = float(input("Digite o valor corespondete ao valor de c: "))

    resultado = a**2 + 2*a*c + b**2
    print("O resultado da expressão é ", resultado)

if __name__ == "__main__":
    inicio()
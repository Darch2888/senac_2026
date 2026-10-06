#resposta questão 1-c referente ao pdf "Atividade 01 - Expressões Aritméticas" - ok
import math

def inicio():
    a = float(input("Digite o número corespondente a A: "))
    b = float(input("Digite o número correspondente a b: "))

    resultado = a**2 - b**2
    print("O resultado da expressão é: ", resultado)

if __name__ == "__main__":
    inicio()
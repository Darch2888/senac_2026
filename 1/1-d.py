#resposta questão 1-d referente ao pdf "Atividade 01 - Expressões Aritméticas" - ok
import math

def inicio():
    a = int(input("Digite o número correspondente a 'a': "))
    b = int(input("Digite o número correspondente a 'b': "))

    resultado = (a + b)*(a - b)
    print("O resultado da expressão é: ", resultado)

if __name__ == "__main__":
    inicio()
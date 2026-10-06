def inicio(): 
    n = float(input("Digite um número de N: "))
    resultado = n**2
    print("Resultado da potência é: ", resultado)

    resultado = n**0.5
    print("Resultado da raiz quadrada é: ", resultado)

    resultado = n/2
    print("Resultado da divisão por 2 é: ", resultado)

    resultado = n//2
    print("Resultado da divisão inteira por 2 é: ", resultado)

    resultado = n%2
    print("Resultado do resto da divisão por 2 é: ", resultado)

if __name__ == "__main__":
    inicio()

def inicio():
    # entrada de dados
    a = float(input("digite o valor de A: "))
    b = float(input("digite o valor de B: "))
    c = float(input("digite o valor de C: "))
    l = input("digite o valor de L (verdadeiro/falso): ") == "verdadeiro"

    # processamento
    resultado = (b == (a * c)) and l
    print("Resposta: ", resultado)

if __name__ == "__main__":
    inicio()
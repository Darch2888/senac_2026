def inicio():
    valor = float(input("Informe o valor emprestado: "))
    prazo = int(input("Numero de parcelas: "))
    
    if prazo <= 4:
        juro = 0.0168
    elif (prazo > 4) and (prazo <= 8):
        juro = 0.0189
    else:
        juro = 0.0211
        
    valor_total = valor * ((1 + juro) ** prazo)
    
    print("")
    print("Resultado do emprestido")
    print(f"{' Valor emprestado':<22}: R$ {valor:.2f}")
    print(f"{' Número de parcelas':<22}: {prazo:.0f}")
    print(f"{' taxa de juros (mês)':<22}: {(juro * 100):.2f}%")
    
    for vParcela in range(1, prazo + 1):
        print(f" Valor da parcela {vParcela:<2}: {(valor_total / prazo):.2f}")
        
    print(f"{' Valor total pago':<22}: R$ {valor_total:.2f}")

if __name__ == "__main__":
    inicio()

def formatar_nome():
    v_nome = input("\n Informe o nome Completo: ")
    
    v_nome_alterado = v_nome.title()
    
    print("Nome:", v_nome_alterado)

if __name__ == "__main__":
    formatar_nome()

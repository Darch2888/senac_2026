import os
from aluno_service import incluir, alterar, listar, excluir
 
def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')
 
def principal():
    while True:
        # limpando a tela
        LimpaTela()
 
        # criando o menu
        print("+--------------------------------------------+")
        print("| Menu principal                             |")
        print("+--------------------------------------------+")
        print("| 1. Cadastrar aluno                         |")
        print("| 2. Listar aluno                            |")
        print("| 3. Alterar aluno                           |")
        print("| 4. Excluir aluno                           |")
        print("|                                            |")
        print("| 9. Sair                                    |")
        print("|                                            |")
        print("+--------------------------------------------+")
        print("")
 
        opcao = input("Escolha uma opção: ")    
       
        if opcao == '1':
            # limpando a tala
            LimpaTela()
            # montando titulo da tabela
            print("+--------------------------------------------+")
            print("| Cadastrar novo aluno                       |")
            print("+--------------------------------------------+")
            incluir()
            print("")
            input(" Pressione enter para continuar!")
           
        elif opcao == '2':
            LimpaTela()
            # montando titulo da tabela
            print("+--------------------------------------------+")
            print("| Listar Alunos cadastrados                  |")
            print("+--------------------------------------------+")
            listar()
            print("")
            input("Pressione enter para continuar!")
 
        elif opcao == '3':
            LimpaTela()
            # montando titulo da tabela
            print("+--------------------------------------------+")
            print("| Alterar aluno                              |")
            print("+--------------------------------------------+")
            listar()
            print("")
            alterar()
            print("")
            input("Pressione enter para continuar!")    
 
        elif opcao == '4':
            LimpaTela()
            # montando titulo da tabela
            print("+--------------------------------------------+")
            print("| Excluir aluno                              |")
            print("+--------------------------------------------+")
            listar()
            print("")
            excluir()
            print("")
            input("Pressione enter para continuar!")    
        elif opcao == '9':
            break
        else:
            print("Opção inválida")
 
if __name__ == "__main__":
    principal()
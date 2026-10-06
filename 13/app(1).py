import os
from funcao import incluirTarefa, listarTarefasPendentes, listarTarefasFinalizadas, finalizarTarefa, reabrirTarefa, alterarTarefa, excluirTarefa
 
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
        print("| 1. Tarefas pendentes                       |")
        print("| 2. Nova tarefa                             |")
        print("| 3. Finalizar tarefa                        |")
        print("| 4. Alterar tarefa                          |")
        print("| 5. Reabrir tarefa                          |")
        print("| 6. Excluir tarefa                          |")
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
            print("| Listar tarefas pendentes                   |")
            print("+--------------------------------------------+")
            listarTarefasPendentes()
            print("")
            input(" Pressione enter para continuar!")
           
        elif opcao == '2':
            # limpando a tala
            LimpaTela()
            # montando titulo da tabela
            print("+--------------------------------------------+")
            print("| Cadastrar nova tarefa                      |")
            print("+--------------------------------------------+")
            incluirTarefa()
            print("")
            input(" Pressione enter para continuar!")
           
        elif opcao == '3':
            LimpaTela()
            # montando titulo da tabela
            print("+--------------------------------------------+")
            print("| Finalizar uma tarefa                       |")
            print("+--------------------------------------------+")
            listarTarefasPendentes()
            print("")
            finalizarTarefa()
            print("")
            input("Pressione enter para continuar!")
 
        elif opcao == '4':
            LimpaTela()
            # montando titulo da tabela
            print("+--------------------------------------------+")
            print("| Alterar uma tarefa                         |")
            print("+--------------------------------------------+")
            listarTarefasPendentes()
            print("")
            alterarTarefa()
            print("")
            input("Pressione enter para continuar!")    
        elif opcao == '5':
            LimpaTela()
            # montando titulo da tabela
            print("+--------------------------------------------+")
            print("| Reabrir uma tarefa                         |")
            print("+--------------------------------------------+")
            listarTarefasFinalizadas()
            print("")
            reabrirTarefa()
            print("")
            input("Pressione enter para continuar!")    
        elif opcao == '6':
            LimpaTela()
            # montando titulo da tabela
            print("+--------------------------------------------+")
            print("| Excluir uma tarefa                         |")
            print("+--------------------------------------------+")
            listarTarefasPendentes()
            print("")
            excluirTarefa()
            print("")
            input("Pressione enter para continuar!")    
        elif opcao == '9':
            break
        else:
            print("Opção inválida")
 
if __name__ == "__main__":
    principal()
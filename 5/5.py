def inicio():
    # entrada de dados
    autor = str(input("Informe o nome: "))
    titulo = str(input("Informe o Titulo: "))
    editora = str(input("Informe o Editora: "))
    local_publicacao = str(input("Informe o Local de Publicação: "))
    ano = int(input("Informe o Ano de Publicação: "))

    # processando o nome
    # Localizando o espaco entre o nome e o sobrenome
    posicao_espaco = autor.find(" ", 0)
    posicao_final = len(autor)
    nome = autor[0:posicao_espaco]
    sobre_nome = autor[posicao_espaco + 1:posicao_final]

    autor = sobre_nome.upper() + ", " + nome.lower()

    # processando o titulo
    primeira_letra = titulo[0:1]
    primeira_letra = primeira_letra.upper()
    posicao_final = len(titulo)
    resto = titulo[1:posicao_final]
    resto = resto.lower()

    titulo = primeira_letra + resto

    # processando o editora
    primeira_letra = editora[0:1]
    primeira_letra = primeira_letra.upper()
    posicao_final = len(editora)
    resto = editora[1:posicao_final]
    resto = resto.lower()

    editora = primeira_letra + resto

    # processando o local de publicacao
    primeira_letra = local_publicacao[0:1]
    primeira_letra = primeira_letra.upper()
    posicao_final = len(local_publicacao)
    resto = local_publicacao[1:posicao_final]
    resto = resto.lower()

    local_publicacao = primeira_letra + resto

    # saida de dados
    print(autor, ". ", titulo, ". ", editora, ": ", local_publicacao, ", ", ano)


if __name__ == "__main__":
    inicio()

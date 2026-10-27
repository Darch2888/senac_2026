from flask import session
import requests
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from conn import BD_Session
from model.filme import Filme

def filme_listar_todos():
    filmes = []

    with BD_Session() as bd_sessao:
        dados = bd_sessao.query(Filme).order_by(Filme.titulo).all()
        if dados:
            filmes = [filme.to_print() for filme in dados]
    return filmes

def filme_listar_id(id):
    filme = None
    with BD_Session() as bd_sessao:
        filme = bd_sessao.get(Filme, id)
        if filme:
            filme = filme.to_print()
    return filme

def filme_listar_pesquisa(titulo):
    filme = None
    with BD_Session() as bd_sessao:
        filme = bd_sessao.get(Filme, titulo)
        if filme:
            filme = filme.to_print()
    return filme

def filme_atualizar_tabela():

    # carregando todos os filmes salvo no banco de dados
    with BD_Session() as bd_sessao:
        dados = bd_sessao.query(Filme).all()
        filmes_salvos = {filme.titulo for filme in dados}

    # carregando todos os dados da API
    api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwODExOGIxM2YwN2NiOWQzYmYwODNiMTFmMjQxYjk1NyIsIm5iZiI6MTc1NzE5NjA5Ny4wNzksInN1YiI6IjY4YmNhZjQxZjIzZDNlMzIwMzk0NzNiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._8jdsXPumfjNOTjnses_QgbQX7syERexuKDQr8kqvHg'
    url = 'https://api.themoviedb.org/3/movie/now_playing?language=pt-BR&region=BR'
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    json_filmes = response.json()
    lista_filmes_site = json_filmes["results"]

    novos_filmes = []

    # montando a lista de filmes com os dados que precisamos
    for item in lista_filmes_site:
        if item["original_title"] not in filmes_salvos:
            novos_filmes.append(
                Filme(
                    id=item["id"],
                    titulo=item["original_title"],
                    descricao=item["overview"],
                    descricao_breve=item["overview"][:100],
                    data_estreia=item["release_date"],
                    url_poster="https://image.tmdb.org/t/p/w185/" + item["poster_path"]
                )
            ) 

    resultado = False
    mensagem = ""
    if novos_filmes:
        with BD_Session() as bd_sessao:
            bd_sessao.add_all(novos_filmes)
            bd_sessao.commit()
            resultado = True
            mensagem = "Lista de filme atualizada"
    else:
        resultado = True
        mensagem = "Nenhum filme novo encontrado"

    return resultado, mensagem
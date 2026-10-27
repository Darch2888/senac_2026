BACKEND_URL = "http://127.0.0.1:5000/filme";
BACKEND_URL_AVALIACAO = "http://127.0.0.1:5000/avaliacao";
listafilmes = document.getElementById("listaFilmes");
carrosel_filmes = document.getElementById("carrosel_filmes");

async function filme_carregar_lista_filmes(){
    if(listafilmes){
        let rota = "/listar";

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota);

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        let filmes = json_retorno.filmes;

        if(filmes){
            listafilmes.innerHTML = "";            
            filmes.forEach(filme => {  

                let parte_inteira = Math.floor(filme.nota_media);
                let estrelas_cheias = "⭐".repeat(parte_inteira);
                let estrelas_vazias = "☆".repeat(5 - parte_inteira);
                let estrelas = estrelas_cheias + estrelas_vazias;

                listafilmes.innerHTML += `
                    <div class="col-md-3 mb-3">
                        <div class="card h-100 shadow-sm">
                            <img src="${ filme.url_poster }" class="card-img-top" alt="${ filme.titulo }">
                            <div class="card-body">
                                <h5 class="card-title">${ filme.titulo }</h5>
                                <p class="card-text">${ filme.descricao_breve }...</p>
                            </div>
                            <div class="card-footer d-flex justify-content-between align-items-center">
                                <small class="text-muted">${estrelas} ${filme.nota_media} <br> ${ filme.quantidade_comentarios } Avaliações</small>
                                <a href="${BACKEND_URL_AVALIACAO + '/ver/' + filme.id}" class="btn btn-sm btn-primary">Detalhes</a>
                            </div>
                        </div>
                    </div>
                `;
            });
        }else {
            listafilmes.innerHTML = ``;
        }        
    }
}


filme_carregar_lista_filmes()
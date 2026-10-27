BACKEND_URL = "http://127.0.0.1:5000/avaliacao";
listaavaliacao = document.getElementById("listaAvaliacoes");
tabela_alertas = document.getElementById("listaAlerta");
id_filme_selecionado = document.getElementById("id_filme").value;
formulario_avaliacao = document.getElementById("frmAvaliacao");

function mostrar_mensagem(mensagem){
    alert(mensagem);
}

async function avaliacao_carregar_lista_avaliacoes(id_filme){
    if(listaavaliacao){
        let rota = "/listar/" + id_filme;

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota);

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        let avaliacoes = json_retorno.avaliacoes;

        if(avaliacoes){
            listaavaliacao.innerHTML = "";            
            avaliacoes.forEach(avaliacao => {  

                let parte_inteira = Math.floor(avaliacao.nota);
                let estrelas_cheias = "⭐".repeat(parte_inteira);
                let estrelas_vazias = "☆".repeat(5 - parte_inteira);
                let estrelas = estrelas_cheias + estrelas_vazias;

                denunciada = ""
                if (avaliacao.alerta_ofensivo == "S") {
                    denunciada = `<small><em><span class="text-danger">Esta avaliação foi <br>denunciada como ofensiva.</span></em></small>`;
                }else{
                    denunciada = `<a onclick="avaliacao_denunciar(${avaliacao.id})" class="btn btn-sm btn-warning">Denunciar</a>`;
                }

                listaavaliacao.innerHTML += `
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <div>
                            <figure>
                                <blockquote class="blockquote">
                                    <p>${avaliacao.comentario}</p>
                                </blockquote>
                                <figcaption class="blockquote-footer">
                                    ${estrelas}
                                    <em>${avaliacao.data_avaliacao2}</em>
                                </figcaption>
                            </figure>
                        </div>
                        <div>
                            ${denunciada}
                        </div>
                    </li>
                `;
            });
        }else {
            listaavaliacao.innerHTML = `<li class="list-group-item">Ainda não há avaliações. Seja o primeiro!</li>`;
        }        
    }
}

async function avaliacao_carregar_lista_alertas(){
    if(tabela_alertas){
        let rota = "/avaliar";

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota);

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        let avaliacoes = json_retorno.avaliacoes;

        if(avaliacoes){
            tabela_alertas.innerHTML = "";            
            avaliacoes.forEach(avaliacao => {  
                
                tabela_alertas.innerHTML += `
                    <tr>
                        <td>${avaliacao.data_avaliacao2}</td>
                        <td>${avaliacao.comentario}</td>
                        <td>${avaliacao.usuario.email}</td>
                        <td>
                            <button class="btn btn-sn btn-success btn-sm" onclick="inofensivo(${avaliacao.id})">Inofensivo</button>
                            <button class="btn btn-sn btn-warning btn-sm" onclick="ofensino(${avaliacao.id})">Ofensivo</button>
                        </td>
                    </tr>
                `;
            });
        }else {
            tabela_alertas.innerHTML = ``;
        }        
    }
}

async function avaliacao_denunciar(id_avaliacao){
    let rota = "/denunciar/" + id_avaliacao;

    // chamando backend para salvar a tarefa
    const retorno = await fetch(BACKEND_URL + rota,{method: 'PUT',});

    // pegando o retorno do backend
    const json_retorno = await retorno.json();
    let mensagem = json_retorno.mensagem;
    alert(mensagem);
    avaliacao_carregar_lista_avaliacoes(id_filme_selecionado);
}

async function inofensivo(id){
    if(tabela_alertas){
        let rota = "/inofensivo/" + id;
        let metodo = "PUT";

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota,{method: metodo});

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        mostrar_mensagem(json_retorno.mensagem);
        if(json_retorno.resultado){
            avaliacao_carregar_lista_alertas();
        }
    }
}

async function ofensino(id){
    if(tabela_alertas){
        let rota = "/ofensivo/" + id;
        let metodo = "PUT";

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota,{method: metodo});

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        mostrar_mensagem(json_retorno.mensagem);
        if(json_retorno.resultado){
            avaliacao_carregar_lista_alertas();
        }
    }
}

//metodos para tela de registro de novo usuario
function avaliacao_registrar_limpar_tela(event){
    event.preventDefault();
    if(formulario_avaliacao){
        document.getElementById("nota").value = "";
        document.getElementById("comentario").value = "";
    }
}

async function avaliacao_registrar_salvar(event){
    event.preventDefault();
    if(formulario_avaliacao){
        let rota = "/novo";
        let metodo = "POST";
        let nota = document.getElementById("nota").value;
        let comentario = document.getElementById("comentario").value;
        
        let avaliacao = {
            nota:nota,
            filme_id:id_filme_selecionado,
            comentario:comentario
        }

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota,{
            method: metodo,
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(avaliacao)
        });

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        mostrar_mensagem(json_retorno.mensagem);
        avaliacao_registrar_limpar_tela(event);
        avaliacao_carregar_lista_avaliacoes(id_filme_selecionado);
    }
}

avaliacao_carregar_lista_alertas();
avaliacao_carregar_lista_avaliacoes(id_filme_selecionado);
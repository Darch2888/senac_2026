BACKEND_URL = "http://localhost:5000/tarefa";
tabelaTarefas = document.getElementById("listaTarefas");

function mostrar_mensagem(mensagem){
    alert(mensagem);
}

function atualizar_tabela(tarefas){
    if(tarefas){
        tabelaTarefas.innerHTML = "";
        tarefas.forEach(tarefa => {

            if(tarefa.finalizada == "S"){
                disabled_finalizar = "disabled";
                disabled_editar = "disabled";
                disabled_excluir = "disabled";
                disabled_reabrir = ""
            }else{
                disabled_finalizar = "";
                disabled_editar = "";
                disabled_excluir = "";
                disabled_reabrir = "disabled"
            };
            
            tabelaTarefas.innerHTML += `
                <tr>
                    <td>${tarefa.id}</td>
                    <td>${tarefa.nome}</td>
                    <td>${tarefa.prioridade}</td>
                    <td>${tarefa.finalizada}</td>
                    <td>
                        <button class="btn btn-sn btn-primary btn-sm" onclick="finalizar(${tarefa.id})" ${disabled_finalizar}>Finalizar</button>
                        <button class="btn btn-sn btn-warning btn-sm" onclick="editar(${tarefa.id})" ${disabled_editar}>Editar</button>
                        <button class="btn btn-sn btn-danger btn-sm" onclick="excluir(${tarefa.id})" ${disabled_excluir}>Excluir</button>
                        <button class="btn btn-sn btn-success btn-sm" onclick="reabrir(${tarefa.id})" ${disabled_reabrir}>Reabrir</button>
                    </td>
                </tr>
            `;
        });
    }else {
        tabelaTarefas.innerHTML = ``;
    }
}

async function listarPendentes(){
    // carregando tabela
    const retorno = await fetch(BACKEND_URL + '/pendentes',{method: "GET"});
    const dados = await retorno.json();
    tarefas = dados.tarefas;
    atualizar_tabela(tarefas);   
}

async function listarFinalizadas(){
    // carregando tabela
    const retorno = await fetch(BACKEND_URL + '/finalizadas',{method: "GET"});
    const dados = await retorno.json();
    tarefas = dados.tarefas;
    atualizar_tabela(tarefas);   
}


//funcao para buscar uma tarefa pelo id e preencher o formulario para edicao
async function editar(id){
    const retorno = await fetch(BACKEND_URL + `/detalhe/${id}`,{method: "GET"});
    const dados = await retorno.json();
    tarefa = dados.tarefa;
    if (tarefa) {
        document.getElementById("id").value = tarefa.id;
        document.getElementById("nome").value = tarefa.nome;
        document.getElementById("prioridade").value = tarefa.prioridade;
    }
}

function limparFormulario(){
    document.getElementById("id").value = "";
    document.getElementById("nome").value = "";
    document.getElementById("prioridade").value = "";
}


// funcao javascript para salvar uma tarefa
async function salvar(){
    // pegando valores do formulario
    let id = document.getElementById("id").value;
    let nome = document.getElementById("nome").value;
    let prioridade = document.getElementById("prioridade").value;

    // verificando se é uma tarefa nova ou uma alteração
    if (id) {
        metodo = "PUT";
        rota = `/alterar`;
        tarefa = {
            id:id,
            nome:nome,
            prioridade:prioridade
        }
    }else{
        metodo = "POST";
        rota = `/salvar`;
        tarefa = {
            nome:nome,
            prioridade:prioridade
        }
    }
    // chamando backend para salvar a tarefa
    const retorno = await fetch(BACKEND_URL + rota,{
            method: metodo,
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(tarefa)
        });

    // pegando o retorno do backend
    const json_retorno = await retorno.json();
    mostrar_mensagem(json_retorno.mensagem);

    limparFormulario();
    listarPendentes();
}

async function excluir(id){
    // carregando tabela
    const retorno = await fetch(BACKEND_URL + `/excluir/${id}`,{method: "DELETE"});
    const dados = await retorno.json();
    mensagem = dados.mensagem;
    mostrar_mensagem(mensagem);
    listarPendentes();   
}

async function reabrir(id){
    // carregando tabela
    const retorno = await fetch(BACKEND_URL + `/reabrir/${id}`,{method: "PATCH"});
    const dados = await retorno.json();
    mensagem = dados.mensagem;
    mostrar_mensagem(mensagem);
    listarPendentes();   
}

async function finalizar(id){
    // carregando tabela
    const retorno = await fetch(BACKEND_URL + `/finalizar/${id}`,{method: "PATCH"});
    const dados = await retorno.json();
    mensagem = dados.mensagem;
    mostrar_mensagem(mensagem);
    listarPendentes();   
}

listarPendentes();
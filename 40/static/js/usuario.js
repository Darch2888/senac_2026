BACKEND_URL = "http://127.0.0.1:5000/usuario";
tabela_usuarios = document.getElementById("listaUsuarios");
formulario_registro = document.getElementById("frmRegistro");
formulario_login = document.getElementById("frmLogin");
formulario_perfil = document.getElementById("frmPerfil");
formulario_gerencial = document.getElementById("frmGerencial");

function mostrar_mensagem(mensagem){
    alert(mensagem);
}

//metodos para tela de registro de novo usuario
function usuario_registrar_limpar_tela(event){
    event.preventDefault();
    if(formulario_registro){
        document.getElementById("nome").value = "";
        document.getElementById("email").value = "";
        document.getElementById("senha").value = "";
    }
}

async function usuario_registrar_salvar(event){
    event.preventDefault();

    if(formulario_registro){
        let rota = "/novo";
        let metodo = "POST";
        let nome = document.getElementById("nome").value;
        let email = document.getElementById("email").value;
        let senha = document.getElementById("senha").value;
        
        let usuario = {
            nome:nome,
            email:email,
            senha:senha
        }

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota,{
            method: metodo,
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(usuario)
        });

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        mostrar_mensagem(json_retorno.mensagem);
        usuario_registrar_limpar_tela(event);
    }
}

//metodos para tela de login
function usuario_login_limpar_tela(event){
    event.preventDefault();
    if(formulario_login){
        document.getElementById("email").value = "";
        document.getElementById("senha").value = "";
    }
}

async function usuario_logon(event){
    event.preventDefault();
    if(formulario_login){
        let rota = "/logon";
        let metodo = "POST";
        let email = document.getElementById("email").value;
        let senha = document.getElementById("senha").value;
        
        let usuario = {
            email:email,
            senha:senha
        }

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota,{
            method: metodo,
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(usuario)
        });

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        mostrar_mensagem(json_retorno.mensagem);
        if(json_retorno.resultado){
            window.location.href = "/";
        }else{
            usuario_login_limpar_tela(event);
        }
    }
}

//metodos para tela de perfil
async function usuario_perfil_carregar_dados(){
    if(formulario_perfil){
        let rota = "/perfil";
        let metodo = "GET";

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota);

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        mostrar_mensagem(json_retorno.mensagem);
        if(json_retorno.resultado){            
            document.getElementById("id").value = json_retorno.usuario.id;
            document.getElementById("nome").value = json_retorno.usuario.nome;
            document.getElementById("email").value = json_retorno.usuario.email;
            document.getElementById("senha").value = "";
        }
    }
}

async function usuario_perfil_atualizar_senha(event){
    event.preventDefault();
    if(formulario_perfil){
        let rota = "/alterar_senha";
        let metodo = "PUT";
        let id = document.getElementById("id").value;
        let senha = document.getElementById("senha").value;
        
        let usuario = {
            id:id,
            senha:senha
        }

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota,{
            method: metodo,
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(usuario)
        });

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        mostrar_mensagem(json_retorno.mensagem);
    }
}

//metodos para tela de gerenciamento
async function usuario_gerenciar_carregar_usuarios(){
    if(formulario_gerencial){
        let rota = "/listar";

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota);

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        let usuarios = json_retorno.usuarios;

        if(usuarios){
            tabela_usuarios.innerHTML = "";            
            usuarios.forEach(usuario => {  

                disabled_bloquear = "";
                disabled_desbloquear = "";
                if(usuario.bloqueado == "S"){
                    disabled_bloquear = "disabled";
                }else{
                    disabled_desbloquear = "disabled";
                };
                
                tabela_usuarios.innerHTML += `
                    <tr>
                        <td>${usuario.id}</td>
                        <td>${usuario.nome}</td>
                        <td>${usuario.email}</td>
                        <td>${usuario.perfil}</td>
                        <td>
                            <button class="btn btn-sn btn-primary btn-sm" onclick="editar(${usuario.id})" >Editar</button>
                            <button class="btn btn-sn btn-success btn-sm" onclick="desbloquear(${usuario.id})" ${disabled_desbloquear}>Desbloquear</button>
                            <button class="btn btn-sn btn-warning btn-sm" onclick="bloquear(${usuario.id})" ${disabled_bloquear}>Bloquear</button>
                            <button class="btn btn-sn btn-danger btn-sm" onclick="excluir(${usuario.id})" >Excluir</button>
                        </td>
                    </tr>
                `;
            });
        }else {
            tabela_usuarios.innerHTML = ``;
        }        
    }
}

async function excluir(id){
    if(formulario_gerencial){
        let rota = "/excluir/" + id;
        let metodo = "DELETE";

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota,{method: metodo});

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        mostrar_mensagem(json_retorno.mensagem);
        if(json_retorno.resultado){
            usuario_gerenciar_carregar_usuarios();
        }
    }
}

async function bloquear(id){
    if(formulario_gerencial){
        let rota = "/bloquear/" + id;
        let metodo = "PUT";

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota,{method: metodo});

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        mostrar_mensagem(json_retorno.mensagem);
        if(json_retorno.resultado){
            usuario_gerenciar_carregar_usuarios();
        }
    }
}

async function desbloquear(id){
    if(formulario_gerencial){
        let rota = "/aprovar/" + id;
        let metodo = "PUT";

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota,{method: metodo});

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        mostrar_mensagem(json_retorno.mensagem);
        if(json_retorno.resultado){
            usuario_gerenciar_carregar_usuarios();
        }
    }
}

function usuario_gerenciar_limpar_tela(event){
    event.preventDefault();
    if(formulario_gerencial){
        document.getElementById("id").value = "";
        document.getElementById("nome").value = "";
        document.getElementById("email").value = "";
        document.getElementById("perfil").value = "";
    }
}

async function editar(id){
    if(formulario_gerencial){
        const retorno = await fetch(BACKEND_URL + `/detalhe/${id}`,{method: "GET"});

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        mostrar_mensagem(json_retorno.mensagem);
        if(json_retorno.resultado){
            usuario = json_retorno.usuario;
            if (usuario) {
                document.getElementById("id").value = usuario.id;
                document.getElementById("nome").value = usuario.nome;
                document.getElementById("email").value = usuario.email;
                document.getElementById("perfil").value = usuario.perfil;
            }            
        }
    }
}

async function usuario_gerenciar_salvar(event){
    event.preventDefault();

    if(formulario_gerencial){
        let rota = "/alterar";
        let metodo = "PUT";
        let id = document.getElementById("id").value;
        let nome = document.getElementById("nome").value;
        let email = document.getElementById("email").value;
        let perfil = document.getElementById("perfil").value;
        
        let usuario = {
            id:id,
            nome:nome,
            email:email,
            login:login,
            perfil:perfil
        }

        // chamando backend para salvar a tarefa
        const retorno = await fetch(BACKEND_URL + rota,{
            method: metodo,
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(usuario)
        });

        // pegando o retorno do backend
        const json_retorno = await retorno.json();
        mostrar_mensagem(json_retorno.mensagem);        
        usuario_registrar_limpar_tela(event);        
        usuario_gerenciar_carregar_usuarios();
    }
}

//metodos para carregar de forma automática
usuario_perfil_carregar_dados();
usuario_gerenciar_carregar_usuarios();

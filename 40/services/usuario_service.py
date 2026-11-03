from flask import session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from conn import BD_Session
from models.usuario import Usuario

# metodos para gerenciamento
def usuario_listar():
    usuarios = []

    with BD_Session() as bd_sessao:
        dados = bd_sessao.query(Usuario).order_by(Usuario.email).all()
        if dados:
            usuarios = [usuario.to_print() for usuario in dados]

    return usuarios

def usuario_detalhe(id):
    usuario = None
    with BD_Session() as bd_sessao:
        usuario = bd_sessao.get(Usuario, id)
        if usuario:
            usuario = usuario.to_print()
    return usuario

def usuario_novo(nome, email, senha):
    resultado = False

    perfil = "USUARIO"
    bloqueado = "N"

    senha_hash = generate_password_hash(senha)

    with BD_Session() as bd_sessao:
        usuario = Usuario(nome=nome,
                          email=email,
                          senha=senha_hash,
                          perfil=perfil,
                          bloqueado=bloqueado)
        bd_sessao.add(usuario)
        bd_sessao.commit()
        resultado = True

    return resultado

def usuario_alterar(id, nome, email, perfil):
    resultado = False
    with BD_Session() as bd_sessao:
        usuario = bd_sessao.get(Usuario, id)
        if(usuario):
            usuario.nome = nome
            usuario.email = email
            usuario.perfil = perfil
            bd_sessao.commit()
            resultado = True

    return resultado

def usuario_excluir(id):
    resultado = False
    with BD_Session() as bd_sessao:
        usuario = bd_sessao.get(Usuario, id)
        if(usuario):
            bd_sessao.delete(usuario)
            bd_sessao.commit()
            resultado = True

    return resultado

def usuario_aprovar(id):
    resultado = False
    with BD_Session() as bd_sessao:
        usuario = bd_sessao.get(Usuario, id)
        if(usuario):
            usuario.bloqueado = "N"
            bd_sessao.commit()
            resultado = True

    return resultado

def usuario_bloquear(id):
    resultado = False
    with BD_Session() as bd_sessao:
        usuario = bd_sessao.get(Usuario, id)
        if(usuario):
            usuario.bloqueado = "S"
            bd_sessao.commit()
            resultado = True
            
    return resultado

# metodos de controle de acesso
def usuario_logon(email, senha):
    resultado = False
    mensagem = ""
    usuario = None
    #limpar sessao
    session.clear()

    with BD_Session() as bd_sessao:
        usuario = bd_sessao.query(Usuario).filter(Usuario.email == email).first()
        if (usuario and check_password_hash(usuario.senha, senha)):
            if usuario.bloqueado == 'N':
                session["usuario_id"] = usuario.id
                session["usuario_nome"] = usuario.nome
                session["usuario_perfil"] = usuario.perfil
                resultado = True
                mensagem = "Logon efetuado com sucesso"            
            else:
                mensagem = "Usuario bloqueado, aguarde aprovação"
        else:
            mensagem = "Usuario e senha inválidos"

    return resultado, mensagem

def usuario_perfil():
    usuario = None
    if "usuario_id" in session:
        with BD_Session() as bd_sessao:
            usuario = bd_sessao.get(Usuario, session["usuario_id"])
            if usuario:
                usuario = usuario.to_print()

    return usuario

def usuario_alterar_senha(id, senha):
    resultado = False

    senha_hash = generate_password_hash(senha)

    with BD_Session() as bd_sessao:
        usuario = bd_sessao.get(Usuario, id)
        if usuario:
            usuario.senha = senha_hash
            bd_sessao.commit()
            resultado = True

    return resultado

def usuario_logout():
    session.clear()
    return True
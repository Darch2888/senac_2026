#verificar a primeira linha do from
#verificar por que usuario ficou estranho
from flask import session
from conn import DB_Session, SessionLocal
from usuario import Usuario
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

#listar todos os usuarios. Retorno: uma lista de dicionario de usuario
def usuario_listar():
    usuarios = []
    with DB_Session() as DB_sessao:
        dados = DB_sessao.query(Usuario).all()
        if dados:
            usuarios = [usuario.to_print() for usuario in dados]

    return usuarios

#selecionar e retornar apenas o susuario informado. Retornar dicionario com os dados do usuario
def usuario_detalhe(id):
    usuario = None
    with DB_Session() as DB_sessao:
        usuario = DB_sessao.query(Usuario, id)
        if usuario:
            usuario = usuario.to_print()
    return usuario

#criar um novo usuario com os campos informados
def usuario_novo(nome, login, senha):
    resultado = False
    perfil = "usuario"
    bloqueado = "S"

    senha_hash = generate_password_hash(senha)


    usuario = Usuario(nome=nome, 
                      login=login, 
                      senha=senha_hash, 
                      perfil=perfil, 
                      bloqueado=bloqueado)
    with DB_Session() as DB_sessao:
        DB_sessao.add(usuario)
        DB_sessao.commit()
        resultado = True

    return resultado

#alterar o usuario informado, apenas esses campos
def usuario_alterar(id, nome, login, perfil):
    resultado = False
    with DB_Session() as DB_sessao:
        usuario = DB_sessao.query(Usuario).get(Usuario, id)
        if (usuario):
            usuario.nome = nome
            usuario.login = login
            usuario.perfil = perfil
            DB_sessao.commit()
            resultado = True
    return resultado

#alterar o valor do campo bloqueano para N para o usuario informado
def usuario_aprovar(id):
    resultado = False
    with DB_Session() as DB_sessao:
        usuario = DB_sessao.query(Usuario).get(Usuario, id)
        if (usuario):
            usuario.bloqueado = 'N'
            DB_sessao.commit()
            resultado = True
    return resultado

#alterar o valor do campo bloqueano para S para o usuario informado
def usuario_bloquear(id):
    resultado = False
    with DB_Session() as DB_sessao:
        usuario = DB_sessao.query(Usuario).get(Usuario, id)
        if (usuario):
            usuario.bloqueado = 'S'
            DB_sessao.commit()
            resultado = True
    return resultado

#adicionar excluir
def usuario_excluir(id):
    resultado = False
    with DB_Session() as DB_sessao:
        usuario = DB_sessao.query(Usuario).get(Usuario, id)
        if (usuario):
            DB_sessao.delete(usuario)
            DB_sessao.commit()
            resultado = True
    return resultado

#verificar se está certo
#verificiar se usuario e senha existem no banco
def usuario_logon(login, senha):
    
    resultado = False
    mensagem = ""
    usuario = None
    session.clear()

    with DB_Session() as DB_sessao:
        usuario = DB_sessao.query(Usuario).filter(Usuario.login==login).first()
        if (usuario and check_password_hash(usuario.senha, senha)):
            if usuario.bloqueado == 'N':
                session["usuario_id"] = usuario.id
                session["usuario_nome"] = usuario.nome
                session["usuario_perfil"] = usuario.perfil
                resultado = True
                mensagem = "login realizado com sucesso"
            else:
                mensagem = "usuario bloqueado"
        else:
            mensagem = "usuario ou senha incorretos"

    return resultado

#selecionar e retornar apenas o usuario informado
def usuario_perfil():
    usuario = None
    if "usuario_id" in session:
        with DB_Session() as DB_sessao:
            usuario = DB_sessao.get(Usuario, session["usuario_id"])
            if usuario:
                usuario = usuario.to_print()
    return usuario

#alterar senha
def usuario_alterar_senha(id, senha):
    resultado = False
    
    senha_hash = generate_password_hash(senha)

    with DB_Session() as DB_sessao:
        usuario = DB_sessao.get(Usuario, id)
        if usuario:
            usuario.senha = senha_hash
            DB_sessao.commit()
            resultado = True
    return resultado

def usuario_logout():
    session.clear()
    return True
from conn import SessionLocal
from services.usuario_service import Usuario

def usuario_registrar(nome, login, senha):
    resultado = False
    with SessionLocal() as sessao:
        usuario = Usuario(nome=nome, login=login, senha=senha)
        sessao.add(usuario)
        sessao.commit()
        resultado = True
    return resultado

def usuario_login(login,senha):
    resultado = False
    with SessionLocal() as sessao:
        usuario = sessao.query(Usuario).filter(Usuario.login == login,
                                                Usuario.senha == senha).first()
        if usuario:
            resultado = True
    return resultado
from functools import wraps
from flask import session
from sqlalchemy import func

def role_required(role):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            if session.get("usuario_perfil") != role:
                print("Acesso Negado: Usuário não possui o perfil necessário.")
                return "Acesso Negado", 403
            return func(*args, **kwargs)
        return wrapper
    return decorator

def admin_required(func):
    return role_required("ADMIN")(func)

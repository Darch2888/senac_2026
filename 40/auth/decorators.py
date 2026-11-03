from functools import wraps
from flask import session

def role_required(perfis):
    if isinstance(perfis, str):
        perfis = [perfis]

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if session.get("usuario_perfil") not in perfis:
                return "Acesso Negado", 403

            return func(*args, **kwargs)

        return wrapper
    return decorator

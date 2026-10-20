from flask import Flask, session, request, redirect, url_for

rotas_publicas = ["static",
                  "usuario_routes.rota_usuario_login",
                  "usuario_routes.rota_usuario_registro",
                  "usuario_routes.rota_usuario_logon",
                  "usuario_routes.rota_usuario_logout"]

def register_middlewares(app):
    
    @app.before_request
    def verificar_autenticacao():
        if request.endpoint not in rotas_publicas:
            if "usuario_id" not in session:
                return redirect(url_for("usuario_routes.rota_usuario_login"))
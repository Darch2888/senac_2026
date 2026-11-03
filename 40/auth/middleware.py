from flask import Flask, session, request, redirect, url_for

rotas_publicas = ["static",
                  #inicio das rotas basica dos sites
                  "index",
                  "filme_routes.rota_filme_listar",
                  "filme_routes.rota_filme_listar_top5",
                  "filme_routes.rota_filme_pesquisar",
                  "avaliacao_routes.rota_avaliacao_ver",
                  "avaliacao_routes.rota_avaliacao_listar",
                  "avaliacao_routes.rota_avaliacao_denunciar",
                  #inicio das rotas acesso
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

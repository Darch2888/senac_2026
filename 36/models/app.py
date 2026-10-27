from flask import Flask, Blueprint
from flask_cors import CORS
from routes.usuario_route import usuario_routes

app = Flask(__name__)
CORS(app)
app.register_blueprint(usuario_routes)

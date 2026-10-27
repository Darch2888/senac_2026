from flask import Flask, Blueprint, jsonify, render_template, request
from flask_cors import CORS
from routes.tarefa_routes import tarefa_routes

# construindo a aplicação flask
app = Flask(__name__)
CORS(app) 

app.register_blueprint(tarefa_routes, url_prefix='/tarefa')

@app.route('/')
def principal():
    return render_template('tarefa.html')

if __name__ == '__main__':
    app.run(debug=True)
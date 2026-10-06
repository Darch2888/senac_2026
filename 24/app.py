from flask import Flask, jsonify
from flask_cors import CORS

# Criando o backend
app = Flask(__name__)
CORS(app)

@app.route('/')
def principal():
    return jsonify({'mensagem': 'Servidor Funcionando'})

@app.route('/dobro/<int:num>')
def dobro(num):
    resultado = num * 2
    return jsonify([{'mensagem': f'o dobro de {num} = {resultado}'}])

if __name__ == '__main__':
    app.run(debug=True)

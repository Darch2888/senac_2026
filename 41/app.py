from flask import Flask, jsonify, render_template
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"mensagem":"backend funcionando"})

@app.errorhandler(404)
def mensagem_rota_invalida(error):
    return render_template('404.html'), 404

@app.route('/teste')
def calculo():
    return 2 / 0

@app.errorhandler(500)
def mensagem_erro_interno(error):
    mensagem = str(error)
    tb_mensagem = traceback.format_exc()
    return render_template('500.html', erro=mensagem, tb=tb_mensagem), 500


if __name__ == "__main__":
    app.run(debug=False)
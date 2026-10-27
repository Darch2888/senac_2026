from flask import Blueprint, request, jsonify
import services.agendamento_service as service

agendamento_routes = Blueprint('agendamento_routes', __name__)

@agendamento_routes.route('/medicos', methods=['GET'])
def get_medicos():
    try:
        return jsonify(service.listar_medicos()), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@agendamento_routes.route('/agendar', methods=['POST'])
def post_agendar():
    try:
        agendamento = service.agendar_consulta(request.get_json())
        return jsonify({'mensagem': 'Consulta agendada com sucesso!', 'disponivel': True, 'agendamento': agendamento}), 201
    except ValueError as ve:
        return jsonify({'erro': str(ve)}), 400
    except PermissionError as pe:
        return jsonify({'erro': str(pe), 'disponivel': False}), 409
    except Exception:
        return jsonify({'erro': 'Erro interno no servidor ao processar o agendamento.'}), 500

@agendamento_routes.route('/agendamentos', methods=['GET'])
def get_agendamentos():
    try:
        return jsonify(service.listar_agendamentos()), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@agendamento_routes.route('/agendamentos/<id_agendamento>/cancelar', methods=['PUT'])
def put_cancelar(id_agendamento):
    try:
        service.cancelar_agendamento(id_agendamento)
        return jsonify({'mensagem': 'Agendamento cancelado com sucesso.'}), 200
    except Exception:
        return jsonify({'erro': 'Erro ao cancelar agendamento.'}), 500
from flask import Blueprint, request, jsonify
import services.agendamento_service as service

agendamento_routes = Blueprint('agendamento_routes', __name__)

@agendamento_routes.route('/medicos', methods=['GET'])
def get_medicos():
    apenas_ativos = request.args.get('ativos', 'true').lower() == 'true'
    try:
        return jsonify(service.listar_medicos(apenas_ativos)), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@agendamento_routes.route('/medicos', methods=['POST'])
def post_medico():
    try:
        novo_medico = service.adicionar_medico(request.get_json())
        return jsonify({'mensagem': 'Médico adicionado!', 'medico': novo_medico}), 201
    except ValueError as ve:
        return jsonify({'erro': str(ve)}), 400
    except Exception as e:
        return jsonify({'erro': 'Erro interno.'}), 500

@agendamento_routes.route('/medicos/<id_medico>/status', methods=['PUT'])
def put_medico_status(id_medico):
    try:
        status = request.get_json().get('status')
        service.alterar_status_medico(id_medico, status)
        return jsonify({'mensagem': 'Status atualizado.'}), 200
    except Exception as e:
        return jsonify({'erro': 'Erro interno.'}), 500

@agendamento_routes.route('/estatisticas', methods=['GET'])
def get_estatisticas():
    try:
        return jsonify(service.obter_estatisticas_admin()), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@agendamento_routes.route('/agendar', methods=['POST'])
def post_agendar():
    try:
        agendamento = service.agendar_consulta(request.get_json())
        return jsonify({'mensagem': 'Sucesso!', 'disponivel': True, 'agendamento': agendamento}), 201
    except ValueError as ve:
        return jsonify({'erro': str(ve)}), 400
    except PermissionError as pe:
        return jsonify({'erro': str(pe), 'disponivel': False}), 409
    except Exception:
        return jsonify({'erro': 'Erro interno no servidor.'}), 500

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
        return jsonify({'mensagem': 'Cancelado com sucesso.'}), 200
    except Exception:
        return jsonify({'erro': 'Erro ao cancelar.'}), 500
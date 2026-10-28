import uuid
from datetime import datetime, timedelta
from model import get_connection
import model.agendamento_model as model

DURACAO_CONSULTA_MINUTOS = 30

def listar_medicos(apenas_ativos=True):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        if apenas_ativos:
            return model.get_medicos_ativos(cursor)
        return model.get_todos_medicos(cursor)
    finally:
        cursor.close()
        conn.close()

def adicionar_medico(dados):
    nome = dados.get('nome_medico')
    especialidade = dados.get('especialidade')
    if not nome or not especialidade:
        raise ValueError("Nome e especialidade são obrigatórios.")
    
    conn = get_connection()
    cursor = conn.cursor()
    try:
        conn.start_transaction()
        id_medico = model.inserir_medico(cursor, nome, especialidade)
        conn.commit()
        return {'id_medico': id_medico, 'nome_medico': nome, 'especialidade': especialidade}
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def alterar_status_medico(id_medico, status):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        conn.start_transaction()
        model.atualizar_status_medico(cursor, id_medico, status)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def agendar_consulta(dados):
    nome_paciente = dados.get('nome_paciente')
    id_medico = dados.get('id_medico')
    data_consulta = dados.get('data_consulta')
    hora_consulta = dados.get('hora_consulta')

    if not all([nome_paciente, id_medico, data_consulta, hora_consulta]):
        raise ValueError("Todos os campos são obrigatórios.")

    try:
        data_hora_inicio = datetime.strptime(f"{data_consulta} {hora_consulta}", "%Y-%m-%d %H:%M")
    except ValueError:
        raise ValueError("Formato de data ou hora inválido.")

    if data_hora_inicio < datetime.now():
        raise ValueError("Não é possível agendar no passado.")

    data_hora_termino = data_hora_inicio + timedelta(minutes=DURACAO_CONSULTA_MINUTOS)
    
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        conn.start_transaction()
        conflitos = model.get_conflito_agenda(cursor, id_medico, data_hora_inicio, data_hora_termino)
        
        if conflitos:
            raise PermissionError("Horário indisponível.")

        paciente = model.get_paciente_por_nome(cursor, nome_paciente)
        id_paciente = paciente['id_paciente'] if paciente else model.criar_paciente(cursor, nome_paciente)

        id_agendamento = str(uuid.uuid4())
        model.criar_agendamento(cursor, id_agendamento, id_paciente, id_medico, data_hora_inicio, data_hora_termino)
        
        conn.commit()
        agendamento_salvo = model.get_agendamento_completo(cursor, id_agendamento)
        agendamento_salvo['data_hora_inicio'] = agendamento_salvo['data_hora_inicio'].isoformat()
        agendamento_salvo['data_hora_termino'] = agendamento_salvo['data_hora_termino'].isoformat()
        return agendamento_salvo
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def listar_agendamentos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        agendamentos = model.listar_todos_agendamentos(cursor)
        for a in agendamentos:
            a['data_hora_inicio'] = a['data_hora_inicio'].isoformat()
        return agendamentos
    finally:
        cursor.close()
        conn.close()

def cancelar_agendamento(id_agendamento):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        conn.start_transaction()
        model.atualizar_status_agendamento(cursor, id_agendamento, 'cancelado')
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def obter_estatisticas_admin():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT COUNT(*) as total FROM agendamentos")
        total_agendamentos = cursor.fetchone()['total']
        
        cursor.execute("SELECT COUNT(*) as ativos FROM medicos WHERE status_medico = 'ativo'")
        medicos_ativos = cursor.fetchone()['ativos']
        
        return {'total_agendamentos': total_agendamentos, 'medicos_ativos': medicos_ativos}
    finally:
        cursor.close()
        conn.close()
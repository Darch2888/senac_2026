def get_medicos_ativos(cursor):
    cursor.execute("SELECT id_medico, nome_medico, especialidade FROM medicos WHERE status_medico = 'ativo'")
    return cursor.fetchall()

def get_conflito_agenda(cursor, id_medico, data_hora_inicio, data_hora_termino):
    query = """
        SELECT id_agendamento FROM agendamentos 
        WHERE id_medico = %s AND status_agenda = 'confirmado'
        AND (data_hora_inicio < %s AND data_hora_termino > %s)
        FOR UPDATE
    """
    cursor.execute(query, (id_medico, data_hora_termino, data_hora_inicio))
    return cursor.fetchall()

def get_paciente_por_nome(cursor, nome_paciente):
    cursor.execute("SELECT id_paciente FROM pacientes WHERE nome_paciente = %s LIMIT 1", (nome_paciente,))
    return cursor.fetchone()

def criar_paciente(cursor, nome_paciente):
    cursor.execute("INSERT INTO pacientes (nome_paciente) VALUES (%s)", (nome_paciente,))
    return cursor.lastrowid

def criar_agendamento(cursor, id_agendamento, id_paciente, id_medico, inicio, termino):
    query = """
        INSERT INTO agendamentos (id_agendamento, id_paciente, id_medico, data_hora_inicio, data_hora_termino)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (id_agendamento, id_paciente, id_medico, inicio, termino))

def get_agendamento_completo(cursor, id_agendamento):
    query = """
        SELECT a.id_agendamento, p.nome_paciente, m.nome_medico, m.especialidade, 
               a.data_hora_inicio, a.data_hora_termino, a.status_agenda
        FROM agendamentos a
        JOIN pacientes p ON a.id_paciente = p.id_paciente
        JOIN medicos m ON a.id_medico = m.id_medico
        WHERE a.id_agendamento = %s
    """
    cursor.execute(query, (id_agendamento,))
    return cursor.fetchone()

def listar_todos_agendamentos(cursor):
    query = """
        SELECT a.id_agendamento, p.nome_paciente, m.nome_medico, m.especialidade, 
               a.data_hora_inicio, a.status_agenda
        FROM agendamentos a
        JOIN pacientes p ON a.id_paciente = p.id_paciente
        JOIN medicos m ON a.id_medico = m.id_medico
        ORDER BY a.data_hora_inicio DESC
    """
    cursor.execute(query)
    return cursor.fetchall()

def atualizar_status_agendamento(cursor, id_agendamento, status):
    cursor.execute("UPDATE agendamentos SET status_agenda = %s WHERE id_agendamento = %s", (status, id_agendamento))
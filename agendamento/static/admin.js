const API_URL = '/api';

document.addEventListener('DOMContentLoaded', () => {
    carregarEstatisticas();
    carregarAgendamentos();
    carregarMedicosAdmin();
});

function mudarAba(id, btn) {
    document.querySelectorAll('.aba').forEach(a => a.style.display = 'none');
    document.getElementById(`aba-${id}`).style.display = 'block';
    
    document.querySelectorAll('.sidebar .nav-item').forEach(b => b.classList.remove('ativo'));
    btn.classList.add('ativo');
}

async function carregarEstatisticas() {
    try {
        const res = await fetch(`${API_URL}/estatisticas`);
        const stats = await res.json();
        document.getElementById('stat-agendamentos').textContent = stats.total_agendamentos;
        document.getElementById('stat-medicos').textContent = stats.medicos_ativos;
    } catch (e) {
        console.error('Erro ao carregar estatísticas');
    }
}

async function carregarAgendamentos() {
    const tbody = document.querySelector('#tabela-admin-consultas tbody');
    try {
        const res = await fetch(`${API_URL}/agendamentos`);
        const agendamentos = await res.json();
        
        tbody.innerHTML = '';
        agendamentos.slice(0, 10).forEach(a => { // Mostra apenas os 10 últimos
            const dt = new Date(a.data_hora_inicio);
            const dataStr = new Intl.DateTimeFormat('pt-BR', { dateStyle: 'short', timeStyle: 'short' }).format(dt);
            tbody.innerHTML += `
                <tr>
                    <td>${dataStr}</td>
                    <td>${a.nome_paciente}</td>
                    <td>${a.nome_medico}</td>
                    <td><span class="badge ${a.status_agenda === 'confirmado' ? 'confirmado' : 'cancelado'}">${a.status_agenda}</span></td>
                </tr>
            `;
        });
    } catch (e) {
        tbody.innerHTML = '<tr><td colspan="4">Erro ao carregar consultas.</td></tr>';
    }
}

async function carregarMedicosAdmin() {
    const tbody = document.querySelector('#tabela-admin-medicos tbody');
    try {
        const res = await fetch(`${API_URL}/medicos?ativos=false`); // Busca todos, incluindo inativos
        const medicos = await res.json();
        
        tbody.innerHTML = '';
        medicos.forEach(m => {
            const isAtivo = m.status_medico === 'ativo';
            tbody.innerHTML += `
                <tr>
                    <td>#${m.id_medico}</td>
                    <td><strong>${m.nome_medico}</strong></td>
                    <td>${m.especialidade}</td>
                    <td><span class="badge ${isAtivo ? 'confirmado' : 'cancelado'}">${m.status_medico}</span></td>
                    <td>
                        <button class="btn-cancel" style="background: ${isAtivo ? '#fee2e2' : '#dcfce7'}; color: ${isAtivo ? '#991b1b' : '#166534'}; border:none;" 
                            onclick="alterarStatusMedico(${m.id_medico}, '${isAtivo ? 'inativo' : 'ativo'}')">
                            ${isAtivo ? 'Desativar' : 'Ativar'}
                        </button>
                    </td>
                </tr>
            `;
        });
    } catch (e) {
        tbody.innerHTML = '<tr><td colspan="5">Erro ao carregar médicos.</td></tr>';
    }
}

document.getElementById('form-novo-medico').addEventListener('submit', async (e) => {
    e.preventDefault();
    const payload = {
        nome_medico: document.getElementById('novo_nome_medico').value,
        especialidade: document.getElementById('nova_especialidade').value
    };

    try {
        const res = await fetch(`${API_URL}/medicos`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        if (res.ok) {
            alert('Médico adicionado com sucesso!');
            e.target.reset();
            carregarMedicosAdmin();
            carregarEstatisticas();
        }
    } catch (e) {
        alert('Erro ao adicionar médico.');
    }
});

async function alterarStatusMedico(id, novoStatus) {
    try {
        const res = await fetch(`${API_URL}/medicos/${id}/status`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ status: novoStatus })
        });
        if (res.ok) {
            carregarMedicosAdmin();
            carregarEstatisticas();
        }
    } catch (e) {
        alert('Erro ao atualizar status.');
    }
}
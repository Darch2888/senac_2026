const API_URL = '/api';

// Elementos
const ui = {
    form: document.getElementById('form-agendamento'),
    selectMedico: document.getElementById('id_medico'),
    btnAgendar: document.getElementById('btn-agendar'),
    inputData: document.getElementById('data_consulta'),
    tabelaConsultas: document.querySelector('#tabela-consultas tbody'),
    pesquisa: document.getElementById('filtro-paciente')
};

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    bloquearDiasPassados();
    carregarMedicos();
    configurarNavegacao();
});

// Impede seleção de dias que já passaram
function bloquearDiasPassados() {
    const hoje = new Date().toISOString().split('T')[0];
    ui.inputData.setAttribute('min', hoje);
}

// Navegação de Telas
function configurarNavegacao() {
    document.getElementById('btn-nav-agendar').addEventListener('click', (e) => mudarTela('tela-agendamento', e.target));
    document.getElementById('btn-nav-consultas').addEventListener('click', (e) => {
        mudarTela('tela-lista-consultas', e.target);
        carregarAgendamentos();
    });
    document.getElementById('btn-novo-agendamento').addEventListener('click', () => {
        ui.form.reset();
        mudarTela('tela-agendamento', document.getElementById('btn-nav-agendar'));
    });
}

function mudarTela(idTela, btnAtivo) {
    document.querySelectorAll('.tela').forEach(t => t.classList.remove('ativa'));
    document.getElementById(idTela).classList.add('ativa');
    document.querySelectorAll('.nav-item').forEach(b => b.classList.remove('ativo'));
    if (btnAtivo) btnAtivo.classList.add('ativo');
}

// Sistema de Notificações (Toast)
function mostrarToast(mensagem, tipo = 'sucesso') {
    const container = document.getElementById('toast-container');
    const toast = document.createElement('div');
    toast.className = `toast ${tipo}`;
    
    const icone = tipo === 'sucesso' ? 'ph-check-circle' : 'ph-warning-circle';
    toast.innerHTML = `<i class="ph ${icone}"></i> <span>${mensagem}</span>`;
    
    container.appendChild(toast);

    setTimeout(() => {
        toast.classList.add('fade-out');
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}

// Controla visual de "Carregando" nos botões
function setCarregando(botao, carregando, textoOriginal) {
    if (carregando) {
        botao.disabled = true;
        botao.innerHTML = `<i class="ph ph-spinner ph-spin"></i> Processando...`;
    } else {
        botao.disabled = false;
        botao.innerHTML = textoOriginal;
    }
}

// Consumo de API: Médicos
async function carregarMedicos() {
    try {
        const res = await fetch(`${API_URL}/medicos`);
        const medicos = await res.json();
        
        ui.selectMedico.innerHTML = '<option value="" disabled selected>Selecione um especialista</option>';
        medicos.forEach(m => {
            ui.selectMedico.innerHTML += `<option value="${m.id_medico}">${m.nome_medico} (${m.especialidade})</option>`;
        });
    } catch (e) {
        mostrarToast('Falha ao comunicar com o servidor.', 'erro');
    }
}

// Consumo de API: Realizar Agendamento
ui.form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Validação de data manual para horário passado no dia de hoje
    const dataEscolhida = new Date(`${ui.inputData.value}T${document.getElementById('hora_consulta').value}:00`);
    if (dataEscolhida < new Date()) {
        mostrarToast('O horário selecionado já passou.', 'erro');
        return;
    }

    const payload = {
        nome_paciente: document.getElementById('nome_paciente').value.trim(),
        id_medico: ui.selectMedico.value,
        data_consulta: ui.inputData.value,
        hora_consulta: document.getElementById('hora_consulta').value
    };

    const textoBtnOriginal = ui.btnAgendar.innerHTML;
    setCarregando(ui.btnAgendar, true, textoBtnOriginal);

    try {
        const response = await fetch(`${API_URL}/agendar`, {
            method: 'POST', 
            headers: { 'Content-Type': 'application/json' }, 
            body: JSON.stringify(payload)
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            mostrarToast(data.erro, 'erro');
            setCarregando(ui.btnAgendar, false, textoBtnOriginal);
            return;
        }

        mostrarToast('Consulta confirmada com sucesso!');
        exibirConfirmacao(data.agendamento);
    } catch (error) {
        mostrarToast('Erro de conexão ao processar agendamento.', 'erro');
    } finally {
        setCarregando(ui.btnAgendar, false, textoBtnOriginal);
    }
});

function exibirConfirmacao(dados) {
    document.getElementById('conf-codigo').textContent = dados.id_agendamento.split('-')[0].toUpperCase();
    document.getElementById('conf-paciente').textContent = dados.nome_paciente;
    document.getElementById('conf-medico').textContent = dados.nome_medico;
    
    const dataFormatada = new Intl.DateTimeFormat('pt-BR', { dateStyle: 'short' }).format(new Date(dados.data_hora_inicio));
    const horaFormatada = new Intl.DateTimeFormat('pt-BR', { timeStyle: 'short' }).format(new Date(dados.data_hora_inicio));
    
    document.getElementById('conf-data').textContent = dataFormatada;
    document.getElementById('conf-hora').textContent = horaFormatada;
    
    mudarTela('tela-confirmacao');
}

// Consumo de API: Listar Agendamentos
async function carregarAgendamentos() {
    ui.tabelaConsultas.innerHTML = '<tr><td colspan="5" class="text-center"><i class="ph ph-spinner ph-spin"></i> Carregando registros...</td></tr>';
    
    try {
        const response = await fetch(`${API_URL}/agendamentos`);
        let agendamentos = await response.json();
        
        const termoBusca = ui.pesquisa.value.toLowerCase();
        if (termoBusca) {
            agendamentos = agendamentos.filter(a => a.nome_paciente.toLowerCase().includes(termoBusca));
        }
        
        ui.tabelaConsultas.innerHTML = '';
        if (agendamentos.length === 0) {
            ui.tabelaConsultas.innerHTML = '<tr><td colspan="5" style="text-align: center; color: #64748b;">Nenhuma consulta localizada.</td></tr>';
            return;
        }

        agendamentos.forEach(a => {
            const dt = new Date(a.data_hora_inicio);
            const dataStr = new Intl.DateTimeFormat('pt-BR').format(dt);
            const horaStr = new Intl.DateTimeFormat('pt-BR', {timeStyle: 'short'}).format(dt);
            const isConfirmado = a.status_agenda === 'confirmado';

            ui.tabelaConsultas.innerHTML += `
                <tr>
                    <td><strong>${dataStr}</strong><br><small style="color: #64748b">${horaStr}</small></td>
                    <td>${a.nome_paciente}</td>
                    <td>${a.nome_medico}<br><small style="color: #64748b">${a.especialidade}</small></td>
                    <td><span class="badge ${isConfirmado ? 'confirmado' : 'cancelado'}">${isConfirmado ? 'Confirmado' : 'Cancelado'}</span></td>
                    <td>
                        ${isConfirmado ? 
                        `<button class="btn-cancel" onclick="cancelarAgendamento('${a.id_agendamento}')">
                            <i class="ph ph-x"></i> Cancelar
                        </button>` : '-'}
                    </td>
                </tr>
            `;
        });
    } catch (e) {
        ui.tabelaConsultas.innerHTML = '<tr><td colspan="5" style="color: red; text-align: center;">Erro ao carregar dados.</td></tr>';
    }
}

// Filtro em tempo real
ui.pesquisa.addEventListener('input', carregarAgendamentos);
document.getElementById('btn-atualizar-lista').addEventListener('click', carregarAgendamentos);

// Consumo de API: Cancelar
async function cancelarAgendamento(id) {
    if (!confirm('Deseja realmente cancelar esta consulta? A ação não pode ser desfeita.')) return;
    
    try {
        const response = await fetch(`${API_URL}/agendamentos/${id}/cancelar`, { method: 'PUT' });
        if (response.ok) {
            mostrarToast('Consulta cancelada com sucesso.', 'sucesso');
            carregarAgendamentos();
        } else {
            mostrarToast('Erro ao tentar cancelar.', 'erro');
        }
    } catch (e) {
        mostrarToast('Erro de conexão.', 'erro');
    }
}
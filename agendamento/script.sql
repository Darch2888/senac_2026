DROP database IF exists clinica_db; 
CREATE DATABASE clinica_db;
USE clinica_db;

CREATE TABLE medicos (
    id_medico INT AUTO_INCREMENT PRIMARY KEY,
    nome_medico VARCHAR(100) NOT NULL,
    especialidade VARCHAR(100) NOT NULL,
    status_medico ENUM('ativo', 'inativo') DEFAULT 'ativo'
);

CREATE TABLE pacientes (
    id_paciente INT AUTO_INCREMENT PRIMARY KEY,
    nome_paciente VARCHAR(100) NOT NULL,
    status_paciente ENUM('ativo', 'inativo') DEFAULT 'ativo'
);

CREATE TABLE agendamentos (
    id_agendamento VARCHAR(36) PRIMARY KEY, -- UUID
    id_paciente INT NOT NULL,
    id_medico INT NOT NULL,
    data_hora_inicio DATETIME NOT NULL,
    data_hora_termino DATETIME NOT NULL,
    status_agenda ENUM('confirmado', 'cancelado') DEFAULT 'confirmado',
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
    FOREIGN KEY (id_medico) REFERENCES medicos(id_medico)
);

-- Índices para otimizar busca de conflitos de horário
CREATE INDEX idx_medico_data ON agendamentos(id_medico, data_hora_inicio, data_hora_termino);

-- Inserindo médicos de teste
INSERT INTO medicos (nome_medico, especialidade) VALUES 
('Dra. Ana Silva', 'Cardiologia'),
('Dr. Carlos Souza', 'Ortopedia'),
('Dra. Beatriz Costa', 'Dermatologia');
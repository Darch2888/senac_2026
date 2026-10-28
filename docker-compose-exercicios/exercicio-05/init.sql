USE senac_db;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    status VARCHAR(20) DEFAULT 'ativo',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO usuarios (nome, email, status) VALUES
    ('Ana Silva', 'ana.silva@email.com', 'ativo'),
    ('Bruno Santos', 'bruno.santos@email.com', 'ativo'),
    ('Carlos Oliveira', 'carlos.oliveira@email.com', 'pendente'),
    ('Diana Costa', 'diana.costa@email.com', 'ativo'),
    ('Eduardo Lima', 'eduardo.lima@email.com', 'inativo');

SELECT 'Banco criado e populado!' AS mensagem;

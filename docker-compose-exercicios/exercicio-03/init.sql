-- Script de inicialização do banco
CREATE TABLE IF NOT EXISTS teste (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mensagem VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO teste (mensagem) VALUES
    ('Dados iniciais carregados!'),
    ('Este dado persiste após docker-compose down'),
    ('Use -v para limpar volumes');

SELECT 'Banco inicializado com sucesso!' AS status;

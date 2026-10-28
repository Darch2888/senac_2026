-- ============================================
-- Senac 2026 - Banco de Dados de Exemplo
-- ============================================

USE senac_db;

-- ============================================
-- Tabela: alunos
-- ============================================
CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    nota1 DECIMAL(4,2) DEFAULT 0.00,
    nota2 DECIMAL(4,2) DEFAULT 0.00,
    media DECIMAL(4,2) DEFAULT 0.00,
    situacao VARCHAR(20) DEFAULT 'Reprovado',
    data_cadastro DATE DEFAULT (CURRENT_DATE)
);

-- ============================================
-- Tabela: produtos
-- ============================================
CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10,2) NOT NULL,
    estoque INT DEFAULT 0,
    categoria VARCHAR(50),
    ativo BOOLEAN DEFAULT TRUE
);

-- ============================================
-- Tabela: livros (para exercícios de strings)
-- ============================================
CREATE TABLE IF NOT EXISTS livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    editora VARCHAR(100),
    local_publicacao VARCHAR(100),
    ano_publicacao INT,
    isbn VARCHAR(20)
);

-- ============================================
-- Tabela: numeros (para exercícios matemáticos)
-- ============================================
CREATE TABLE IF NOT EXISTS numeros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    x INT,
    y INT,
    z INT,
    descricao VARCHAR(100)
);

-- ============================================
-- POPULAR DADOS DE EXEMPLO
-- ============================================

-- Alunos
INSERT INTO alunos (nome, email, nota1, nota2, media, situacao) VALUES
('Ana Silva', 'ana.silva@email.com', 8.5, 9.0, 8.75, 'Aprovado'),
('Bruno Santos', 'bruno.santos@email.com', 6.5, 7.5, 7.00, 'Aprovado'),
('Carlos Oliveira', 'carlos.oliveira@email.com', 5.0, 6.0, 5.50, 'Reprovado'),
('Diana Costa', 'diana.costa@email.com', 9.5, 8.0, 8.75, 'Aprovado'),
('Eduardo Lima', 'eduardo.lima@email.com', 4.5, 5.5, 5.00, 'Reprovado'),
('Fernanda Gomes', 'fernanda.gomes@email.com', 7.0, 8.0, 7.50, 'Aprovado'),
('Gabriel Rocha', 'gabriel.rocha@email.com', 3.0, 4.5, 3.75, 'Reprovado'),
('Helena Martins', 'helena.martins@email.com', 10.0, 9.5, 9.75, 'Aprovado');

-- Produtos
INSERT INTO produtos (nome, descricao, preco, estoque, categoria) VALUES
('Notebook Dell', 'Intel i5, 8GB RAM, 256GB SSD', 3500.00, 15, 'Eletrônicos'),
('Mouse Logitech', 'Wireless, ergonômico', 89.90, 50, 'Periféricos'),
('Teclado Mecânico', 'Switches Blue, RGB', 299.00, 30, 'Periféricos'),
('Monitor LG 24"', 'Full HD, IPS', 899.00, 20, 'Eletrônicos'),
('HD Externo 1TB', 'USB 3.0, portátil', 349.00, 40, 'Armazenamento'),
('Impressora HP', 'Multifuncional, wireless', 599.00, 12, 'Impressoras'),
('Webcam Logitech', '1080p, micro embutido', 199.00, 25, 'Periféricos'),
('SSD 480GB', 'SATA III, 2.5"', 279.00, 35, 'Armazenamento');

-- Livros
INSERT INTO livros (titulo, autor, editora, local_publicacao, ano_publicacao, isbn) VALUES
('Python Para Todos', 'John Silva', 'Novatec', 'São Paulo', 2023, '978-85-7522-123-4'),
('Algoritmos Estruturados', 'Maria Santos', 'Campus', 'Rio de Janeiro', 2022, '978-85-352-456-7'),
('Banco de Dados MySQL', 'Pedro Costa', 'Elsevier', 'Porto Alegre', 2024, '978-85-302-789-0'),
('Estruturas de Dados', 'Ana Lima', 'Bookman', 'São Paulo', 2021, '978-85-411-012-3'),
('Programação Web', 'Carlos Souza', ' Alta Books', 'Rio de Janeiro', 2023, '978-85-508-345-6');

-- Números
INSERT INTO numeros (x, y, z, descricao) VALUES
(5, 10, 15, 'Sequência simples'),
(2, 4, 8, 'Potências de 2'),
(10, 20, 30, 'Múltiplos de 10'),
(7, 14, 21, 'Múltiplos de 7'),
(3, 6, 9, 'Múltiplos de 3');

-- ============================================
-- CRIAR VIEWS ÚTEIS
-- ============================================

CREATE OR REPLACE VIEW vw_alunos_aprovados AS
SELECT id, nome, email, media
FROM alunos
WHERE situacao = 'Aprovado';

CREATE OR REPLACE VIEW vw_alunos_reprovados AS
SELECT id, nome, email, media
FROM alunos
WHERE situacao = 'Reprovado';

CREATE OR REPLACE VIEW vw_produtos_estoque_baixo AS
SELECT id, nome, preco, estoque
FROM produtos
WHERE estoque < 20 AND ativo = TRUE;

-- ============================================
-- CRIAR PROCEDURE EXEMPLO
-- ============================================

DELIMITER //

CREATE PROCEDURE sp_atualizar_media(IN p_aluno_id INT)
BEGIN
    DECLARE v_nota1 DECIMAL(4,2);
    DECLARE v_nota2 DECIMAL(4,2);
    DECLARE v_media DECIMAL(4,2);
    DECLARE v_situacao VARCHAR(20);

    SELECT nota1, nota2 INTO v_nota1, v_nota2
    FROM alunos
    WHERE id = p_aluno_id;

    SET v_media = (v_nota1 + v_nota2) / 2;

    IF v_media >= 7 THEN
        SET v_situacao = 'Aprovado';
    ELSE
        SET v_situacao = 'Reprovado';
    END IF;

    UPDATE alunos
    SET media = v_media, situacao = v_situacao
    WHERE id = p_aluno_id;
END //

DELIMITER ;

-- ============================================
-- CONCLUSÃO
-- ============================================
SELECT 'Banco de dados criado e populado com sucesso!' AS mensagem;
SELECT COUNT(*) AS total_alunos FROM alunos;
SELECT COUNT(*) AS total_produtos FROM produtos;
SELECT COUNT(*) AS total_livros FROM livros;

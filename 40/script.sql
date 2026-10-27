drop database if exists avaliacao_filmes;
CREATE DATABASE IF NOT EXISTS avaliacao_filmes;
USE avaliacao_filmes;
 
-- TABELA DE USUARIOS
CREATE TABLE IF NOT EXISTS usuarios (
    idusuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    perfil ENUM('ADMIN', 'COMUM') NOT NULL DEFAULT 'COMUM',
    bloqueado BOOLEAN NOT NULL DEFAULT FALSE
);
 
-- TABELA DE FILMES
CREATE TABLE IF NOT EXISTS filmes (
    idfilme INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    descricao TEXT,
    descricao_breve VARCHAR(300),
    data_estreia DATE,
    url_poster TEXT,
    id_tmdb INT UNIQUE
);
 
-- TABELA DE AVALIACOES
CREATE TABLE IF NOT EXISTS avaliacoes (
    idavaliacao INT AUTO_INCREMENT PRIMARY KEY,
    data_avaliacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    comentario TEXT,
    nota DECIMAL(3,1) NOT NULL,
    alerta_ofensivo BOOLEAN NOT NULL DEFAULT FALSE,
    check_ofensivo BOOLEAN NOT NULL DEFAULT FALSE,
    idusuario INT NOT NULL,
    idfilme INT NOT NULL,
 
    CONSTRAINT fk_avaliacoes_usuario
        FOREIGN KEY (idusuario)
        REFERENCES usuarios(idusuario)
        ON DELETE CASCADE,
 
    CONSTRAINT fk_avaliacoes_filme
        FOREIGN KEY (idfilme)
        REFERENCES filmes(idfilme)
        ON DELETE CASCADE,
 
    CONSTRAINT chk_nota
        CHECK (nota >= 0 AND nota <= 10),
 
    CONSTRAINT uq_usuario_filme
        UNIQUE (idusuario, idfilme)
);
 
-- CRIAR USUARIO ADMINISTRADOR
INSERT INTO usuarios (nome, email, senha, perfil)
VALUES (
    'Administrador',
    'admin@filmes.com',
    '1234',
    'ADMIN'
);
 
-- LISTAR FILMES POR DATA DE ESTREIA
SELECT *
FROM filmes
ORDER BY data_estreia DESC;
 
-- LISTAR FILMES PELA MELHOR AVALIACAO
SELECT
    f.idfilme,
    f.titulo,
    ROUND(AVG(a.nota), 1) AS media_notas,
    COUNT(a.idavaliacao) AS total_avaliacoes
FROM filmes f
LEFT JOIN avaliacoes a
    ON f.idfilme = a.idfilme
GROUP BY f.idfilme, f.titulo
ORDER BY media_notas DESC;
 
-- LISTAR FILMES QUE O USUARIO AINDA NAO AVALIOU
SELECT f.*
FROM filmes f
WHERE NOT EXISTS (
    SELECT 1
    FROM avaliacoes a
    WHERE a.idfilme = f.idfilme
      AND a.idusuario = 1
);
 
-- LISTAR FILMES QUE O USUARIO JA AVALIOU
SELECT
    f.titulo,
    a.nota,
    a.comentario,
    a.data_avaliacao
FROM avaliacoes a
INNER JOIN filmes f
    ON f.idfilme = a.idfilme
WHERE a.idusuario = 1
ORDER BY a.data_avaliacao DESC;
 
-- LISTAR COMENTARIOS PENDENTES DE VERIFICACAO
SELECT
    a.idavaliacao,
    f.titulo,
    u.nome,
    a.comentario,
    a.alerta_ofensivo,
    a.check_ofensivo
FROM avaliacoes a
INNER JOIN filmes f
    ON f.idfilme = a.idfilme
INNER JOIN usuarios u
    ON u.idusuario = a.idusuario
WHERE a.alerta_ofensivo = TRUE
  AND a.check_ofensivo = FALSE;
 
-- CONTAR AVALIACOES DO USUARIO
SELECT
    u.idusuario,
    u.nome,
    COUNT(a.idavaliacao) AS total_avaliacoes
FROM usuarios u
LEFT JOIN avaliacoes a
    ON u.idusuario = a.idusuario
WHERE u.idusuario = 1
GROUP BY u.idusuario, u.nome;
 
-- BLOQUEAR USUARIO
UPDATE usuarios
SET bloqueado = TRUE
WHERE idusuario = 2;
 
-- DESBLOQUEAR USUARIO
UPDATE usuarios
SET bloqueado = FALSE
WHERE idusuario = 2;
 
-- CONFIRMAR AVALIACAO OFENSIVA
UPDATE avaliacoes
SET check_ofensivo = TRUE
WHERE idavaliacao = 1;
 
-- ALTERAR SENHA DE USUARIO
UPDATE usuarios
SET senha = '1234'
WHERE idusuario = 2;
 
-- CADASTRAR UMA AVALIACAO
INSERT INTO avaliacoes (
    comentario,
    nota,
    idusuario,
    idfilme
)
VALUES (
    'Filme muito bom!',
    9.0,
    1,
    1
);
 
-- SINALIZAR COMENTARIO POTENCIALMENTE OFENSIVO
UPDATE avaliacoes
SET alerta_ofensivo = TRUE
WHERE idavaliacao = 1;
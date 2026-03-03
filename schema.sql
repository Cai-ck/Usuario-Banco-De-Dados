CREATE DATABASE IF NOT EXISTS login_local;
USE login_local;

-- Tabela de Usuário
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    foto_perfil VARCHAR(255) DEFAULT 'default_avatar.png'
);

-- Tabela de Jogos
CREATE TABLE IF NOT EXISTS jogos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    titulo VARCHAR(100) NOT NULL,
    plataforma VARCHAR(50),
    status ENUM('Iniciado', 'Zerado', 'Engavetado', 'Abandonado') DEFAULT 'Engavetado',
    data_inicio DATE,
    data_fim DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

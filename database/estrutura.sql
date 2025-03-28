CREATE DATABASE IF NOT EXISTS teste_dev;
USE teste_dev;

CREATE TABLE procedimentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(20) NOT NULL,
    descricao TEXT NOT NULL,
    tipo VARCHAR(50) NOT NULL
);

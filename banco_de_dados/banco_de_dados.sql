CREATE DATABASE IF NOT EXISTS ans_data;
USE ans_data;

-- Tabela para os dados financeiros das operadoras
CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cnpj VARCHAR(20) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    ano INT NOT NULL,
    trimestre INT NOT NULL,
    receita DECIMAL(15,2),
    despesa DECIMAL(15,2),
    eventos_sinistros DECIMAL(15,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela para os dados cadastrais das operadoras
CREATE TABLE IF NOT EXISTS operadoras_ativas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registro_ans VARCHAR(20) NOT NULL,
    cnpj VARCHAR(20) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    modalidade VARCHAR(50),
    uf VARCHAR(2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    operadora_id INT,
    trimestre VARCHAR(10),
    ano INT,
    receita DECIMAL(15,2),
    despesa DECIMAL(15,2),
    lucro DECIMAL(15,2),
    FOREIGN KEY (operadora_id) REFERENCES operadoras(id)
);

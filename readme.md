📌 Etapas do Teste

1️⃣ Web Scraping

Acessar o site da ANS.

Baixar os arquivos Anexo I e Anexo II (PDFs) das demonstrações contábeis.

Compactar os arquivos baixados.

2️⃣ Transformação de Dados

Extrair os dados do Anexo I.

Salvar as informações extraídas em um arquivo CSV.

Compactar o arquivo CSV.

Substituir abreviações dos dados transformados.

3️⃣ Banco de Dados (MySQL)

Criar as tabelas para armazenar os dados:

operadoras → Dados cadastrais das operadoras.

procedimentos → Lista de procedimentos médicos.

cobertura → Relacionamento entre operadoras e procedimentos.

demonstracoes_contabeis → Informações financeiras trimestrais das operadoras.

Criação das Tabelas
CREATE TABLE operadoras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registro_ans VARCHAR(10) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    cnpj VARCHAR(18) NOT NULL UNIQUE
);

CREATE TABLE procedimentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(20) NOT NULL UNIQUE,
    descricao TEXT NOT NULL
);

CREATE TABLE cobertura (
    id INT AUTO_INCREMENT PRIMARY KEY,
    operadora_id INT,
    procedimento_id INT,
    cobertura VARCHAR(10) NOT NULL,
    FOREIGN KEY (operadora_id) REFERENCES operadoras(id),
    FOREIGN KEY (procedimento_id) REFERENCES procedimentos(id)
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
Importação dos Dados

Para importar os arquivos baixados:
LOAD DATA INFILE 'C:/Users/user/demonstracoes_contabeis/1T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(operadora_id, trimestre, ano, receita, despesa, lucro);
epita o processo para os outros arquivos trimestrais.

4️⃣ API com Vue.js e Python

Criar um servidor para buscar informações das operadoras.

Permitir busca textual pelos registros da ANS.

Documentar os endpoints via Postman.

🚀 Execução do Projeto

Baixar os arquivos da ANS e salvar em C:/Users/user/demonstracoes_contabeis.

Criar o banco de dados e as tabelas no MySQL.

Inserir os dados transformados.

Criar a API para consulta dos dados.

🛠 Tecnologias Utilizadas

Python (para web scraping e transformação de dados)

MySQL (para armazenamento dos dados)

Vue.js (para frontend da API)

Postman (para documentação dos endpoints)

# 📌 Teste Dev

## 🛠 Tecnologias Utilizadas

- **Python** (para web scraping e transformação de dados)
- **MySQL** (para armazenamento dos dados)
- **Vue.js** (para frontend da API)
- **Postman** (para documentação dos endpoints)
- **Selenium** (para automação de scraping)

## 🚀 Setup do Projeto

### 1️⃣ Instalação de Dependências

Antes de rodar o projeto, é necessário configurar o ambiente. Siga os passos abaixo:

#### **1.1 Instalar Python e Dependências**
Certifique-se de que você tem o **Python 3.8+** instalado.

```bash
pip install -r requirements.txt
```

#### **1.2 Instalar MySQL**
Baixe e instale o MySQL 8.0 ou superior. Durante a instalação:
- Configure um usuário **root** com senha.
- Anote o caminho do executável do MySQL (ex: `C:\Program Files\MySQL\MySQL Server 8.0\bin`).

#### **1.3 Instalar o ChromeDriver**
O Selenium requer um driver para interagir com o navegador. Faça o download do **ChromeDriver** compatível com a versão do seu Chrome em:

[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

Após o download, extraia e mova o executável para dentro do projeto (exemplo: `C:/Users/user/teste-dev/web_scraping/chromedriver.exe`).

---

### 2️⃣ Executando o Teste

#### **2.1 Configurar Banco de Dados**

1. Abra o MySQL e crie o banco de dados:
```sql
CREATE DATABASE ans_data;
USE ans_data;
```
2. Execute o script de criação das tabelas:
```bash
mysql -u root -p ans_data < banco_de_dados.sql
```

#### **2.2 Executar Web Scraping**
```bash
python script_scraping.py
```
Isso irá baixar e compactar os PDFs da ANS.

#### **2.3 Transformação de Dados**
```bash
python processamentos.py
```
Isso extrairá dados do Anexo I e salvará um CSV compactado.

#### **2.4 Inserir Dados no Banco**
Importe os arquivos CSV no MySQL:
```sql
LOAD DATA INFILE 'C:/Users/user/demonstracoes_contabeis/1T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(operadora_id, trimestre, ano, receita, despesa, lucro);
```
Repita para os outros arquivos trimestrais.

#### **2.5 Rodar a API**
```bash
python api.py
```
A API estará disponível em `http://localhost:5000`.

#### **2.6 Testar no Postman**
Use os endpoints disponíveis para buscar dados no banco:
- `GET /operadoras?search=Unimed`
- `GET /procedimentos?codigo=001`

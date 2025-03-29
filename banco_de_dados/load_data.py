import mysql.connector

conn = mysql.connector.connect(
    host="localhost",         
    user="root",              
    password="Wa@270619",     
    database="ans_data",      
    allow_local_infile=True 
)

cursor = conn.cursor()

cursor.execute("SHOW VARIABLES LIKE 'local_infile';")
result = cursor.fetchone()
if result and result[1] == 'ON':
    print("A opção LOCAL INFILE está habilitada.")
else:
    print("A opção LOCAL INFILE não está habilitada. Verifique as configurações do MySQL.")

sql = """
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(registro_ans, nome, cnpj);
"""

try:
    cursor.execute(sql)
    conn.commit()  
    print("Dados carregados com sucesso!")

    cursor.execute("SELECT * FROM despesas LIMIT 10;")
    resultados = cursor.fetchall()
    if not resultados:
        print("Nenhum dado encontrado na tabela 'despesas'.")
    else:
        cursor.execute("SELECT DISTINCT categoria FROM despesas LIMIT 10;")
        categorias = cursor.fetchall()
        print("Categorias encontradas na tabela despesas:")
        for categoria in categorias:
            print(categoria)

        cursor.execute("SELECT * FROM despesas WHERE data IS NULL OR categoria IS NULL LIMIT 10;")
        dados_invalidos = cursor.fetchall()
        if dados_invalidos:
            print("Dados inválidos encontrados:")
            for dado in dados_invalidos:
                print(dado)
        else:
            print("Nenhum dado inválido encontrado.")

            query_ultimo_trimestre = """
            SELECT operadora, SUM(valor) AS total_despesas
            FROM despesas
            WHERE categoria = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
              AND data BETWEEN CURDATE() - INTERVAL 6 MONTH AND CURDATE()
            GROUP BY operadora
            ORDER BY total_despesas DESC
            LIMIT 10;
            """
            cursor.execute(query_ultimo_trimestre)
            resultado_trimestre = cursor.fetchall()

            if resultado_trimestre:
                print("10 Operadoras com maiores despesas no último trimestre (últimos 6 meses):")
                for row in resultado_trimestre:
                    operadora, total_despesas = row
                    print(f"{operadora}: R$ {float(total_despesas):,.2f}")
            else:
                print("Nenhum resultado encontrado para o último trimestre.")

            query_ultimo_ano = """
            SELECT operadora, SUM(valor) AS total_despesas
            FROM despesas
            WHERE categoria = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
              AND data BETWEEN CURDATE() - INTERVAL 2 YEAR AND CURDATE()
            GROUP BY operadora
            ORDER BY total_despesas DESC
            LIMIT 10;
            """
            cursor.execute(query_ultimo_ano)
            resultado_ano = cursor.fetchall()

            if resultado_ano:
                print("10 Operadoras com maiores despesas no último ano (últimos 2 anos):")
                for row in resultado_ano:
                    operadora, total_despesas = row
                    print(f"{operadora}: R$ {float(total_despesas):,.2f}")
            else:
                print("Nenhum resultado encontrado para o último ano.")

            cursor.execute("""
            SELECT operadora, SUM(valor) AS total_despesas
            FROM despesas
            WHERE categoria = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
            GROUP BY operadora
            ORDER BY total_despesas DESC
            LIMIT 10;
            """)
            resultado_despesas = cursor.fetchall()

            if resultado_despesas:
                print("Operadoras com maiores despesas (sem intervalo de tempo):")
                for row in resultado_despesas:
                    operadora, total_despesas = row
                    print(f"{operadora}: R$ {float(total_despesas):,.2f}")
            else:
                print("Nenhum resultado encontrado para despesas gerais.")

except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    cursor.close()  
    conn.close()

from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar o Flask-CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas as rotas

# Configuração do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Wa@270619',
    'database': 'ans_data'
}

# Rota para busca textual
@app.route('/search', methods=['GET'])
def search_operators():
    query = request.args.get('query', '').strip()
    if not query:
        return jsonify([])  # Retorna uma lista vazia se a consulta estiver vazia

    try:
        # Conectar ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Query para buscar operadoras pelo nome ou registro
        sql = """
        SELECT registro_ans AS REGISTRO, nome AS NOME
        FROM operadoras
        WHERE registro_ans LIKE %s OR nome LIKE %s
        LIMIT 10;
        """
        like_query = f"%{query}%"
        cursor.execute(sql, (like_query, like_query))
        results = cursor.fetchall()

        return jsonify(results)

    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return jsonify({'error': 'Erro ao buscar dados no banco de dados'}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)


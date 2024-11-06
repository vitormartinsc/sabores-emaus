from flask import Flask, request, jsonify
from flask_cors import CORS  # Importa o CORS
import sqlite3
PATH_TO_DB = r'C:\Users\wlr\sabores-emaus\backend\data\sabores_emus.db'
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})  # Permitir requisições do front-end específico

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect(PATH_TO_DB)
    conn.row_factory = sqlite3.Row  # Retornar resultados como dicionários
    return conn

# Rota para login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Obtém os dados enviados pelo frontend
    print(data)
    username = data.get('username')  # Usa CPF como username
    password = data.get('password')
    #breakpoint()
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    
    print(user)

    if not user:
        return jsonify({"message": "Usuário não encontrado."}), 401

    # Verifica se a senha está correta
    if user['password'] != password:
        return jsonify({"message": "Senha incorreta."}), 401

    conn.close()
    return jsonify({
        "message": "Login bem-sucedido!",
        "user": {
            "name": user['name'],
            'username': user['username']
        }   
    }), 200
    
# Rota para obter o histórico de pedidos de um usuário
@app.route('/orders', methods=['GET'])
def get_orders():
    name = request.args.get('username')
    conn = get_db_connection()
    breakpoint()
    orders = conn.execute('SELECT * FROM orders WHERE username = ?', (name,)).fetchall()
    conn.close()

    # Convertendo os dados para uma lista de dicionários
    orders_list = []
    for order in orders:
        orders_list.append({
            'date': order['date'],
            'name_item': order['name_item'],
            'quantity': order['quantity']
        })

    return jsonify(orders_list)  # Retorna a lista de pedidos em formato JSON


if __name__ == '__main__':
    app.run(debug=True)


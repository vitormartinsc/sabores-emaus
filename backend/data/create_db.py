import os
import sqlite3

# Caminho para o banco de dados
PATH_TO_DB = '/home/vitor/sabores-emaus/backend/data/sabores_emaus.db'

# Verifica se o arquivo do banco de dados existe
if os.path.exists(PATH_TO_DB):
    os.remove(PATH_TO_DB)  # Apaga o arquivo do banco de dados
    print("Banco de dados existente foi removido.")

# Conectar ao banco de dados (ou criar um se não existir)
conn = sqlite3.connect(PATH_TO_DB)
c = conn.cursor()

# Criar tabela de usuários com username
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    name TEXT NOT NULL
)
''')

# Inserir usuários com username (sem formatação) se a tabela estiver vazia
c.execute('SELECT COUNT(*) FROM users')
if c.fetchone()[0] == 0:
    users = [
        ('15402478643', 'vitor123', 'Vitor Martins Carvalho'),
        ('23456789011', 'ana456', 'Ana Martins'),
        ('34567890122', 'joao789', 'João Ribeiro'),
        ('45678901233', 'lucas101112', 'Lucas Assis'),
        ('56789012344', 'maria131415', 'Maria Madalena')
    ]
    c.executemany('INSERT INTO users (username, password, name) VALUES (?, ?, ?)', users)

# Criar tabela de pedidos
c.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username INTEGER NOT NULL,
    name_item TEXT NOT NULL,
    date DATE NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (username) REFERENCES users (username)
)
''')

c.execute('SELECT COUNT(*) FROM orders')
if c.fetchone()[0] == 0:
    orders = [
        ('15402478643', 'Bolo de Chocolate', '2024-10-18', '4'),  # username de Vitor
        ('15402478643', 'Bolo de Cenoura', '2024-10-20', '2'),   # username de Vitor
        ('23456789011', 'Bolo de Morango', '2024-10-21', '3'),
        ('15402478643', 'Bolo de Chocolate', '2024-10-30', '1')# username de Ana
    ]
    c.executemany('INSERT INTO orders (username, name_item, date, quantity) VALUES (?, ?, ?, ?)', orders)

# Salvar (commit) as mudanças e fechar a conexão
conn.commit()
conn.close()

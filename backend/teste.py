from flask import Flask, request, jsonify
from flask_cors import CORS  # Importa o CORS
import sqlite3
PATH_TO_DB = r'C:\Users\wlr\sabores-emaus\backend\data\sabores_emus.db'
def get_db_connection():
    conn = sqlite3.connect(PATH_TO_DB)
    conn.row_factory = sqlite3.Row  # Retornar resultados como dicionários
    return conn
conn =get_db_connection()

user = conn.execute('SELECT * FROM orders WHERE username = ?', (15402478643,)).fetchall()

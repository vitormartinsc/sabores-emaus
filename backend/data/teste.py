import sqlite3
import pandas as pd

# Conecte ao banco de dados
conn = sqlite3.connect('sabores_emaus.db')

# Ler a tabela de usuários
usuarios_df = pd.read_sql_query("SELECT * FROM usuarios", conn)
print("Tabela de Usuários:")
print(usuarios_df)

# Ler a tabela de pedidos
pedidos_df = pd.read_sql_query("SELECT * FROM pedidos", conn)
print("\nTabela de Pedidos:")
print(pedidos_df)

# Fechar a conexão
conn.close()

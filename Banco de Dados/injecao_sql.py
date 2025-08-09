import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Estabelece a conexão com o banco de dados SQLite
conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')

# Cria um cursor para executar comandos SQL
cur = conexao.cursor()

# Configura o cursor para retornar os resultados como dicionários
cur.row_factory = sqlite3.Row

id_cliente = input("Digite o ID do cliente que deseja recuperar: ")
cliente = cur.execute('SELECT * FROM clientes WHERE id = ?', (id_cliente,)).fetchone()
print(dict(cliente))
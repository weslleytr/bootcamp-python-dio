import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Estabelece a conexão com o banco de dados SQLite
conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')

# Cria um cursor para executar comandos SQL
cur = conexao.cursor()

# Configura o cursor para retornar os resultados como dicionários
cur.row_factory = sqlite3.Row

try:
    cur.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', ('Teste 1', 'teste1@email.com'))
    cur.execute('INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)', (3, 'Teste 2', 'teste2@email.com'))
    conexao.commit()
except Exception as ex:
    print(f'Ocorreu um erro: {ex}')
    conexao.rollback()
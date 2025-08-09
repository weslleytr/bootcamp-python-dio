import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Estabelece a conexão com o banco de dados SQLite
conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')

# Cria um cursor para executar comandos SQL
cur = conexao.cursor()

# Configura o cursor para retornar os resultados como dicionários
cur.row_factory = sqlite3.Row

# Cria a tabela 'clientes' se ela não existir
def criar_tabela(conexao, cur):
    cur.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(100))')
    
    # Salva as alterações no banco de dados
    conexao.commit()

# Insere um registro de exemplo na tabela 'clientes'
def inserir_registro(conexao, cur, nome, email):
    data = (nome, email)
    cur.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', data)

    # Salva as alterações no banco de dados
    conexao.commit()

# Atualiza um registro existente na tabela 'clientes'
def atualizar_registro(conexao, cur, cliente_id, nome, email):
    data = (nome, email, cliente_id)
    cur.execute('UPDATE clientes SET nome = ?, email = ? WHERE id = ?', data)

    # Salva as alterações no banco de dados
    conexao.commit()

# Exclui um registro da tabela 'clientes'
def excluir_registro(conexao, cur, cliente_id):
    cur.execute('DELETE FROM clientes WHERE id = ?', (cliente_id,))

    # Salva as alterações no banco de dados
    conexao.commit()

def inserir_registros_lote(conexao, cur, registros):
    cur.executemany('INSERT INTO clientes (nome, email) VALUES (?,?)', registros)

    # Salva as alterações no banco de dados
    conexao.commit()

# Lista todos os registros da tabela 'clientes'
def listar_clientes(cur):
    cur.execute('SELECT * FROM clientes')
    return cur.fetchall()

# Recupera um cliente específico pelo ID
def recuperar_cliente(cur, cliente_id):
    cur.execute('SELECT * FROM clientes WHERE id = ?', (cliente_id,))
    return cur.fetchone()

# --------------- Exemplos de uso ---------------
atualizar_registro(conexao, cur, 1, 'Weslley Araujo', 'weslley.araujo@email.com')

excluir_registro(conexao, cur, 1)

dados = [
    ('Guilherme', 'guilherme@email.com'),
    ('João', 'joao@email.com'),
    ('Bernardo', 'bernardo.araujo@email.com'),
    ('Ana', 'aninha123@email.com'),
    ('Jonas', 'jonas.e.a.baleia@email.com'),
]
inserir_registros_lote(conexao, cur, dados)

clientes = listar_clientes(cur)
for cliente in clientes:
    print(dict(cliente))

print(dict(recuperar_cliente(cur, 2)))
import sqlite3

# conectar ao banco de dados
conexao = sqlite3.connect('banco_de_dados.db')

# Criar uma tabela
conexao.execute('''
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT
    )
''')

# Fecha a conexão com o banco de dados
conexao.close()
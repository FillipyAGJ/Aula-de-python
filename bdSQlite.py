import sqlite3

# conectar ao banco de dados
conexao = sqlite3.connect('banco_de_dados.db')

# Fecha a conexão com o banco de dados
conexao.close()
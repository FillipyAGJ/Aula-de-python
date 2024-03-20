import sqlite3
import bdSQlite4

# conectar ao banco de dados
conexao = sqlite3.connect('banco_de_dados.db')

bdSQlite4.imprimeValores()

bdSQlite4.atualizarEmail()

# Salvar as alterações no banco de dados
conexao.commit()

# Fecha a conexão com o banco de dados
conexao.close()
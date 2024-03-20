import bdSQlite3


def createTable():
    # Criar uma tabela
    bdSQlite3.conexao.execute('''
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT
        )
    ''')

def inserirUsuarios():
    # Inserir um registro na tabela
    bdSQlite3.conexao.execute('''
        INSERT INTO usuarios (nome, email)
        VALUES('Fillipy', 'fillipy@example.com'),
            ('Gabriel', 'Gabriel@example.com'),
            ('Carlos', 'Carlos@example.com'),
            ('Allan', 'Allan@example.com'),
            ('Luis', 'Luis@example.com'),
            ('Érica', 'Érica@example.com'),
            ('Juliana', 'Juliana@example.com'),
            ('Regilson', 'Regilson@example.com'),
            ('Hiana', 'Hiana@example.com'),
            ('Natalia', 'Natalia@example.com')
    ''')

def imprimeValores():
    # Recuperar todos os registros da tabela
    resultado = bdSQlite3.conexao.execute('SELECT * FROM usuarios')

    # Iterar sobre os resultados
    for row in resultado:
        print(f'ID: {row[0]}, Nome: {row[1]}, Email: {row[2]}')

def atualizarEmail():
    # Atualizar o email do usuário com ID 1
    bdSQlite3.conexao.execute('''
        UPDATE usuarios
        SET email = 'novo_email@example.com'
        WHERE id = 1
    ''')

def removerUsuario1():
    bdSQlite3.conexao('DELETE FROM usuarios WHERE id = 1')
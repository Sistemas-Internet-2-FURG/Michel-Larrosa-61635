import sqlite3
from flask import current_app
# Inicializa o banco de dados e cria a tabela de usuários
def init_db():
    conn = sqlite3.connect('storage/acl.db')
    cursor = conn.cursor()

    # Criação da tabela de USUÁRIOS LOGADOS
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS equipe (
        matricula INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        cargo TEXT NOT NULL
    )
    ''')

    cursor.execute('INSERT OR IGNORE INTO equipe (nome, senha, cargo) VALUES (?, ?, ?)', ('Silvia', 'diretores', 'DIRETOR'))
    cursor.execute('INSERT OR IGNORE INTO equipe (nome, senha, cargo) VALUES (?, ?, ?)', ('Rafael', 'coordenadores', 'COORDENADOR'))
    cursor.execute('INSERT OR IGNORE INTO equipe (nome, senha, cargo) VALUES (?, ?, ?)', ('Fernanda', 'professores', 'PROFESSOR'))
    cursor.execute('INSERT OR IGNORE INTO equipe (nome, senha, cargo) VALUES (?, ?, ?)', ('publico', 'publico_pass', 'PÚBLICO'))

    # Criação da tabela de TURMAS
    # não coloquei AUTOINCREMENT pois o nome da turma pode ser escolhido na hora
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS turmas (
        identificador TEXT PRIMARY KEY,
        disciplina TEXT NOT NULL,
        professor INTEGER NOT NULL,
        FOREIGN KEY (professor) REFERENCES equipe(matricula)
    )
    ''')
    # Criação da tabela de ALUNOS (posteriormnte melhorar para notas por disciplina e bimestre)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        matricula INTEGER PRIMARY KEY,
        turma TEXT,
        nome TEXT NOT NULL,
        nota INTEGER NOT NULL,
        FOREIGN KEY (turma) REFERENCES turmas(identificador)
    )
    ''')

    conn.commit()
    conn.close()

# Função para verificar login no banco de dados
def check_login(nome, senha):
    try:
        conn = sqlite3.connect('storage/acl.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM equipe WHERE nome = ? AND senha = ?', (nome, senha))
        user = cursor.fetchone()
        return user
    except sqlite3.Error as e:
        return f'Erro ao realizar login: {e}'
    finally:
        conn.close()


# ### ### ### ### ### ### manipulação de equipe

def cria_user(nome, senha, cargo):
    current_app.logger.info("ENTROU NA FUNÇÃO")
    try:
        conn = sqlite3.connect('storage/acl.db')
        if conn:
            current_app.logger.info("CONN OK")
        cursor = conn.cursor()
        cursor.execute('INSERT INTO equipe (nome, senha, cargo) VALUES (?, ?, ?)', (nome, senha, cargo))
        conn.commit()
        if cursor.rowcount > 0:
            current_app.logger.info("RAWCONT > 0")
        else:
            current_app.logger.info("RAWCONT 0")

    except sqlite3.Error as e:
        return f'Erro ao criar usuario: {e}'
    finally:
        conn.close()

# ### ### ### ### ### ### manipulação de turmas

def cria_turma(identificador, disciplina, professor):
    try:
        conn = sqlite3.connect('storage/acl.db')
        cursor = conn.cursor()
        cursor.execute('INSERT OR IGNORE INTO turmas (identificador, disciplina, professor) VALUES (?, ?, ?)', (identificador, disciplina, professor))
        conn.commit()
        # estudar try: catch
        return 1
    except sqlite3.Error as e:
        return f'Erro ao criar turma: {e}'
    finally:
        conn.close()


def read_turma(turma):
    conn = sqlite3.connect('storage/acl.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM turmas WHERE identificador = ?)', (turma))
    # estudar try: catch
    conn.close()
    return 1

def update_turma(turma, disciplina):
    conn = sqlite3.connect('storage/acl.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE turmas (identificador, disciplina) VALUES (?, ?)', (turma, disciplina))
    # estudar try: catch
    conn.close()
    return 1

def delete_turma(turma):
    conn = sqlite3.connect('storage/acl.db')
    cursor = conn.cursor()
    cursor.execute('DELETE * FROM turmas WHERE identificador = ?)', (turma))
    # estudar try: catch
    conn.close()
    return 1

# ### ### ### ### ### ### manipulação de ALUNOS

def cria_aluno(matricula, turma):
    try:
        conn = sqlite3.connect('storage/acl.db')
        cursor = conn.cursor()
        cursor.execute('INSERT OR IGNORE INTO turmas (matricula, disciplina) VALUES (?, ?)', (turma, disciplina))
        # estudar try: catch
        return 1
    except sqlite3.IntegrityError as e:
        return f'Erro de integridade (provavelmente chave estrangeira): {e}'
    except sqlite3.Error as e:
        return f'Erro ao inserir aluno: {e}'
    finally:
        conn.close()


def read_aluno(matricula):
    conn = sqlite3.connect('storage/acl.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM turmas WHERE matricula = ?)', (matricula))
    # estudar try: catch
    conn.close()
    return 1

def update_turma(matricula, nome, nota):
    conn = sqlite3.connect('storage/acl.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE turmas (matricula, nota) VALUES (?, ?)', (matricula, nota))
    # estudar try: catch
    conn.close()
    return 1

def delete_turma(matricula):
    conn = sqlite3.connect('storage/acl.db')
    cursor = conn.cursor()
    cursor.execute('DELETE * FROM alunos WHERE matricula = ?)', (matricula))
    # estudar try: catch
    conn.close()
    return 1

import sqlite3
from flask import current_app, jsonify
# Inicializa o banco de dados e cria a tabela de usuários
def conectar():
    return sqlite3.connect('storage/acl.db')

def init_db():
    conn = conectar()
    conn.execute("PRAGMA foreign_keys = ON")  # Ativa a verificação de chaves estrangeiras
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

    cursor = conn.cursor()
    conn.close()

# Função para verificar login no banco de dados
def check_login(nome, senha):
    try:
        conn = conectar()
        current_app.logger.info("CONN OK")

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM equipe WHERE nome = ? AND senha = ?', (nome, senha))
        user = cursor.fetchone()
        return user
    except sqlite3.Error as e:
        return f'Erro ao obter aluno: {e}'
    finally:
        conn.close()


# ### ### ### ### ### ### manipulação de equipe


def cria_user(nome, senha, cargo):
    current_app.logger.info("ENTROU NA FUNÇÃO")
    try:
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")  # Ativa a verificação de chaves estrangeiras
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
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")  # Ativa a verificação de chaves estrangeiras
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
    conn = conectar()
    conn.execute("PRAGMA foreign_keys = ON")  # Ativa a verificação de chaves estrangeiras
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM turmas WHERE identificador = ?)', (turma))
    # estudar try: catch
    conn.close()
    return 1


def update_turma(turma, disciplina):
    conn = conectar()
    conn.execute("PRAGMA foreign_keys = ON")  # Ativa a verificação de chaves estrangeiras
    cursor = conn.cursor()
    cursor.execute('UPDATE turmas (identificador, disciplina) VALUES (?, ?)', (turma, disciplina))
    # estudar try: catch
    conn.close()
    return 1


def delete_turma(turma):
    conn = conectar()
    conn.execute("PRAGMA foreign_keys = ON")  # Ativa a verificação de chaves estrangeiras
    cursor = conn.cursor()
    cursor.execute('DELETE * FROM turmas WHERE identificador = ?)', (turma))
    # estudar try: catch
    conn.close()
    return 1


# ### ### ### ### ### ### GERENCIAMENTO DE ALUNOS


def obter_alunos():
    """Obtém todos os alunos do banco de dados."""
    try:
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")  # Ativa a verificação de chaves estrangeiras
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM alunos')
        alunos = cursor.fetchall()
        if isinstance(alunos, str):  # Se houver um erro, `obter_alunos` retornará uma string de erro
            return jsonify({'success': False, 'error': alunos}), 500  # Retorne um JSON de erro
        return [{'matricula': a[0], 'turma': a[1], 'nome': a[2], 'nota': a[3]} for a in alunos]  # Retorne os dados dos alunos como JSON
    except sqlite3.Error as e:
        return f"Erro ao obter alunos: {e}"
    finally:
        conn.close()


def read_aluno(matricula):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM alunos WHERE matricula = ?', (matricula,))
        aluno = cursor.fetchone()
        return aluno
    except sqlite3.Error as e:
        return f'Erro ao realizar login: {e}'
    finally:
        conn.close()


def inserir_aluno(matricula, turma, nome, nota): # NÃO TESTADO
    """Insere um novo aluno no banco de dados."""
    try:
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")  # Ativa a verificação de chaves estrangeiras
        cursor = conn.cursor()
        cursor.execute('INSERT INTO alunos (matricula, turma, nome, nota) VALUES (?, ?, ?, ?)', (matricula, turma, nome, nota))
        conn.commit()
        current_app.logger.info(cursor.lastrowid)
        return cursor.lastrowid
    except sqlite3.IntegrityError as e:
        return f"Erro de integridade (verificar-chaves-estrangeiras) (verificar-chaves-prma rias): {e}"
    except sqlite3.Error as e:
        return f"Erro ao inserir aluno: {e}"
    finally:
        conn.close()


def editar_aluno(matricula, turma, nome, nota): # NÃO TESTADO
    """Edita os dados de um aluno."""
    try:
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")  # Ativa a verificação de chaves estrangeiras
        cursor = conn.cursor()
        cursor.execute('UPDATE alunos SET turma = ?, nome = ?, nota = ? WHERE matricula = ?', (turma, nome, nota, matricula))
        conn.commit()
        return cursor.rowcount
    except sqlite3.Error as e:
        return f"Erro ao editar aluno: {e}"
    finally:
        conn.close()


def delete_aluno(matricula):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM alunos WHERE matricula = ?', (matricula,))
        conn.commit()

        if cursor.rowcount > 0:  # Verifica se uma linha foi realmente afetada
            return True
        else:
            return False
    except sqlite3.Error as e:
        return f'Erro ao excluir aluno: {e}'
    finally:
        conn.close()

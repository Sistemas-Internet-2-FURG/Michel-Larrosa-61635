from flask import current_app, jsonify
from flask_sqlalchemy import SQLAlchemy
# Não gostei do SQLAlchemy, pelo menos não da documentação
# A linha acima nada mais é do que a importação de tudo
# O que não fica nada explícito na documentação
# É muita leitura para aprender o básico
# E as possibilidades são tão amplas que o sentido do ORM se perde

# Não esquecer da classe Mapa:
# file:///home/michel/Estudos/PYTHON/sqlalchemy_20/orm/mapping_styles.html#declarative-mapping
# E como usar Session:
# file:///home/michel/Estudos/PYTHON/sqlalchemy_20/orm/session_api.html#session-api
# file:///home/michel/Estudos/PYTHON/sqlalchemy_20/orm/queryguide/query.html

db = SQLAlchemy() # Instancia SQLAlchemy

# Importando as CLASSES modelos
from models.alunos import Aluno
from models.equipe import Equipe
from models.turmas import Turma

# ### Inicialização do banco de dados com flask.
def init_db(app):
    # Configuração do banco de dados PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mxl553@localhost:5432/akademiq'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app) # db = SQLAlchemy()
    return db

# ### funções globais
def check_db_connection():
    # Realiza uma consulta simples para testar a conexão
    return db.session.execute('SELECT 1').scalar()

# Função para verificar login no banco de dados DEPRECATED
def check_login(nome, senha):
    try:
        conn = conectar()
        current_app.logger.info("CONN OK")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM equipe WHERE nome = ? AND senha = ?', (nome, senha))
        user = cursor.fetchone()
        return user
    except sqlite3.Error as e:
        return f'Erro ao obter Pessoa: {e}'
    finally:
        conn.close()

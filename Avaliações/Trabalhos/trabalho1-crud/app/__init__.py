from flask import Flask
from flask_cors import CORS
from app.models import init_db, db
import logging

from app.routes.auth import auth
from app.routes.routes import main
from app.routes.api import api

# from models.alunos import alunos
# from models.equipe import equipe
# from models.turmas import turmas

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})  # Permite requisições de qualquer origem
    # >_ sys.senha 64 12
    app.secret_key = 'iAPrRYstWHTjnkVk0HQyOUQeUYamYRWFM9naGoPj7YhMl3g96UbsQlGPDLbg3EHU'


    # Configuração básica do logging
    logging.basicConfig(level=logging.DEBUG)  # Configura o nível do log para DEBUG

    # Inicializa o banco de dados
    init_db(app)

    # Importa e registra os blueprints de rotas e autenticação
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(api)
    # app.register_blueprint(alunos)
    # app.register_blueprint(equipe)
    # app.register_blueprint(turmas)


    return app

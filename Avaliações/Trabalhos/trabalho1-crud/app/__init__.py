from flask import Flask

from app.models import init_db
from .routes.auth import auth
from .routes.routes import main
from .routes.api import api


import logging


def create_app():
    app = Flask(__name__)
    # >_ sys.senha 64
    app.secret_key = 'iAPrRYstWHTjnkVk0HQyOUQeUYamYRWFM9naGoPj7YhMl3g96UbsQlGPDLbg3EHU'
    # Configuração básica do logging
    logging.basicConfig(level=logging.DEBUG)  # Configura o nível do log para DEBUG

    # Inicializa o banco de dados
    init_db()

    # Importa e registra os blueprints de rotas e autenticação
    # from app.routes import main
    # from app.routes import API
    # from app.auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(api)



    return app

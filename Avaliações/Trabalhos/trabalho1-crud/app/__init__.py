from flask import Flask
from app.models import init_db
import logging



def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    # Configuração básica do logging
    logging.basicConfig(level=logging.DEBUG)  # Configura o nível do log para DEBUG

    # Inicializa o banco de dados
    init_db()

    # Importa e registra os blueprints de rotas e autenticação
    from app.routes import main_routes
    from app.auth import auth_routes

    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)

    return app

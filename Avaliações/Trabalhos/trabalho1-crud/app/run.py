from app import create_app
import logging


app = create_app()

# Configuração básica do logging
logging.basicConfig(level=logging.DEBUG)  # Configura o nível do log para DEBUG

if __name__ == '__main__':
    app.run(debug=True)

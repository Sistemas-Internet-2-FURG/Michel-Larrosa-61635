from app import create_app

import logging
# Configuração básica do logging
logging.basicConfig(level=logging.DEBUG)  # Configura o nível do log para DEBUG

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)

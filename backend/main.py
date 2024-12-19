import os

from flask import Flask
from src.db import config_sql_alchemy, db_instance
from src.init_db import init_load_data
from src.login_manager import init_login_manager
from src.migrate import load_migrate
from src.routes import config_app_routes
from src.schema import config_marshmallow
from src.security import config_app_cors, config_jwt_token
from src.swagger_docs import config_swagger
from src.versioning_db import config_versioning

app = Flask(__name__)

app.config['BUNDLE_ERRORS'] = True
app.config['DEBUG'] = int(os.environ.get('FLASK_DEBUG', '0')) == 1
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback_sk')

# Config SQLAlchemy
config_sql_alchemy(app)
config_versioning()


@app.cli.command('initdb')
def initdb_command():
    init_load_data()
    print('Base de dados inicializada.')


# Config Marshmallow
config_marshmallow(app)

# Init Login Manager
init_login_manager(app)

# Config Flask JWT Extended
jwt = config_jwt_token(app)

# Config App CORS
config_app_cors(app)

# Config Swagger Documentation
docs = config_swagger(app)

# Config Flask Restful
api = config_app_routes(app, docs)

# Load Flask Migrate
migrate = load_migrate(db_instance, app)


if __name__ == '__main__':
    app.run()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_restful import Api

app = Flask(__name__)
app.config.from_object('api.config')  # Carregar a configuração do config.py

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

from .models import user_model  # Importar os modelos
#from .routes import user_routes  # Importar as rotas
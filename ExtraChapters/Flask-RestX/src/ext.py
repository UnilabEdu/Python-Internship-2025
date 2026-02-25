from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_jwt_extended import JWTManager

from src.config import Config

db = SQLAlchemy()
migrate = Migrate()
api = Api(title="My Api", authorizations=Config.SWAGGER_AUTHORIZATION)
jwt = JWTManager()
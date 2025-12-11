from datetime import timedelta
from os import path, environ


class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SECRET_KEY = environ.get("SECRET_KEY", "defaultsecretkey123!456@")
    JWT_SECRET_KEY = "super-secret-key"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    FLASK_ADMIN_SWATCH = 'Cerulean'

    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static", "upload")
    SWAGGER_AUTHORIZATION = {
        "JsonWebToken": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization"
        }
    }

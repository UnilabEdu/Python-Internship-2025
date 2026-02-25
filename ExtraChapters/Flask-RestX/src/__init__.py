from flask import Flask

from src.models import User
from src.config import Config
from src.ext import db, migrate, api, jwt
from src.commands import init_db, populate_db, init_db_command, populate_db_command
from src.endpoints import ProductApi

COMMANDS = [init_db_command, populate_db_command]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_commands(app)

    return app


def register_extensions(app):
    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    #Flask-RestX
    api.init_app(app)

    #Flask-JWT-Extended
    jwt.init_app(app)

    @jwt.user_identity_loader
    def user_identity_loader(user):
        return user.username

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        username = jwt_data["sub"]
        return User.query.filter_by(username=username).first()


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)

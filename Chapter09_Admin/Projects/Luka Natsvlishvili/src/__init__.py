from flask import Flask
from src.views import auth_blueprint, main_blueprint, movie_blueprint
from src.ext import db, migrate, login_manager, admin
from src.config import Config
from src.commands import init_db
from src.models import User, Movie
from src.admin_views.base import SecureModelView
from src.admin_views.movie import MovieView
from flask_admin.menu import MenuLink

BLUEPRINTS = [
    auth_blueprint, main_blueprint, movie_blueprint
]

COMMANDS = [
    init_db
]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_blueprint(app)
    register_extensions(app)
    register_commands(app)

    return app

def register_blueprint(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    admin.init_app(app)
    admin.add_view(MovieView(Movie, db.session))
    admin.add_view(SecureModelView(User, db.session))

    admin.add_link(MenuLink("მთავარი", url="/", icon_type="fa", icon_value="fa-home"))
    admin.add_link(MenuLink("გასვლა", url="/logout", icon_type="fa", icon_value="fa-sign-out"))


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
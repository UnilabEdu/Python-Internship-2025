from flask import Flask

from src.commands import init_db_command, populate_db_command
from src.config import Config
from src.ext import db, migrate, login_manager, admin
from src.views import main_blueprint, auth_blueprint, product_blueprint
from src.models import User, Tour
from src.admin_views.base import SecureModelView
from src.admin_views import UserView, TourView
from flask_admin.menu import MenuLink

BLUEPRINTS = [main_blueprint, product_blueprint, auth_blueprint]
COMMANDS = [init_db_command, populate_db_command]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)

    admin.init_app(app)
    admin.add_view(UserView(User, db.session))
    admin.add_view(TourView(Tour, db.session))
    admin.add_link(MenuLink("To site", url="/"))

def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
from flask import Flask

from MyPage.src.views import main_blueprint, auth_blueprint, product_blueprint
from MyPage.src.ext import db, migrate, login_manager, admin
from MyPage.src.config import Config
from MyPage.src.commands import init_db, populate_db
from MyPage.src.models import User, Product
from MyPage.src.admin_views.base import SecureModelView
from MyPage.src.admin_views.product import ProductView


BLUE_PRINTS = [auth_blueprint, main_blueprint, product_blueprint]

COMMANDS = [init_db,populate_db]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_blueprints(app)
    register_extensions(app)
    register_commands(app)



    from MyPage.src.models.user import User

    return app

def register_blueprints(app):
    for blue_print in BLUE_PRINTS:
        app.register_blueprint(blue_print)

def register_extensions(app):
    db.init_app(app)

    #Flask migrate
    migrate.init_app(app, db)

    #Flask_login
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    #Flask admin
    admin.init_app(app)
    admin.add_view(ProductView(Product, db.session))
    admin.add_view(SecureModelView(User, db.session))

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)

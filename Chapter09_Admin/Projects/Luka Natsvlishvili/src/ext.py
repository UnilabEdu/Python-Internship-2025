from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from src.admin_views.base import SecureIndexView
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
db = SQLAlchemy()
admin = Admin(name="Coffeewood Entertainment Python Panel", index_view = SecureIndexView())

import os
import pytest
import tempfile
from src import create_app
from src.ext import db
from src.models import User


@pytest.fixture(scope="session")
def app():
    db_path, db_file = tempfile.mkstemp()

    app = create_app()
    app.config.update({
        'TESTING': True,
        "WTF_CSRF_ENABLED": False,
        "DEBUG": False,
        "SQLALCHEMY_DATABASE_URI": f'sqlite:///{db_file}.sqlite'
    })

    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='nika').first():
            user = User(username='nika')
            user.password = 'nika1234'
            db.session.add(user)
            db.session.commit()

    yield app

    os.close(db_path)
    os.unlink(db_file)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def server(app):
    return app.test_cli_runner()

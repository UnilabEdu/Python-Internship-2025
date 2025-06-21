from os import path

class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SECRET_KEY = "GJFKLDJKljklhhjkhjk@595jijkjd"
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static", "upload")

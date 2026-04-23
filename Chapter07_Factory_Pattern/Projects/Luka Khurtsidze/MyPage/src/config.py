from os import path




class Config(object):

    SECRET_KEY = "SJQKJS1320UWEWSWjkusop@"

    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static", "uploads")

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")

    print(SQLALCHEMY_DATABASE_URI)

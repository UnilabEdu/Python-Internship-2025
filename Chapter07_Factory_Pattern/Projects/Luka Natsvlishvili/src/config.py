from os import path

BASE_DIRECTORY = path.abspath(path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "instance", "database.db")
    SECRET_KEY = "a9F#kP2!Zr8M@xQwL7dS$E4yHcN%VJmT"
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static", "img")

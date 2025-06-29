from os import environ


class Config:

    DB_USER = environ.get("DB_USER")
    DB_PASSWORD = environ.get("DB_PASSWORD")
    DB_DATABASE = environ.get("DB_DATABASE")

    print(DB_USER)
    print(DB_PASSWORD)
    print(DB_DATABASE)
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_DATABASE}"
    SECRET_KEY = environ.get("SECRET_KEY")
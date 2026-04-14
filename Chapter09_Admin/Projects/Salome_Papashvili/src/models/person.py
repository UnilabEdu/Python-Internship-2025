from src.ext import db
from src.models.base import BaseModel
class Person(BaseModel):
    __tablename__ = "persons"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    profile_image = db.Column(db.String)

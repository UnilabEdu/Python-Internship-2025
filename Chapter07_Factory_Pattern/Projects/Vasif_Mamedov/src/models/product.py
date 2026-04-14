from src.ext import db
from src.models.base import BaseModel

class Product(BaseModel):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    category = db.Column(db.String)
    img = db.Column(db.String)
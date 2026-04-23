from MyPage.src.models.base import BaseModel
from MyPage.src.ext import db

class Product(BaseModel):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    price = db.Column(db.String)
    img = db.Column(db.String)


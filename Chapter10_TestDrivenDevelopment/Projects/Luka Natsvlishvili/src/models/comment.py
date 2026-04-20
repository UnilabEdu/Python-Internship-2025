from src.ext import db
from src.models.base import BaseModel

class Comment(BaseModel):
    __tablename__ = "comments"

    author = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"), nullable=False)
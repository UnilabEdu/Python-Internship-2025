from src.ext import db
from src.models.base import BaseModel


class Movie(BaseModel):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    release_date = db.Column(db.Integer)
    genre = db.Column(db.String)
    description = db.Column(db.String)
    comment1_author = db.Column(db.String)
    comment1_text = db.Column(db.String)
    comment2_author = db.Column(db.String)
    comment2_text = db.Column(db.String)
    comments = db.relationship("Comment", backref="movie", lazy=True, cascade="all, delete-orphan")
    watch_links = db.Column(db.String)
    img = db.Column(db.String)
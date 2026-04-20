from flask import render_template, Blueprint

from src.models.movie import Movie

main_blueprint = Blueprint("main", __name__)
users = []

### ROUTE ###

@main_blueprint.route("/")
def index():
    movies = Movie.query.all()
    return render_template("main/index.html", users=users, movies=movies)

@main_blueprint.route("/about")
def about():
    return render_template("main/about.html")
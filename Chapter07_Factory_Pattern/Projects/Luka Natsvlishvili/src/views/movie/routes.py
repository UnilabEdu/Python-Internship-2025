from flask import render_template, redirect, url_for, Blueprint
from os import path
from uuid import uuid4
from src.config import Config

from src.models import Movie
from src.views.movie.forms import MovieForm


movie_blueprint = Blueprint("movies", __name__)

@movie_blueprint.route("/view_movie/<int:movie_id>")
def view_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template("movie/view_movie.html", movie=movie)

@movie_blueprint.route("/create_movie", methods=["GET","POST"])
def create_movie():
    form = MovieForm()
    if form.validate_on_submit():
        file = form.img.data
        _, ext = path.splitext(file.filename)
        filename = f"{uuid4()}{ext}"
        file.save(path.join(Config.UPLOAD_PATH, filename))

        new_movie = Movie(
            name=form.name.data,
            release_date=form.release_date.data,
            genre=form.genre.data,
            comment1_author=form.comment1_author.data,
            comment1_text=form.comment1_text.data,
            comment2_author=form.comment2_author.data,
            comment2_text=form.comment2_text.data,
            img=f"img/{filename}"
        )
        new_movie.create()
        return redirect(url_for("main.index"))

    return render_template("movie/create_movie.html", form=form)

@movie_blueprint.route("/edit_movie/<int:movie_id>", methods=["GET","POST"])
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    form = MovieForm(name=movie.name,
                     comment1_author=movie.comment1_author,
                     comment1_text=movie.comment1_text,
                     comment2_author=movie.comment2_author,
                     comment2_text=movie.comment2_text,
                     release_date = movie.release_date,
                     genre = movie.genre
                     )
    if form.validate_on_submit():
        if form.img.data:
            file = form.img.data
            _, ext = path.splitext(file.filename)
            filename = f"{uuid4()}{ext}"
            file.save(path.join(Config.UPLOAD_PATH, filename))
            movie.img = f"img/{filename}"

        movie.name = form.name.data
        movie.comment1_author = form.comment1_author.data
        movie.comment1_text = form.comment1_text.data
        movie.comment2_author = form.comment2_author.data
        movie.comment2_text = form.comment2_text.data
        movie.release_date = form.release_date.data
        movie.genre = form.genre.data

        movie.save()
        return redirect(url_for("main.index"))

    return render_template("movie/create_movie.html", form=form)

@movie_blueprint.route("/delete_movie/<int:movie_id>")
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    movie.delete()
    return redirect(url_for("main.index"))
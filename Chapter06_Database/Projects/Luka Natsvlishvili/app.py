from flask import Flask, render_template, redirect, url_for

from forms import RegisterForm, MovieForm
from os import path
from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy


#### EXTENSIONS ###
app = Flask(__name__)
app.config["SECRET_KEY"] = "a9F#kP2!Zr8M@xQwL7dS$E4yHcN%VJmT"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
UPLOAD_PATH = path.join(app.root_path, "static", "img")

db = SQLAlchemy(app)
### MODELS ###

class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    release_date = db.Column(db.String)
    genre = db.Column(db.String)
    comment1_author = db.Column(db.String)
    comment1_text = db.Column(db.String)
    comment2_author = db.Column(db.String)
    comment2_text = db.Column(db.String)
    img = db.Column(db.String)


users = []

### ROUTE ###

@app.route("/")
def index():
    movies = Movie.query.all()
    return render_template("index.html", users=users, movies=movies)

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        users.append(
            {
                "username": form.username.data,
                "birthday": form.birthdate.data,
                "gender": form.gender.data,
                "country": form.country.data
            }
        )
        file = form.profile_image.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(UPLOAD_PATH, filename))
        print("Everything fine!")
    else:
        print(form.errors)
    return render_template("register.html", form=form)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/view_movie/<int:movie_id>")
def view_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template("view_movie.html", movie=movie)

@app.route("/create_movie", methods=["GET","POST"])
def create_movie():
    form = MovieForm()
    if form.validate_on_submit():
        file = form.img.data
        _, ext = path.splitext(file.filename)
        filename = f"{uuid4()}{ext}"
        file.save(path.join(UPLOAD_PATH, filename))

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
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("create_movie.html", form=form)

@app.route("/edit_movie/<int:movie_id>", methods=["GET","POST"])
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
            file.save(path.join(UPLOAD_PATH, filename))
            movie.img = f"img/{filename}"

        movie.name = form.name.data
        movie.comment1_author = form.comment1_author.data
        movie.comment1_text = form.comment1_text.data
        movie.comment2_author = form.comment2_author.data
        movie.comment2_text = form.comment2_text.data
        movie.release_date = form.release_date.data
        movie.genre = form.genre.data

        db.session.commit()
        return redirect(url_for("index"))

    return render_template("create_movie.html", form=form)

@app.route("/delete_movie/<int:movie_id>")
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("index"))



if __name__ == '__main__':
    app.run(debug=True)
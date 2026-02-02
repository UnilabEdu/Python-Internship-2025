from flask import Flask, render_template, redirect, url_for
from forms import RegisterForm
from os import path
from uuid import uuid4


app = Flask(__name__)
app.config["SECRET_KEY"] = "a9F#kP2!Zr8M@xQwL7dS$E4yHcN%VJmT"
UPLOAD_PATH = path.join(app.root_path, "static", "img")

movies = [
    {
        "movie_id": "0",
        "name": "Home Alone",
        "release_date": "1990",
        "genre": "Family / Comedy",
        "description": "ნინი: ჩემთვის ახალი წლის გარეშე ეს ფილმი არ არსებობს 🎄",
        "img": "img/91tXzecvy-L._AC_UF1000,1000_QL80_.jpg",
        "comment1_author": "ნინი",
        "comment1_text": "ჩემთვის ახალი წლის გარეშე ეს ფილმი არ არსებობს 🎄",
        "comment2_author": "გიორგი",
        "comment2_text": "ბავშვობის ყველაზე თბილი მოგონებები უკავშირდება"
    },
    {
        "movie_id": "1",
        "name": "It",
        "release_date": "2017",
        "genre": "Horror",
        "description": "ლაშა: ძალიან დაძაბული საშინელებაა",
        "img": "img/It_(2017)_poster.jpg",
        "comment1_author": "ლაშა",
        "comment1_text": "ძალიან დაძაბული და კარგად გადაღებული საშინელებაა",
        "comment2_author": "მარი",
        "comment2_text": "მუსიკა და ატმოსფერო განსაკუთრებით მომეწონა"
    },
    {
        "movie_id": "2",
        "name": "The Dark Knight",
        "release_date": "2008",
        "genre": "Action / Crime / Drama",
        "description": "დავით: ჯოკერი ლეგენდარულია",
        "img": "img/thedarkknight.jpg",
        "comment1_author": "დავით",
        "comment1_text": "ჯოკერის შესრულება უბრალოდ ლეგენდარულია",
        "comment2_author": "ანა",
        "comment2_text": "ერთ-ერთი საუკეთესო ფილმია, რაც ოდესმე მინახავს"
    },
    {
        "movie_id": "2",
        "name": "Interstellar",
        "release_date": "2014",
        "genre": "Sci-Fi / Drama",
        "description": "საბა: ვიზუალურად საოცარია",
        "img": "img/91JnoM0khKL._AC_UF1000,1000_QL80_.jpg",
        "comment1_author": "საბა",
        "comment1_text": "ემოციურად ძალიან ძლიერი და ვიზუალურად საოცარი",
        "comment2_author": "ეკა",
        "comment2_text": "ბოლოს ყოველთვის goosebumps მაქვს"
    }
]

users = []

@app.route("/")
def index():
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
    if 0 <= movie_id < len(movies):
        return render_template("view_movie.html", movie=movies[movie_id])
    else:
        return "<h1>Movie not found</h1>"


if __name__ == '__main__':
    app.run(debug=True)
from fileinput import filename
from flask_wtf import FlaskForm
from flask import Flask, render_template, redirect, url_for, request
from os import path

from sqlalchemy import ForeignKey

from forms import RegisterForm, ProductForm
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.file import FileAllowed, FileField, FileRequired, FileSize
from uuid import uuid4
### EXTENSIONS ###


app = Flask(__name__)
UPLOAD_PATH = path.join(app.root_path, 'static', 'upload')
app.config["SECRET_KEY"] = "AWDWQDASDSAFHSFJWIasjdalskfjqwoijf@1234098"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

### MODELS ###

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    img = db.Column(db.String)

### ONE TO ONE ###
class Person(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    birth_date = db.Column(db.Date)
    idcard_id = db.Column(db.Integer, db.ForeignKey('id_cards.id'))
    idcard = db.relationship('IDCard', back_populates='person')

class IDCard(db.Model):
    __tablename__ = 'id_cards'
    id = db.Column(db.Integer, primary_key=True)
    personal_number = db.Column(db.String)
    serial_number = db.Column(db.String)
    expiration_date = db.Column(db.Date)
    person = db.relationship('Person', back_populates='idcard', uselist=False)

### ONE TO MANY ###
class University(db.Model):
    __tablename__ = 'universities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    students = db.relationship('Student', back_populates='university')
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    university_id = db.Column(db.Integer, db.ForeignKey('universities.id'))
    university = db.relationship('University', back_populates='students')

### MANY TO MANY ###
class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    movies = db.relationship('Movie', back_populates='actors', secondary='actors_movies')
class ActorMovie(db.Model):
    __tablename__ = 'actors_movies'
    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
### ASSOCIATION TABLE ###

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    actors = db.relationship('Actor', back_populates='movies', secondary = 'actors_movies')
users=[]

### ROUTES ###

@app.route('/')
def index():
    products = Product.query.all()
    #product = Product.query.filter(Product.name.ilike("%Iphone%")).all()
    #print(product)
    return render_template("index.html", users=users, product_list=products)
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
            file = form.profile_image.data
            _, extension = path.splitext(file.filename)
            filename = f"{uuid4()}{extension}"
            file.save(path.join(UPLOAD_PATH, filename))
    else:
        print(form.errors)
    return render_template("register.html", form=form)
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/view_product/<int:product_id>')
def view_product(product_id):
    product = Product.query.get(product_id)
    return render_template("view_product.html", product=product )
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/create_product', methods=["GET", "POST"])
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        file = form.img.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(UPLOAD_PATH, filename))
        new_product = Product(name=form.name.data, price=form.price.data, img=filename)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_product.html', form=form)

@app.route('/edit_product/<int:product_id>', methods=["GET", "POST"])
def edit_product(product_id):
    product = Product.query.get(product_id)
    form = ProductForm(name=product.name, price=product.price)
    if form.validate_on_submit():
        if form.img.data:
            file = form.img.data
            _, extension = path.splitext(file.filename)
            filename = f"{uuid4()}{extension}"
            file.save(path.join(UPLOAD_PATH, filename))
            product.img=filename

        product.name = form.name.data
        product.price = form.price.data

        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_product.html', form=form)

@app.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
from flask.cli import with_appcontext
import click
from MyPage.src.models import Product
from MyPage.src.ext import db

products = [
    {"id":0, "name": "შოთა", "surname": "რუსთაველი", "ფასი": "68", "img":"shotaOqro.jpg.jpeg"},
    {"id":1, "name": "ვაჟა", "surname": "ფშაველა", "ფასი": "48", "img":"tetriVaja.jpg.jpeg"},
    {"id":2, "name": "ილია", "surname": "ჭავჭავაძე", "ფასი": "48", "img": "Nacarilia.jpg.jpeg"},
    {"id":3, "name": "აკაკი", "surname": "წერეთელი", "ფასი":" 48", "img": "akaki.jpg.jpeg"},
    {"id":4, "name": "გალაკტიონ", "surname": "ტაბიძე", "ფასი": "48", "img": "shaviGala.jpg.jpeg"},
    {"id":5, "name": "ილია", "surname": "ჭავჭავაძე", "ფასი": "48", "img": "bajagloIlia.jpg.jpeg"},
    {"id":6, "name": "გალაკტიონ", "surname": "ტაბიძე", "ფასი": "48", "img": "tetriGa;a.jpg.jpeg"},
    {"id":7, "name": "ვაჟა", "surname": "ფშაველა", "ფასი": "68", "img":"oqrosVaja.jpg.jpeg"}

]

@click.command("init_db")
@with_appcontext
def init_db():

    click.echo("Initializing database...")

    db.drop_all()
    db.create_all()

    click.echo("Database Created.")

@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Populating database...")
    for product in products:
        new_product = Product(name=product["name"], surname=product["surname"], price=product["ფასი"],
                              img=product["img"])
        new_product.create(commit=False)

    new_product.save()
    click.echo("Database Populated.")



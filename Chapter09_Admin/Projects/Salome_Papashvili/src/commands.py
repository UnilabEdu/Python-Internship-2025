from flask.cli import with_appcontext
import click
from src.ext import db
from src.models import Tour, User

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Initializing database...")
    db.drop_all()
    db.create_all()
    click.echo("Initialized database")


@click.command("populate_db")
@with_appcontext
def populate_db():
    tours = [
        {
            "id": 0,
            "country": "Italy",
            "title": "Rome Ancient Wonders Tour",
            "description": "Discover the Colosseum, Roman Forum, and Vatican City.",
            "price": 279.99,
            "currency": "EUR",
            "image": "https://www.agoda.com/wp-content/uploads/2024/08/Colosseum-Rome-Featured.jpg",
            "duration": "4 days",
        },
        {
            "id": 1,
            "country": "Egypt",
            "title": "Cairo & Pyramids Adventure",
            "description": "Visit the Great Pyramids of Giza and the Egyptian Museum.",
            "price": 349.99,
            "currency": "USD",
            "image": "https://upload.wikimedia.org/wikipedia/commons/a/af/All_Gizah_Pyramids.jpg",
            "duration": "5 days",
        },
        {
            "id": 2,
            "country": "Australia",
            "title": "Sydney & Blue Mountains",
            "description": "Explore Sydney Opera House, Harbour Bridge, and Blue Mountains.",
            "price": 499.99,
            "currency": "AUD",
            "image": "https://www.sydneytravelguide.com.au/wp-content/uploads/2024/09/sydney-australia.jpg",
            "duration": "6 days",
        },
        {
            "id": 3,
            "country": "Spain",
            "title": "Barcelona",
            "description": "Admire Sagrada Familia, Park Güell, and Gothic Quarter.",
            "price": 259.99,
            "currency": "EUR",
            "image": "https://www.introducingbarcelona.com/f/espana/barcelona/barcelona.jpg",
            "duration": "3 days",
        },
        {
            "id": 4,
            "country": "Turkey",
            "title": "Istanbul Heritage Tour",
            "description": "Visit Hagia Sophia, Blue Mosque, and Grand Bazaar.",
            "price": 199.99,
            "currency": "USD",
            "image": "https://deih43ym53wif.cloudfront.net/small_cappadocia-turkey-shutterstock_1320608780_9fc0781106.jpeg",
            "duration": "4 days",
        }
    ]

    for tour in tours:
        new_tour = Tour(country=tour["country"],
                        title=tour["title"],
                        description=tour["description"],
                        price=tour["price"],
                        currency=tour["currency"],
                        image=tour["image"],
                        duration=tour["duration"])
        db.session.add(new_tour)
    db.session.commit()

    # Admin
    User(username="Admin", password="password12345", profile_image="admin.png", role="Admin").create()
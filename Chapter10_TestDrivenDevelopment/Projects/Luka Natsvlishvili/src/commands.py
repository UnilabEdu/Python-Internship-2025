from flask.cli import with_appcontext
import click

from src.ext import db

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Initializing database")
    db.create_all()
    click.echo("Finished initializing database")

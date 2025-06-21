from flask import Blueprint, render_template, redirect, url_for
from uuid import uuid4
from os import path
from src.views.product.forms import AddTourForm
from src.models.product import Tour
from src.config import Config
from flask_login import login_required
from src.utils import admin_required

product_blueprint = Blueprint("products", __name__)

@product_blueprint.route("/trips")
def trips():
    tours = Tour.query.all()
    return render_template("product/trips.html", tours=tours)

@product_blueprint.route("/trips/<int:tour_id>")
def tour_detail(tour_id):
    chosen_tour = Tour.query.get(tour_id)
    return render_template("product/tour_detail.html", tour=chosen_tour)

@product_blueprint.route("/add_tour", methods=["GET", "POST"])
@admin_required
def add_tour():
    form = AddTourForm()
    if form.validate_on_submit():
        file = form.image.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(Config.UPLOAD_PATH, filename))
        new_tour = Tour(country=form.country.data,
                        title=form.title.data,
                        description=form.description.data,
                        price=form.price.data,
                        currency=form.currency.data,
                        duration=form.duration.data,
                        image = filename)
        new_tour.image = filename
        new_tour.create()
        return redirect(url_for("products.trips"))
    else:
        print(form.errors)
    return render_template("product/add_tour.html", form=form)

@product_blueprint.route("/edit_tour/<int:tour_id>", methods=["GET", "POST"])
@admin_required
def edit_tour(tour_id):
    tour = Tour.query.get(tour_id)
    form = AddTourForm(country=tour.country,
                        title=tour.title,
                        description=tour.description,
                        price=tour.price,
                        currency=tour.currency,
                        duration=tour.duration)
    if form.validate_on_submit():
        tour.country = form.country.data
        tour.title = form.title.data
        tour.description = form.description.data
        tour.price = form.price.data
        tour.currency = form.currency.data
        tour.duration = form.duration.data

        if form.image.data:
            file = form.image.data
            _, extension = path.splitext(file.filename)
            filename = f"{uuid4()}{extension}"
            file.save(path.join(Config.UPLOAD_PATH, filename))
            tour.image = filename
        tour.save()
        return redirect(url_for("products.trips"))
    return render_template("product/add_tour.html", form=form)


@product_blueprint.route("/delete_tour/<int:tour_id>")
@admin_required
def delete_tour(tour_id):
    tour = Tour.query.get(tour_id)
    tour.delete()
    return redirect(url_for("products.trips"))
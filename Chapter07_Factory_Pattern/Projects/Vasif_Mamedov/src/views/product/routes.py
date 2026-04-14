
from flask import render_template, redirect, url_for, Blueprint
from uuid import uuid4
from os import path

from src.views.product.forms import ProductForm
from src.config import Config
from src.models import Product

product_blueprint = Blueprint("products", __name__)

@product_blueprint.route('/view_product/<int:product_id>')
def view_product(product_id):
    product = Product.query.get(product_id)
    return render_template("product/view_product.html", product=product )


@product_blueprint.route('/create_product', methods=["GET", "POST"])
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        file = form.img.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(Config.UPLOAD_PATH, filename))
        new_product = Product(name=form.name.data, price=form.price.data, img=filename)
        new_product.create()
        return redirect(url_for('main.index'))
    return render_template('product/create_product.html', form=form)

@product_blueprint.route('/edit_product/<int:product_id>', methods=["GET", "POST"])
def edit_product(product_id):
    product = Product.query.get(product_id)
    form = ProductForm(name=product.name, price=product.price)
    if form.validate_on_submit():
        if form.img.data:
            file = form.img.data
            _, extension = path.splitext(file.filename)
            filename = f"{uuid4()}{extension}"
            file.save(path.join(Config.UPLOAD_PATH, filename))
            product.img=filename

        product.name = form.name.data
        product.price = form.price.data

        product.save()
        return redirect(url_for('main.index'))
    return render_template('product/create_product.html', form=form)

@product_blueprint.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    product = Product.query.get(product_id)
    product.delete()
    return redirect(url_for('main.index'))
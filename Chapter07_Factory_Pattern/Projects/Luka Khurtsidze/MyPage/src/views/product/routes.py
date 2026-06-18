from flask import render_template,redirect,url_for,Blueprint
from flask_login import login_required,current_user

from os import path
from uuid import uuid4



from MyPage.src.models import Product

from MyPage.src.views.product.forms import ProductForm
from MyPage.src.config import Config


product_blueprint = Blueprint('products', __name__)




@product_blueprint.route('/view_products/<int:product_id>')
def view_products(product_id):
    product = Product.query.get(product_id)
    return render_template("product/view_products.html", product=product)

@product_blueprint.route('/create_product/', methods=['GET', 'POST'])
@login_required
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        file = form.img.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(Config.UPLOAD_PATH, filename))

        new_product = Product(
            name=form.name.data,
            surname=form.surname.data,
            price=form.price.data,
            img =filename
        )
        new_product.create()
        return redirect(url_for("main.home"))
    return render_template("product/create_product.html", form=form)




@product_blueprint.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    product = Product.query.get(product_id)
    form = ProductForm(obj=product)

    print("Form errors:", form.errors)
    if form.validate_on_submit():
        if form.img.data and hasattr(form.img.data, 'filename'):
            file = form.img.data
            _, extension = path.splitext(file.filename)
            filename = f"{uuid4()}{extension}"
            file.save(path.join(Config.UPLOAD_PATH, filename))
            product.img = filename

        product.name = form.name.data
        product.surname = form.surname.data
        product.price = form.price.data
        product.save()
        return redirect(url_for("main.home"))

    return render_template("product/create_product.html", form=form)




@product_blueprint.route('/delete_product/<int:product_id>')
@login_required
def delete_product(product_id):
    products = Product.query.get(product_id)
    products.delete()
    return redirect(url_for("main.home"))

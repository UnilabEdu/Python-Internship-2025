from flask import render_template,Blueprint

from MyPage.src.models.product import Product

main_blueprint = Blueprint('main',__name__)

users = [

]

#### Routes ####


@main_blueprint.route('/')
def home():
    products = Product.query.all()
    print("PRODUCTS COUNT:", len(products))
    return render_template("main/home.html",users=users, products=products)

@main_blueprint.route('/about')
def about():
    product = Product.query.all()
    return render_template("main/about.html", product=product)
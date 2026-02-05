from flask import render_template, Blueprint

from src.models.product import Product


main_blueprint = Blueprint('main', __name__)
users = []
@main_blueprint.route('/')
def index():
    products = Product.query.all()
    #product = Product.query.filter(Product.name.ilike("%Iphone%")).all()
    #print(product)
    return render_template('main/index.html', users=users, product_list=products)

@main_blueprint.route('/about')
def about():
    return render_template("main/about.html")
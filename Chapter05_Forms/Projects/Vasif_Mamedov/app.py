from flask import Flask, render_template
from forms import RegisterForm
app = Flask(__name__)
app.config["SECRET_KEY"] = "AWDWQDASDSAFHSFJWIasjdalskfjqwoijf@1234098"
products = []
products = [
    {"id":0, "name":"s25", "price":100, "img":"/static/s25.jpg" },
    {"id":1, "name":"s25", "price":100, "img":"/static/s25.jpg" },
    {"id":2, "name":"s25", "price":100, "img":"/static/s25.jpg" },
    {"id":3, "name":"s25", "price":100, "img":"/static/s25.jpg" },
    {"id":4, "name":"iphone17", "price":200, "img":"/static/iphone17.jpg" },
    {"id":5, "name":"iphone17", "price":200, "img":"/static/iphone17.jpg" },
    {"id":6, "name":"iphone17", "price":200, "img":"/static/iphone17.jpg" },
    {"id":7, "name":"iphone17", "price":200, "img":"/static/iphone17.jpg" },
    {"id":8, "name":"iphone17", "price":200, "img":"/static/iphone17.jpg" },
    {"id":9, "name":"iphone17", "price":200, "img":"/static/iphone17.jpg" },
]

@app.route('/')
def index():
    return render_template("index.html", product_list=products)
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print("user registered")
    else:
        print("Something went wrong")
    return render_template("register.html", form=form)
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/view_product/<int:product_id>')
def view_product(product_id):
    return render_template("view_product.html", product=products[product_id] )
@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
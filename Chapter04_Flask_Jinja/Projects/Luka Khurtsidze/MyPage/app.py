from flask import Flask, render_template, url_for

app = Flask(__name__)

names = [
    {"id":0, "name": "შოთა", "surname": "რუსთაველი", "ფასი": "68 ლარი", "img":"shotaOqro.jpg.jpeg"},
    {"id":1, "name": "ვაჟა", "surname": "ფშაველა", "ფასი": "48 ლარი", "img":"tetriVaja.jpg.jpeg"},
    {"id":2, "name": "ილია", "surname": "ჭავჭავაძე", "ფასი": "48 ლარი", "img": "Nacarilia.jpg.jpeg"},
    {"id":3, "name": "აკაკი", "surname": "წერეთელი", "ფასი":" 48 ლარი", "img": "akaki.jpg.jpeg"},
    {"id":4, "name": "გალაკტიონ", "surname": "ტაბიძე", "ფასი": "48 ლარი", "img": "shaviGala.jpg.jpeg"},
    {"id":5, "name": "ილია", "surname": "ჭავჭავაძე", "ფასი": "48 ლარი", "img": "bajagloIlia.jpg.jpeg"},
    {"id":6, "name": "გალაკტიონ", "surname": "ტაბიძე", "ფასი": "48 ლარი", "img": "tetriGa;a.jpg.jpeg"},
    {"id":7, "name": "ვაჟა", "surname": "ფშაველა", "ფასი": "68 ლარი", "img":"oqrosVaja.jpg.jpeg"}

]


@app.route('/')
def home():
    return render_template("home.html",names=names)

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/about')
def about():
    return render_template("about.html", names=names)

@app.route('/view_names/<int:names_id>')
def view_names(names_id):
    return render_template("view_names.html",name=names[names_id])



if __name__ == "__main__":
    app.run(debug=True)
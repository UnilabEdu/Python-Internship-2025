from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/order')
def info():
    orders = [
        {'id': 1, 'name': 'order A', 'status': 'Processing'},
        {'id': 2, 'name': 'order B', 'status': 'Shipped'},
        {'id': 3, 'name': 'order C', 'status': 'Delivered'},
    ]
    return render_template('order.html', message="Your Orders", orders=orders)


if __name__ == '__main__':
    app.run(debug=True)

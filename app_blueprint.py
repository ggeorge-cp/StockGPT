from flask import Blueprint, render_template, url_for

app_blueprint = Blueprint('app_blueprint', __name__)

# Variables
example_stocks = [
    {'ticker': 'AAPL', 'name': 'Apple', 'img': '/images/aapl.png'},
    {'ticker': 'PANW', 'name': 'Palo Alto Networks', 'img': '/images/panw.png'},
    {'ticker': 'PG', 'name': 'Procter & Gamble Co', 'img': '/images/pg.png'}
]

@app_blueprint.route('/')
def index():
    return render_template("index.html", example_stocks=example_stocks)

@app_blueprint.route('/about')
def about():
    return render_template("about.html")
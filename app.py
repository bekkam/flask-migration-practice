from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Order


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        customer_name = request.form['customer-name']
        order_item = request.form['order-item']
        order = Order(customer_name=customer_name, order_item=order_item)
        db.session.add(order)
        db.session.commit()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

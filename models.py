from app import db
from datetime import datetime


class Order(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(30), nullable=False)
    order_item = db.Column(db.String(30), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, customer_name, order_item):
        self.customer_name = customer_name
        self.order_item = order_item

    def __repr__(self):
        return '<id {}>'.format(self.order_id)

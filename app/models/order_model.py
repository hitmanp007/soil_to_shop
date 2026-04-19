from app.extensions import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    buyer_name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
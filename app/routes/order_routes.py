from flask import Blueprint, request, jsonify
from app.models.order_model import Order
from app.extensions import db

order_bp = Blueprint('orders', __name__)

# 🛒 Place Order
@order_bp.route("/place", methods=["POST"])
def place_order():
    data = request.json

    order = Order(
        product_id=data['product_id'],
        buyer_name=data['buyer_name'],
        quantity=data['quantity']
    )

    db.session.add(order)
    db.session.commit()

    return jsonify({"message": "Order placed successfully"})
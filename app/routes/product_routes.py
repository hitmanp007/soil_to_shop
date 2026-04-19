from flask import Blueprint, request, jsonify
from app.models.product_model import Product
from app.extensions import db

product_bp = Blueprint('products', __name__)

# ➕ Add Product (Farmer)
@product_bp.route("/add", methods=["GET", "POST"])
def add_product():
    if request.method == "GET":
        return "Use POST to add product"

    data = request.json

    product = Product(
        name=data['name'],
        price=data['price'],
        quantity=data['quantity'],
        farmer_name=data['farmer_name'],
        location=data['location']
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product added successfully"})


# 📦 Get All Products
@product_bp.route("", methods=["GET"])
def get_products():
    products = Product.query.all()

    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "quantity": p.quantity,
            "farmer": p.farmer_name,
            "location": p.location
        })

    return jsonify(result)
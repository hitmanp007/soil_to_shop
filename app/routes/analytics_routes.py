from flask import Blueprint, jsonify

analytics_bp = Blueprint('analytics', __name__)

# 📈 Dummy Price Insights (Use your bill data later)
@analytics_bp.route("/prices", methods=["GET"])
def price_insights():
    data = {
        "tomato": {"market_price": 30, "platform_price": 25},
        "onion": {"market_price": 25, "platform_price": 20},
        "potato": {"market_price": 20, "platform_price": 18}
    }

    return jsonify(data)
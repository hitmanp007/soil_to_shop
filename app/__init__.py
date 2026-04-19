from flask import Flask
from .extensions import db

def create_app():
    app = Flask(__name__)

    # Config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///soil_to_shop.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Init extensions
    db.init_app(app)

    # Register routes
    from .routes.product_routes import product_bp
    from .routes.order_routes import order_bp
    from .routes.analytics_routes import analytics_bp

    app.register_blueprint(product_bp, url_prefix="/products")
    app.register_blueprint(order_bp, url_prefix="/orders")
    app.register_blueprint(analytics_bp, url_prefix="/analytics")

    return app
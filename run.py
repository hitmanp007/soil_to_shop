from app import create_app
from app.extensions import db

app = create_app()
@app.route("/")
def home():
    return "Soil to Shop Backend Running 🚀"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
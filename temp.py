import os

folders = [
    "app/models",
    "app/routes",
    "app/services",
    "app/utils",
    "migrations",
    "tests"
]

files = [
    "app/__init__.py",
    "app/config.py",
    "app/models/__init__.py",
    "app/models/user_model.py",
    "app/models/product_model.py",
    "app/models/order_model.py",
    "app/routes/__init__.py",
    "app/routes/user_routes.py",
    "app/routes/product_routes.py",
    "app/routes/order_routes.py",
    "app/routes/analytics_routes.py",
    "app/services/price_service.py",
    "app/services/ai_service.py",
    "app/utils/helpers.py",
    "app/extensions.py",
    "run.py",
    "requirements.txt",
    ".env",
    "README.md"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file in files:
    with open(file, "w") as f:
        f.write("")

print("✅ Project structure created successfully!")
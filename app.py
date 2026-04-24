from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.get("/product/<ids>")
def get_product(ids):
    id_list = ids.split(",")
    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = f"SELECT * FROM products WHERE id IN ({','.join(['%s'] * len(id_list))})"

    cursor.execute(query, id_list)
    product = cursor.fetchall()

    cursor.close()
    db.close()

    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    combined = {
        "name": product[0]["name"],
        "description": product[0]["description"],
        "image": product[0]["image"],
        "price": [products["price"] for products in product],
        "gram": [products["gram"] for products in product],
        "stock": [products["stock"] for products in product]
    }
    return jsonify(combined)

app.run()

from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os
import base64

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5500", "http://localhost:5500"]}})

@app.get("/test")
def test():
    return "Backend is running"
"""
def get_db():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
    except Exception as e:
        print("DB ERROR:", e)
        raise
        

@app.get("/product/<ids>")
def get_product(ids):
    id_list = ids.split(",")
    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = f"SELECT * FROM products WHERE id IN ({','.join(['%s'] * len(id_list))})"
    cursor.execute(query, id_list)
    rows = cursor.fetchall()

    cursor.close()
    db.close()

    if not rows:
        return jsonify({"error": "Product not found"}), 404

    combined = {
        "name": rows[0]["name"],
        "description": rows[0]["description"],
        "image": base64.b64encode(rows[0]["image"]).decode("utf-8"),
        "price": [r["price"] for r in rows],
        "gram": [r["gram"] for r in rows],
        "stock": [r["stock"] for r in rows]
    }

    return jsonify(combined)
"""

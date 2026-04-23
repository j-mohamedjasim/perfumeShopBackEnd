from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def get_db():
    return mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )

@app.get("/product/<id>")
def get_product(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products WHERE id = %s",(id))
    product = cursor.fetchone()

    cursor.close()
    db.close()

    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    return jsonify(product)

app.run()
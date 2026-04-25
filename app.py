from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os
import base64


@app.get("/product/<ids>")
def get_product(ids):
    print("REQUEST IDS:", ids)
    try:
        id_list = ids.split(",")
        print("ID LIST:", id_list)

        db = get_db()
        print("DB CONNECTED")

        cursor = db.cursor(dictionary=True)

        query = f"SELECT * FROM products WHERE id IN ({','.join(['%s'] * len(id_list))})"
        print("QUERY:", query)

        cursor.execute(query, id_list)
        rows = cursor.fetchall()
        print("ROWS:", rows)

        cursor.close()
        db.close()

        if not rows:
            print("NO ROWS FOUND")
            return jsonify({"error": "Product not found"}), 404

        combined = {
            "name": rows[0]["name"],
            "description": rows[0]["description"],
            "image": base64.b64encode(rows[0]["image"]).decode("utf-8"),
            "price": [r["price"] for r in rows],
            "gram": [r["gram"] for r in rows],
            "stock": [r["stock"] for r in rows]
        }

        print("COMBINED:", combined)
        return jsonify(combined)

    except Exception as e:
        print("ROUTE ERROR:", e)
        raise

from flask import Flask, jsonify
from flask_cors import CORS
import redis
import json

app = Flask(__name__)
CORS(app)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route("/scraped-content", methods=["GET"])
def get_scraped_content():
    """
    Get all scraped data from Redis.
    Returns head, header, and products from the Croma website.
    """
    data = r.get("scraped_content")
    if data:
        return jsonify({"success": True, "data": json.loads(data)})
    else:
        return jsonify({"success": False, "message": "No data found"}), 404

@app.route("/products", methods=["GET"])
def get_products():
    """
    Get only the products list from scraped data.
    Returns TV and accessory products with prices, discounts, and offers.
    """
    data = r.get("scraped_content")
    if data:
        products = json.loads(data).get("products", [])
        return jsonify({"success": True, "products": products})
    else:
        return jsonify({"success": False, "message": "No product data found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
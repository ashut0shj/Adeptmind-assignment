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
    TODO: Implement an API to retrieve scraped content from Redis.
    This endpoint should do the following:
    2. Retrieve the scraped content from Redis.
    4. If no data is found, return a 404 error with a message.
    5. If data is found, return a success response with the data in JSON format.
    """
    data = r.get("scraped_content")
    if data:
        return jsonify({"success": True, "data": json.loads(data)})
    else:
        return jsonify({"success": False, "message": "No data found"}), 404

@app.route("/products", methods=["GET"])
def get_products():
    """
    This endpoint returns a list of products with their details.
    """
    data = r.get("scraped_content")
    if data:
        products = json.loads(data).get("products", [])
        return jsonify({"success": True, "products": products})
    else:
        return jsonify({"success": False, "message": "No product data found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
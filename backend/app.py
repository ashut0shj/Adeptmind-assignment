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
    return [
        {"product_id": "1", "title": "Smart LED TV 32 inch", "price": "₹20,000", "sale_price": "₹18,000", "discount_message": "10% off"},
        {"product_id": "2", "title": "4K UHD Smart TV 43 inch", "price": "₹35,000", "sale_price": "₹31,500", "discount_message": "10% off"},
        {"product_id": "3", "title": "OLED TV 55 inch", "price": "₹1,20,000", "sale_price": "₹1,08,000", "discount_message": "10% off"},
        {"product_id": "4", "title": "Soundbar with Subwoofer", "price": "₹15,000", "sale_price": "₹13,500", "discount_message": "10% off"},
        {"product_id": "5", "title": "TV Wall Mount", "price": "₹2,000", "sale_price": "₹1,800", "discount_message": "10% off"},
        {"product_id": "6", "title": "Streaming Stick", "price": "₹4,000", "sale_price": "₹3,600", "discount_message": "10% off"},
        {"product_id": "7", "title": "Smart LED TV 40 inch", "price": "₹25,000", "sale_price": "₹22,500", "discount_message": "10% off"},
        {"product_id": "8", "title": "Bluetooth Speakers", "price": "₹5,000", "sale_price": "₹4,500", "discount_message": "10% off"},
        {"product_id": "9", "title": "4K Smart LED TV 50 inch", "price": "₹45,000", "sale_price": "₹40,500", "discount_message": "10% off"},
        {"product_id": "10", "title": "TV Remote", "price": "₹1,500", "sale_price": "₹1,350", "discount_message": "10% off"}
    ]



if __name__ == "__main__":
    app.run(debug=True)
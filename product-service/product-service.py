from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = {"id": len(products) + 1, **data}
    products.append(new_product)
    return jsonify(new_product), 201

if __name__

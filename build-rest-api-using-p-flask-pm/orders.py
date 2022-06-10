from asyncio.windows_events import NULL
import json
from flask import Flask, jsonify, make_response, render_template, request

app = Flask(__name__)

order = {
    "order1": {
        "Size":"Small",
        "Toppings":"Cheese",
        "Crust": "Thin Crust"
    },
    "order2": {
        "Size":"Medium",
        "Toppings":"Chocolate",
        "Crust": "Thick Crust"
    },
    "order3": {
        "Size":"Extra Large",
        "Toppings":"Double Cheese",
        "Crust": "Mega Crust"
    }
}

@app.route("/orders")
def get_order():
    response = make_response(jsonify(order), 200)
    return response

@app.route("/orders/<order_id>")
def get_order_details(order_id):
    if order_id in order:
        response=make_response(jsonify(order[order_id]), 200)
        return response
    return "Order not Found"

@app.route("/orders/<order_id>/<items>")
def get_item_details(order_id, items):
    item = order[order_id].get(items)
    if item:
        response=make_response(jsonify(item), 200)
        return response
    return "Item not Found"

@app.route("/orders/<order_id>", methods=['POST'])
def post_order_details(order_id):
    req=request.get_json()
    if order_id in order:
        response=make_response(jsonify({"error": "Order ID already exists!"}), 400)
        return response
    order.update({order_id:req})
    response=make_response(jsonify({"message": "Order created!"}), 201)
    return response

@app.route("/orders/<order_id>", methods=['PUT'])
def put_order_details(order_id):
    req=request.get_json()
    if order_id in order:
        order[order_id]=req
        response=make_response(jsonify({"message": "Order updated!"}), 200)
        return response
    order[order_id]=req
    response=make_response(jsonify({"message": "Order created!"}), 201)
    return response

@app.route("/orders/<order_id>", methods=['PATCH'])
def patch_order_details(order_id):
    req=request.get_json()
    if order_id in order:
        for k, v in req.items():
            order[order_id][k]=v
        response=make_response(jsonify({"message": "Order updated!"}), 200)
        return response
    order[order_id]=req
    response=make_response(jsonify({"message": "Order created!"}), 201)
    return response

@app.route("/orders/<order_id>", methods=['DELETE'])
def delete_order_details(order_id):
    if order_id in order:
        del order[order_id]
        response=make_response(jsonify({"message": "Order deleted!"}), 204)
        return response
    response=make_response(jsonify({"message": "Order not found!"}), 404)
    return response

if __name__ == '__main__':
    app.run(debug=True)
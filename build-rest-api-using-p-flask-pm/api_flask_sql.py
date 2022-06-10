from flask import Flask, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///myapp.sqlite'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class MyApp(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(500))
    toppings = db.Column(db.String(500))
    crust = db.Column(db.String(500))

class MyAppSchema(ma.Schema):
    class Meta:
        fields = ('order_id', 'size', 'toppings', 'crust')

my_app_schema = MyAppSchema(many=True)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/order')
def get_order():
    entries = MyApp.query.all()
    result = my_app_schema.dump(entries)
    return jsonify(result)

@app.route('/order/<int:order_id>')
def get_order_id(order_id):
    entries = MyApp.query.all()
    result = my_app_schema.dump(entries)
    return jsonify(result[order_id])

@app.route('/order', methods=["POST"])
def post_order():
    req = request.get_json()
    order_id = req["order_id"]
    size = req["size"]
    toppings = req["toppings"]
    crust = req["crust"]
    new_entry = MyApp(order_id=order_id, size=size, toppings=toppings, crust=crust)
    db.session.add(new_entry)
    db.session.commit()    
    return {"message": "Order %d created." % order_id}, 200

@app.route('/order/<int:order_id>', methods=["PUT"])
def update_order(order_id):
    req = request.get_json()
    entry = MyApp.query.get_or_404(order_id)
    entry.order_id = req["order_id"]
    entry.size = req["size"]
    entry.toppings = req["toppings"]
    entry.crust = req["crust"]
    db.session.add(entry)
    db.session.commit()    
    return {"message": "Order %d updated." % order_id}, 200

@app.route('/order/<int:order_id>', methods=["DELETE"])
def delete_order(order_id):
    entry = MyApp.query.get_or_404(order_id)
    db.session.delete(entry)
    db.session.commit()
    return {"message": "Order %d removed." % order_id}, 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
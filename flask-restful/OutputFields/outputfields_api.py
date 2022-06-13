from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+mysqlconnector://root:password123@localhost/bookshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)

class Book(db.Model):

    book_id = db.Column(db.String(24), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float())
    quantity = db.Column(db.Integer())

    def __init__(self, book_id, title, author, price, quantity):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

class AvailableItem(fields.Raw):
    def format(self, value):
        return "Available" if value > 0 else "Unavailable"

class SpecialOfferItem(fields.Raw):
    def format(self, value):
        return "Special Offer!!" if value < 1.0 else "No offer yet"

class LowercaseItem(fields.Raw):
    def format(self, value):
        return value.lower()

class UppercaseItem(fields.Raw):
    def format(self, value):
        return value.upper()

resource_fields = {
    #renaming fields
    'book_id': fields.String,
    'book_title': UppercaseItem(attribute='title'),
    'book_author': fields.String(attribute=lambda book: book.author.lower()),
    'book_price_quantity': {
        'book_price': fields.Float(attribute='price', default=1.99), #default sets default value when retrieving data
        'book_quantity': fields.Integer(attribute='quantity', default=1),
    },
    'uri': fields.Url('book'),
    'https_uri': fields.Url('book', absolute=True, scheme='https'),
    'status': AvailableItem(attribute='quantity'),
    'offer': SpecialOfferItem(attribute='price')
}

class Books(Resource):

    @marshal_with(resource_fields)
    def get(self):
        
        return Book.query.all()


class PhilipKDickBooks(Resource):

    @marshal_with(resource_fields, envelope='pkd_books')
    def get(self):

        books = Book.query.filter_by(author="Philip K. Dick").all()
        return books


class  RayBradburyBooks(Resource):

    @marshal_with(resource_fields, envelope='ray_books')
    def get(self):

        books = Book.query.filter_by(author="Ray Bradbury").all()
        return books


class  UrsulaKLeGuinBooks(Resource):

    @marshal_with(resource_fields, envelope='ursula_books')
    def get(self):
        
        books = Book.query.filter_by(author="Ursula K. LeGuin").all()
        return books


class  ArthurCClarkeBooks(Resource):

    @marshal_with(resource_fields, envelope='clarke_books')
    def get(self):
        
        books = Book.query.filter_by(author="Arthur C. Clarke").all()
        return books


api.add_resource(Books, '/books/all', endpoint='book')
api.add_resource(PhilipKDickBooks, '/books/pkd')
api.add_resource(RayBradburyBooks, '/books/ray')
api.add_resource(UrsulaKLeGuinBooks, '/books/ursula')
api.add_resource(ArthurCClarkeBooks, '/books/clarke')

if __name__ == '__main__':
    app.run(debug=True)        
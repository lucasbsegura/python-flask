from flask import Flask, jsonify, make_response, request
from flask_restful import Resource, Api, marshal_with, reqparse, abort, fields, marshal
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password123@localhost/bookshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

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


resource_fields = {
    'book_id': fields.String,
    'title': fields.String,
    'author': fields.String,
    'price': fields.Float,
    'quantity': fields.Integer,
}

add_book_parser = reqparse.RequestParser()
add_book_parser.add_argument("author", type=str, required=True)
add_book_parser.add_argument("title", type=str, required=True)
add_book_parser.add_argument("price", type=float, required=True)
add_book_parser.add_argument("quantity", type=int, required=True)

update_book_parser = add_book_parser.copy()
update_book_parser.remove_argument("author")
update_book_parser.remove_argument("title")
update_book_parser.replace_argument("price", type=float)
update_book_parser.replace_argument("quantity", type=int)

class Books(Resource):

    @marshal_with(resource_fields)
    def get(self):
        
        return Book.query.all()

class SingleBook(Resource):

    @marshal_with(resource_fields)
    def get(self, book_id):

        book = Book.query.get(book_id)

        if not book:
            abort(404, message='Book id ' + book_id + ' not found.')

        return book, 200

    @marshal_with(resource_fields)
    def post(self, book_id):

        args = add_book_parser.parse_args()
        book = Book.query.filter_by(book_id = book_id).first()

        if book:
            abort(412, message='Book id ' + book_id + ' already exists.')
        
        book = Book(book_id=book_id,
                    title=args['title'],
                    author=args['author'],
                    price=args['price'],
                    quantity=args['quantity'])

        db.session.add(book)
        db.session.commit()

        return book, 201

    @marshal_with(resource_fields)
    def put(self, book_id):

        args = update_book_parser.parse_args()
        book = Book.query.filter_by(book_id = book_id).first()

        if not book:
            abort(404, message='Book id ' + book_id + ' not found.')
        
        for key, value in args.items():
            if key == "price" and value:
                book.price = value
            if key == "quantity" and value:
                book.quantity = value
        
        db.session.add(book)
        db.session.commit()

        return book, 200

    def delete(self, book_id):

        book = Book.query.filter_by(book_id = book_id).first()

        if not book:
            abort(404, message='Book id ' + book_id + ' not found.')

        db.session.delete(book)
        db.session.commit()

        return "", 204

        
api.add_resource(Books, '/books/all')
api.add_resource(SingleBook, '/books/<string:book_id>')


if __name__ == '__main__':
    app.run(debug=True)
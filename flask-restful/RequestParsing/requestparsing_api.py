from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

book_details = {}

book_parser = reqparse.RequestParser() #args = from query, form = from form
book_parser.add_argument("author", type=str, required=True, 
                            location=["args", "form"], help="Author should not be empty.")
book_parser.add_argument("title", type=str, required=True, action='append', 
                            location='form', dest="titles")
book_parser.add_argument("details", type=str, dest="additional-info", 
                            location='form')
book_parser.add_argument("price", type=float, required=True, 
                            location='form', help="Price should be a valid numeric value.")
book_parser.add_argument("quantity", type=int, required=True, 
                            location='form', dest="inventory", help="Quantity  should be a valid integer value.")
#its possible to get the user-agent or cookies
book_parser.add_argument("User-Agent", type=str, location='headers')

class Book(Resource):
    
    def get(self, book_id):
        if book_id in book_details:
            return book_details[book_id]

        return {'message': 'Book id ' + book_id + ' not found.'}

    def post(self, book_id):
        if book_id in book_details:
            return {'message': 'Book id ' + book_id + ' already exists.'}

        args = book_parser.parse_args()
        book_details[book_id] = args

        print("Arguments: " + str(args))

        return {'message': 'Book id ' + book_id + ' added.'}

api.add_resource(Book, '/books/<string:book_id>')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
api = Api(app)

book_details = {}

book_parser = reqparse.RequestParser() #bundle_errors=True
book_parser.add_argument("author", type=str, required=True)
book_parser.add_argument("title", type=str, required=True, help="Title should not be empty.")
book_parser.add_argument("details", type=str)
book_parser.add_argument("price", type=float, required=True)
book_parser.add_argument("quantity", type=int, required=True,
                            choices=(0,1,2,3,4,5), help="Invalid quantity: {error_msg}")


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
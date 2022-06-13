from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

book_details = {}

add_book_parser = reqparse.RequestParser()
add_book_parser.add_argument("author", type=str, required=True)
add_book_parser.add_argument("title", type=str, required=True)
add_book_parser.add_argument("details", type=str)
add_book_parser.add_argument("price", type=float, required=True)
add_book_parser.add_argument("quantity", type=int, required=True)

update_book_parser = add_book_parser.copy()
update_book_parser.remove_argument("author")
update_book_parser.remove_argument("title")
update_book_parser.replace_argument("price", type=float)
update_book_parser.replace_argument("quantity", type=int)


class Book(Resource):
    def get(self, book_id):
        if book_id in book_details:
            return book_details[book_id]

        return {'message': 'Book id ' + book_id + ' not found.'}

    def post(self, book_id):
        if book_id in book_details:
            return {'message': 'Book id ' + book_id + ' already exists.'}

        args = add_book_parser.parse_args()
        book_details[book_id] = args

        print("Arguments: " + str(args))

        return {'message': 'Book id ' + book_id + ' added.'}

    def put(self, book_id):
        if book_id not in book_details:
            return {'message': 'Book id ' + book_id + ' not found.'}
        
        args = update_book_parser.parse_args()

        print("Arguments: " + str(args))

        for key, value in args.items():
            if value:
                book_details[book_id][key] = value

        return {'message': 'Book id ' + book_id + ' updated.'}
    

api.add_resource(Book, '/books/<string:book_id>')


if __name__ == '__main__':
    app.run(debug=True)
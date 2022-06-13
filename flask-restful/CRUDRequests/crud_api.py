from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True

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

class Books(Resource):

    def get(self):
        return {"books": book_details}, 200

class Book(Resource):

    def get(self, book_id):

        if book_id in book_details:
            return book_details[book_id], 200

        abort(404, message='Book id: ' + book_id + ' not found.')

    def post(self, book_id):

        if book_id in book_details:
            abort(412, message='Book id ' + book_id + ' already exists.')

        args = add_book_parser.parse_args()
        book_details[book_id] = args

        return book_details[book_id], 201

    def put(self, book_id):

        if book_id not in book_details:
            abort(404, message='Book id ' + book_id + ' not found.')
        
        args = update_book_parser.parse_args()

        for key, value in args.items():
            if value:
                book_details[book_id][key] = value

        return book_details[book_id], 200

    def delete(self, book_id):

        if book_id in book_details:
            del book_details[book_id]
    
        return "", 204

api.add_resource(Book, '/books/<string:book_id>')
api.add_resource(Books, '/books/all')

if __name__ == '__main__':
    app.run(debug=True)
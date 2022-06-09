from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

book_details = {}

class Book(Resource):

    def get(self, book_id):

        if book_id in book_details:
            return book_details[book_id]

        return {'message': 'Book Id: ' + book_id + ' not found.'}

    def post(self, book_id):

        if book_id in book_details:
            return {'message': 'Book Id: ' + book_id + ' exists!'}

        #print('Request body contents: ' + str(request.data))
        #json_body = request.json
        #print('Title: ' + json_body["title"])
        #print('Author: ' + json_body["author"])
        #print('Details: ' + json_body["details"])
        print('Title: ' + request.form["title"])
        print('Author: ' + request.form["author"])
        print('Details: ' + request.form["details"])

        book_info = {}
        for key in request.form:
            book_info[key] = request.form[key]

        book_details[book_id] = book_info

        print(book_details)

        return {'message': 'Book Id: ' + book_id + ' added.'}


api.add_resource(Book, '/books/<string:book_id>')



if __name__ == '__main__':
    app.run(debug=True)
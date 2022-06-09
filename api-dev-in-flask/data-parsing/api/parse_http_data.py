from flask import request
from flask_restful import Resource

class ParseHTTPDataView(Resource):

    def get(self):
        print()
        print(' *** GET Request ***')
        print('Request args:', request.args)
        print('Request args "hello":', request.args.get('hello'))
        print()
        print(' *** HEADERS ***')
        print('Headers:\n', request.headers)
        print('User-Agent:', request.headers.get('User-Agent'))

        return { 'message' : 'GET ok' }, 200

    def post(self):
        print()
        print(' *** POST Request ***')

        json_data = request.get_json()
        
        print('POST Data (JSON):', json_data)
        print('POST email:', json_data.get('email'))
        
        return { 'message' : 'POST ok' }, 200

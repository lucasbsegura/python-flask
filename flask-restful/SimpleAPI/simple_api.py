from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello Worllllld! this is a response to GET!'}
    def post(self):
        return {'message': 'this is a response to POST!'}
    def put(self):
        return {'message': 'this is a response to PUT!'}
    def patch(self):
        return {'message': 'this is a response to PATCH!'}
    def delete(self):
        return {'message': 'this is a response to DELETE!'}

api.add_resource(HelloWorld, '/greeting')

if __name__ == "__main__":
    app.run(debug=True)
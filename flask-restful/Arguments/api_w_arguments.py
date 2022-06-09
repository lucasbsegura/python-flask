from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, name, name_2):
        return {'message': 'Hello ' + name + ' & ' + name_2 +'!'}
api.add_resource(HelloWorld, '/greeting/<string:name>/<string:name_2>')

emp_data_dict = \
    {
        100: {
            "name": "John",
            "designation": "Senior Engineer",
            "salary": 34000
        },
        200: {
            "name": "Mary",
            "designation": "Software Engineer",
            "salary": 25000
        }
    }

class Employee(Resource):
#    def get(self, emp_id, name):
#        return{'emp_id': emp_id, 'name': name}

#api.add_resource(Employee, '/employee/<int:emp_id>/<string:name>')

    def get(self, emp_id):
        return emp_data_dict[emp_id]

api.add_resource(Employee, '/employee/<int:emp_id>')


if __name__ == '__main__':
    app.run(debug=True)
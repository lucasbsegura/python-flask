from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

engg_emp_data_dict = \
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

sales_emp_data_dict = \
    {
        500: {
            "name": "Emily",
            "designation": "VP, Sales",
            "salary": 123000
        },
        600: {
            "name": "Joseph",
            "designation": "Field Sales Engineer",
            "salary": 27000
        }
    }

class EngineeringEmployee(Resource):
    def get(self, emp_id):
        return engg_emp_data_dict[emp_id]

class SalesEmployee(Resource):
    def get(self, emp_id):
        return sales_emp_data_dict[emp_id]

#api.add_resource(EngineeringEmployee, '/engg_employee/<int:emp_id>', '/engg/<int:emp_id>')
api.add_resource(EngineeringEmployee, '/engg_employee/<int:emp_id>', endpoint="eng_1")
api.add_resource(EngineeringEmployee, '/engg/<int:emp_id>', endpoint="eng_2")

api.add_resource(SalesEmployee, '/sales_employee/<int:emp_id>', '/sales/<int:emp_id>')

if __name__ == '__main__':
    app.run(debug=True)
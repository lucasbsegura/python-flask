from flask_restful import Resource
from datetime import datetime

class EntityView(Resource):
    
    def get(self):
        return { 'time': f'{datetime.today()}' }, 200
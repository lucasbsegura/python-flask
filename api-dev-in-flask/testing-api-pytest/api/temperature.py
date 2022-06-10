from flask import request
from flask_restful import Resource
import sys

class TemperatureView(Resource):

    def post(self):      
        try:
            data = request.get_json()
            temperature = float(data.get('temperature'))
            unit = data['unit']
            result = {}
                    
            if unit == 'f':
                result['temperature'] = (temperature - 32) / 9 * 5
                result['unit'] = 'c'
            else:
                result['temperature'] = temperature * 9 / 5 + 32
                result['unit'] = 'f'

            return result, 200

        except:
            for e in sys.exc_info():
                print(e)

            message = str(sys.exc_info()[0])
            return { 'error' : True, 'message' : message }, 400

from flask import request
from flask_restful import Resource
import sys
import logging

class DistanceView(Resource):

    def get(self):
        return { 'mi' : 1.0, 'km': 1.609344 }, 200
    
    def post(self):
        try:
            data = request.get_json()
            distance = float(data.get('distance'))
            unit = data['unit']
            result = {}
                    
            if unit == 'mi':
                result['distance'] = distance * 1.609344
                result['unit'] = 'km'
            else:
                result['distance'] = distance * 0.6213712
                result['unit'] = 'mi'

            return result, 200

        except:
            message = ''
            for e in sys.exc_info():
                message += str(e) + '\n'

            logging.debug(message)
            
            return { 'error' : True }, 400

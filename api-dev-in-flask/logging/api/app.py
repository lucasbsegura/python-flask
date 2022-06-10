from flask import Flask, jsonify
from api.extensions import Api
from api.temperature import TemperatureView

from werkzeug.exceptions import HTTPException, default_exceptions

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')

    # default all errors to JSON errors (instead of HTML)
    for code in default_exceptions:
        app.register_error_handler(code, json_error)
    app.register_error_handler(Exception, json_error)
    
    # associate the Flask app with the flask_restful Api
    api = Api(app)

    # endpoints (resources)
    api.add_resource(TemperatureView, '/temperature')

    return app


def json_error(error):    
    if isinstance(error, HTTPException):
        status_code = error.code
    else:
        status_code = 500 # default to 'Internal Server Error'
        
    return jsonify({ 'error' : str(error) }), status_code

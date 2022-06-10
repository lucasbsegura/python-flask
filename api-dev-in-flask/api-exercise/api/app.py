from flask import Flask, jsonify
from api.extensions import Api
from api.distance import DistanceView

from werkzeug.exceptions import HTTPException, default_exceptions

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')

    api = Api(app)
    api.add_resource(DistanceView, '/distance')

    return app

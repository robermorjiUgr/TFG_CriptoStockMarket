from urllib import request
from flask import jsonify
from flask import Blueprint
from flask_restx import Api, Resource
# from app import api

import pandas as pd

import json

import numpy as np

criptosocket_bp = Blueprint('criptosocket', __name__)

api = Api( criptosocket_bp )
ns_criptosocket = api.namespace('criptosocket', "Proyect api dashboard CriptoSocket:")


@ns_criptosocket.route('/hello',endpoint="hello")
@ns_criptosocket.doc(description="Hello service")
class helloworld(Resource):
    ''''
    To do: 
      hello world del servicio
    '''
    
    def get(self):
        return jsonify({'hello':'world'})



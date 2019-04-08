from flask_restful import Resource
from flask_restful import reqparse, Resource
from application import models, db

class Brands(Resource):
    def __init__(self):
        super(Brands, self).__init__()

    def get(self):
        hola = 'hola'
        return hola



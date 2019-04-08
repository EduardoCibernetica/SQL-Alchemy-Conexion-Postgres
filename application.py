# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import or_, and_, UniqueConstraint, func
from marshmallow import fields
from flask import Flask, render_template

app = Flask(__name__)

api = Api(app)


app.config.from_pyfile('settings/credenciales.py')

db = SQLAlchemy(app)
ma = Marshmallow(app)

from appi.models import models


from appi.resources.brands import Brands


api.add_resource(Brands, '/brands')



if __name__ == '__main__':
     app.run(host='0.0.0.0', debug=True, port=5040)

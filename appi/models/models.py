# -*- coding: utf-8 -*-

import uuid
import application

db = application.db
ma = application.ma
fields = application.fields
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

class Tienda(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR(), nullable=False)

    def __init__(self, name=None):
        self.name = name
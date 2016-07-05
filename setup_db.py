#!/usr/bin/env python

from piserver import db
from piserver.db_models import *  # NOQA


db.drop_all()
db.create_all()

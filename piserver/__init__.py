from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='fdjiaglhewughrusipghfusdi',
    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/piserver.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)


from .views import *  # NOQA

#!flask/bin/python
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')

bootstrap = Bootstrap(app)

from nuomi_dict.models import city_dict
city_dict = city_dict.CityDict()

from nuomi_dict import views

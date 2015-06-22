#!flask/bin/python
from flask_wtf import Form
#from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length

class QueryForm(Form):
    city_key = StringField('city_key', validators = [Required()])
    city_value = StringField('city_value', validators = [Length(min = 0, max = 140)])
    submit = SubmitField('submit')


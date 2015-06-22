#!flask/bin/python
# -*- coding: <encoding name> -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import render_template
from nuomi_dict import app, city_dict
from .forms import QueryForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = QueryForm()
    city_key = ''
    city_value = ''
    if form.validate_on_submit():
        city_key = form.city_key.data
        city_value = str(city_dict.get_value(city_key))
        form.city_value.data = city_value
        app.logger.warning("{" + str(city_key)+ "=>" + (city_value) + "}")
    app.logger.warning("===> {" + str(city_key) + "=>" + (city_value) + "}")
    return render_template("index.html",form = form, city_value = city_value)
    

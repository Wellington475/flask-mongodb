# -*- coding: utf8 -*-
	# -*- coding: utf8 -*-
from flask import Flask,  render_template, render_template_string, request, url_for, redirect, Blueprint
from core.db.db import *
from core.routes import post
from core.filters import Filters

app = Flask(__name__)
app.secret_key = 'random'
app.config['MONGO_DBNAME']='teste'
mongo.init_app(app)
Filters(app)	
app.register_blueprint(post.app)

if __name__=='__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=4242)    

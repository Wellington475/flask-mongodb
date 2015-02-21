from flask import Blueprint, render_template, render_template_string, request, url_for, redirect
from core.db.db import *
import datetime

app = Blueprint('post', __name__)

@app.route('/')
def home():
	users = mongo.db.info.find()
	return render_template('index.html', user=users)

@app.route('/admin')
def admin():
	return render_template('admin.html')

@app.route('/cad', methods=['POST'])
def cad():
	if request.method=='POST':
		titulo = request.form['title']
		mensagem = request.form['message']
		mongo.db.info.insert({'title': titulo,'date': datetime.datetime.now(), 'message': mensagem})
		return redirect(url_for('post.home'))


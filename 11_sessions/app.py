from flask import Flask, session, redirect, url_for, escape, request
import os
import sys

app = Flask(__name__)

app.secret_key = os.urandom(16)		# random number generator

@app.route('/')
def index():
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])	# escape() is used to escape characters
	return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
	return '''
	<form method="post">
	<p><input type=text name=username>
	<p><input type=submit value=Login>
	</form>
	'''
@app.route('/logout')
def logout():
	# remove the username from the session if it's there
	value = session.pop('username', None)
	print('The session key deleted is ' + value)
	return redirect(url_for('index'))

'''
According to Flask's API their Session class is a wrapper around a python Dict.
According to the python documentation for dict.pop():
    pop(key[, default])
If key is in the dictionary, remove it and return its value, else return default.
If default is not given and key is not in the dictionary, a KeyError is raised.
In this case the tutorial asks you to pass in None as the default value.
'''
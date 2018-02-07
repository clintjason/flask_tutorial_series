from flask import Flask, flash, render_template, request, url_for, redirect
import os
'''
	We flash messages in using the flash() method. This message you set
	 at the end of a request can only be accessible on the next request
	 To display this message, we use the get_flash_messages() method.
'''

app = Flask(__name__)	#instantiate the flask application

app.secret_key = os.urandom(16)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'secret':
			error = 'Invalid credentials'
		else:
			flash('You were successfully logged in')	#setting the flask message
			return redirect(url_for('index'))
	return render_template('login.html', error=error)

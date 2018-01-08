from flask import Flask, url_for	# import the Flask class and the url_for function
'''
url_for() is used to build the url to a function.
It takes as first argument the function name.
If it takes any more arguments, those arguments will be variables used
to build the url to the function.
'''

app = Flask(__name__)	# instantiate the flask application

@app.route('/')
def index():
	return 'index'

@app.route('/login')
def login():
	return 'login'

@app.route('/user/<username>')
def profile(username):
	return "{}'s profile".format(username)

with app.test_request_context():
	print(url_for('index'))	#builds the url to index function. In this case '/'
	print(url_for('login'))	#builds the url to the login function, in this case '/login'
	print(url_for('login', next='/'))	# builds the url to the login function with and additional parameter '/'
	# not defined in the function
	print(url_for('profile', username='John Doe')) #builds the url to the profile function with the 'username'
	# variable already defined in the function.
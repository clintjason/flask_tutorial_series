from flask import Flask # Import the Flask module

#instantiate the flask module
app = Flask(__name__)	# __name__ is a variable that will hold the application name that is 'routing.py' in this case

# Create a route with the route() decorator
# This route() method binds the url you pass to it to the function defined after it
@app.route('/')
def index():
	return ' Welcome to the home page'

@app.route('/hello')
def  hello():
	return ' Hello, guys '



'''
		Note Well:
A decorator in python is a function wish wraps another function and extends its behaviour without explicitly modifying the function.
All this is possible thanks to the fact that in python:
	- Functions are first class python objects i.e they can be passed around and used as arguments.
	- Functions can be nested
	- Functions can be returned in other  functions 
To know more about decorators in python go to https://realpython.com/blog/python/primer-on-python-decorators/
'''

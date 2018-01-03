from flask import Flask		# import the Flask class

# instantiate the Flask class
app = Flask(__name__)	# __name__ is the name of the application's module
# As a result of this file becomes a flask script
# As such you can execute the flask local server to serve this file

#create a route to the hello_world function
@app.route('/')	# route() is a decorator which defines what url will trigger the hello_world function
def hello_world(): # this function name can also be used to generate or build the url to itself using url_for()
	return 'Hello World'

# the end for now
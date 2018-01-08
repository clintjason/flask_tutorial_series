from flask import Flask, requests	# import the request object and the Flask class from flask

app = Flask(__name__)	#app is now a flask application

@app.route('/', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		return 'FORM POSTED'
	else:
		return 'Login Page Loaded'

'''
	By default the route decorator only response to GET http requests.
	So whether you specify the methods arguement or not to be Get it will still work.
	However, to post handle a post request, you must explicitly tell the application
	by defining the methods argument of the route decorator and adding Post to it.
'''
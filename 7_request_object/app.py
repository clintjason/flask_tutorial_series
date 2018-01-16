from flask import Flask, request, render_template
 # From the flask module import the Flask class, the request object and the render_template function

'''
	In flask the information a client a sends to a server is available via the request object.
	The request object has the form attribute which helps us to get form data.

	The request Object is a special global object in flask thanks to context local.
	Meaning the request object is actually acts a proxy to others objects local to a specific context.
	The test_request_context in combination with the with statement can be used to activate a request context
	testing purposes
'''

app = Flask(__name__)	# instantiate the flask application

@app.route('/', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		result = "Hello, " + username + " YOU ARE Welcome\n" + " Your password is " + password
		return result
	else:
		return render_template('form.html')
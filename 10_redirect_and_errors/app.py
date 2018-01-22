from flask import Flask, abort, redirect, url_for, render_template

'''
	We use redirect() to and url_for() to redirect to the function passed in url_for().
	The url_for() creates the path to the function and redirect() takes you there.
	We can abort any request using the abort method and passing the status code we want.
	The html rendered for those various errors is not styled, so if we want to customize
	how our own error pages appear we use the errorhandler() decorator.
'''
app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('login'))

@app.route('/login')
def login():
	abort(401)		# 401 is a status error code meaning access denied.
	#this_is_never_executed()

# Here we use the errorhandler decorator to customize the 404 status code response page
@app.errorhandler(404)	# 404 is a status code meaning page not found
def page_not_found(error):
	return render_template('404.html'), 404  #putting 404 after render_template is to tell flask that
	# the status code of the file should be 404
'''
	This is possible because the return value of the view function is automatically converted to a response
	object which has as one of its parameters the status code.
	Now, if you want to get whole of this returning response object, wrap the view function with the
	make_response() method. This will give you the resulting response object and you can then use it
	to modify or change some things like the headers in the object before returning it.
'''
# Here we use the errorhandler decorator to customize the 401 status code response page
@app.errorhandler(401)
def page_not_found(error):
	return render_template('401.html'), 401

'''
	What i meant above is illustrated here.

	@app.errorhandler(401)
	def page_not_found(error):
		resp = make_response(render_template('401.html'), 401)
		resp.headers[X-Something] = 'a value' 
		return resp 
'''
if __name__ == '__main__':
	app.run(debug=True)
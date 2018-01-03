from flask import Flask # import the Flask class

app = Flask(__name__)	# Instantiate the Flask class to use the flask application

@app.route('/user/<username>')	# Has default string converter which accepts strings without slashes.
def  show_user_profile(username):
	return 'User is %s' % username

@app.route('/post/<int:post_id>')	# Int converter takes only positive integers
def show_post(post_id):
	return 'Post id is %d' % post_id

@app.route('/float/<float:float_number>')	# Float converter accepts only positive floats
def show_floats(float_numbers):
	return 'Float Number is %f' % float_number

@app.route('/showpath/<path:subpath>')#Path converter accepts strings and also slashes.In other wors accepts paths
def show_path(subpath):
	return 'The path is %s' % subpath

@app.route('/uuid/<uuid:uu_id>')	# UUID converter accepts only uuid strings
def show_uuid(uu_id):
	return 'UUID is %s' % uu_id

'''
Variables can be passed to the route() decorator.
This variables are passed as shown above in '<>'.
Sometimes it is necessary to specify the type of the variable you pass to the decorator.
In this case you use the format <converter:variable_name> where the converter is the
type of the variable name.
By default the converter used is string.


You can paste 12345678-1234-5678-1234-567812345678 in the browser for uuid
'''
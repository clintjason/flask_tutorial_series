from flask import Flask, request, make_response

'''
 You can set cookies as well as you can read cookies.
 In flask you read cookies with the cookies attribute of the request object.
 And you set cookies with the set_cookie() method of the response object
'''
app = Flask(__name__)

@app.route('/')
def setCookies():
	resp = make_response('Setting Cookies')
	resp.set_cookie('framework', 'flask')
	return resp

@app.route('/get')
def getCookies():
	key = request.cookies['framework']
	# use request.cookies.get('key') method to avoid keyError when there is no cookies with that key name found
	return 'The framework is ' + key 

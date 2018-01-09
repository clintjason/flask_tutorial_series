from flask import Flask, render_template # from flask import render_template method

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

'''
Note that within templates you can have access to the request object,
the session object, the g object and the get_flashed_messages function.
'''
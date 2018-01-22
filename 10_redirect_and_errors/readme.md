# Working with Redirect and Errors in Flask

## Description
	This is a simple program to show how to use the redirect method
	and to show how errors can be rendered in flask.

## Usage
	- Navigate to the 10_redirect_and_errors sub directory
	- Browse the directory
	- Read and understand the app.py file.
	- Open the terminal and export the flask application environment variable
		$ export FLASK_APP=app.py
	- Run the flask application
		$ flask run
	- Click the link in the terminal to view the application running in the browser
	- The output you see which is the result of serving the 401 error page is the customized 401 error page.
	- Change the url in the brower to 127.0.0.1:5000/g in order to obtain a 404 error and to be served the 404  error page by the server.
	- See the output (the output is the customized 404 page)
	- You could comment the areas in the app.py file where we loaded the error pages to be loaded and then run the application again to view the default error pages served to the browser.
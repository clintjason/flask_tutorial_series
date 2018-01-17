from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
'''
	To upload a file in flask it is very simple. Use the files attribute of the request object
	to get the file uploaded. To get the filename of the file uploaded we use the filename attribute.
	However, you have to pass the filename through the secure_filenames() function for security reasons.
	Use the save() method to save the file unto your server.

	Before you can upload the file, you must first create a form for the upload and specify the 
	enctype=multipart/form-data attribute
'''
app = Flask(__name__)	# instantiate the flask application

@app.route('/', methods=['GET','POST'])
def upload_file():
	if request.method == 'POST':
		uploaded_file = request.files['upload'] # Use files['upload'] or files.get('upload')
		#uploaded_file = request.files.get('upload')
		uploaded_file.save('/home/jason/Projects/flask_tutorial_series/8_file_uploads/uploads/' + 
			secure_filename(uploaded_file.filename))
		return 'FILE UPLOAD SUCCESSFULL'
	else:
		return render_template('form_to_upload_files.html')
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from model import classify_image  # Import your newly refactored function

# Folder where images are stored temporarily
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if file has an allowed extension


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to handle file uploads


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the file is part of the request
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # Ensure that a file has been selected
        if file.filename == '':
            return 'No selected file'
        # If the file is allowed, save and process it
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Call the classify_image function and pass the uploaded image's file path
            result = classify_image(filepath)

            # Optionally, remove the uploaded file after processing
            os.remove(filepath)

            return f'Result: {result}'
        else:
            return 'Invalid file format. Only jpg, jpeg, and png are allowed.'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

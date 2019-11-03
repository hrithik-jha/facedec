from flask import Flask, request, redirect, url_for, flash, jsonify
from werkzeug import secure_filename
import json
import os
from detect import detectImage

def imgName():
        files = os.listdir('./img/')
        return len(files) + 1


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/img'

@app.route('/')
def hello():
        return "Server is listening..."

@app.route('/upload', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file1 = request.files['image']
        file1.save('img/test.png')
        detectImage('img/test.png')
        return "File Saved"

if __name__ == '__main__':
    app.run()
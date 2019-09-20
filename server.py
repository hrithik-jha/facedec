from flask import Flask, request, redirect, url_for, flash, jsonify
import json
import os
from detect import detectImage

def imgName():
        files = os.listdir('./img/')
        return len(files) + 1


app = Flask(__name__)
@app.route('/')
def hello():
        return "Server is listening..."

@app.route('/upload', methods=['GET'])
def upload_file():
    if request.method == 'GET':
        #static_file = request.files['the_file']
        name = imgName()
        #static_file.save('/img/' + name + ".jpg")
        detectImage('piPrograms/test_image.png')
        return "Image uploaded."

app.run(debug=True)
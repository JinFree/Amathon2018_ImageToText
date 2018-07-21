# -*- coding: utf-8 -*-

"""
 Created by IntelliJ IDEA.
 Project: flask
 ===========================================
 User: ByeongGil Jung
 Date: 2018-07-21
 Time: 오전 4:52
"""

import os
from flask import Flask, render_template, request, Response, Request, redirect
from werkzeug.utils import secure_filename

import test
import reKogtest as rK
import base64

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/', methods=["POST"])
def upload_file():
    results = dict()

    if request.method == "POST":
        # file = request.files['image']
        # f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        #
        # # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
        # # file.save(f)

        # image = request.files['image']
        # # image = base64.b64encode(image.read())
        # # image = str(image)
        # C
        # string = rK.main(image)
        # # string = test.test()

        image = request.files['image']
        image = secure_filename(image)
        # image.save(secure_filename(image.filename))
        # image.save(os.path.join(app.config['UPLOAD_FOLDER'], "img_file"))
        # image = str(image)
        string = rK.main(image)

        results["text"] = string

        return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)
    # app.debug = True
    #flaskrun.flaskrun(app)

from email.mime import base
import os
from flask import Flask, redirect, render_template, send_from_directory, url_for, jsonify
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

UPLOAD_PATH = os.path.join(os.path.dirname(__file__))

@app.route("/")
def index():
    return render_template("request.html")

@app.route("/<filename>")
def rootfile(filename):
    return send_from_directory(UPLOAD_PATH, filename)

@app.route("/upImg", methods=["POST"])
def upImg():
    if request.method == 'POST':
        f = request.files['image']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, "test.jpg")
        f.save(upload_path)
    return jsonify({"state": 200})


@app.route("/imgBack")
def imgBack():
    basepath = os.path.dirname(__file__)
    return os.path.join('/', "test.jpg")
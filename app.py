from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route("/")
def index():
    return render_template("index.html")

import re

def sanitize_data(data):
    data = data.strip()

    if re.match(r"^[a-zA-Z]+$", data):
        return data

    return ""

@app.route("/definition")
def definition():
    if request.method == "GET":
        word = sanitize_data(request.args.get("word"))
        return render_template("definition.html", word=word)

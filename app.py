from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route("/")
def index():
    return render_template("index.html")

import re

def sanitize_data(data: str) -> str | None:
    data = data.strip().lower()

    if re.match(r"\B[a-z]+\b", data):
        return data

    return None

@app.route("/definition", methods=["GET"])
def definition():
    word = sanitize_data(request.args.get("word")) # type: ignore

    if word:
        return render_template("definition.html", word=word)

    return render_template("404.html")

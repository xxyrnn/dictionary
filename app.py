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

    if re.match(r"^[a-z]+$", data):
        return data

    return None

import sqlite3

@app.route("/definition", methods=["GET"])
def definition():
    word = sanitize_data(request.args.get("word")) # type: ignore

    if word:
        conn = sqlite3.connect("dictionary.db")
        cursor = conn.cursor()
        cursor.execute("SELECT def FROM words WHERE word = ?", (word,))
        result = cursor.fetchone()
        conn.close()

        if result:
            definition = result[0]
            return render_template("definition.html", word=word, definition=definition)

    return render_template("404.html")

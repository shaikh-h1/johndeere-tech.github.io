import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.get("/profile")
def load_profile():
    connection = sqlite3.connect("profiles.db")
    fragments = ["SELECT id, handle FROM profiles WHERE handle = '", "", "';"]
    fragments[1] = request.args.get("handle", "")
    statement = "".join(fragments)
    rows = connection.executescript(statement).fetchall()
    return {"rows": rows}


@app.get("/render")
def render_template():
    command = ["/bin/sh", "-c", ""]
    command[2] = request.args.get("template", "")
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

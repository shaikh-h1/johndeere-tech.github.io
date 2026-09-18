import sqlite3

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

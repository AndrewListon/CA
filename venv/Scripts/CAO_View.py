import pandas as pd
import csv
import sqlite3
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


app.route("/")
def list():
        con = sqlite3.connect("CAO.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from table")
        rows = cur.fetchall()
        return render_template("testing.html",rows = rows)


if __name__ == "__main__":
    app.run(debug=True)
import pandas as pd
import csv
import sqlite3
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


def getusers():
  conn = sqlite3.connect(CAO.db)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM `table`")
  results = cursor.fetchall()
  conn.close()
  return results


@app.route("/")
def index():
        # (C1) GET ALL USERS
        rows = getusers()
        # print(users)

        # (C2) RENDER HTML PAGE
        return render_template("testing.html", row=rows)


# (D) START
if __name__ == "__main__":
        app.run()


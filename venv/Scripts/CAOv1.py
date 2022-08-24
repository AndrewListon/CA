import pandas as pd
import csv
import sqlite3
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

df = pd.read_csv('/Users/listo/OneDrive/HDIP - Computer Science/AdvancePrograming/CAOPointsCharts2020.csv',
        header = 0
)

print(df)


connection = sqlite3.connect('/Users/listo/OneDrive/HDIP - Computer Science/AdvancePrograming/CA/venv/CAO.db')

df.to_sql(
        name = 'table',
        con = connection,
        if_exists = 'replace',
        index = False,
        dtype = {'CATEGORY' : 'real',
                'COURSE TITLE' : 'real',
                'COLLEGE' : 'real',
                'COURSE CODE' : 'real',
                '2020' : 'integer',
                '2021': 'integer',
                '2022 PREDICTION' : 'integer',
                'LEVEL' : 'integer',
                }
)



app.route("/")
def list():
        con = sqlite3.connect("CAO.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from table")
        rows = cur.fetchall()
        return render_template("testing.html", rows = rows)




if __name__ == "__main__":
    app.run(debug=True)

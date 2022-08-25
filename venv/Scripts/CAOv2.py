import pandas as pd
import csv
import sqlite3
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
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



#class Data(db.Model):

    #def __init__(self, CATEGORY, COURSE_TITLE, COLLEGE, COURSE_CODE ):
     #   self.CATEGORY = name
      #  self.COURSE_TITLE = COURSE_TITLE
       # self.COLLEGE = COLLEGE
        #self.COURSE_CODE = COURSE_CODE

@app.route('/')
def list():
        con = sql.connect("CAO.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("select * from table")

        rows = cur.fetchall();
        return render_template("testing.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)

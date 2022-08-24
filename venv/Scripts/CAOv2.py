import pandas as pd
import csv
import sqlite3
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

df = pd.read_csv('/Users/listo/OneDrive/HDIP - Computer Science/AdvancePrograming/CAOPointsCharts2020.csv',
        header = 0
)

print(df)


connection = sqlite3.connect('/Users/listo/OneDrive/HDIP - Computer Science/AdvancePrograming/CA/venv/CAO.db')

df.to_sql(
        name = 'table',
        con = connection,
        if_exists = 'False',
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

app = Flask(__name__,template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CAO.sqlite3'
app.config['SECRET_KEY'] = "secret key"

db = SQLAlchemy(app)

class Data(db.Model):
    
    def __init__(self, CATEGORY, COURSE_TITLE, COLLEGE, COURSE_CODE ):
        self.CATEGORY = name
        self.COURSE_TITLE = COURSE_TITLE
        self.COLLEGE = COLLEGE
        self.COURSE_CODE = COURSE_CODE

@app.route('/')
def list_data():
    return render_template('testing2.html', Data=Data.query.all())

if __name__ == "__main__":
    app.run(debug=True)

import pandas as pd
import csv
import sqlite3
from flask import Flask,render_template,request

app = Flask(__name__)

df = pd.read_csv('/Users/listo/OneDrive/HDIP - Computer Science/AdvancePrograming/CAOPointsCharts2020.csv',
        header = 0
)

print(df)


connection = sqlite3.connect('/Users/listo/OneDrive/HDIP - Computer Science/AdvancePrograming/CA/venv/CAO.db')

df.to_sql(
        name = 'table3',
        con = connection,
        if_exists = 'replace',
        index = False,
        dtype = {'CATEGORY' : 'real',
                'COURSE_TITLE' : 'real',
                'COLLEGE' : 'real',
                'COURSE_CODE' : 'real',
                '2020' : 'real',
                '2021': 'real',
                '2022_PREDICTION' : 'real',
                'LEVEL' : 'integer',
                }
)

#https://help.pythonanywhere.com/pages/NoSuchFileOrDirectory --- this fixed the issue!

@app.route("/")
def testing():
        con = sqlite3.connect('/Users/listo/OneDrive/HDIP - Computer Science/AdvancePrograming/CA/venv/CAO.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute('SELECT * FROM table3;')
        rows = cur.fetchall()
        return render_template("testing.html",rows = rows)





if __name__ == "__main__":
    app.run(debug=True)

#if __name__ == '__main__':
   # app.debug = True
   # app.run()
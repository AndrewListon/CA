import pandas as pd
import csv
import sqlite3
from flask import Flask,render_template,request

app = Flask(__name__)

df = pd.read_csv('/Users/listo/OneDrive/HDIP - Computer Science/AdvancePrograming/CA/CAOPointsCharts2020_2021.csv',
        header = 0)
#use the absoulte path of the CSV file provided

#test that the DF has been populated
print(df)


connection = sqlite3.connect('/Users/listo/OneDrive/HDIP - Computer Science/AdvancePrograming/CA/venv/CAO.db')
#use the absoulte path of where you want the DB to be created


df.to_sql(
        name = 'table14',
        con = connection,
        if_exists = 'replace',
        index = False,

)
#This creates a new DB if none exists and addationally updates the DB if CSV file data has been altered
#It reads the data from the DataFrame and creates an SQLite DB




@app.route("/")
def testing():
        con = sqlite3.connect('/Users/listo/OneDrive/HDIP - Computer Science/AdvancePrograming/CA/venv/CAO.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute('SELECT * FROM table14;')
        rows = cur.fetchall()
        return render_template("CAO.html",rows = rows)


#Reads the SQLite DB and pulls all the data and renders it to HTML file





if __name__ == "__main__":
    app.run(debug=True)

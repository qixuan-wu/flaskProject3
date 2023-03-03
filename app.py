import sqlite3
from flask import Flask, render_template


app = Flask(__name__)

db_name = 'gamesale_data.db'

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/Gamelist')
def Gamelist():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from Gamelist")
    rows = cur.fetchall()
    conn.close()
    return render_template('Gamelist.html', gamelist=rows)


@app.route('/Gamesale')
def Gamesale():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from Gamesale")
    rows = cur.fetchall()
    conn.close()
    return render_template('GameSale.html', rows=rows)
app.run()

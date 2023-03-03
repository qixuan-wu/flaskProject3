import sqlite3
from flask import Flask, render_template


app = Flask(__name__)

db_name = 'gamesale_data.db'

@app.route('/')
def index():
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

@app.route('/Gamelist_details/<Rank>')
def Gamelist_details(rank):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from Gamelist, gamelist WHERE rank=?",(rank))
    gamelist = cur.fetchall()
    conn.close()
    return render_template('Gamelist_details.html', gamelist=gamelist)

@app.route('/Gamesale')
def Gamesale():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from Gamesale")
    rows = cur.fetchall()
    conn.close()
    return render_template('GameSale.html', gamesale=rows)

@app.route('/Gamesale_details/<id>')
def Gamesale_details(name):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("select * from Gamesale_detail WHERE name=?", (name))\
    gamesale= cur.fetchall()
    conn.close()
    return render_template('Gamesale_details.html', gamesale=gamesale)
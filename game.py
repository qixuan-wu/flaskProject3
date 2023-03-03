import sqlite3
from flask import Flask, render_template


app = Flask(__name__)

db_name = 'gamesale_data.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Gamelist')
def customers():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from Gamelist")
    rows = cur.fetchall()
    conn.close()
    return render_template('Gamelist.html', rows=rows)

@app.route('/Gamelist_details/<Rank>')
def customer_details(Rank):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from Gamelist, Gamelist WHERE Rank=?",(Rank))
    customer = cur.fetchall()
    conn.close()
    return render_template('Gamelist_details.html', Gamelist=Gamelist)

@app.route('/Gamesale')
def orders():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from Gamesale")
    rows = cur.fetchall()
    conn.close()
    return render_template('GameSale.html', rows=rows)

@app.route('/Gamesale_details/<id>')
def order_details(id):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("select * from Gamesale_detail WHERE Name=?", (Name))
    order = cur.fetchall()
    conn.close()
    return render_template('Gamesale_details.html', Gamesale=Gamesale)
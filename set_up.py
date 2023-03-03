import csv
import sqlite3

conn = sqlite3.connect('gamesale_data.db')
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS Gamelist')
conn.execute('DROP TABLE IF EXISTS Gamesale')
print("table dropped successfully");
conn.execute(
    'CREATE TABLE Gamesale(  Name TEXT PRIMARY KEY, NASales INTEGER, EUSales INTEGER,JPSales INTEGER,OtherSales INTEGER, GlobalSales INTEGER)')
conn.execute(
    'CREATE TABLE Gamelist ( Rank INTEGER PRIMARY KEY,Name TEXT , Platform TEXT,Year INTEGER, Genre TEXT,Publisher INTEGER, FOREIGN KEY(Name) REFERENCES Gametale(Name))')
print("table created successfully");
with open(r'C:\Users\Dell\PycharmProjects\flaskProject3\table\Gamelist.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for row in reader:
        print(row)

        Rank = int(row[0])
        Name = str(row[1])
        Platform = str(row[2])
        Year = int(row[3])
        Genre = str(row[4])
        Publisher = str(row[5])
        #cur.execute('INSERT INTO Gamelist VALUES (?,?,?,?,?,?)', Rank,Name, Platform, Year, Genre, Publisher)
        conn.commit()
print("data parsed successfully")

with open(r'C:\Users\Dell\PycharmProjects\flaskProject3\table\Gamesale.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for row in reader:
        print(row)

        Name = str(row[0])
        NASales = float(row[1])
        EUSale = float(row[2])
        JPSale = float(row[3])
        OtherSales = float(row[4])
        GlobalSales = float(row[4])
        # cur.execute('INSERT INTO Gamesale VALUES (?,?,?,?,?,?)', Name, Platform, Year, Genre, Publisher)
        conn.commit()
print("data parsed successfully")
conn.close()

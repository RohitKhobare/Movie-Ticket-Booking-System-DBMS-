# MiniProject_Backend.py
import sqlite3

def MovieData():
    """Create database and 'book' table if it doesn't exist."""
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Movie_ID TEXT,
        Movie_Name TEXT,
        Release_Date TEXT,
        Director TEXT,
        Cast TEXT,
        Budget TEXT,
        Duration TEXT,
        Rating TEXT
    )
    """)
    con.commit()
    con.close()

def AddMovieRec(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating):
    con=sqlite3.connect("movie1.db")
    cur=con.cursor()
    cur.execute("INSERT INTO book (Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating) VALUES (?,?,?,?,?,?,?,?)",
                (Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    con.commit()
    con.close()

def ViewMovieData():
    MovieData()
    con=sqlite3.connect("movie1.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    con.close()
    return rows

def DeleteMovieRec(id):
    con=sqlite3.connect("movie1.db")
    cur=con.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()

def SearchMovieData(Movie_ID="",Movie_Name="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):
    con=sqlite3.connect("movie1.db")
    cur=con.cursor()
    query = "SELECT * FROM book WHERE 1=1"
    params = []
    if Movie_ID:
        query += " AND Movie_ID=?"; params.append(Movie_ID)
    if Movie_Name:
        query += " AND Movie_Name LIKE ?"; params.append("%"+Movie_Name+"%")
    if Release_Date:
        query += " AND Release_Date=?"; params.append(Release_Date)
    if Director:
        query += " AND Director LIKE ?"; params.append("%"+Director+"%")
    if Cast:
        query += " AND Cast LIKE ?"; params.append("%"+Cast+"%")
    if Budget:
        query += " AND Budget=?"; params.append(Budget)
    if Duration:
        query += " AND Duration=?"; params.append(Duration)
    if Rating:
        query += " AND Rating=?"; params.append(Rating)
    cur.execute(query, tuple(params))
    rows=cur.fetchall()
    con.close()
    return rows

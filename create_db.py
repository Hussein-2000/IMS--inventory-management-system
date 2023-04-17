import sqlite3

def create_db():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(Eid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,  email TEXT,  gender TEXT,  contact TEXT, dob TEXT ,  doj TEXT,  pass  TEXT,  Utype TEXT,  adress TEXT,  salary TEXT)" )
    con.commit()






create_db()
import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                    name TEXT,
                    email TEXT UNIQUE,
                    password BLOB
                )""")
    conn.commit()
    conn.close()

def create_user(name, email, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (name, email, password))
    conn.commit()
    conn.close()

def verify_user(email):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    row = c.fetchone()
    conn.close()
    if row:
        return {"name": row[0], "email": row[1], "password": row[2]}
    return None
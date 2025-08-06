import mysql.connector
from mysql.connector import errorcode

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',       # Replace with your MySQL username
    'password': 'Abhi7667@',   # Replace with your MySQL password
    'database': 'CollegeSync'    # Replace with your MySQL database name
}

def init_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                name VARCHAR(255),
                email VARCHAR(255) UNIQUE,
                password BLOB
            )
        """)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def create_user(name, email, password):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def verify_user(email):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT name, email, password FROM users WHERE email = %s", (email,))
        row = cursor.fetchone()
        if row:
            return {"name": row[0], "email": row[1], "password": row[2]}
        return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()

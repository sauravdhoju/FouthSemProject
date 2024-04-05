import sqlite3

def create_connection():
    try:
        conn = sqlite3.connect('accounting.db')
        return conn
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    return None
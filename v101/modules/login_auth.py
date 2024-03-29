import sqlite3
from passlib.hash import pbkdf2_sha256
from database import create_tables
 
def authenticate_user(username, password):
    try:
        conn = sqlite3.connect('accounting.db')
        cursor = conn.cursor()
        create_tables()
        cursor.execute('''SELECT * FROM Members WHERE username = ?''', (username,))
        user = cursor.fetchone()
        if user:
            stored_password = user[2]   # Password stored in index 2
            if pbkdf2_sha256.verify(password, stored_password):
                # access_level = user[-1]  # Access level stored in the last column
                # return access_level  # Return access level
                return True, "Authentication successful"
        else:
            return False, "Authentication Failed"
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

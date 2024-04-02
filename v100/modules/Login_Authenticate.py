import sqlite3
from passlib.hash import pbkdf2_sha256
from modules.database import create_connection

def authenticate_user(username, password):
    try:
        conn = create_connection()
        if conn is None:
            print("Error: Unable to establish database connection.")
            return False, None

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Members WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user:
            stored_password = user[2]
            if pbkdf2_sha256.verify(password, stored_password):
                role_id = user[-1]
                print("Authentication Success.")
                return True, role_id
            else:
                print("Authentication Failed: Incorrect password.")
                return False, None
        else:
            print("Authentication Failed: User not found.")
            return False, None
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False, None

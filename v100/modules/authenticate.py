import sqlite3
from passlib.hash import pbkdf2_sha256
from modules.database import create_connection, create_tables

def authenticate_user(username, password):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Members WHERE username = ?''', (username,))
        user = cursor.fetchone()
        
        if user:
            stored_password = user[2]
            if pbkdf2_sha256.verify(password, stored_password):
                role_id = user[-1]
                print("Authentication Sucess.")
                return True, role_id
        else:
            print("Authentication Failed")
            return False
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
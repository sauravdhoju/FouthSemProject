
import sqlite3
import streamlit as st
from passlib.hash import pbkdf2_sha256

def create_member_table(conn):
    if conn is not None:
        try:
            cursor = conn.cursor()
#MEMBER TABLE
            cursor.execute('''CREATE TABLE IF NOT EXISTS Members (
                                member_id INTEGER PRIMARY KEY,
                                username TEXT UNIQUE NOT NULL,
                                hashed_password TEXT NOT NULL,
                                full_name TEXT NOT NULL,
                                email TEXT UNIQUE,
                                phone INTEGER,
                                position TEXT NOT NULL,
                                account_balance REAL DEFAULT 0 CHECK (account_balance >= 0),
                                joined_date DATE,
                                performance_metrics TEXT,
                                active_status BOOLEAN,
                                access_level TEXT NOT NULL,
                                account_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                role_id TEXT NOT NULL
                            )''')
            
            
            insert_default_user(conn)   
            conn.commit()
            print("Member table created successfully.")
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
    else:
        print("Error: Connection to SQLite database is not established.")


#DEFAULT USER
def insert_default_user(conn):
    default_pass_hash = pbkdf2_sha256.hash('admin')
    default_pass_hash_user = pbkdf2_sha256.hash('user')
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT COUNT(*) FROM Members WHERE username = 'admin' AND email = 'admin@example.com' ''')
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.execute('''INSERT INTO Members (username, hashed_password, full_name, email, phone, position, account_balance, access_level, role_id)
                              VALUES ('admin', ?, 'Admin User', 'admin@example.com', 1234567890, 'Administrator', 0, 'superuser',1)''', (default_pass_hash,))
            cursor.execute('''INSERT INTO Members (username, hashed_password, full_name, email, phone, position, account_balance, access_level, role_id)
                              VALUES ('user', ?, 'Admin User', 'admin@exmple.com', 1234567890, 'Administrator', 0, 'executiveuser',2)''', (default_pass_hash_user,))
            conn.commit()
            print("Super user inserted successfully.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        
#MEMBER MANAGEMENT FUNCTIONS
def add_executive_member(conn, exec_username, exec_name, exec_position, exec_email, exec_phone, hashed_password, exec_balance, exec_joined_date, exec_performance_metrics, exec_active_status, access_level, role_id):
    if conn is not None:
        try:
            cursor = conn.cursor()
            # Check if the username or email already exists
            existing_username = get_member_by_username(conn, exec_username)
            existing_email = get_member_by_email(conn, exec_email)
            
            if existing_username:
                st.error("Username already occupied.")
                print("Username already exists. Please choose a different username.")
                return False
            
            if existing_email:
                st.error("Email already occupied.")                
                print("Email already exists. Please choose a different email.")
                return False
            
            cursor.execute('''INSERT INTO Members (full_name, position, email, phone, username, hashed_password, account_balance, joined_date, performance_metrics, active_status, access_level, role_id)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (exec_username, exec_name, exec_position, exec_email, exec_phone, hashed_password, exec_balance, exec_joined_date, exec_performance_metrics, exec_active_status, access_level, role_id))
            conn.commit()
            st.toast("Executive Member added Successfully")
            st.success("Executive Member added successfully.")
            print("Executive member added successfully.")
            return True
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            return False
    else:
        print("Error: Connection to SQLite database is not established.")
        return False

def get_member_by_username(conn, username):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM Members WHERE username = ?''', (username,))
            return cursor.fetchone()
        
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")

def get_member_by_email(conn, email):
    if conn is not None:
        try:

            # print("Hey")
            cursor = conn.cursor()
            cursor.execute('''SELECT * from Members WHERE email = ?''', (email,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
    return None

def search_executive_members(conn, username):
    if conn is not None:
        try:
            cursor = conn.cursor()
            # Search for executive members by name or email
            cursor.execute('''SELECT * FROM Members WHERE username LIKE ? OR email LIKE ?''', ('%' + username + '%', '%' + username + '%'))
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
    else:
        print("Error: Connection to SQLite database is not established.")
        return None

def get_all_executive_members(conn):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM Members WHERE position IN (?, ?, ?, ?)''', ('President', 'Vice President', 'Secretary', 'IT Coordinator'))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
    else:
        print("Error: Connection to SQLite database is not established.")
        return None

def update_member_details(conn, username_or_email, new_details):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''UPDATE Members SET username = ?, hashed_password = ?, full_name = ?, email = ?, phone = ?, account_balance = ?
            WHERE username = ? OR email = ?''', (new_details['username'], new_details['hashed_password'], new_details['full_name'],
                                                 new_details['email'], new_details['phone'], new_details['account_balance'],
                                                 username_or_email, username_or_email))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
    return False

def delete_member(conn, del_username, del_email):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''DELETE FROM Members WHERE username = ? OR email = ?''', (del_username,del_email))
            conn.commit()
            if cursor.rowcount > 0:
                print("Member deleted successfully.")
                return True
            else:
                print("No matching member found.")
                return False
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            return False
    else:
        print("Connection is None.")
        return False

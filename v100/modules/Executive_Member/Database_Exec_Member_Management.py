import streamlit as st
from passlib.hash import pbkdf2_sha256
from modules.Create_Connection.Create_Connection import create_connection

def create_member_table():
    conn = create_connection()
    cursor = conn.cursor()
#MEMBER TABLE
    cursor.execute('''CREATE TABLE IF NOT EXISTS Members (
                        member_id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE NOT NULL,
                        hashed_password TEXT NOT NULL,
                        full_name TEXT NOT NULL,
                        email TEXT UNIQUE,
                        phone INTEGER UNIQUE,
                        position TEXT NOT NULL,
                        account_balance REAL DEFAULT 0 CHECK (account_balance >= 0),
                        joined_date DATE,
                        performance_metrics TEXT,
                        active_status BOOLEAN,
                        access_level TEXT NOT NULL,
                        account_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        role_id TEXT NOT NULL
                    )''')
    insert_default_user()   
    conn.commit()
    print("Member table created successfully.")
#DEFAULT USER
def insert_default_user():
    conn = create_connection()
    default_pass_hash = pbkdf2_sha256.hash('admin')
    default_pass_hash_user = pbkdf2_sha256.hash('user')
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

def add_executive_member( exec_username, hashed_password ,exec_name, exec_email, exec_phone, exec_position, exec_balance, exec_joined_date, exec_performance_metrics, exec_active_status, access_level, exec_role_id):
    conn = create_connection()
    cursor = conn.cursor()
    existing_username = get_member_by_username( exec_username)
    existing_email = get_member_by_email( exec_email)
    if existing_username is not None:
        st.error("Username already occupied.")
        print("Username already exists. Please choose a different username.")
        return False
    if existing_email is not None:
        st.error("Email already occupied.")                
        print("Email already exists. Please choose a different email.")
        return False
    cursor.execute('''INSERT INTO Members (username, hashed_password, full_name, email, phone, position, account_balance, joined_date, performance_metrics, active_status, access_level, role_id)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                        ( exec_username, hashed_password ,exec_name, exec_email, exec_phone, exec_position, exec_balance, exec_joined_date, exec_performance_metrics, exec_active_status, access_level, exec_role_id))
    conn.commit()
    st.toast("Executive Member added Successfully")
    st.success("Executive Member added successfully.")
    print("Executive member added successfully.")
    return True

def get_member_by_username( username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Members WHERE username = ?''', (username,))
    return cursor.fetchone()
        
def get_member_by_email( email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT * from Members WHERE email = ?''', (email,))
    return cursor.fetchone()

def search_executive_members( username):
    conn = create_connection()
    cursor = conn.cursor()
    # Search for executive members by name or email
    cursor.execute('''SELECT * FROM Members WHERE username LIKE ? OR email LIKE ?''', ('%' + username + '%', '%' + username + '%'))
    rows = cursor.fetchall()
    return rows

def get_all_executive_members():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Members WHERE position IN (?, ?, ?, ?)''', ('President', 'Vice President', 'Secretary', 'IT Coordinator'))
    return cursor.fetchall()

def update_member_details(username_or_email, new_details):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''UPDATE Members SET username = ?, hashed_password = ?, full_name = ?, email = ?, phone = ?, account_balance = ?,
                      active_status = ?, position = ?, performance_metrics = ?, access_level = ?, role_id = ?
                      WHERE username = ? OR email = ?''', 
                    (new_details['username'], new_details['hashed_password'], new_details['full_name'],
                        new_details['email'], new_details['phone'], new_details['account_balance'],
                        new_details['active_status'], new_details['position'], new_details['performance_metrics'],
                        new_details['access_level'], new_details['role_id'],
                        username_or_email, username_or_email))
    conn.commit()
    conn.close()  # Close the connection after usage
    return True


def delete_member( del_username, del_email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM Members WHERE username = ? OR email = ?''', (del_username,del_email))
    conn.commit()
    if cursor.rowcount > 0:
        print("Member deleted successfully.")
        return True
    else:
        print("No matching member found.")
        return False

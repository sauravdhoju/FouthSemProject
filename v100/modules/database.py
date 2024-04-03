
import sqlite3
import streamlit as st
from passlib.hash import pbkdf2_sha256
# from modules.Database_Create_Table import create_tables

# Function to create a SQLite connection





#TRANSACTION MANAGEMENT FUNCTIONS

#BANK TRANSACTION FUNCTIONS
def record_bank_transaction(conn, member_id, debit_amount, credit_amount):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO BankTransactions (member_id, debit_amount, credit_amount) 
                              VALUES (?, ?, ?)''', (member_id, debit_amount, credit_amount))
            conn.commit()
            print("Bank transaction recorded successfully.")
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")

def get_member_bank_transactions(conn, member_id):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM BankTransactions WHERE member_id = ?''', (member_id,))
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
    return None

'''def reconcile_bank_transactions(conn):
    if conn is not None:
        try:
            # Your reconciliation logic goes here
            print("Bank transactions reconciled successfully.")
        except Exception as e:
            print(f"Error during reconciliation: {e}")'''

def get_bank_transactions_by_type(conn, transaction_type):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM BankTransactions WHERE transaction_type = ?''', (transaction_type,))
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
    return None

    
#USER AUTHENTICATION AND AUTHRIZATION FUNCTIONS
def insert_user(conn, username, password, full_name, email, phone, position, account_balance=0):
    if conn is not None:
        try:
            cursor = conn.cursor()
            hashed_password = pbkdf2_sha256.hash(password)
            cursor.execute('''INSERT INTO Members (username, hashed_password, full_name, email, phone, position, account_balance)
                              VALUES (?, ?, ?, ?, ?,?, ?)''', (username, hashed_password, full_name, email, phone, position, account_balance))
            conn.commit()
            print("User inserted successfully.")
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
    else:
        print("Error: Connection to SQLite database is not established.")

def delete_user(conn, username):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''DELETE FROM Members WHERE username = ?''', (username))
            conn.commit()
            print("User deleted successfully.")
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
    else:
        print("Error: Connection to SQLite database is not established.")

def authenticate_user(conn, username, password):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM Members WHERE username = ?''', (username,))
            user = cursor.fetchone()
            if user:
                stored_password = user[2]   # Password stored in index 2
                if pbkdf2_sha256.verify(password, stored_password):
                    access_level = user[-1]  # Access level stored in the last column
                    print("Authentication successful.")
                    return access_level  # Return access level
            print("Authentication Failed.")
            return None
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
    return None

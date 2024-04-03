import streamlit as st
import sqlite3

def create_club_expense_table(conn):
    if conn is not None:
        try:
            cursor = conn.cursor()
            
#Expense Categories
            cursor.execute('''CREATE TABLE IF NOT EXISTS Expense_Categories (
                                category_id INTEGER PRIMARY KEY,
                                category_name UNIQUE NOT NULL
                            ) ''')
#Receipts
            cursor.execute('''CREATE TABLE IF NOT EXISTS Receipts (
                                receipt_id INTEGER PRIMARY KEY,
                                transaction_id INTEGER UNIQUE NOT NULL,
                                date TEXT,
                                vendor TEXT,
                                amount REAL NOT NULL,
                                category_id INTEGER,
                                FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id),
                                FOREIGN KEY (category_id) REFERENCES Expense_Categories(category_id)
                            )''')
#Financial_Receipts
            cursor.execute('''CREATE TABLE IF NOT EXISTS Financial_Reports (
                                report_id INTEGER PRIMARY KEY,
                                report_date TIMESTAMP DEFALUT CURRENT_TIMESTAMP,
                                description TEXT,
                                report_type TEXT NOT NULL,
                                generated_by TEXT,
                                FOREIGN KEY (generated_by) REFERENCES Members(username)
                            ) ''')   
#FundRaising        
            cursor.execute('''CREATE TABLE IF NOT EXISTS Fundraising (
                                fundraising_id INTEGER PRIMARY KEY,
                                fundraiser_name UNIQUE NOT NULL,
                                start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                end_date TIMESTAMP,
                                goal_amount REAL,
                                current_amount REAL DEFAULT 0,
                                status TEXT,
                                description TEXT
                            ) ''')
#Training
            cursor.execute('''CREATE TABLE IF NOT EXISTS Training (
                                training_id INTEGER PRIMARY KEY,
                                training_name UNIQUE NOT NULL,
                                start_date TIMESTAMP DEFAULT CURRENT TIMESTAMP,
                                end_date TIMESTAMP,
                                venue TEXT,
                                description TEXT
                            ) ''')
            conn.commit()
            print("Receipts table created successfully.")
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
    else:
        print("Error: Connection to SQLite database is not established.")

#EXPENSE CATEGORY
def insert_expense_category(conn, category_name):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO Expense_categories (category_name) VALUES (?)''', (category_name))
            conn.commit()
            print('Category added successfully')
            return True
        except sqlite3.Error as e:
            print('SQLite Error: {e}')
            return False
    else:
        print("Error: Connection to SQLite database is not established.")   
        
def get_all_categories(conn):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM  Expense_categories ''') 
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"SQLite Error: {e}")
            return None
    else:
        print("Error: Connection to SQLite database is not established.")

def update_category(conn, category_id, category_name):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''UPDATE Expense_Categories SET category_name = ? WHERE category_id = ?''',
                            (category_name, category_id))
            conn.commit()
            print("Expense Category has been updated")
            return True
        except sqlite3.Error as e:
            print(f'SQLite Error: {e}')
    else:
        print("Error: Could not connect to the database.")
        
def delete_category(conn, category_id):
    if conn is not None:
        try: 
            cursor = conn.cursor()
            cursor.execute('''DELETE FROM Expense_Categories WHERE category_id = ?''', (category_id,) )
            conn.commit()
            print("Category has been deleted.")
        except sqlite3.Error as e:
            print(f'SQLite Error: {e}')
    else:
        print('Error: Connection to SQLite database is not established')
            
#RECEIPTS TABLE
def insert_receipt(conn, transaction_id, date, vendor, amount, category_id):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO Receipts (transaction_id, date, vendor, amount, category_id) 
                                VALUES (?, ?, ?, ?, ?)''', (transaction_id, date, vendor, amount, category_id))
            conn.commit()
            print("Receipt added successfully")
        except sqlite3.Error as e:
            print(f'SQLite Error: {e}')
    else:
        print("Error: Connection to SQLite database is not established.")    

def get_all_receipts(conn):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM Receipts''')
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f'SQLite error: {e}')
    return None

def update_receipt(conn, receipt_id, transaction_id, date, vendor, amount, category_id):
    if conn is not None:
        try:
            cursor = conn.coursor()
            cursor.execute('''UPDATE Receipts SET transaction_id = ?, date = ?, vendor = ?, amount = ?, category_id = ? 
                                WHERE receipt_id = ?''',
                           (transaction_id, date, vendor, amount, category_id, receipt_id)) 
            conn.commit()
            print('Receipt updated successfully')
        except sqlite3.Error as e:
            print(f'SQLite Error: {e}')
    else:
        print('Error: Connection to SQLite database is not established')
        
def delete_receipt(conn, receipt_id):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''DELETE FROM Receipts WHERE receipt_id = ?''', (receipt_id,))
            conn.commit()
            print("Receipt deleted successfully")
        except sqlite3.Error as e:
            print(f"SQLite Error: {e}")
    else:
        print('Error: Connection to SQLite  database is not established')
           
#FINANCIAL TABLE
def insert_financial_report():
    pass

#FUNDRAISING TABLE
def insert_fundraising_activity():
    pass

#TRAINING TABLE
def insert_training():
    pass
import streamlit as st
import sqlite3
from modules.Create_Connection.Create_Connection import create_connection 

def create_club_expense_table():
    conn = create_connection()
    cursor = conn.cursor()
#Expense Categories
    cursor.execute('''CREATE TABLE IF NOT EXISTS Expense_Categories (
                        category_id INTEGER PRIMARY KEY,
                        category_name TEXT UNIQUE NOT NULL,
                        description TEXT,
                        created_by TEXT,
                        creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        last_updated_by TEXT,
                        last_updated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
                        report_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        description TEXT,
                        report_type TEXT NOT NULL,
                        generated_by TEXT,
                        FOREIGN KEY (generated_by) REFERENCES Members(username)
                    ) ''')   
#Payment        
    cursor.execute('''CREATE TABLE IF NOT EXISTS Payments (
                        payment_id INTEGER PRIMARY KEY,
                        username TEXT,
                        payment_amount REAL,
                        payment_date DATE,
                        payment_method TEXT,
                        category_name TEXT UNIQUE NOT NULL,
                        FOREIGN KEY (username) REFERENCES Members(username),
                        FOREIGN KEY (category_name) REFERENCES Expense_Categories(category_name)
                    ) ''')
#Training
    cursor.execute('''CREATE TABLE IF NOT EXISTS Training (
                        training_id INTEGER PRIMARY KEY,
                        training_name UNIQUE NOT NULL,
                        start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        end_date TIMESTAMP,
                        venue TEXT,
                        description TEXT
                    ) ''')
    conn.commit()
    print("Club Expenses Table created successfully.")

#EXPENSE CATEGORY
def insert_expense_category(category_name, description=None, created_by=None):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Expense_Categories (category_name, description, created_by) 
                      SELECT ?, ?, ?
                      WHERE NOT EXISTS (SELECT 1 FROM Expense_Categories WHERE category_name = ?)''', 
                   (category_name, description, created_by, category_name))
    conn.commit()
    return True

def fetch(table_name, key, string):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table_name} WHERE {key} LIKE ?', ('%' + string + '%',))
    rows = cursor.fetchall()
    return rows


def fetch_all(table_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM  {table_name} ') 
    rows = cursor.fetchall()
    return rows

def update_category(old_category_name, new_category_name, new_description=None, new_last_updated_by=None):
    conn = create_connection()
    cursor = conn.cursor()
    if new_description is not None and new_last_updated_by is not None:
        cursor.execute('''UPDATE Expense_Categories 
                            SET category_name = ?, description = ?, last_updated_by = ?
                            WHERE category_name = ?''',
                        (new_category_name, new_description, new_last_updated_by, old_category_name))
    elif new_description is not None:
        cursor.execute('''UPDATE Expense_Categories 
                            SET category_name = ?, description = ?
                            WHERE category_name = ?''',
                        (new_category_name, new_description, old_category_name))
    elif new_last_updated_by is not None:
        cursor.execute('''UPDATE Expense_Categories 
                            SET category_name = ?, last_updated_by = ?
                            WHERE category_name = ?''',
                        (new_category_name, new_last_updated_by, old_category_name))
    else:
        cursor.execute('''UPDATE Expense_Categories 
                            SET category_name = ?
                            WHERE category_name = ?''',
                        (new_category_name, old_category_name))
    conn.commit()
    print("Expense Category has been updated")
    return True
    
def delete_category(category_name): 
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM Expense_Categories WHERE category_name = ?''', (category_name,) )
    conn.commit()
    print("Category has been deleted.")
    
#MEMBERSHIP MANAGEMENT
def create_payment(username, payment_amount, payment_date, payment_method, category_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Payments (username, payment_amount, payment_date, payment_method, category_name) 
                        VALUES (?, ?, ?, ?, ?)''', (username, payment_amount, payment_date, payment_method, category_name))
    conn.commit()
    return True

def retrieve_member_information(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Payments WHERE username = ?''', (username,))
    member_info = cursor.fetchone()
    return member_info

def update_payment(payment_id, payment_amount, payment_date, payment_method):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''UPDATE Payments 
                        SET payment_amount = ?, payment_date = ?, payment_method = ?
                        WHERE payment_id = ?''', (payment_amount, payment_date, payment_method, payment_id))
    conn.commit()
    return True

def delete_payment(payment_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM Payments WHERE payment_id = ?''', (payment_id,))
    conn.commit()
    return True


#RECEIPTS TABLE
def insert_receipt(transaction_id, date, vendor, amount, category_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Receipts (transaction_id, date, vendor, amount, category_id) 
                        VALUES (?, ?, ?, ?, ?)''', (transaction_id, date, vendor, amount, category_id))
    conn.commit()
    print("Receipt added successfully")  

def get_all_receipts():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Receipts''')
    rows = cursor.fetchall()
    return rows

def update_receipt(receipt_id, transaction_id, date, vendor, amount, category_id):
    conn = create_connection()
    cursor = conn.coursor()
    cursor.execute('''UPDATE Receipts SET transaction_id = ?, date = ?, vendor = ?, amount = ?, category_id = ? 
                        WHERE receipt_id = ?''',
                    (transaction_id, date, vendor, amount, category_id, receipt_id)) 
    conn.commit()
    print('Receipt updated successfully')
        
def delete_receipt(receipt_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM Receipts WHERE receipt_id = ?''', (receipt_id,))
    conn.commit()
    print("Receipt deleted successfully")
    
#FINANCIAL TABLE
def insert_financial_report():
    pass

#FUNDRAISING TABLE
def insert_fundraising_activity():
    pass

#TRAINING TABLE
def insert_training():
    pass
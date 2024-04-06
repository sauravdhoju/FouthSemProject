import streamlit as st
import sqlite3
from modules.Create_Connection.Create_Connection import create_connection 

def create_club_expense_table(db):
    expense_categories_columns = {
        "category_id": "INTEGER PRIMARY KEY",
        "category_name": "TEXT UNIQUE NOT NULL",
        "description": "TEXT",
        "created_by": "TEXT",
        "creation_date": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
        "last_updated_by": "TEXT",
        "last_updated_date": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
    }
    
    receipts_columns = {
        "receipt_id": "INTEGER PRIMARY KEY",
        "transaction_id": "INTEGER UNIQUE NOT NULL",
        "date": "TEXT",
        "vendor": "TEXT",
        "amount": "REAL NOT NULL",
        "category_id": "INTEGER",
        "FOREIGN KEY (transaction_id)": "REFERENCES Transactions(transaction_id)",
        "FOREIGN KEY (category_id)": "REFERENCES Expense_Categories(category_id)"
    }

    financial_reports_columns = {
        "report_id": "INTEGER PRIMARY KEY",
        "report_date": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
        "description": "TEXT",
        "report_type": "TEXT NOT NULL",
        "generated_by": "TEXT",
        "FOREIGN KEY (generated_by)": "REFERENCES Members(username)"
    }

    payments_columns = {
        "payment_id": "INTEGER PRIMARY KEY",
        "username": "TEXT NOT NULL",
        "payment_amount": "REAL",
        "payment_date": "DATE",
        "payment_method": "TEXT",
        "category_name": "TEXT UNIQUE NOT NULL",
        "FOREIGN KEY (username)": "REFERENCES Members(username)",
        "FOREIGN KEY (category_name)": "REFERENCES Expense_Categories(category_name)"
    }

    training_columns = {
        "training_id": "INTEGER PRIMARY KEY",
        "training_name": "TEXT UNIQUE NOT NULL",
        "start_date": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
        "end_date": "TIMESTAMP",
        "venue": "TEXT",
        "description": "TEXT"
    }
    
    
    db.create_table("Expense_Categories", expense_categories_columns)
    db.create_table("Receipts", receipts_columns)
    db.create_table("Financial_Reports", financial_reports_columns)
    db.create_table("Payments", payments_columns)
    db.create_table("Training", training_columns)
    print("Expense tables created successfully.")
    
#EXPENSE CATEGORY
def insert_expense_category(db, category_name, description=None, created_by=None):
    category_data = {
        "category_name": category_name,
        "description": description,
        "created_by": created_by
    }
    existing_categories = db.fetch_if("Expense_Categories", {"category_name": category_name})
    if not existing_categories:
        if db.create_record("Expense_Categories", category_data):
            print("Expense category added successfully.")
            return True
        else:
            print("Failed to add expense category.")
            return False
    else:
        print("Expense category already exists.")
        return False

def display_category_table(categories):
    st.table(categories)     

def update_category(db, old_category_name, new_category_name, new_description=None, new_last_updated_by=None):
    update_data = {"category_name": new_category_name}
    if new_description is not None:
        update_data["description"] = new_description
    if new_last_updated_by is not None:
        update_data["last_updated_by"] = new_last_updated_by

    conditions = {"category_name": old_category_name}
    db.update_record("Expense_Categories", update_data, conditions)
    print("Expense Category has been updated")
    return True
  
def delete_category(db, category_name):
    try:
        conditions = {'category_name': category_name}
        deleted = db.delete_record('Expense_Categories', conditions)
        if deleted:
            print("Category has been deleted.")
            return True
        else:
            print("No matching category found.")
            return False
    except Exception as e:
        print(f"Error deleting category: {e}")
        return False
    
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
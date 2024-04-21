import streamlit as st
from modules.database import SQLiteDatabase


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
        
    receipt_columns = {
        'receipt_number': 'TEXT',
        'date': 'TEXT',
        'payment_type': 'TEXT',
        'payer_name': 'TEXT',
        'purpose': 'TEXT',
        'quantity': 'INTEGER',
        'rate': 'REAL',
        'vat_percent': 'REAL',  # Store as decimal or float
        'discount_percent': 'REAL' , # Store as decimal or float
        'amount': 'REAL'
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
        "category_name": "TEXT",
        "FOREIGN KEY (username)": "REFERENCES Members(username)",
        "FOREIGN KEY (category_name)": "REFERENCES Expense_Categories(category_name)"
    }

    # training_columns = {
    #     "training_id": "INTEGER PRIMARY KEY",
    #     "training_name": "TEXT UNIQUE NOT NULL",
    #     "start_date": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
    #     "end_date": "TIMESTAMP",
    #     "venue": "TEXT",
    #     "description": "TEXT"
    # }
    
    
    db.create_table("Expense_Categories", expense_categories_columns)
    db.create_table("Receipts", receipt_columns)
    db.create_table("Financial_Reports", financial_reports_columns)
    db.create_table("Payments", payments_columns)
    # db.create_table("Training", training_columns)
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
def record_payment(username, payment_amount, payment_date, payment_method, selected_category):
    with SQLiteDatabase("accounting.db") as db:
        # Check if the username exists in the database
        user_exists = db.fetch_if("Members", {"username": username})
        if user_exists:
            payment_record = {
                "username": username,
                "payment_amount": payment_amount,
                "payment_date": payment_date,
                "payment_method": payment_method,
                "category_name": selected_category
            }
            if db.create_record("Payments", payment_record):
                st.success("Payment recorded successfully.")
                inserted_record = db.retrieve_records("Payments", {"username": username, "payment_date": payment_date})
                if inserted_record:
                    st.write("Inserted Payment Record:", inserted_record)
                else:
                    st.error("Failed to retrieve payment record.")
            else:
                st.error("Failed to record payment.")
        else:
            st.error("Username does not exist in the database. Please check and try again.")

def display_payment_table(pay):
    st.table(pay) 

def update_payment(username, payment_amount, payment_date, payment_method, category_name):
    with SQLiteDatabase("accounting.db") as db:
        user_exists = db.fetch_if("Payments", {"username": username})
        if user_exists:
            conditions = {"username": username}
            new_data = {
                "payment_amount": payment_amount,
                "payment_date": payment_date,
                "payment_method": payment_method,
                "category_name": category_name
            }
            db.update_record("Payments", new_data, conditions)
            return True
        else:
            return False

def delete_payment(username):
    with SQLiteDatabase("accounting.db") as db:
        conditions = {"username": username}
        return db.delete_record("Payments", conditions)



def add_receipt_backend(data):
    # Add receipt to the database
    with SQLiteDatabase("accounting.db") as db:
        columns = {
            'quantity': 'INTEGER',
            'rate': 'REAL',
            'date': 'TEXT',
            'receipt_number': 'TEXT',
            'amount': 'REAL',
            'purpose': 'TEXT',
            'payer_name': 'TEXT',
            'payment_type': 'TEXT'
        }
        db.create_table('receipts', columns)
        success = db.create_record('receipts', data)
        return success

def retrieve_receipts_backend():
    # Retrieve all receipts from the database
    with SQLiteDatabase("accounting.db") as db:
        return db.retrieve_records('receipts')

def search_receipts_backend(query):
    # Search for receipts in the database based on query
    with SQLiteDatabase("accounting.db") as db:
        conditions = {'receipt_number': query}
        return db.fetch_if('receipts', conditions)

def update_receipt_backend(receipt_id, new_data):
    # Update receipt in the database
    with SQLiteDatabase("accounting.db") as db:
        existing_receipts = db.fetch_if("Receipts", {"receipt_number": receipt_id})
        if not existing_receipts:
            print("Receipt Id does not exists")
            return False
        else:
            db.update_record("receipts", new_data, {"id": receipt_id})
            print("Receipt updated successfully.")
            return True

def remove_receipt_backend(receipt_id):
    # Remove receipt from the database
    with SQLiteDatabase("accounting.db") as db:
        conditions = {'receipt_number': receipt_id}
        db.delete_record('receipts', conditions)

    
#FINANCIAL TABLE
def insert_financial_report():
    pass

#FUNDRAISING TABLE
def insert_fundraising_activity():
    pass

#TRAINING TABLE
def insert_training():
    pass
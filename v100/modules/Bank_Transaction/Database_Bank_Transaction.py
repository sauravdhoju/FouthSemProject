import streamlit as st
from modules.database import SQLiteDatabase

# Function to create the Bank Transactions table
def create_bank_transaction_table(db):
    bank_transaction_columns = {
        "transaction_number": "INTEGER PRIMARY KEY",
        "transaction_date": "TIMESTAMP",
        "description": "TEXT NOT NULL",
        "last_updated_by": "TEXT",
        "last_updated_date": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
        "debit": "INTEGER",
        "credit": "INTEGER",
        "amount": "INTEGER"
    }
    db.create_table("Bank_Transactions", bank_transaction_columns)
    st.success("Bank transaction table created successfully.")

# Function to insert a new transaction
def insert_transaction(db, transaction_date, description, last_updated_by, debit, credit, amount):
    record_data = {
        "transaction_date": transaction_date,
        "description": description,
        "last_updated_by": last_updated_by,
        "debit": debit,
        "credit": credit,
        "amount": amount
    }
    db.create_record("Bank_Transactions", record_data)
    return True

def fetch_all_transactions(db):
    return db.retrieve_records("Bank_Transactions")

def update_transaction(db, transaction_number, transaction_date, description, last_updated_by, debit, credit):
    new_data = {
        "transaction_date": transaction_date,
        "description": description,
        "last_updated_by": last_updated_by,
        "debit": debit,
        "credit": credit,
        "amount": debit - credit
    }
    conditions = {"transaction_number": transaction_number}
    db.update_record("Bank_Transactions", new_data, conditions)

def delete_transaction(db, transaction_number):
    try:
        conditions = {"transaction_number": transaction_number}
        deleted = db.delete_record("Bank_Transactions", conditions)
        if deleted:
            print("transaction has been deleted")
            return True
        else:
            print("No matchning transaction found")
            return False
    except Exception as e:
        print(f"Error deleting category: {e}")
        return False
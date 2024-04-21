import streamlit as st
from modules.Bank_Transaction.Database_Bank_Transaction import *
from modules.database import *

# Function to display UI for inserting a new transaction
def insert_transaction_ui():
    st.header("Insert New Transaction")
    with st.form(key="bank_transaction", clear_on_submit=True):
        transaction_date = st.date_input("Transaction Date")
        description = st.text_input("Description")
        logged_in_user = st.session_state['username']

        # Radio button to select transaction type
        transaction_type = st.radio("Transaction Type", ("Debit", "Credit"))

        # Display the appropriate input box based on transaction type
        if transaction_type == "Debit":
            debit = st.number_input("Debit", min_value=0)
            credit = None  # Set credit to None to avoid conflicts
        else:
            credit = st.number_input("Credit", min_value=0)
            debit = None  # Set debit to None to avoid conflicts

        # Perform calculations based on selected transaction type
        if transaction_type == "Debit":
            amount = -debit if debit is not None else None
        else:
            amount = credit if credit is not None else None

        if st.form_submit_button("Add Transaction"):
            if description.strip() == "":
                st.error("Please enter a description")
            else:
                with SQLiteDatabase("accounting.db") as db:
                    if insert_transaction(db, transaction_date, description, logged_in_user, debit, credit, amount):
                        st.success("Transaction added successfully.")
                    else:
                        st.error("Failed to add transaction")

# Function to display UI for updating a transaction
def update_transaction_ui():
    transaction_number = st.text_input("Enter Transaction Number")
    with st.form(key="update_transactions", clear_on_submit=True):
        new_transaction_date = st.text_input("*Updated Transaction Date*")
        new_description = st.text_input("*Updated Description*")
        logged_in_user = st.session_state.get('username', '')
        new_debit = st.number_input("*Updated Debit Amount*")
        new_credit = st.number_input("*Updated Credit Amount*")


# Function to display UI for deleting a transaction
def delete_transaction_ui(db):
    st.header("Delete Transaction")
    transaction_number = st.text_input("Enter Transaction Number")

    if st.button("Delete"):
        delete_transaction(db, transaction_number)

# Function to display UI for fetching all transactions
def display_all_transactions_ui(db):
    st.header("All Transactions")
    transactions = fetch_all_transactions(db)
    for transaction in transactions:
        st.write(f"Transaction Number: {transaction['transaction_number']}")
        st.write(f"Date: {transaction['transaction_date']}")
        st.write(f"Description: {transaction['description']}")
        st.write(f"Last Updated By: {transaction['last_updated_by']}")
        st.write(f"Debit: {transaction['debit']}")
        st.write(f"Credit: {transaction['credit']}")
        st.write(f"Amount: {transaction['amount']}")
        st.markdown("---")

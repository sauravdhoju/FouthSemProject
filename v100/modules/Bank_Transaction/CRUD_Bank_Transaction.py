import streamlit as st
from modules.Bank_Transaction.Database_Bank_Transaction import *
from modules.database import *

def insert_transaction_ui():
    st.header("Insert New Transaction")
    col1, col2, col3 = st.columns([4,4,4])
    with col2:
        with st.form(key="bank_transaction", clear_on_submit=True):
            transaction_date = st.date_input("Transaction Date")
            description = st.text_input("Description")
            logged_in_user = st.session_state['username']
            
            # select = st.selectbox("Select", ["Debit", "Credit"])
            debit = st.number_input("Debit", min_value=0)
            credit = st.number_input("Credit", min_value=0)
                

            amount = credit - debit if credit else debit

            if st.form_submit_button("Add Transaction"):
                if description.strip() == "":
                    st.error("Please enter date")
                else:
                    with SQLiteDatabase("accounting.db") as db:
                        if insert_transaction(db, transaction_date, description, logged_in_user, debit, credit, amount):
                            st.success("Transaction added successfully.")
                        else:
                            st.error("Failed to add trasaction")

def update_transaction_ui():
    col1, col2, col3 = st.columns([4,4,4])
    with col2:
        transaction_number = st.text_input("Enter Transaction Number")
        with st.form(key="update_transactions", clear_on_submit=True):
            new_transaction_date = st.text_input("*Updated Transaction Date*")
            new_description = st.text_input("*Updated Description*")
            logged_in_user = st.session_state.get('username', '')
            new_debit = st.number_input("*Updated Debit Amount*")
            new_credit = st.number_input("*Updated Credit Amount*")
            update_button = st.form_submit_button('Update')
            if update_button:
                with SQLiteDatabase ("accounting.db") as db:
                    existing_transaction = db.fetch_if("Bank_Transaction", {"transaction_number": transaction_number})
                    if existing_transaction:
                        if new_description.strip() == "":
                            st.error("Fill descriptoin properly")
                        else:
                            if update_transaction(db, transaction_number, new_transaction_date, new_description, logged_in_user, new_debit, new_credit):
                                st.success("Updated Successfully")
                            else:
                                st.error("Failed")
                    else:
                        st.error("Transaction Not found")


def remove_transaction_ui():
    with st.form(key="search_form", clear_on_submit=True):
        col1, col2, col3 = st.columns([4, 4, 4])
        with col2:
            transaction_number = st.text_input("Transaction Number")
            search_button = st.form_submit_button("Search")
        with col3:
            delete_button = st.form_submit_button("Delete")

    if search_button:
        with SQLiteDatabase("accounting.db") as db:
            search_result = db.fetch_if('Bank_Transactions',{'transaction_number': transaction_number})
            if search_result:
                st.write("Search Results:")
                st.table(search_result)
            else:
                st.write("No matching transaction found.")

    if delete_button:
        if transaction_number.strip() == "":
            st.error('Please enter a valid transaction number')
        else:
            with SQLiteDatabase("accounting.db") as db:
                deleted = delete_transaction(db, transaction_number)
                if deleted:
                    st.success("Transaction deleted successfully.")

def view_transaction_ui():
    st.header("View transaction")
    col1, col2, col3 = st.columns([4, 4, 4])
    with col2: 
        with st.form(key="transaction_view", clear_on_submit= True):
            Transaction_number = st.text_input('Transaction Nuber')
            search_button = st.form_submit_button('View Category')

    if search_button:
        with SQLiteDatabase("accounting.db") as db:
            search_results = db.fetch_if("Bank-Transactions", {"transaction_number": Transaction_number})
            if search_results:
                st.write("Search Results:")
                st.table(search_results)
            else:
                st.write("No matching categories found")
    else:
        with st.form("all_categories_form", clear_on_submit= True):
            col1, col2, col3 = st.columns([6, 4, 4])
            with col2:
                all_categories_button = st.form_submit_button("Show All transaction")
        
        if all_categories_button:
            with SQLiteDatabase("accounting.db") as db:
                al_Transaction = db.fetch_if("Bank_Transactions", {})
                if al_Transaction:
                    st.write('All Transaction: ')
                    st.table(al_Transaction)
                else:
                    st.write("No categories found.")


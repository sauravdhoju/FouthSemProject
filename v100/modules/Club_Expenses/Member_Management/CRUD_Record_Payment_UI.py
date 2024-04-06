import streamlit as st
from modules.Club_Expenses.Database_Club_Expenses import record_payment, update_payment, delete_payment, display_payment_table
from modules.database import SQLiteDatabase

def create_payment_ui():
    st.header("Record Payment")
    username = st.text_input("Username")
    payment_amount = st.number_input("Payment Amount", min_value=0.0)
    payment_date = st.date_input("Payment Date")
    payment_method = st.selectbox("Payment Method", ["Cash", "Bank Transfer", "Esewa", "Khalti"])
    
    selected_category = fetch_payment_categories_ui()
    
    if st.button("Record Payment"):
        record_payment(username, payment_amount, payment_date, payment_method, selected_category)

def fetch_payment_categories_ui():
    try:
        with SQLiteDatabase("accounting.db") as db:
            categories = [category[1] for category in db.retrieve_records("Expense_Categories")]
        selected_category = st.selectbox("Payment Category", categories)
        return selected_category
    except Exception as e:
        print(f"Error fetching payment categories: {e}")
        return None

def search_payment_by_username_ui():
    st.header("Search Payments by Username")
    col1, col2, col3 = st.columns([4, 4, 4])
    with col2: 
        with st.form(key="payment_search_form"):
            username = st.text_input('Enter Username')
            search_button = st.form_submit_button('Search Payments')

    if search_button:
        with SQLiteDatabase("accounting.db") as db:
            payments = db.fetch_if("Payments", {"username": username})
            if payments:
                st.write("Search Results:")
                display_payment_table(payments)
            else:
                st.write("No payments found for this username.")
    else:
        with st.form("all_payments_form"):
            col1, col2, col3 = st.columns([6, 4, 4])
            with col2:
                all_payments_button = st.form_submit_button("Show All Payments")
        
        if all_payments_button:
            with SQLiteDatabase("accounting.db") as db:
                all_payments = db.fetch_if("Payments", {})
                if all_payments:
                    st.write('All Payments: ')
                    display_payment_table(all_payments)
                else:
                    st.write("No payments found.")

def update_payment_ui():
    '''Updating Payment Executives'''
    st.header("Update Payment")
    username = st.text_input("Username")
    payment_amount = st.number_input("Payment Amount", min_value=0.0)
    payment_date = st.date_input("Payment Date")
    payment_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Debit Card", "Bank Transfer"])

    if st.button("Update Payment"):
        if update_payment(username, payment_amount, payment_date, payment_method):
            st.success("Payment updated successfully.")
        else:
            st.error("Failed to update payment.")
        
def delete_payment_ui():
    '''Delete Record Payments'''
    st.header("Delete Payment")
    payment_id = st.number_input("Payment ID", min_value=1, step=1)

    if st.button("Delete Payment"):
        if delete_payment(payment_id):
            st.success("Payment deleted successfully.")
        else:
            st.error("Failed to delete payment.")

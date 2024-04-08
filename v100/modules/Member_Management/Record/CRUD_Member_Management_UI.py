import streamlit as st
from modules.Club_Expenses.Database_Club_Expenses import record_payment, update_payment, delete_payment, display_payment_table
from modules.database import SQLiteDatabase

#Records
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
            categories = [category["category_name"] for category in db.fetch_if("Expense_Categories", {})]
        selected_category = st.selectbox("Payment Category", categories)
        return selected_category
    except Exception as e:
        print(f"Error fetching payment categories: {e}")
        print(f"SQL Query: SELECT * FROM Expense_Categories")
        return None


def search_payment_by_username_ui():
    st.header("Search Payments by Username")
    col1, col2, col3 = st.columns([4, 4, 4])
    with col2: 
        with st.form(key="payment_search_form", clear_on_submit= True):
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
        with st.form("all_payments_form", clear_on_submit= True):
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
    selected_category = fetch_payment_categories_ui()

    if st.button("Update Payment"):
        if update_payment(username, payment_amount, payment_date, payment_method, selected_category):
            st.success("Payment updated successfully.")
        else:
            st.error("No Username in the database")
        
def delete_payment_ui():
    '''Delete Record Payments'''
    st.header("Delete Payment")
    # payment_id = st.number_input("Payment ID", min_value=1, step=1)
    username = st.text_input("Username")

    if st.button("Delete Payment"):
        if delete_payment(username):
            st.success("Payment deleted successfully.")
        else:
            st.error("No user found.")

#View History
def fetch_payment_history(start_date, end_date):
    try:
        with SQLiteDatabase("accounting.db") as db:
            start_date_str = start_date.strftime('%Y-%m-%d')
            end_date_str = end_date.strftime('%Y-%m-%d')
            
            # Define the SQL query to select payment information within the specified date range
            query = "SELECT payment_date, username,   payment_method, category_name,payment_amount FROM Payments WHERE payment_date BETWEEN ? AND ?"
            
            db.cursor.execute(query, (start_date_str, end_date_str))
            column_names = [description[0] for description in db.cursor.description]
            
            rows = db.cursor.fetchall()
            
            payment_history = []
            for row in rows:
                payment_info = dict(zip(column_names, row))
                payment_history.append(payment_info)
            
        return payment_history
    except Exception as e:
        print(f"Error fetching payment history: {e}")
        return None
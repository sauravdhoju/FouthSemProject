import streamlit as st
from modules.Club_Expenses.Database_Club_Expenses import create_payment, retrieve_member_information, update_payment, delete_payment
from modules.Create_Connection.Create_Connection import create_connection, fetch_if
def fetch_categories():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT category_name FROM Expense_Categories''')
    categories = [row[0] for row in cursor.fetchall()]
    return categories

def create_payment_ui():
    st.header("Record Payment")
    username = st.text_input("Username")
    payment_amount = st.number_input("Payment Amount", min_value=0.0)
    payment_date = st.date_input("Payment Date")
    payment_method = st.selectbox("Payment Method", ["Cash", "Bank Transfer", "Esewa", "Khalti"])
    
    # Fetch categories from the database
    categories = fetch_categories()
    selected_category = st.selectbox("Payment Category", categories)
    
    if st.button("Record Payment"):
        if create_payment(username, payment_amount, payment_date, payment_method, selected_category):
            st.success("Payment recorded successfully.")
        else:
            st.error("Failed to record payment.")

def display_member_payment_table(username):
    username_data = []
    for usernam in username:
        username_info = {
            "payment_id": usernam[0],
            "username": usernam[1],
            "payment_amount": usernam[2],
            "payment_date": usernam[3],
            "payment_method": usernam[4],
            "category_name": usernam[5]
        }
        username_data.append(username_info)
    st.table(username_data)   
    
# Function to retrieve member information
def retrieve_member_information_ui():
    st.header("Retrieve Member Information")
    username = st.text_input("Username")
    if st.button("Retrieve Information"):
        # member_info = retrieve_member_information(username)
        member_info = fetch_if('Payments', {'username': username})
        print("DEBUG:", member_info)  # Add this line for debugging
        if member_info:
            st.write("Member Information:")
            # display_member_payment_table(username)
            st.table(member_info)
        else:
            st.error("Member not found.")


# Function to update a payment
def update_payment_ui():
    st.header("Update Payment")
    payment_id = st.number_input("Payment ID", min_value=1, step=1)
    payment_amount = st.number_input("Payment Amount", min_value=0.0)
    payment_date = st.date_input("Payment Date")
    payment_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Debit Card", "Bank Transfer"])

    if st.button("Update Payment"):
        if update_payment(payment_id, payment_amount, payment_date, payment_method):
            st.success("Payment updated successfully.")
        else:
            st.error("Failed to update payment.")

# Function to delete a payment
def delete_payment_ui():
    st.header("Delete Payment")
    payment_id = st.number_input("Payment ID", min_value=1, step=1)

    if st.button("Delete Payment"):
        if delete_payment(payment_id):
            st.success("Payment deleted successfully.")
        else:
            st.error("Failed to delete payment.")

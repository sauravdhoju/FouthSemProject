import streamlit as st
from modules.Club_Expenses.Database_Club_Expenses import display_payment_table
from modules.Club_Expenses.Member_Management.Record.CRUD_Member_Management_UI import fetch_payment_history

def view_payment_history_ui():
    st.header("View Payment History")
    
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    
    if st.button("Search"):
        if start_date > end_date:
            st.error("End date must be after start date.")
        else:
            payment_history = fetch_payment_history(start_date, end_date)
            if payment_history:
                display_payment_table(payment_history)
            else:
                st.write("No payments found in the selected date range.")




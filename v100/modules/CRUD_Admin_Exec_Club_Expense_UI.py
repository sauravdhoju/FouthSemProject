import streamlit as st

def receipt_management_ui():
    st.header(f"Receipt Management")

def add_receipt():
    col1,col2,col3 = st.columns(3)
    with col1:
        st.text_input('Customer Name')
    with col2:
        st.text_input('vendor')
    with col3:
        st.text_input('vendor1')
def financial_reporting_ui():
    st.header("financila ma")
def expense_categories_ui():
    st.header("expense category")

def fundraising_ui():
    st.header("fundraising ")

def training_and_education_ui():
    st.header("training category")

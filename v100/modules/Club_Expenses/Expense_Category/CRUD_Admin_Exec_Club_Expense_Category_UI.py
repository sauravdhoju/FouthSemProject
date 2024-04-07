import streamlit as st
from modules.Club_Expenses.Database_Club_Expenses import insert_expense_category, display_category_table, update_category, delete_category
from modules.database import *
def receipt_management_ui():
    st.header(f"Receipt Management")

# def add_receipt():
    

def add_expense_category_ui():
    st.header("Add Expense Category")
    col1, col2, col3 = st.columns([4, 4, 4])
    with col2:
        with st.form(key="expense_category", clear_on_submit=True):
            category_name = st.text_input('Category name')
            category_description = st.text_area('Description')
            logged_in_user = st.session_state['username']

            if st.form_submit_button("Add Category"):
                if category_name.strip() == "":
                    st.error("Please enter a category name.")
                else:
                    with SQLiteDatabase("accounting.db") as db:
                        if insert_expense_category(db, category_name, category_description, logged_in_user):
                            print(insert_expense_category(db, category_name, category_description, logged_in_user))
                            st.success("Expense category added successfully.")
                        else:
                            st.error("Already Exists Category")

def view_expense_category_ui():
    st.header("View Expense Category")
    col1, col2, col3 = st.columns([4, 4, 4])
    with col2: 
        with st.form(key="expense_view_form", clear_on_submit= True):
            view_category = st.text_input('Category Name')
            search_button = st.form_submit_button('View Category')

    if search_button:
        with SQLiteDatabase("accounting.db") as db:
            search_results = db.fetch_if("Expense_Categories", {"category_name": view_category})
            if search_results:
                st.write("Search Results:")
                display_category_table(search_results)
            else:
                st.write("No matching categories found")
    else:
        with st.form("all_categories_form", clear_on_submit= True):
            col1, col2, col3 = st.columns([6, 4, 4])
            with col2:
                all_categories_button = st.form_submit_button("Show All Categories")
        
        if all_categories_button:
            with SQLiteDatabase("accounting.db") as db:
                all_categories = db.fetch_if("Expense_Categories", {})
                if all_categories:
                    st.write('All Categories: ')
                    display_category_table(all_categories)
                else:
                    st.write("No categories found.")

def update_expense_category_ui():
    st.header("Update Expense Category")
    col1, col2, col3 = st.columns([4, 4, 4])
    
    with col2:
        category_name = st.text_input("Category Name*")
        with st.form(key="expense_update_form", clear_on_submit= True):
            new_category = st.text_input("New Category*")
            new_description = st.text_area("Description*")
            logged_in_user = st.session_state.get('username', '') 
            update_button = st.form_submit_button('Update')
            if update_button and category_name.strip():
                with SQLiteDatabase("accounting.db") as db:
                    existing_categories = db.fetch_if("Expense_Categories", {"category_name": category_name})
                    if existing_categories:
                        if new_category.strip() == "" or new_description.strip() == "":
                            st.error("Please fill all required fields")
                        else:
                            if update_category(db, category_name, new_category, new_description, logged_in_user):
                                st.success('Updated Successfully')
                    else:
                        st.error("Category not found. Please enter a valid category name.")

def remove_expense_category_ui():
    with st.form(key="search_form", clear_on_submit= True):
        col1, col2, col3 = st.columns([4, 4, 4])
        with col2:
            category_name = st.text_input("Category Name")
            search_button = st.form_submit_button("Search")
        with col3:
            delete_button = st.form_submit_button("Delete")
    with SQLiteDatabase("accounting.db") as db:
        if search_button:
            search_results = db.fetch_if('Expense_Categories', {'category_name': category_name})
            if search_results:
                st.write("Search Results:")
                st.table(search_results)
            else:
                st.write("No matching category found.")
        
        if delete_button:
            if category_name.strip() == "":
                st.error('Please enter valid category name')
            else:
                deleted = delete_category(db, category_name)  # Pass db object as argument
                if deleted:
                    st.success("Deleted Successfully")
    
def fundraising_ui():
    st.header("fundraising ")

def training_and_education_ui():
    st.header("training category")

import streamlit as st
from modules.Database_Club_Expenses import insert_expense_category, search_category, get_all_categories, update_category
from modules.Create_Connection import create_connection

conn = create_connection()
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
   

def display_category_table(categories):
    category_data = []
    for category in categories:
        category_info = {
            "category_id": category[0],
            "category_name": category[1],
            "description": category[2],
            "created_by": category[3],
            "creation_date": category[4],
            "last_updated_by": category[5],
            "last_updated_date": category[6] 
        }
        category_data.append(category_info)
    st.table(category_data)     
    
def add_expense_category_ui(conn):
    st.header("Add Expense Category")
    col1,col2,col3 = st.columns([4,4,4])
    with col2:
        category_name = st.text_input('Category name')
        category_description = st.text_area('Description')
        logged_in_user = st.session_state['username']

        if st.button("Add Category"):
            if category_name.strip() == "":
                st.error("Please enter a category name.")
            else:
                if insert_expense_category(conn, category_name, category_description, logged_in_user):
                    st.success("Expense category added successfully.")
                else:
                    st.error("Failed to add expense category")
def view_expense_category_ui():
    st.header("View Expense Category")
    col1, col2, col3 = st.columns([4,4,4])
    with col2: 
        with st.form(key="expense_view_form"):
            view_category = st.text_input('View Category')
            search_button = st.form_submit_button('View Category')
        if search_button:
            search_results = search_category(conn, view_category)
            if search_results:
                st.write("Search Results:")
                display_category_table(search_results)
            else:
                
                st.write("No matching categories found")
        else:
            with st.form("all_categories_form"):
                all_categories_button = st.form_submit_button("Show All Categories")
            
            if all_categories_button:
                all_categories = get_all_categories(conn)
                if all_categories:
                    st.write('All Categories: ')
                    display_category_table(all_categories)
                else:
                    st.write("No categories found.")
                    
def update_expense_category_ui():
    st.header("Update Expense Category")
    col1, col2, col3 = st.columns([4,4,4])
    with col2:
        with st.form(key="expense_search_form"):
            category_name = st.text_input("Category Name")
            search_button = st.form_submit_button('Search')
        if search_button:
            search_results = search_category(conn, category_name)
            if search_results:
                st.write('Search Results')
                display_category_table(search_results)
                
                with st.form(key="expense_update_form"):
                    new_category = st.text_input("New Category")
                    new_description = st.text_area("Description")
                    logged_in_user = st.session_state['username']
                    update_button = st.form_submit_button('Update')
                    print('Update Button:', update_button)
                    if update_button:
                        print('Hey Rabisha')
                        if category_name.strip() == "":
                            st.error("Enter valid category name")
                            print("Type correct category name you bullshit")
                        else:
                            new_category = {
                                'category_name':  new_category,
                                'description': new_description,
                                'last_updated_by': logged_in_user
                            }
                            if update_category(conn, category_name, new_category, new_description, logged_in_user):
                                st.success('Updated Successfully')
                            else:
                                st.error('Failed to Update.')
                    else:
                        st.error('Not updated')
            else:
                st.write('Category not found.')

            
                
            
            
        
def fundraising_ui():
    st.header("fundraising ")

def training_and_education_ui():
    st.header("training category")

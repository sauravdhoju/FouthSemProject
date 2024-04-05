import streamlit as st
from modules.Club_Expenses.Database_Club_Expenses import insert_expense_category, update_category, delete_category, fetch, fetch_all
from modules.Create_Connection.Create_Connection import create_connection, fetch_if
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
   
#Categories UI
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
    
def add_expense_category_ui():
    st.header("Add Expense Category")
    col1,col2,col3 = st.columns([4,4,4])
    with col2:
        category_name = st.text_input('Category name')
        category_description = st.text_area('Description')
        logged_in_user = st.session_state['username']
        print(logged_in_user)

        if st.button("Add Category"):
            if category_name.strip() == "":
                st.error("Please enter a category name.")
            else:
                if insert_expense_category( category_name, category_description, logged_in_user):
                    st.success("Expense category added successfully.")
                else:
                    st.error("Failed to add expense category")

def view_expense_category_ui():
    st.header("View Expense Category")
    col1, col2, col3 = st.columns([4,4,4])
    with col2: 
        with st.form(key="expense_view_form"):
            view_category = st.text_input('Category Name')
            search_button = st.form_submit_button('View Category')
    if search_button:
        search_results = fetch('Expense_Categories', 'category_name', view_category )
        if search_results:
            st.write("Search Results:")
            display_category_table(search_results)
        else:
            st.write("No matching categories found")
    else:
        with st.form("all_categories_form"):
            col1, col2, col3 = st.columns([6,4,4])
            with col2:
                all_categories_button = st.form_submit_button("Show All Categories")
        if all_categories_button:
            all_categories = fetch_all('Expense_Categories')
            if all_categories:
                st.write('All Categories: ')
                display_category_table(all_categories)
            else:
                st.write("No categories found.")
                
def category_exists(category_name):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM Expense_Categories WHERE category_name = ?", (category_name,))
    result = cursor.fetchone()[0]
    conn.close() 
    # If result > 0, the category exists; otherwise, it does not exist
    return result > 0
        
def update_expense_category_ui():
    st.header("Update Expense Category")
    col1, col2, col3 = st.columns([4, 4, 4])
    
    with col2:
        category_name = st.text_input("Category Name*")
        with st.form(key="expense_update_form"):
            new_category = st.text_input("New Category*")
            new_description = st.text_area("Description*")
            logged_in_user = st.session_state.get('username', '') 
            update_button = st.form_submit_button('Update')
            if update_button and category_name.strip():
                if category_exists(category_name):
                    if new_category.strip() == "" or new_description.strip() == "":
                        st.error("Please fill all required fields")
                    else:
                        update_category(category_name, new_category, new_description, logged_in_user)
                        st.success('Updated Successfully')
                        st.rerun()
                else:
                    st.error("Category not found. Please enter a valid category name.")

def remove_expense_category_ui():
    conn = create_connection()
    email = None
    with st.form(key="search_form"):
        col1,col2, col3 = st.columns([4, 4, 4])
        with col2:
            category_name = st.text_input("Category Name")
            search_button = st.form_submit_button("Search")
        with col3:
            delete_button = st.form_submit_button("Delete")

    if search_button:
        search_results = fetch_if('Expense_Categories', {'category_name': category_name})
        if search_results:
            st.write("Search Results:")
            st.table(search_results)
        else:
            st.write("No matching category found.")
    
    if delete_button:
        if category_name.strip() == "":
            st.error('Please enter valid category name')
        else:
            delete = delete_category(category_name)
            if delete:
                st.success("Deleted Successfully")
    
def fundraising_ui():
    st.header("fundraising ")

def training_and_education_ui():
    st.header("training category")

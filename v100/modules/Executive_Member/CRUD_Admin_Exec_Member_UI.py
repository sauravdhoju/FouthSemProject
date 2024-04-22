import streamlit as st
from passlib.hash import pbkdf2_sha256
from modules.Executive_Member.Database_Exec_Member_Management import *
from modules.database import SQLiteDatabase

def add_executive_members_ui():
    st.subheader("Add Executive Members")
    with st.form(key="add_executive_form", clear_on_submit= True):
        col1, col2, col3 = st.columns([5, 5, 5])
        with col1:
            st.write("Personal Details")
            exec_username = st.text_input("Username")
            exec_name = st.text_input("Full Name")
            exec_password = st.text_input("Password", type="password")
        with col2:
            st.write("Contact Details")
            exec_email = st.text_input("Email Address")
            exec_phone = st.text_input("Contact Number")
            exec_balance = None
            exec_active_status = st.checkbox("Active Status")
        with col3:
            st.write("Club Member Details")
            exec_position = st.selectbox('Position', ['President', 'Vice President', 'Secretary', 'IT Coordinator','Lens Man', 'Social Media Handler', 'Membership Handler'])
            exec_joined_date = st.date_input("Joined Date")
            exec_performance_metrics = st.number_input("Performance Metrics (Stars)", min_value=0, max_value=3, step=1)
            access_level = st.selectbox("Access Level", ["Treasurer", "Secretary", "President", "Vice President"])
            exec_role_id = st.selectbox("Role Id",["1", "2"])
            
        if st.form_submit_button("Add Executive Member"):
            hashed_password = pbkdf2_sha256.hash(exec_password)
            member_info = {
                "username": exec_username,
                "hashed_password": hashed_password,
                "full_name": exec_name,
                "email": exec_email,
                "phone": exec_phone,
                "position": exec_position,
                "account_balance": exec_balance,
                "joined_date": exec_joined_date,
                "performance_metrics": exec_performance_metrics,
                "active_status": exec_active_status,
                "access_level": access_level,
                "role_id": exec_role_id
            }
            with SQLiteDatabase("accounting.db") as db:
                add_executive_member(db, member_info)

def display_executive_members_ui():
    with SQLiteDatabase("accounting.db") as db:
        with st.form(key="search_form", clear_on_submit= True):
            col1, col2, col3 = st.columns([4, 4, 4])
            with col2:
                username = st.text_input("Search by name or email")
                search_button = st.form_submit_button("Search")

            if search_button:
                search_results = db.fetch_if("Members", {"username": username}) or db.fetch_if("Members", {"email": username}) or db.fetch_if("Members", {"phone": username})
                if search_results:
                    st.write("Search Results:")
                    display_member_table(search_results)
                else:
                    st.write("No matching executive members found.")
            
        with st.form(key="all_members_form", clear_on_submit= True):
            col1, col2, col3 = st.columns([4, 4, 4])
            with col2:
                all_members_button = st.form_submit_button("Show All Executive Members")

            if all_members_button:
                executive_members = db.fetch_if("Members", {})
                if executive_members:
                    st.write("All Executive Members:")
                    display_member_table(executive_members)
                else:
                    st.write("No executive members found.")

def update_executive_members_ui():
    st.header("Update Executive Member")
    executive_username = st.text_input("Username*")
    st.markdown("---")
    col1, col2, col3 = st.columns([4, 4, 4])
    update_button = st.button('Update')
    with col2:
        with col1:
            st.write("Personal Details")
            new_username = st.text_input('New Username')
            new_full_name = st.text_input('New Full Name')
            new_password = st.text_input('New Password', type="password")
        with col2:
            st.write("Contact Details")
            new_email_address = st.text_input('New Email Address')
            new_contact = st.number_input('New Contact Number')
            new_active_status = st.checkbox('New Active Status')
        with col3:
            st.write("Club Info")
            new_position = st.selectbox('New Position', ['President', 'Vice President', 'Secretary', 'IT Coordinator','Lens Man', 'Social Media Handler', 'Membership Handler'])
            new_performance_metrics = st.number_input("Performance Metrics (Stars) (1,2,3)", min_value=0, max_value=3, step=1)
            new_access_level = st.selectbox("Access Level", ["Treasurer", "Secretary", "President", "Vice President"])
            new_role_id = st.selectbox("Role Id",["1", "2"])
                
    if update_button and executive_username.strip():
        # Connect to the database
        with SQLiteDatabase("accounting.db") as db:
            if not all([new_username, new_full_name, new_password, new_email_address, new_contact, new_position, new_performance_metrics, new_access_level, new_role_id]):
                st.error("Please fill all fields")
            else:
                hashed_password = pbkdf2_sha256.hash(new_password)
                
                new_details = {
                    'username': new_username,
                    'hashed_password': hashed_password,
                    'full_name': new_full_name,
                    'email': new_email_address,
                    'phone': new_contact,
                    'account_balance': None,
                    'active_status': new_active_status,
                    'position': new_position,
                    'performance_metrics': new_performance_metrics,
                    'access_level': new_access_level,
                    'role_id': new_role_id
                }
                
                if db.fetch_if("Members", {"username": executive_username}):
                    if update_member_details(db, executive_username, new_details):
                        st.success('Updated Successfully')
                    else:
                        st.error("Failed to update")
                else:
                    st.error("Executive member not found. Please enter a valid username.")

def delete_executive_members_ui():
    with st.form(key="search_form1", clear_on_submit= True):
        username = st.text_input("Search by username")
        search_button = st.form_submit_button("Search")
        delete_button = st.form_submit_button("Delete")
        
    if search_button:
        with SQLiteDatabase("accounting.db") as db:
            search_results = db.fetch_if("Members", {"username": username})
            if search_results:
                st.write("Search Results:")
                display_member_table(search_results)
            else:
                st.write("No matching executive members found.")
                
    
    if delete_button:
        if username.strip() == "":
            st.error('Please enter a valid username')
        else:
            with SQLiteDatabase("accounting.db") as db:
                deleted = delete_member(db, username)
                if deleted:
                    st.success("Deleted Successfully")
                else:
                    st.error("Failed to Delete")
  
def get_logged_in_user_details():
    if 'username' in st.session_state:
        username = st.session_state.username
        return username
    else:
        return None, None 
    
def view_user_details_ui():
    logged_in_username = get_logged_in_user_details() 
    if logged_in_username:
        st.write(f"Logged in as: {logged_in_username}")

        st.subheader("User Details")
        
        # Create three columns layout
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            with st.container():
                with SQLiteDatabase("accounting.db") as db:
                    user_details = db.fetch_if("Members", {"username": logged_in_username})

                if user_details:
                    user_detail = user_details[0]  # Assuming there is only one user detail record
                    st.markdown("**Profile Details:**")
                    st.write("**Username:**", user_detail.get("username", ""))
                    st.write("**Name:**", user_detail.get("full_name", ""))
                    st.write("**Email:**", user_detail.get("email", ""))
                    st.write("**Phone Number:**", user_detail.get("phone", ""))
                    st.write("**Position:**", user_detail.get("position", ""))
                    st.write("**Joined Date:**", user_detail.get("joined_date", ""))
                    st.write("**Performance Metrics:**", user_detail.get("performance_metrics", ""))
                else:
                    st.error("User details not found.")
    else:
        st.error("User details not found. Please log in.")



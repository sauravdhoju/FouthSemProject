# app.py

import streamlit as st
from passlib.hash import pbkdf2_sha256
from modules.database import create_connection, add_executive_member, search_executive_members, get_all_executive_members, delete_member, update_member_details
import datetime
conn = create_connection()

def add_executive_members_ui(conn):
    col1, col2, col3 = st.columns([1, 5, 1])
    with col1:
        pass
    with col2:
        st.subheader("Add Executive Members")
        # Start the form context with a unique key
        with st.form(key="add_executive_form"):
            exec_username = st.text_input("Username")
            exec_name = st.text_input("Full Name")
            exec_position = st.selectbox('Position', ['President', 'Vice President', 'Secretary', 'IT Coordinator','Lens Man', 'Social Media Handler', 'Membership Handler'])
            exec_email = st.text_input("Email Address")
            exec_phone = st.text_input("Contact Number")
            exec_password = st.text_input("Password", type="password")
            exec_balance = None
            exec_joined_date = st.date_input("Joined Date")
            exec_performance_metrics = st.number_input("Performance Metrics (Stars)", min_value=0, max_value=3, step=1)
            exec_active_status = st.checkbox("Active Status")
            access_level = st.selectbox("Access Level", ["Treasurer", "Secretary", "President", "Vice President"])
            exec_role_id = st.selectbox("Role Id",["1", "2"])

            # If the form is submitted
            if st.form_submit_button("Add Executive Member"):
                hashed_password = pbkdf2_sha256.hash(exec_password)
                add_executive_member(conn, exec_name, exec_position, exec_email, exec_phone, exec_username, hashed_password, exec_balance, exec_joined_date, exec_performance_metrics, exec_active_status, access_level, exec_role_id)

    with col3:
        pass
def display_executive_members_ui(conn):
    with st.form(key="search_form"):
        username = st.text_input("Search by name or email")
        search_button = st.form_submit_button("Search")

    if search_button:
        search_results = search_executive_members(conn, username)
        if search_results:
            st.write("Search Results:")
            display_member_table(search_results)
        else:
            st.write("No matching executive members found.")
    else:
        with st.form(key="all_members_form"):
            all_members_button = st.form_submit_button("Show All Executive Members")
        
        if all_members_button:
            executive_members = get_all_executive_members(conn)
            if executive_members:
                st.write("All Executive Members:")
                display_member_table(executive_members)
            else:
                st.write("No executive members found.")


def display_member_table(members):
    member_data = []
    for member in members:
        phone = member[5] if member[5] else "N/A"
        member_info = {
            "Username": member[1],
            "Full Name": member[3],
            "Position": member[6],
            "Email": member[4],
            "Phone": phone,
            "Account Balance": member[7],
            "Joined Date": member[8],
            "Performance Metrics": member[9],
            "Active Status": "Active" if member[10] else "Inactive",
            "Access Level": member[11]
        }
        member_data.append(member_info)
    st.table(member_data)

def update_executive_members_ui(conn):
    print("hey")
    username = st.text_input("Enter Username")
    if st.button("Search"):
        if username.strip() == "":
            st.error("Invalid Username")
        else:
            member = display_executive_members_ui(conn, username)
            if member:
                st.write("Current Member Details:")
                display_member_table(member)
            #     st.subheader("Update Member Details:")
            #     new_username = st.text_input("New Username", value=member['Username'])
            #     # new_password = 
            #     if st.button("Update"):
            #         new_details = {
            #             "Username": new_username,
            #             # Add other fields and get their values
            #         }
            #         success = update_member_details(conn, username, new_details)
            #         if success:
            #             st.success("Member details updated successfully.")
            #         else:
            #             st.error("Failed to update member details.")
            # else:
            #     st.error("Member not found.")
                
def delete_executive_members_ui(conn):
    with st.form(key="delete_member"):
        del_username = st.text_input("Enter Username")
        delete_button = st.form_submit_button("Delete")

        if delete_button:
            if del_username.strip() == "":
                st.error("Please enter a valid Member ID.")
            else:
                success = delete_member(conn, del_username)
                if success:
                    st.success("Member deleted successfully.")
                else:
                    st.error("Failed to delete member.")
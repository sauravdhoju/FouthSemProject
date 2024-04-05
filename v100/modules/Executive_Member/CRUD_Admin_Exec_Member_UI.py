import streamlit as st
from passlib.hash import pbkdf2_sha256
from modules.Create_Connection.Create_Connection import create_connection, fetch_if
from modules.Executive_Member.Database_Exec_Member_Management import add_executive_member, search_executive_members, get_all_executive_members, delete_member, update_member_details

def add_executive_members_ui():
    st.subheader("Add Executive Members")
    with st.form(key="add_executive_form"):
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
            add_executive_member( exec_username, hashed_password ,exec_name, exec_email, exec_phone, exec_position, exec_balance, exec_joined_date, exec_performance_metrics, exec_active_status, access_level, exec_role_id)
    
def display_executive_members_ui():
    conn = create_connection()
    with st.form(key="search_form"):
        col1, col2, col3 = st.columns([4,4,4])
        with col2:
            username = st.text_input("Search by name or email")
            search_button = st.form_submit_button("Search")

        if search_button:
            search_results = search_executive_members( username)
            if search_results:
                st.write("Search Results:")
                display_member_table(search_results)
            else:
                st.write("No matching executive members found.")
        
    with st.form(key="all_members_form"):
        col1, col2, col3 = st.columns([4,4,4])
        with col2:
            all_members_button = st.form_submit_button("Show All Executive Members")

        if all_members_button:
            executive_members = get_all_executive_members()
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

def exec_member_exists(executive_username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT COUNT(*) FROM Members WHERE username = ?''', (executive_username,))
    result = cursor.fetchone()[0]
    conn.close()
    return result > 0

def update_executive_members_ui():
    st.header("Update Executive Member")
    executive_username = st.text_input("Username*")
    st.markdown("---")
    col1, col2, col3 = st.columns([4, 4, 4])
    update_button = st.button('Update')
    with col2:
        # with st.form(key="update_executive_member"):
        
        with col1:
            st.write("Personal Details")
            new_username = st.text_input('New Username')
            new_full_name = st.text_input('New Full Name')
            new_password = st.text_input('New Password', type="password")
        with col2:
            st.write("Contact Details")
            new_email_address = st.text_input('New Email Address')
            new_contact = st.text_input('New Contact Number')
            new_active_status = st.checkbox('New Active Status')
        with col3:
            st.write("Club Info")
            new_position = st.selectbox('New Position', ['President', 'Vice President', 'Secretary', 'IT Coordinator','Lens Man', 'Social Media Handler', 'Membership Handler'])
            new_performance_metrics = st.number_input("Performance Metrics (Stars) (1,2,3)", min_value=0, max_value=3, step=1)
            new_access_level = st.selectbox("Access Level", ["Treasurer", "Secretary", "President", "Vice President"])
            new_role_id = st.selectbox("Role Id",["1", "2"])
                
    if update_button and executive_username.strip():
        if exec_member_exists(executive_username):
            if not all([new_username, new_full_name, new_password, new_email_address, new_contact, new_active_status, new_position, new_performance_metrics, new_access_level, new_role_id]):
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
                if update_member_details(executive_username, new_details):
                    st.success('Updated Successfully')
                else:
                    st.error("Failed to update")
        else:
            st.error("Executive member not found. Please enter a valid username.")
            
def delete_executive_members_ui():
    conn = create_connection()
    email = None
    with st.form(key="search_form"):
        username = st.text_input("Search by username or email")
        col1,col2, col3 = st.columns([5, 2, 1])
        with col2:
            search_button = st.form_submit_button("Search")
        with col3:
            delete_button = st.form_submit_button("Delete")

    if search_button:
        search_results = search_executive_members( username)
        if search_results:
            st.write("Search Results:")
            display_member_table(search_results)
            # print(type(search_results))
            # print(search_results)
            email = search_results[0][4] if search_results else None
        else:
            st.write("No matching executive members found.")
    
    if delete_button:
        if username.strip() == "":
            st.error('Please enter valid username or email')
        else:
            delete = delete_member(username, email)
            if delete:
                st.success("Deleted Successfully")
            else:
                st.error("Failed to Delete")

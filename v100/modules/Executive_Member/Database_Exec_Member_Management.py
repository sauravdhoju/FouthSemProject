import streamlit as st

def create_member_table(db):
    '''Member Table Creation with columns'''
    columns = {
        "member_id": "INTEGER PRIMARY KEY",
        "username": "TEXT UNIQUE NOT NULL",
        "hashed_password": "TEXT NOT NULL",
        "full_name": "TEXT NOT NULL",
        "email": "TEXT UNIQUE",
        "phone": "INTEGER",
        "position": "TEXT NOT NULL",
        "account_balance": "REAL DEFAULT 0 CHECK (account_balance >= 0)",
        "joined_date": "DATE",
        "performance_metrics": "TEXT",
        "active_status": "BOOLEAN",
        "access_level": "TEXT NOT NULL",
        "account_creation": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
        "role_id": "TEXT NOT NULL"
    }

    db.create_table("Members", columns)
    
def add_executive_member(db, member_info):
    '''Add an executive member to the database.

    This function checks whether the username or email already exists in the database.
    If the username or email already exists, it prints a message and returns False.
    If the username or email does not exist, it adds the member to the 'Members' table in the database
    using the provided member_info dictionary.
    Upon successful addition, it prints a success message and returns True.

    Args:
        db (SQLiteDatabase): The SQLiteDatabase instance for interacting with the database.
        member_info (dict): A dictionary containing information about the executive member,
                            including 'username', 'email', and other details.

    Returns:
        bool: True if the member is successfully added, False otherwise.
    '''
    existing_user = db.fetch_if("Members", {"username": member_info.get("username")}) or db.fetch_if("Members", {"email": member_info.get("email")})

    if existing_user:
        print("Username or email already exists. Please choose different ones.")
        st.error("Try with different username or email.")
        return False

    db.create_record("Members", member_info)
    print("Executive member added successfully.")
    st.success("Executive Member added successfully.")
    return True

def display_member_table(members):
    member_data = []
    for member in members:
        phone = member["phone"] if member["phone"] else "N/A"
        member_info = {
            "Username": member["username"],
            "Full Name": member["full_name"],
            "Position": member["position"],
            "Email": member["email"],
            "Phone": phone,
            "Account Balance": member["account_balance"],
            "Joined Date": member["joined_date"],
            "Performance Metrics": member["performance_metrics"],
            "Active Status": "Active" if member["active_status"] else "Inactive",
            "Access Level": member["access_level"]
        }
        member_data.append(member_info)
    st.table(member_data)

def update_member_details(db, executive_username, new_details):
    try:
        if db.fetch_if("Members", {"username": executive_username}):
            db.update_record("Members", new_details, {"username": executive_username})
            return True
        else:
            return False
    except Exception as e:
        print(f"Error updating executive member details: {e}")
        return False

def delete_member(db, del_username):
    try:
        conditions = {"username": del_username}
        result = db.delete_record("Members", conditions)
        return result
    except Exception as e:
        print(f"Error deleting member: {e}")
        return False

# `#DEFAULT USER
# def insert_default_user():
#     # Hash default passwords
#     default_pass_hash = pbkdf2_sha256.hash('admin')
#     default_pass_hash_user = pbkdf2_sha256.hash('user')

#     # Check if default user already exists
#     with SQLiteDatabase("example.db") as db:
#         cursor = db.cursor
#         cursor.execute('''SELECT COUNT(*) FROM Members WHERE username = 'admin' AND email = 'admin@example.com' ''')
#         count = cursor.fetchone()[0]

#         if count == 0:
#             # Insert default users
#             record_data_admin = {
#                 "username": "admin",
#                 "hashed_password": default_pass_hash,
#                 "full_name": "Admin User",
#                 "email": "admin@example.com",
#                 "phone": 1234567890,
#                 "position": "Administrator",
#                 "account_balance": 0,
#                 "access_level": "superuser",
#                 "role_id": 1
#             }
#             db.create_record("Members", record_data_admin)

#             record_data_user = {
#                 "username": "user",
#                 "hashed_password": default_pass_hash_user,
#                 "full_name": "Admin User",
#                 "email": "admin@exmple.com",
#                 "phone": 1234567899,
#                 "position": "Administrator",
#                 "account_balance": 0,
#                 "access_level": "executiveuser",
#                 "role_id": 2
#             }
#             db.create_record("Members", record_data_user)

#             print("Super user inserted successfully.")

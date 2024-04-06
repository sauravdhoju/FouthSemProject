import streamlit as st
from modules.Executive_Member.Database_Exec_Member_Management import create_member_table
from modules.database import *
from passlib.hash import pbkdf2_sha256
from modules.Executive_Member.Database_Exec_Member_Management import add_executive_member

st.session_state['is_logged_in'] = False



def main():
    with SQLiteDatabase("accounting.db") as db:
        create_member_table(db)
        
        if not db.fetch_if("Members", {"username": "admin"}):
            default_pass_hash = pbkdf2_sha256.hash('admin')
            superuser_info = {
                "username": "admin",
                "hashed_password": default_pass_hash,
                "full_name": "Superuser",
                "email": "admin@example.com",
                "phone": 1234567890,
                "position": "Administrator",
                "account_balance": 0,
                "access_level": "superuser",
                "role_id": 1
            }
            add_executive_member(db, superuser_info)
    
    if st.session_state['is_logged_in']:
        st.switch_page("pages/homepage.py")
    else:
        st.switch_page("pages/Login_Page.py")
        

def debug_program():
    # Connect to the SQLite database
    with SQLiteDatabase("debug.db") as db:
        # Create a 'Members' table
        db.create_table("Members", {
            "id": "INTEGER PRIMARY KEY",
            "username": "TEXT",
            "email": "TEXT"
        })

        # Insert records into the 'Members' table
        # db.create_record("Members", {"username": "user1", "email": "user1@example.com"})
        # db.create_record("Members", {"username": "user2", "email": "user2@example.com"})

        # # Fetch and display all records from the 'Members' table
        # print("Records in 'Members' table:")
        # print(db.fetch_records("Members"))

        # # Update a record in the 'Members' table
        # db.update_record("Members", {"username": "updated_user"}, {"id": 1})

        # # Fetch and display all records from the 'Members' table after update
        # print("Records in 'Members' table after update:")
        # print(db.fetch_records("Members"))

        # Delete a record from the 'Members' table
        db.delete_record("Members", {"id": 2})

        # # Fetch and display all records from the 'Members' table after delete
        # print("Records in 'Members' table after delete:")
        # print(db.fetch_records("Members"))


if __name__ == "__main__":
    # debug_program()
    main()
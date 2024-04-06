import streamlit as st
from modules.Executive_Member.Database_Exec_Member_Management import create_member_table
from modules.Club_Expenses.Database_Club_Expenses import create_club_expense_table
from modules.database import *
from passlib.hash import pbkdf2_sha256
from modules.Executive_Member.Database_Exec_Member_Management import add_executive_member

st.session_state['is_logged_in'] = False

def main():
    with SQLiteDatabase("accounting.db") as db:
        create_member_table(db)
        create_club_expense_table(db)
        
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
        
if __name__ == "__main__":
    main()
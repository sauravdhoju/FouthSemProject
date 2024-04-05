import streamlit as st
from modules.Create_Connection.Create_Connection import create_connection
from modules.Executive_Member.Database_Exec_Member_Management import create_member_table
from modules.Club_Expenses.Database_Club_Expenses import create_club_expense_table
# from modules.database import create_connection, create_tables

st.session_state['is_logged_in'] = False
def main():
    create_member_table()
    create_club_expense_table()
    
    
    if st.session_state['is_logged_in']:
        st.switch_page("pages/homepage.py")
    else:
        st.switch_page("pages/Login_Page.py")
        
if __name__ == "__main__":
    main()
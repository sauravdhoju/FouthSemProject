import streamlit as st
from modules.Create_Connection import create_connection
from modules.Database_Member_Management import create_member_table
# from modules.database import create_connection, create_tables

st.session_state['is_logged_in'] = False
def main():
    conn = create_connection()
    cursor = conn.cursor()
    create_member_table(conn)
    
    if st.session_state['is_logged_in']:
        st.switch_page("pages/homepage.py")
    else:
        st.switch_page("pages/Login_Page.py")
        
if __name__ == "__main__":
    main()
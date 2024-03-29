import streamlit as st
from modules.database import create_connection, create_tables

st.session_state['is_logged_in'] = False
def main():
    conn = create_connection()
    cursor = conn.cursor()
    create_tables(conn)
    
    if st.session_state['is_logged_in']:
        st.switch_page("pages/homepage.py")
    else:
        st.switch_page("pages/login.py")
        
if __name__ == "__main__":
    main()
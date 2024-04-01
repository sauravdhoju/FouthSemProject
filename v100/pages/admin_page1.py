import streamlit as st
from pages.Login_Page import main as login
from modules.database import create_connection
from modules.executives import add_executive_members_ui, display_executive_members_ui, delete_executive_members_ui

# st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

conn =create_connection()
def display_dashboard(conn):
    # Initialize session state for buttons if not already present
    if 'executives_clicked' not in st.session_state:
        st.session_state.executives_clicked = False
    if 'dashboard_clicked' not in st.session_state:
        st.session_state.dashboard_clicked = False
    if 'club_expenses_clicked' not in st.session_state:
        st.session_state.club_expenses_clicked = False
    if 'bank_transactions_clicked' not in st.session_state:
        st.session_state.bank_transactions_clicked = False

    col1, col2 = st.columns([1,6])
    with col1:
        st.markdown("### Navigation Panel")
        dashboard_clicked = st.button("Dashboard")
        executives_clicked = st.button("Executives") 
        club_expenses_clicked = st.button("Club Expenses")
        bank_transactions_clicked = st.button("Bank Transaction")
        logout_clicked = st.button("Logout")

        # Debugging print statements
        print("Dashboard Clicked:", dashboard_clicked)
        print("Executives Clicked:", executives_clicked)
        print("Club Expenses Clicked:", club_expenses_clicked)
        print("Bank Transaction Clicked:", bank_transactions_clicked)
        print("Logout Clicked:", logout_clicked)
        print("Session State:", st.session_state)

    with col2:
        if dashboard_clicked:
            st.session_state.dashboard_clicked = True
            print("Displaying Dashboard")
            # Display dashboard content here
            
            
        elif executives_clicked:
            st.session_state.executives_clicked = True
            print("Displaying Executives")
            sub_option = st.selectbox("Suboption", ["Add", "Display", "Remove"])
            # st.session_state.sub_option = sub_option
            print("Selected Suboption:", sub_option)
            if sub_option == "Add":
                add_executive_members_ui(conn)
            elif sub_option == "Display":
                display_executive_members_ui(conn)
            elif sub_option == "Remove":
                delete_executive_members_ui(conn)
            # st.session_state.executives_clicked = False  # Reset executives_clicked after handling sub-option
        elif club_expenses_clicked:
            pass
        elif bank_transactions_clicked:
            pass
        elif logout_clicked:
            st.session_state.clear()  # Clear session state to logout
            login()
            st.rerun()

def main():
    conn = create_connection()
    # Check if user is logged in
    if 'username' in st.session_state:
        st.markdown(f"# Welcome, {st.session_state['username']}")
        display_dashboard(conn)
    else:
        st.warning("Login to access homepage")
        login()

if __name__ == "__main__":
    main()

# pages/admin_page.py

import streamlit as st
from streamlit_option_menu import option_menu
from pages.Login_Page import main as login
from modules.Dashboard.dashboard import main as dashboard

def main():
    col1_nav_panel, col2_dashboard_pan= st.columns([1,5])
    with col1_nav_panel:
        st.image("background.png", output_format="auto")
        selected_option = option_menu(
            menu_title=None,  # Title of the menu
            options=["Dashboard", "Executives", "Club Expenses", "Membership Management", "Bank Transaction","View Profile", "Logout"], 
            icons=["house", "people-fill", "wallet2", "wallet2", "bank2","people", "power"], 
            menu_icon="th-large",  
            default_index=0, 
            orientation="vertical",  # Orientation of the menu (vertical or horizontal)
            styles={
                "container": {"padding": "0!important", "background-color": "#cef6ff"},
                "icon": {"color": "green", "font-size": "20px"},  # Customize icon appearance
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "grey"},
            },
        )
        
    with col2_dashboard_pan:
        st.markdown(
            """
            <div style="text-align:center">
                <h1>Account Management System</h1>
                <h3>Trojan Club of Robotics-TCR</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        if selected_option == "Dashboard":      
            dashboard()
        elif selected_option == "Executives":
            st.switch_page("pages/Admin_Executive_Management.py")
        elif selected_option == "Club Expenses":
            st.switch_page("pages/Admin_Club_Expenses.py")
        if selected_option == "Membership Management":
            st.switch_page('pages/Admin_Membership_Management.py')
        elif selected_option == "Bank Transaction":
            st.switch_page("pages/Admin_Bank_Transaction.py")
        elif selected_option == "View Profile":
            st.switch_page("pages/Profile.py")
        elif selected_option == "Logout":
            st.session_state.clear()
            st.rerun()
    
if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        # login()
        st.switch_page("pages/Login_Page.py")
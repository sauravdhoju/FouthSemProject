# pages/admin_page.py

import streamlit as st
from streamlit_option_menu import option_menu
from pages.Login_Page import main as login

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
def main():
    col1_nav_panel, col2_dashboard_pan= st.columns([1,5])
    with col1_nav_panel:
        st.image("background.png", output_format="auto")
        selected_option = option_menu(
            menu_title=None,  # Title of the menu
            options=["Dashboard", "Executives", "Club Expenses", "Bank Transaction", "Logout"], 
            icons=["house", "people-fill", "wallet2", "bank2", "power"], 
            menu_icon="th-large",  
            default_index=0, 
            orientation="vertical",  # Orientation of the menu (vertical or horizontal)
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
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
        if selected_option == "Dashboard":
            pass
        if selected_option == "Executives":
            st.switch_page("pages/0202_Executive_Management.py")
        if selected_option == "Club Expenses":
            st.switch_page("pages/Admin_Club_Expenses.py")
        if selected_option == "Bank Transaction":
            st.switch_page("pages/Admin_Bank_Transaction.py")
        if selected_option == "Logout":
            st.session_state.clear()
            st.rerun()
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
        with st.container():
            pass
    
if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        # login()
        st.switch_page("pages/Login_Page.py")
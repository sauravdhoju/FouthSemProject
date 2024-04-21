import streamlit as st
from streamlit_option_menu import option_menu
from pages.Login_Page import main as login
from modules.Bank_Transaction.CRUD_Bank_Transaction import *

def main():
    col1_exe_nav_panel,col2_exe_dashboard = st.columns([1,5])
    with col1_exe_nav_panel:
        st.image("background.png", output_format="auto")
        selected_option = option_menu(
            menu_title=None,  
            options=["Add Transaction", "View Transaction", "Edit Transaction","Remove Transaction", "Return"],
            icons=["plus-circle", "eye", "cloud-upload", "person-x-fill","arrow-return-left"],
            orientation="vertical",
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
    with col2_exe_dashboard:
        st.markdown(
            """
            <div style="text-align:center">
                <h1>Account Management System</h1>
                <h3>Trojan Club of Robotics-TCR</h3>
                <h4>Bank Transaction</h4
            </div>
            """,
            unsafe_allow_html=True
        )
        if  selected_option == 'Add Transaction':
            insert_transaction_ui()
        elif selected_option == 'View Transaction':
            view_transaction_ui()
        elif selected_option == 'Edit Transaction':
            update_transaction_ui()
        elif selected_option == 'Remove Transaction':
            remove_transaction_ui()
        elif selected_option == 'Return':
            st.switch_page('pages/Admin_Admin_Panel.py')
        
if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        login()
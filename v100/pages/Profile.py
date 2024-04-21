# pages/admin_page.py

import streamlit as st
from streamlit_option_menu import option_menu
from pages.Login_Page import main as login

from modules.Executive_Member.CRUD_Admin_Exec_Member_UI import view_user_details_ui


def main():
    col1_nav_panel, col2_dashboard_pan= st.columns([1,5])
    with col1_nav_panel:
        st.image("background.png", output_format="auto")
        selected_option = option_menu(
            menu_title=None,  # Title of the menu
            options=["My Profile", "Return"], 
            icons=["people", "power"], 
            menu_icon="th-large",  
            default_index=0, 
            orientation="vertical", 
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "green", "font-size": "20px"}, 
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
                <h4>My Profile</h4
            </div>
            """,
            unsafe_allow_html=True
        )
        if selected_option == "My Profile":
            view_user_details_ui()
        elif selected_option == "Return":
            st.switch_page('pages/Admin_Admin_Panel.py')
    
if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        # login()
        st.switch_page("pages/Login_Page.py")
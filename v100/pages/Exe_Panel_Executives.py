import streamlit as st
from streamlit_option_menu import option_menu
from pages.Login_Page import main as login
from modules.CRUD_Admin_Exec_Member_UI import add_executive_members_ui, display_executive_members_ui, delete_executive_members_ui, update_executive_members_ui
from modules.database import create_connection
conn = create_connection()
def main():
    col1_exe_nav_panel,col2_exe_dashboard = st.columns([1,5])
    with col1_exe_nav_panel:
        st.image("background.png", output_format="auto")
        selected_option = option_menu(
            menu_title=None,  
            options=["View Executive Member", "Return"],
            icons=["eye","arrow-return-left"],
            orientation="vertical",
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
    with col2_exe_dashboard:
        st.markdown(
            """
            <div style="text-align:center">
                <h1>Account Management System</h1>
                <h3>Trojan Club of Robotics-TCR</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        if selected_option == 'View Executive Member':
            display_executive_members_ui(conn)
        elif selected_option == 'Return':
            st.switch_page('pages/0301_Executive_Panel.py')
        
if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        login()

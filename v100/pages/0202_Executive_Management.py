import streamlit as st
from streamlit_option_menu import option_menu
from pages.Login_Page import main as login
from modules.executives import add_executive_members_ui, display_executive_members_ui, delete_executive_members_ui, update_executive_members_ui
from modules.database import create_connection
conn = create_connection()
def main():
    col1_exe_nav_panel,col2_exe_dashboard = st.columns([1,5])
    with col1_exe_nav_panel:
        st.image("background.png", output_format="auto")
        selected_option = option_menu(
            menu_title=None,  
            options=["Add Executive Member", "View Executive Member", "Updata Executive Member","Remove Executive Member", "Return"],
            icons=["plus-circle", "eye", "cloud-upload", "person-x-fill","arrow-return-left"],
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
        if  selected_option == 'Add Executive Member':
            add_executive_members_ui(conn)
        elif selected_option == 'View Executive Member':
            display_executive_members_ui(conn)
        elif selected_option == 'Update Executive Member':
            update_executive_members_ui(conn)
        elif selected_option == 'Remove Executive Member':
            delete_executive_members_ui(conn)
        elif selected_option == 'Return':
            st.switch_page('pages/0201_Admin_Panel.py')
        
if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        login()

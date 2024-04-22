import streamlit as st
from streamlit_option_menu import option_menu
from pages.Login_Page import main as login
from modules.Executive_Member.CRUD_Admin_Exec_Member_UI import add_executive_members_ui, display_executive_members_ui, delete_executive_members_ui, update_executive_members_ui
from modules.Permission.hasPermission import *

def optionsByRole(options_dict, on):
    opt = []
    for option in options_dict:
            if has_permission(st.session_state['username'], options_dict[option], "executives"):
                opt.append(option)
            # print(option, options_dict[option], has_permission(st.session_state['username'], options_dict[option], "executives"))
    opt.append("Return")
    return opt
def main():
    col1_exe_nav_panel,col2_exe_dashboard = st.columns([1,5])
    with col1_exe_nav_panel:
        st.image("background.png", output_format="auto")
        options_dict = {"Add Executive Member" : "add", 
                   "View Executive Member": "view", 
                   "Update Executive Member": "edit",
                   "Remove Executive Member": "delete"
                }
        selected_option = option_menu(
            menu_title=None,  
            icons=["plus-circle", "eye", "cloud-upload", "person-x-fill","arrow-return-left"],
            orientation="vertical",
            # options=["Add Executive Member", "View Executive Member", "Update Executive Member","Remove Executive Member", "Return"],    
            options=optionsByRole(options_dict, "executives"),       
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
                <h4>Executives</h4>
            </div>
            """,
            unsafe_allow_html=True
        )
        if  selected_option == 'Add Executive Member':
            add_executive_members_ui()
        elif selected_option == 'View Executive Member':
            display_executive_members_ui()
        elif selected_option == 'Update Executive Member':
            update_executive_members_ui()
        elif selected_option == 'Remove Executive Member':
            delete_executive_members_ui()
        elif selected_option == 'Return':
            st.switch_page('pages/Admin_Admin_Panel.py')
        
if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        login()

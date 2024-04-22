import streamlit as st
from pages.login import main as login
from modules.Executive_Member.CRUD_Admin_Exec_Member_UI import add_executive_members_ui, display_executive_members_ui, delete_executive_members_ui, update_executive_members_ui
from modules.PickMeIfYouLike.options import *

def main():
    dashboardOption(
        options_dict = {"Add Executive Member" :    ["add",                 add_executive_members_ui                ,"plus-circle"], 
                        "View Executive Member":    ["view",                display_executive_members_ui            ,"eye"], 
                        "Update Executive Member":  ["edit",                update_executive_members_ui             ,"cloud-upload"],           
                        "Remove Executive Member":  ["delete",              delete_executive_members_ui             ,"person-x-fill"],
                        "Return":                   ["return",      lambda: st.switch_page("pages/dashboard.py")    ,"arrow-return-left"],
                    }
    )

if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        st.switch_page('pages/login.py')

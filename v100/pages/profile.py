import streamlit as st
from modules.Executive_Member.CRUD_Admin_Exec_Member_UI import view_user_details_ui
from modules.PickMeIfYouLike.options import *

def main():
    dashboardOption(
        options_dict = {"My Profile" : ["view",                view_user_details_ui                     ,"people"], 
                        "Return":      ["return",      lambda: st.switch_page("pages/dashboard.py")     ,"arrow-return-left"],
                    }, functionality="profile"
    )

if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        st.switch_page('pages/login.py')

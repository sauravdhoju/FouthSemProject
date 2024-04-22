import streamlit as st
from streamlit_option_menu import option_menu
from pages.login import main as login
from modules.Member_Management.History.Admin_view_History import view_payment_history_ui
from modules.PickMeIfYouLike.options import *

def main():
    dashboardOption(
        options_dict = {"History" :    ["view",                view_payment_history_ui                              ,"clock-history"], 
                        "Return":      ["return",      lambda: st.switch_page("pages/membership_management.py")     ,"arrow-return-left"],
                    }, functionality="view_history_payment"
    )

if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        st.switch_page('pages/login.py')
        
        
  
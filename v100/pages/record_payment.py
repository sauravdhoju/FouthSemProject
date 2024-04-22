import streamlit as st
from modules.Member_Management.Record.CRUD_Member_Management_UI import *
from modules.PickMeIfYouLike.options import *

def main():
    dashboardOption(
        options_dict = {"Add Payment" :    ["add",                 create_payment_ui                ,"plus-circle"], 
                        "View Payment":    ["view",                search_payment_by_username_ui            ,"eye"], 
                        "Update Payment":  ["edit",                update_payment_ui             ,"cloud-upload"],           
                        "Remove Payment":  ["delete",              delete_payment_ui             ,"person-x-fill"],
                        "Return":          ["return",      lambda: st.switch_page("pages/membership_management.py")    ,"arrow-return-left"],
                    }
    )

if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        st.switch_page('pages/login.py')
        
        
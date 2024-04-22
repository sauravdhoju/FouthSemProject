import streamlit as st
from modules.Bank_Transaction.CRUD_Bank_Transaction import *
from modules.PickMeIfYouLike.options import *

def main():
    dashboardOption(
        options_dict = {"Add Transaction" :    ["add",                 insert_transaction_ui                        ,"plus-circle"], 
                        "View Transaction":    ["view",                view_transaction_ui                          ,"eye"], 
                        "Update Transaction":  ["edit",                update_transaction_ui                        ,"cloud-upload"],           
                        "Remove Transaction":  ["delete",              remove_transaction_ui                        ,"person-x-fill"],
                        "Return":              ["return",      lambda: st.switch_page("pages/dashboard.py")         ,"arrow-return-left"],
                    }
    )

if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        st.switch_page('pages/login.py')
        
        
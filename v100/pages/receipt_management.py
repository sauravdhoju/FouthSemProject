import streamlit as st
from modules.Club_Expenses.Receipt.receipt import add_receipt_ui, view_receipts_ui, search_receipt_ui, update_receipt_ui, remove_receipt_ui
from modules.PickMeIfYouLike.options import *
   
def main():
    dashboardOption(
        options_dict = {"Add Receipt" :    ["add",                 add_receipt_ui                               ,"plus-circle"], 
                        "Search Receipt":  ["search",              search_receipt_ui                            ,"search"], 
                        "View Receipt":    ["view",                view_receipts_ui                             ,"eye"], 
                        "Update Receipt":  ["edit",                update_receipt_ui                            ,"cloud-upload"],           
                        "Remove Receipt":  ["delete",              remove_receipt_ui                            ,"person-x-fill"],
                        "Return":          ["return",      lambda: st.switch_page("pages/club_expenses.py")     ,"arrow-return-left"],
                    }, functionality="receipt_management"
    )

if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        st.switch_page('pages/login.py')


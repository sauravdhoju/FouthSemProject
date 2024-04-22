import streamlit as st
from modules.Member_Management.Generate_Reports.Generate_reports import generate_membership_report, generate_payment_report

from modules.PickMeIfYouLike.options import *
def func1():
    pass
def main():
    dashboardOption(
        options_dict = {"Generate Report on" :    ["add",         lambda: func1()                                             ,"home"], 
                        "Membership Report":      ["view",                generate_membership_report                          ,"person-down"], 
                        "Payment Report":         ["edit",                generate_payment_report                             ,"currency-dollar"],           
                        # "Expense Report":       ["delete",              delete_executive_members_ui                         ,"receipt"],
                        "Return":                 ["return",      lambda: st.switch_page("pages/membership_management.py")    ,"arrow-return-left"],
                    }, functionality="generate_report"
    )

if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        st.switch_page('pages/login.py')


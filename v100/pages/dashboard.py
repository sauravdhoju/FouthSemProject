import streamlit as st
from streamlit_option_menu import option_menu
from pages.login import main as login
from modules.Club_Expenses.Expense_Category.CRUD_Admin_Exec_Club_Expense_Category_UI import add_expense_category_ui
from modules.PickMeIfYouLike.options import *
from modules.Dashboard.dashboard import main as dashboard

def func1():
    pass
def main():
    print("it is dashbapord")
    dashboardOption(
        options_dict = {"Dashboard" : ["",                       dashboard                                                ,"house"], 
                        "Executives": ["",              lambda:  st.switch_page('pages/executives.py')                      ,"people-fill"], 
                        "Club Expenses": ["",           lambda:  st.switch_page('pages/club_expenses.py')             ,"wallet2"],   
                        "Membership Management": ["",   lambda:  st.switch_page('pages/membership_management.py')     ,"wallet2"],  
                        "Bank Transaction": ["",        lambda:  st.switch_page('pages/bank_transaction.py')          ,"bank2"],  
                        "View Profile": ["",            lambda:  st.switch_page('pages/profile.py')                         ,"people"],   
                        "Logout":["",                   lambda:  (st.session_state.clear(), st.rerun())                     ,"power"],
                        }
        )
    
if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        st.switch_page("pages/login.py")
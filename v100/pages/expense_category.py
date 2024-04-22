import streamlit as st
from modules.Club_Expenses.Expense_Category.CRUD_Admin_Exec_Club_Expense_Category_UI import *
from modules.PickMeIfYouLike.options import *

def main():
    dashboardOption(
        options_dict = {"Add    Categories" :    ["add",                 add_expense_category_ui                    ,"plus-circle"], 
                        "View   Categories":     ["view",                view_expense_category_ui                   ,"eye"], 
                        "Update Categories":     ["edit",                update_expense_category_ui                 ,"cloud-upload"],           
                        "Remove Categories":     ["delete",              remove_expense_category_ui                 ,"person-x-fill"],
                        "Return":                ["return",      lambda: st.switch_page("pages/club_expenses.py")   ,"arrow-return-left"],
                    }
    )

if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        st.switch_page('pages/login.py')



import streamlit as st
from modules.PickMeIfYouLike.options import *

def func1():
    pass
def main():
    dashboardOption(
        options_dict = {"Expense Tracking" :    ["",        lambda:  func1()                                                ,"bar-chart-fill"   ], 
                    "Receipt Management":       ["",        lambda:  st.switch_page('pages/receipt_management.py')          ,"receipt"          ], 
                    # "Training and Education": ["",        lambda:  st.switch_page('pages/Admin_Training_Education.py')    ,"tag-fill"         ],   
                    "Expense Categories":       ["",        lambda:  st.switch_page('pages/expense_category.py')            ,"cloud-upload"     ],   
                    "Return":                   ["return",  lambda:  st.switch_page("pages/dashboard.py")                   ,"arrow-return-left"],
                    }
    )

if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        st.switch_page('pages/login.py')



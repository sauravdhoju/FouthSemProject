import streamlit as st
from modules.PickMeIfYouLike.options import *

def func1():
    pass
def main():
    dashboardOption(
        options_dict = {"Club" :                ["",        lambda:  func1()                                                ,"bar-chart-fill"   ], 
                        "Record Payments":      ["",        lambda:  st.switch_page('pages/record_payment.py')              ,"receipt"          ], 
                        "View History":         ["",        lambda:  st.switch_page('pages/view_history_payment.py')        ,"tag-fill"         ],   
                        "Generate Reports":     ["",        lambda:  st.switch_page('pages/generate_report.py')             ,"cloud-upload"     ],   
                        # "Send Reminder":      ["",        lambda:  st.switch_page('pages/Admin_Training_Education.py')    ,"tag-fill"         ],   
                        # "Fee Status Tracking":["",        lambda:  st.switch_page('pages/Admin_Training_Education.py')    ,"tag-fill"         ],   
                        # "Manage Renewals":    ["",        lambda:  st.switch_page('pages/Admin_Training_Education.py')    ,"tag-fill"         ],   
                        # "Update Information": ["",        lambda:  st.switch_page('pages/Admin_Training_Education.py')    ,"tag-fill"         ],   
                        "Return":               ["return",  lambda:  st.switch_page("pages/dashboard.py")                   ,"arrow-return-left"], 
                    }
    )

if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        st.switch_page('pages/login.py')

import streamlit as st
from modules.PickMeIfYouLike.options import *

def func1():
    pass
def main():
    dashboardOption(
        options_dict = {"Permission" :    ["",        lambda:  func1()                                                ,"bar-chart-fill"   ],  
                        "Return"     :    ["return",  lambda:  st.switch_page("pages/dashboard.py")                   ,"arrow-return-left"],
                        }, functionality="permission"
    )

if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        st.switch_page('pages/login.py')



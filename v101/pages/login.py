import streamlit as st
from modules.login_auth import authenticate_user

# st.set_page_config(page_title="Login Page", layout="centered", initial_sidebar_state="collapsed")
st.session_state['is_logged_in'] = False


def main():
    st.header("Account Management System")
    st.subheader("Trojan Club of Robotics")
    
    with st.form("login_form", border=True):
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Login"):
            if authenticate_user(username, password):
                st.success("GOOOOOOOOOOOO")
                st.session_state['is_logged_in'] = True
                st.session_state['username'] = username
                st.switch_page("pages/homepage.py")
            else:
                st.error("Invalid username or password")
                
                
if __name__ == "__main__":
    if st.session_state['is_logged_in']:
            st.switch_page("pages/homepage.py")
    else:
        main()
    
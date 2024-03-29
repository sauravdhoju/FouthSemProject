import streamlit as st
from modules.authenticate import authenticate_user
st.session_state['is_logged_in'] = False

def main():
    with st.form("login_form", border=True):
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type= "password")
        if st.form_submit_button("Login"):
            auth_result =authenticate_user(username, password)
            if auth_result is not None and auth_result[0] :
                role_id = int(auth_result[1])
                print(auth_result, role_id)
                if role_id == 1:
                    st.session_state['is_logged_in'] =True
                    st.session_state['username'] = username
                    # print(st.session_state['username'])
                    st.session_state['role_id'] = role_id
                    print(f"Logged in as SuperUser -- {role_id}")
                    st.switch_page("pages/admin_page.py")
                elif role_id == 2:
                    st.session_state['is_logged_in'] =True
                    st.session_state['username'] = username
                    st.session_state['role_id'] = role_id
                    print(f"Logged in as Executive User -- {role_id}")
                    st.switch_page("pages/executive_page.py")
            else:
                print("Try again")
                st.error("Invalid username or password")

if __name__ =="__main__":
    if st.session_state['is_logged_in']:
        st.switch_page("pages/homepage.py")
    else:
        main()
            
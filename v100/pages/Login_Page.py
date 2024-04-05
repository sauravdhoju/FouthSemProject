import streamlit as st
from modules.Authenticator.Login_Authenticate import authenticate_user

st.set_page_config( layout="wide", initial_sidebar_state = "collapsed")
st.session_state['is_logged_in'] = False
def main():
    col1, col2,col3 = st.columns([1,2,1])  
    with col1:
        pass
    with col2:
        st.markdown(
            """
            <div style="text-align:center">
                <h1>Account Management System</h1>
                <h3>Trojan Club of Robotics-TCR</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        with st.form("login_form", border=True):
            st.subheader("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Login", type="secondary"):
                auth_result = authenticate_user(username, password)
                if auth_result is not None and auth_result[0]:
                    role_id = int(auth_result[1])
                    if role_id == 1:
                        st.session_state['is_logged_in'] = True
                        st.session_state['username'] = username
                        st.session_state['role_id'] = role_id
                        st.success("Logged in as SuperUser")
                        st.switch_page("pages/Admin_Admin_Panel.py")
                    elif role_id == 2:
                        st.session_state['is_logged_in'] = True
                        st.session_state['username'] = username
                        st.session_state['role_id'] = role_id
                        st.success("Logged in as Executive User")
                        st.switch_page("pages/Exe_Executive_Panel.py")
                else:
                    # st.toast("Invalid Usernamr or Pasword")
                    st.error("Invalid username or password")
        # print("Login - Session State:", st.session_state)  # Debug: Print session state
    with col3:
        pass

if __name__ =="__main__":
    if st.session_state['is_logged_in']:
        st.switch_page("pages/homepage.py")
    else:
        main()
            
import streamlit as st

st.session_state['is_logged_in'] = False

def main():
    if st.session_state['is_logged_in']:
            st.switch_page("pages/homepage.py")
    else:
        st.switch_page("pages/login.py")
        
        
if __name__ == "__main__":
    main()
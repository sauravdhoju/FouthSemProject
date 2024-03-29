# pages/admin_page.py

import streamlit as st
from pages.login import main as login

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
def main():
    st.markdown(f"# Welcome, {st.session_state['username']}")
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown("### Navigation Panel")
        dashboard =st.button("Dashboard")
        executives = st.button("Executives")
        club_expenses = st.button("Club Expenses")
        bank_transactions = st.button("Bank Transaction")
        logout = st.button("Logout")
        
        if dashboard:
            pass
        elif executives:
            pass
        elif club_expenses:
            pass
        elif bank_transactions:
            pass
        elif logout:
            pass
        
    with col2:
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.container(border= True):
                st.markdown("### Total balance ")
    
if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access homepage")
        login()
import streamlit as st
from pages.login import main as login
import pandas as pd
import numpy as np
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
'''
def main():
    st.header("Account Management System")
    st.subheader("Trojan Club of Robotics - TCR")
    st.markdown("# :orange[Dashboard]")
    st.markdown(f":green[Welcome], {st.session_state['username']}")
    
    col1, col2 = st.columns([1,4])
    with col1: 
        st.markdown("## :hammer_and_wrench: Navigation Panel")

        # Main options as buttons with icons
        selected_option = st.button(":house_with_garden: Homepage")
        if selected_option:
            st.session_state.selected_option = "Homepage"

        selected_option = st.button(":moneybag: Financial Management")
        if selected_option:
            st.session_state.selected_option = "Financial Management"

        # If "Financial Management" is selected, show suboptions
        if st.session_state.get("selected_option") == "Financial Management":
            sub_option = st.button("")


    with col2:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            with st.container(border=True):
                st.markdown("### Total Balance")
                st.markdown("## :blue[Rs.9999]")
                # st.markdown("---")
                st.metric(label="Last month: Rs. 99999", value=("2.37 %"), delta="+2.37")

        with col2:
            with st.container(border=True):
                st.markdown("### Total Period Change")
                st.markdown("## :blue[Rs.9999]")
                # st.markdown("---")
                st.metric(label="Last month: Rs. 99999", value=("2.37 %"), delta="-2.37")
            
        with col3:
            with st.container(border=True):
                st.markdown("### Total Expenses")
                st.markdown("## :blue[Rs.9999]")
                # st.markdown("---")
                st.metric(label="Last month: Rs. 99999", value=("2.37 %"), delta="+2.37")

        with col4:
            with st.container(border=True):
                st.markdown("### Total Period Change")
                st.markdown("## :blue[Rs.9999]")
                # st.markdown("---")
                st.metric(label="Last month: Rs. 99999", value=("2.37 %"), delta="-2.37")
        
        st.subheader("Balance Trends")
        chart_data = pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
        )
        
        st.area_chart(chart_data, x="col1", y="col2", color="col3")


if __name__ == "__main__":
    if 'is_logged_in' in st.session_state:
        main()
    else:
        st.warning("Log in to access homepage")
        login()'''
    
def main():
    st.header("Account Management System")
    st.subheader("Trojan Club of Robotics - TCR")
    st.markdown("# :orange[Dashboard]")
    st.markdown(f":green[Welcome], {st.session_state['username']}")
    
    col1, col2 = st.columns([1,4])
    with col1: 
        st.page_link("main.py", label="Home", icon="🏠")
        st.page_link("pages/homepage.py", label="Homepage", icon="1️⃣")
        st.page_link("pages/login.py", label="Login", icon="2️⃣", disabled=False)
        st.page_link("http://www.google.com", label="Google", icon="🌎")


    with col2:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            with st.container(border=True):
                st.markdown("### Total Balance")
                st.markdown("## :blue[Rs.9999]")
                # st.markdown("---")
                st.metric(label="Last month: Rs. 99999", value=("2.37 %"), delta="+2.37")

        with col2:
            with st.container(border=True):
                st.markdown("### Total Period Change")
                st.markdown("## :blue[Rs.9999]")
                # st.markdown("---")
                st.metric(label="Last month: Rs. 99999", value=("2.37 %"), delta="-2.37")
            
        with col3:
            with st.container(border=True):
                st.markdown("### Total Expenses")
                st.markdown("## :blue[Rs.9999]")
                # st.markdown("---")
                st.metric(label="Last month: Rs. 99999", value=("2.37 %"), delta="+2.37")

        with col4:
            with st.container(border=True):
                st.markdown("### Total Period Change")
                st.markdown("## :blue[Rs.9999]")
                # st.markdown("---")
                st.metric(label="Last month: Rs. 99999", value=("2.37 %"), delta="-2.37")
        
        st.subheader("Balance Trends")
        chart_data = pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
        )
        
        st.area_chart(chart_data, x="col1", y="col2", color="col3")


if __name__ == "__main__":
    if 'is_logged_in' in st.session_state:
        main()
    else:
        st.warning("Log in to access homepage")
        login()

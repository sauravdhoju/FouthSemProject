# pages/admin_page.py

import streamlit as st
from streamlit_option_menu import option_menu
from pages.Login_Page import main as login

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
def main():
    col1_nav_panel, col2_dashboard_pan= st.columns([1,5])
    with col1_nav_panel:
        st.image("background.png", output_format="auto")
        selected_option = option_menu(
            menu_title=None,  # Title of the menu
            options=["Dashboard", "Executives", "Club Expenses", "Bank Transaction", "Logout"], 
            icons=["house", "people-fill", "wallet2", "bank2", "power"], 
            menu_icon="th-large",  
            default_index=0, 
            orientation="vertical",  # Orientation of the menu (vertical or horizontal)
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "green", "font-size": "20px"},  # Customize icon appearance
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "grey"},
            },
        )
        
        if selected_option == "Executives":
            st.switch_page("pages/0202_Executive_Management.py")
    with col2_dashboard_pan:
        container = st.container()
        container.markdown(
            """
            <style>
            .containerStyle {
                padding: 20px;
                border: 2px solid #ccc;
                border-radius: 5px;
                background-color: #ffffff;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        with container:
            st.markdown(f"# Welcome, {st.session_state['username']}")
            st.selectbox("Navigation Paanel", options = ["Dashboard", "Executives", "Club Expenses", "Bank Transactions"])
    
if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        login()
from streamlit_option_menu import option_menu
import streamlit as st  

def generate_option_menu(options):
    st.image("background.png")
    selected_option = option_menu(
        menu_title=None,
        options=list(options.keys()),
        icons=["home", "credit-card", "clock-history", "file-text", "bell", "clipboard-data", "gear-wide-connected", "person-gear", "arrow-return-left"],
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "green", "font-size": "20px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "grey"},
        },
    )
    return selected_option, options[selected_option]

def display_dashboard():
    st.markdown(
        """
        <div style="text-align:center">
            <h1>Account Management System</h1>
            <h3>Trojan Club of Robotics-TCR</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
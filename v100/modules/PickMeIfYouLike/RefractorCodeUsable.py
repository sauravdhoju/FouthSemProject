from streamlit_option_menu import option_menu
import streamlit as st  

def option_menu(menu_title, options, icons, selected_option):
    with st.container():
        st.title(menu_title)
        for option, icon in zip(options, icons):
            st.write(f"{icon} {option}")
        st.write(f"Selected Option: {selected_option}")


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
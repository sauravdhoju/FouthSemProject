import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
def main():
    col1_exec_option_panel, col2_exec_dashboard = st.columns([1,5])

    with col1_exec_option_panel:
        st.image("background.png", output_format="auto")
        selected_option = option_menu(
            menu_title=None,  # Title of the menu
            options=["Dashboard", "Executives", "Club Expenses", "Bank Transaction", "My Profile", "Logout"], 
            icons=["house", "people-fill", "wallet2", "bank2", "people" , "power"], 
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
    
    if selected_option == "Dashboard":
        pass
    elif selected_option == "Executives":
        st.switch_page('pages/Exe_Panel_Executives.py')
        pass
    elif selected_option == "Club Expenses":
        pass
    elif selected_option == "Bank Trasactions":
        pass
    elif selected_option == "My Profile":
        pass
    elif selected_option == "Logout":
        st.switch_page('pages/Login_Page.py')
    with col2_exec_dashboard:
        st.markdown(
            """
            <div style="text-align:center">
                <h1>Account Management System</h1>
                <h3>Trojan Club of Robotics-TCR</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        
if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        # login()
        st.switch_page("pages/Login_Page.py")

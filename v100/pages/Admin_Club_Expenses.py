import streamlit as st
from streamlit_option_menu import option_menu
from pages.Login_Page import main as login
def main():
    col1_Club_Expenses_Panel, col2_Club_Expenses_Dashboard = st.columns([1,5])
    with  col1_Club_Expenses_Panel:
        st.image("background.png", output_format="auto")
        selected_option = option_menu(
            menu_title=None,  # Title of the menu
            options=["Expense Tracking", "Receipt Management", "Financial Reporting", "Expense Categories", "Fundraising Activities", "Return"], 
            icons=["bar-chart-fill", "receipt", "box-fill", "tag-fill", "wallet2", "arrow-return-left"], 
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
        if selected_option == "Expense Tracking":
            pass
        if selected_option == "Receipt Management":
            pass
        if selected_option == "Financial Reporting":
            pass
        if selected_option == "Expense Categories":
            pass
        if selected_option == "Fundraising Activities":
            pass
        if selected_option == "Return":
            st.switch_page("pages/0201_Admin_Panel.py")
    with col2_Club_Expenses_Dashboard:
        st.markdown(
            """
            <div style="text-align:center">
                <h1>Account Management System</h1>
                <h3>Trojan Club of Robotics-TCR</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        with st.container():
            pass
    
if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        login()
        
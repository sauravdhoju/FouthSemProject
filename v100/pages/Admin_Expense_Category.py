import streamlit as st
from streamlit_option_menu import option_menu
from pages.Login_Page import main as login
from modules.Club_Expenses.CRUD_Admin_Exec_Club_Expense_UI import add_expense_category_ui, view_expense_category_ui, update_expense_category_ui, remove_expense_category_ui
from modules.Create_Connection.Create_Connection import create_connection

conn = create_connection()
def main():
    col1_exe_nav_panel,col2_exe_dashboard = st.columns([1,5])
    with col1_exe_nav_panel:
        st.image("background.png", output_format="auto")
        selected_option = option_menu(
            menu_title=None,  
            options=["Add Categories", "View Categories", "Update Categories","Remove Categories", "Return"],
            icons=["plus-circle", "eye", "cloud-upload", "person-x-fill","arrow-return-left"],
            orientation="vertical",
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
    with col2_exe_dashboard:
        st.markdown(
            """
            <div style="text-align:center">
                <h1>Account Management System</h1>
                <h3>Trojan Club of Robotics-TCR</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        if  selected_option == 'Add Categories':
            add_expense_category_ui()
        elif selected_option == 'View Categories':
            view_expense_category_ui()
        elif selected_option == 'Update Categories':
            update_expense_category_ui()
        elif selected_option == 'Remove Categories':
            remove_expense_category_ui()
        elif selected_option == 'Return':
            st.switch_page('pages/Admin_Club_Expenses.py')
        
if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        login()

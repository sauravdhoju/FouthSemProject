import streamlit as st
from streamlit_option_menu import option_menu
from pages.Login_Page import main as login
from modules.Club_Expenses.Expense_Category.CRUD_Admin_Exec_Club_Expense_Category_UI import add_expense_category_ui
def main():
    col1_Club_Expenses_Panel, col2_Club_Expenses_Dashboard = st.columns([1,5])
    with  col1_Club_Expenses_Panel:
        st.image("background.png", output_format="auto")
        selected_option = option_menu(
            menu_title=None,  # Title of the menu
            options=["Expense Tracking", "Receipt Management", "Expense Categories", "Return"], 
            icons=["bar-chart-fill", "receipt", "tag-fill", "arrow-return-left"], 
            menu_icon="th-large",  
            default_index=0, 
            orientation="vertical",  # Orientation of the menu (vertical or horizontal)
            styles={
                "container": {"padding": "0!important", "background-color": "#cef6ff"},
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
        if selected_option == "Expense Tracking":
            pass
        
        if selected_option == "Receipt Management":
            st.switch_page('pages/Admin_Receipt_Management.py')
        
        if selected_option == "Expense Categories":
            st.switch_page('pages/Admin_Expense_Category.py')
            
            
        # if selected_option == "Training and Education":
        #     st.switch_page("pages/Admin_Training_Education.py")
            
        if selected_option == "Return":
            st.switch_page("pages/Admin_Admin_Panel.py")
    
if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        login()
        
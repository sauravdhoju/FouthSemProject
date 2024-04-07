import streamlit as st
from streamlit_option_menu import option_menu
from pages.Login_Page import main as login

# Import functions for generating reports (not implemented here)

def main():
    col1_exe_nav_panel, col2_exe_dashboard = st.columns([1,5])
    with col1_exe_nav_panel:
        st.image("background.png", output_format="auto")
        selected_option = option_menu(
            menu_title=None,  
            options=["Generate Reports On ","Membership Report", "Payment Report", "Expense Report", "Return"],
            icons=["home", "person-down", "currency-dollar", "receipt", "arrow-left"],
            
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
        if selected_option == 'Membership Report':
            pass
            # generate_membership_report()  # Call function to generate membership report
        elif selected_option == 'Payment Report':
            pass
            # generate_payment_report()  # Call function to generate payment report
        elif selected_option == 'Expense Report':
            pass
            # generate_expense_report()  # Call function to generate expense report
        elif selected_option == 'Return':
            st.switch_page('pages/Admin_Membership_Management.py')

if __name__ == "__main__":
    if 'username' in st.session_state:
        main()
    else:
        st.warning("Login To access admin page")
        login()

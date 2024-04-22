import streamlit as st
from streamlit_option_menu import option_menu
from modules.Permission.hasPermission import *

def optionsByRole(options_dict, on):
    opt = []
    icons = []
    for option in options_dict:
            if has_permission(st.session_state['username'], options_dict[option][0], on) or option=="Return" or options_dict[option][0]=="":
                opt.append(option)
                icons.append(options_dict[option][2])
            print(option, options_dict[option], has_permission(st.session_state['username'], options_dict[option][0], "executives"))
    return opt, icons

def dashboardOption(options_dict):
    col1_exe_nav_panel,col2_exe_dashboard = st.columns([1,5])
    with col1_exe_nav_panel:
        st.image("background.png", output_format="auto")
        option, icon = optionsByRole(options_dict, "executives")
        selected_option = option_menu(
            menu_title=None,  
            icons=icon,
            orientation="vertical",  
            options= option,
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
    with col2_exe_dashboard:
        st.markdown(
            """
            <div style="text-align:center">
                <h1>Account Management System</h1>
                <h3>Trojan Club of Robotics-TCR</h3>
                <h4>Executives</h4>
            </div>
            """,
            unsafe_allow_html=True
        )
        # if selected_option == 'Return':
        #     options_dict[selected_option][1](return_page)
        # else:
        options_dict[selected_option][1]()

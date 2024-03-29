# executive_management.py
from pages.login import main as login
from modules.executives import (
    add_executive_members_ui,
    display_executive_members_ui,
    delete_executive_members_ui
)
import streamlit as st
from modules.executives import (
    add_executive_member,
    display_executive_members_ui,
    delete_executive_members_ui
)
from modules.database import create_connection

def main():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
    st.markdown("# Executive Management")
    
    suboption = st.radio("Manage Executive Members", ["Add", "View", "Remove"])

    conn = create_connection()
    if suboption == "Add":
        add_executive_members_ui(conn)
    elif suboption == "View":
        display_executive_members_ui(conn)
    elif suboption == "Remove":
        delete_executive_members_ui(conn)

if __name__ == "__main__":
    main()

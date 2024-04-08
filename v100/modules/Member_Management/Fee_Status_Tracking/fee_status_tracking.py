import streamlit as st
from modules.database import SQLiteDatabase
from datetime import datetime

def track_fee_status_ui():
    st.header("Fee Status Tracking")
    
    # Fetch all members from the database
    with SQLiteDatabase("accounting.db") as db:
        members = db.retrieve_records("Members")
    
    if members:
        st.subheader("Member Details")
        st.write("Use the table below to track fee payment status for each member.")
        
        # Display member table with fee status
        with st.expander("View Members"):
            for member in members:
                st.write(f"**{member['full_name']}**")
                st.write(f"Username: {member['username']}")
                st.write(f"Email: {member['email']}")
                st.write(f"Phone: {member['phone']}")
                st.write(f"Position: {member['position']}")
                st.write(f"Active Status: {'Active' if member['active_status'] else 'Inactive'}")
                st.write(f"Fee Status: {'Paid' if member['fee_paid'] else 'Not Paid'}")
                st.write("---")
                
    else:
        st.warning("No members found.")

def mark_fee_as_paid(member_id, amount_paid, payment_date=None):
    """Mark the fee as paid for a specific member."""
    payment_date = payment_date or datetime.now().date()
    with SQLiteDatabase("accounting.db") as db:
        db.update_record("Members", {"fee_paid": True}, {"member_id": member_id})
        # Add payment record to the database
        payment_record = {
            "member_id": member_id,
            "amount_paid": amount_paid,
            "payment_date": payment_date,
            "description": "Fee Payment"
        }
        db.create_record("Payments", payment_record)
        st.success("Fee marked as paid successfully.")
        

def get_fee_status(member_id):
    """Retrieve the fee payment status for a specific member."""
    with SQLiteDatabase("accounting.db") as db:
        member = db.retrieve_records("Members", {"member_id": member_id})
        if member:
            return member[0]["fee_paid"]
        else:
            return None

def send_fee_reminder(member_id):
    """Send a fee reminder to a specific member."""
    # Implement email sending functionality here
    pass

def generate_fee_status_report():
    """Generate a report summarizing fee payment status for all members."""
    # Fetch all members from the database
    with SQLiteDatabase("accounting.db") as db:
        members = db.retrieve_records("Members")
    
    if members:
        # Create a PDF report
        # Populate the report with fee status information for each member
        # Save or download the generated report
        pass
    else:
        st.warning("No members found.")
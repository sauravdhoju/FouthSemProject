import streamlit as st
from modules.database import SQLiteDatabase
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.platypus import PageBreak
import base64
def generate_membership_report():
    # Fetch active and inactive membership data separately
    with SQLiteDatabase("accounting.db") as db:
        active_membership_data = db.fetch_if("Members", {"active_status": True})
        inactive_membership_data = db.fetch_if("Members", {"active_status": False})
    
    # Check if there is any active membership data
    if active_membership_data or inactive_membership_data:
        # Create a PDF document
        doc = SimpleDocTemplate("membership_report.pdf", pagesize=A4)
        elements = []  # List to hold all elements
        
        if active_membership_data:
            # Define table data for active members
            active_table_data = [["Username", "Full Name", "Email", "Phone", "Position", "Active Status"]]
            for member in active_membership_data:
                active_table_data.append([member["username"], member["full_name"], member["email"], member["phone"], member["position"], member["active_status"]])
            
            # Create table for active members
            active_table = Table(active_table_data)
            style = TableStyle([('BACKGROUND', (0,0), (-1,0), colors.white),
                                ('TEXTCOLOR', (0,0), (-1,0), colors.black),
                                ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0,0), (-1,0), 12),
                                ('BACKGROUND', (0,1), (-1,-1), colors.white),
                                ('GRID', (0,0), (-1,-1), 1, colors.black)])
            active_table.setStyle(style)
            
            # Add active members table to PDF
            elements.append(active_table)
            elements.append(PageBreak())  # Add page break
        
        if inactive_membership_data:
            # Define table data for inactive members
            inactive_table_data = [["Username", "Full Name", "Email", "Phone", "Position", "Active Status"]]
            for member in inactive_membership_data:
                inactive_table_data.append([member["username"], member["full_name"], member["email"], member["phone"], member["position"], member["active_status"]])
            
            # Create table for inactive members
            inactive_table = Table(inactive_table_data)
            inactive_table.setStyle(style)
            
            # Add inactive members table to PDF
            elements.append(inactive_table)
        
        # Build the PDF document with all elements
        doc.build(elements)
        
        # Display the PDF in the web page using an iframe
        with open("membership_report.pdf", "rb") as f:
            pdf_contents = f.read()
            st.write(f'<div style="display: flex; justify-content: center;"><iframe src="data:application/pdf;base64,{base64.b64encode(pdf_contents).decode("utf-8")}" width="700" height="1000" allowfullscreen></iframe></div>', unsafe_allow_html=True)
        
        # Provide a download button for users to download the PDF file
        st.download_button(label="Download Membership Report", data=pdf_contents, file_name="membership_report.pdf", mime="application/pdf")
        
        st.success("Membership report generated successfully.")
    else:
        st.write("No members found.")

def generate_payment_report():
    # Fetch payment data
    with SQLiteDatabase("accounting.db") as db:
        payment_data = db.retrieve_records("Payments")
    
    # Check if there is any payment data
    if payment_data:
        # Create a PDF document
        doc = SimpleDocTemplate("payment_report.pdf", pagesize=A4)
        elements = []  # List to hold all elements
        
        # Define table data for payments
        payment_table_data = [["Payment ID", "Username", "Amount", "Date", "Payment Method", "Category Name"]]
        for payment in payment_data:
            payment_table_data.append([payment[0], payment[1], payment[2], payment[3], payment[4], payment[5]])
        
        # Create table for payments
        payment_table = Table(payment_table_data)
        style = TableStyle([('BACKGROUND', (0,0), (-1,0), colors.white),
                            ('TEXTCOLOR', (0,0), (-1,0), colors.black),
                            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0,0), (-1,0), 12),
                            ('BACKGROUND', (0,1), (-1,-1), colors.white),
                            ('GRID', (0,0), (-1,-1), 1, colors.black)])
        payment_table.setStyle(style)
        
        # Add payment table to PDF
        elements.append(payment_table)
        
        # Build the PDF document with all elements
        doc.build(elements)
        
        # Display the PDF in the web page using an iframe
        with open("payment_report.pdf", "rb") as f:
            pdf_contents = f.read()
            st.write(f'<div style="display: flex; justify-content: center;"><iframe src="data:application/pdf;base64,{base64.b64encode(pdf_contents).decode("utf-8")}" width="700" height="1000" allowfullscreen></iframe></div>', unsafe_allow_html=True)
        
        # Provide a download button for users to download the PDF file
        st.download_button(label="Download Payment Report", data=pdf_contents, file_name="payment_report.pdf", mime="application/pdf")
        
        st.success("Payment report generated successfully.")
    else:
        st.write("No payments found.")


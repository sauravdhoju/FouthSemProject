
import streamlit as st
from datetime import datetime
from modules.Club_Expenses.Database_Club_Expenses import add_receipt_backend, remove_receipt_backend, retrieve_receipts_backend, search_receipts_backend, update_receipt_backend

def add_receipt_ui():
    st.subheader("Add Receipt")
    with st.form("add_receipt_form"):
        col1, col2, col3 = st.columns([4,4,4])
        with col1:
            st.write("Receipt Details")
            receipt_number = st.text_input("Receipt Number")
            date = st.date_input("Date")
        with col2:
            st.write("Payer Details")
            payer_name = st.text_input("Payer Name")
            payment_type = st.selectbox("Payment Type", ["Cash", "Credit Card", "Debit Card", "Online Transfer"])
            purpose = st.text_area("Purpose")
        with col3:
            st.write("Purchased Amounts")
            quantity = st.number_input("Quantity", min_value=1)
            rate = st.number_input("Rate", min_value=0.01, step=0.01)
            vat_percent = st.number_input("VAT Percent", min_value=0.0, max_value=100.0, step=0.01, value=0.0)
            discount_percent = st.number_input("Discount Percent", min_value=0.0, max_value=100.0, step=0.01, value=0.0)
        submit_button = st.form_submit_button("Add Receipt")

        if submit_button:
            # Calculate total amount
            vat_amount = (quantity * rate * vat_percent) / 100
            discount_amount = (quantity * rate * discount_percent) / 100
            total_amount = (quantity * rate) + vat_amount - discount_amount

            # Call backend function to add receipt
            success = add_receipt_backend({
                'receipt_number': receipt_number,
                'date': date,
                'payment_type': payment_type,
                'payer_name': payer_name,
                'purpose': purpose,
                'quantity': quantity,
                'rate': rate,
                'vat_percent': vat_percent,
                'discount_percent': discount_percent,
                'amount': total_amount  # Store the calculated total amount
            })
            if success:
                st.success("Receipt added successfully!")
            else:
                st.error("Failed to add receipt. Please try again.")



def view_receipts_ui():
    st.subheader("View Receipts")
    # UI for viewing receipts
    with st.spinner("Loading receipts..."):
        receipts = retrieve_receipts_backend()
        if receipts:
            st.write(receipts)
        else:
            st.warning("No receipts found.")

def search_receipt_ui():
    st.subheader("Search Receipt")
    # UI for searching receipts
    search_query = st.text_input("Enter Receipt Number:")
    if st.button("Search"):
        with st.spinner("Searching..."):
            result = search_receipts_backend(search_query)
            if result:
                st.write(result)
            else:
                st.warning("Receipt not found.")

                
def update_receipt_ui():
    st.subheader("Update Receipt")
    # UI for updating receipts
    with st.form("receipt_id_search"):
        receipt_id = st.text_input("Enter Receipt ID:")
        fetch_receipt_button = st.form_submit_button("Fetch Receipt")

    # Debug prints
    print("Fetch Receipt button value:", fetch_receipt_button)

    if fetch_receipt_button:
        with st.spinner("Fetching receipt..."):
            # Fetch the receipt details based on ID
            # Display the fetched receipt details in the form for updating
            fetched_receipt = search_receipts_backend(receipt_id)
            if fetched_receipt:
                # Display the fetched receipt details in the form for updating
                receipt = fetched_receipt[0]  # Assuming only one receipt is fetched
                st.write("Receipt Details:")
                st.write(receipt)
                # UI elements for updating receipt details
                with st.form("update_receipt_form"):
                    receipt_number = st.text_input("Receipt Number", value=receipt['receipt_number'])
                    
                    # Convert date string to datetime object
                    date_obj = datetime.strptime(receipt['date'], "%Y-%m-%d")

                    # Now, you can pass date_obj to the date_input function
                    date = st.date_input("Date", value=date_obj)
                    payer_name = st.text_input("Payer Name", value=receipt['payer_name'])
                    payment_type = st.selectbox("Payment Type", ["Cash", "Credit Card", "Debit Card", "Online Transfer"], index=0)
                    purpose = st.text_area("Purpose", value=receipt['purpose'])
                    quantity = st.number_input("Quantity", min_value=1, value=receipt['quantity'])
                    rate = st.number_input("Rate", min_value=0.01, step=0.01, value=receipt['rate'])
                    vat_percent = st.number_input("VAT Percent", min_value=0.0, max_value=100.0, step=0.01, value=receipt['vat_percent'])
                    discount_percent = st.number_input("Discount Percent", min_value=0.0, max_value=100.0, step=0.01, value=receipt['discount_percent'])
                    submit_button = st.form_submit_button("Update Receipt")
                    print(submit_button)

                    if submit_button:
                        # Calculate total amount
                        vat_amount = (quantity * rate * vat_percent) / 100
                        discount_amount = (quantity * rate * discount_percent) / 100
                        total_amount = (quantity * rate) + vat_amount - discount_amount
                        
                        # Debug prints
                        print("Updating receipt...")
                        print("Receipt ID:", receipt_id)
                        print("Updated receipt data:")
                        print("Receipt Number:", receipt_number)
                        print("Date:", date)
                        print("Payer Name:", payer_name)
                        print("Payment Type:", payment_type)
                        print("Purpose:", purpose)
                        print("Quantity:", quantity)
                        print("Rate:", rate)
                        print("VAT Percent:", vat_percent)
                        print("Discount Percent:", discount_percent)
                        print("Total Amount:", total_amount)

                        # Update receipt details in the database
                        success = update_receipt_backend(receipt_id, {
                            'receipt_number': receipt_number,
                            'date': date.strftime("%Y-%m-%d"),  # Convert datetime object back to string
                            'payment_type': payment_type,
                            'payer_name': payer_name,
                            'purpose': purpose,
                            'quantity': quantity,
                            'rate': rate,
                            'vat_percent': vat_percent,
                            'discount_percent': discount_percent,
                            'amount': total_amount
                        })
                        if success:
                            st.success("Receipt updated successfully!")
                        else:
                            st.error("Failed to update receipt. Please try again.")
            else:
                st.warning("No receipt found with the provided ID.")
    else:
        print("Fetch Receipt button not clicked")






def remove_receipt_ui():
    st.subheader("Remove Receipt")
    # UI for removing receipts
    receipt_id = st.text_input("Enter Receipt ID:")
    if st.button("Delete Receipt"):
        with st.spinner("Deleting receipt..."):
            remove_receipt_backend(receipt_id)
            st.success("Receipt deleted successfully!")






























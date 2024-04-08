import streamlit as st
from modules.database import SQLiteDatabase
import altair as alt
import pandas as pd

def members():
    # Connect to the database
    with SQLiteDatabase("accounting.db") as db:
        # Retrieve data from tables
        members_count = len(db.retrieve_records("Members"))
        payments_data = db.retrieve_records("Payments")

    # Convert payments data to DataFrame for visualization
    payments_df = pd.DataFrame(payments_data)

    # Display dashboard
    st.title("Accounting Dashboard")

    # Container for the layout with border
    with st.container(border=True):
        # Membership overview
        st.header("Membership Overview")

        # Check if payments_df is empty
        if not payments_df.empty:
            # Metrics for total members, added members, and removed members
            total_members = len(db.retrieve_records("Members"))
            added_members = 10  # Placeholder, replace with actual calculation
            removed_members = 5  # Placeholder, replace with actual calculation

            # Metrics for total members, added members, and removed members
            st.metric(label="Total Members", value=total_members, delta=calculate_delta(total_members))
            st.metric(label="Added Members", value=added_members,delta=calculate_delta(added_members))
            st.metric(label="Removed Members", value=removed_members, delta=calculate_delta(removed_members))

            # Line chart for membership overview
            try:
                chart_data = pd.DataFrame({"Date": payments_df["payment_date"], "Total Members": range(1, total_members + 1)})
                line_chart = alt.Chart(chart_data).mark_line().encode(
                    x="Date:T",
                    y="Total Members:Q",
                    tooltip=["Date", "Total Members"]
                ).properties(width=700, height=400)

                st.altair_chart(line_chart, use_container_width=True)
            except KeyError:
                st.error("Error: 'payment_date' column not found in the payments data.")
            except Exception as e:
                st.error(f"Error occurred while creating the chart: {e}")
        else:
            st.warning("No payment data available for creating the chart.")

def receipts():
    # Connect to the database
    with SQLiteDatabase("accounting.db") as db:
        # Retrieve data from tables
        receipts_data = db.retrieve_records("receipts")

    # Convert receipts data to DataFrame for visualization
    receipts_df = pd.DataFrame(receipts_data)

    # Display receipts analytics
    st.header("Receipts Analytics")
    total_receipts = len(receipts_df)
    st.metric(label="Total Receipts", value=total_receipts, delta=calculate_delta(total_receipts))

    # Check if receipts_df is empty
    if not receipts_df.empty:
        # Line chart for receipts overview
        try:
            chart_data = pd.DataFrame({"Date": receipts_df["date"], "Total Receipts": range(1, total_receipts + 1)})
            line_chart = alt.Chart(chart_data).mark_line().encode(
                x="Date:T",
                y="Total Receipts:Q",
                tooltip=["Date", "Total Receipts"]
            ).properties(width=700, height=400)

            st.altair_chart(line_chart, use_container_width=True)
        except KeyError:
            st.error("Error: 'date' column not found in the receipts data.")
        except Exception as e:
            st.error(f"Error occurred while creating the chart: {e}")
    else:
        st.warning("No receipt data available for creating the chart.")

def calculate_delta(value):
    # Calculate the delta value to indicate ups and downs
    # For simplicity, you can customize this function based on your specific requirements
    if value > 0:
        return f"+{value}"
    elif value < 0:
        return f"-{value}"
    else:
        return value

def main():
    col1, col2 = st.columns(2)
    # with col1:
    #     members()
    with col2:
        receipts()

if __name__ == "__main__":
    main()


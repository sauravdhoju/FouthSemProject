import streamlit as st
from modules.database import SQLiteDatabase

# Function to create the Permissions table
def create_permissions_table(db):
    permissions_columns = {
        "permission_id": "INTEGER PRIMARY KEY",
        "permission_name": "TEXT UNIQUE"
    }
    db.create_table("Permissions", permissions_columns)
    st.success("Permissions table created successfully.")

# Function to insert a new permission
def insert_permission(db, permission_name):
    record_data = {
        "permission_name": permission_name
    }
    db.create_record("Permissions", record_data)
    return True

# Function to retrieve all permissions
def fetch_all_permissions(db):
    return db.retrieve_records("Permissions")

# Function to update a permission
def update_permission(db, permission_id, new_permission_name):
    new_data = {
        "permission_name": new_permission_name
    }
    conditions = {"permission_id": permission_id}
    db.update_record("Permissions", new_data, conditions)

# Function to delete a permission
def delete_permission(db, permission_id):
    try:
        conditions = {"permission_id": permission_id}
        deleted = db.delete_record("Permissions", conditions)
        if deleted:
            print("Permission has been deleted")
            return True
        else:
            print("No matching permission found")
            return False
    except Exception as e:
        print(f"Error deleting permission: {e}")
        return False

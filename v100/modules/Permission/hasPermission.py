# Define roles and their corresponding permissions
from modules.database import SQLiteDatabase

ROLES_PERMISSIONS = {
    "superuser": {
        "club_expenses":            {"add", "view", "edit", "delete"},
        "membership_management":    {"add", "view", "edit", "delete"},
        "bank_transaction":         {"add", "view", "edit", "delete"},
        "executives":               {"add", "view", "edit", "delete"}
    },
    "Secretary": {
        "club_expenses":            {"view"},
        "membership_management":    {"view"},
        "bank_transaction":         {"view"},        
        "executives":               {"view"},
        "profile":                  {"view"},
        "record_payment":           {"view"},
        "view_history_payment":     {"view"},
        "generate_report":          {"view"},
        "receipt_management":       {"view"},
        "expense_category":         {"view"},
    },
    "Treasurer": {
        "club_expenses":            {"view"},
        "membership_management":    {"view"},
        "bank_transaction":         {"add", "view"},        
        "executives":               {"view"},
        "profile":                  {"view"},
        "record_payment":           {"view"},
        "view_history_payment":     {"view"},
        "generate_report":          {"view"},
        "receipt_management":       {"view"},
        "expense_category":         {"view"},
    },
}

def has_permission(logged_in_username, action, on):
    with SQLiteDatabase("accounting.db") as db:
        user_details = db.fetch_if("Members", {"username": logged_in_username})
        if user_details:
            user_role = user_details[0].get("access_level")
            if user_role == "superuser":
                return True  # Admin has unrestricted access
            elif user_role in ROLES_PERMISSIONS:
                return action in ROLES_PERMISSIONS[user_role].get(on, set())
    return False

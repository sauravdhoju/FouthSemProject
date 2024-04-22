# Define roles and their corresponding permissions
from modules.database import SQLiteDatabase

ROLES_PERMISSIONS = {
    "superuser": {
        "club_expenses": {"view", "add", "edit", "delete"},
        "membership_management": {"view", "add", "edit", "delete"},
        "bank_transactions": {"view", "add", "edit", "delete"},
        "executives": {"view", "add", "edit", "delete"}
    },
    "Secretary": {
        "club_expenses": {"view"},
        "membership_management": {"view"},
        "bank_transactions": {"view"}
    },
    "Treasurer": {
        "club_expenses": {"view"},
        "membership_management": {"view", "generate_report"},
        "bank_transactions": {"view", "add", "edit", "delete"},
        "executives": {"add", "edit"},
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
                # print(user_role) 
                return action in ROLES_PERMISSIONS[user_role][on]
    return False
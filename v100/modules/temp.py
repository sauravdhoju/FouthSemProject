import sqlite3

class SQLiteDatabase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def create_table(self, table_name, columns):
        try:
            with self.connection:
                sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{col} {col_type}' for col, col_type in columns.items()])})"
                self.cursor.execute(sql)
            print(f"Table '{table_name}' created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating table '{table_name}': {e}")

    def create_record(self, table_name, record_data):
        try:
            with self.connection:
                columns = ', '.join(record_data.keys())
                placeholders = ', '.join('?' * len(record_data))
                sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                self.cursor.execute(sql, tuple(record_data.values()))
            print("Record inserted successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting record into '{table_name}': {e}")

    def retrieve_records(self, table_name, conditions=None):
        try:
            with self.connection:
                if conditions:
                    condition_str = ' AND '.join([f"{column} = ?" for column in conditions.keys()])
                    sql = f"SELECT * FROM {table_name} WHERE {condition_str}"
                    self.cursor.execute(sql, tuple(conditions.values()))
                else:
                    sql = f"SELECT * FROM {table_name}"
                    self.cursor.execute(sql)
                return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving records from '{table_name}': {e}")
            return []

    def update_record(self, table_name, new_data, conditions):
        try:
            with self.connection:
                set_str = ', '.join([f"{column} = ?" for column in new_data.keys()])
                condition_str = ' AND '.join([f"{column} = ?" for column in conditions.keys()])
                sql = f"UPDATE {table_name} SET {set_str} WHERE {condition_str}"
                self.cursor.execute(sql, tuple(new_data.values()) + tuple(conditions.values()))
            print("Record updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating record in '{table_name}': {e}")

    def delete_record(self, table_name, conditions):
        try:
            with self.connection:
                condition_str = ' AND '.join([f"{column} = ?" for column in conditions.keys()])
                sql = f"DELETE FROM {table_name} WHERE {condition_str}"
                self.cursor.execute(sql, tuple(conditions.values()))
            print("Record deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting record from '{table_name}': {e}")

# Example usage:
if __name__ == "__main__":
    db_file = "example.db"

    # Creating and using SQLiteDatabase within a context manager
    with SQLiteDatabase(db_file) as db:
        # Define table schemas
        table_schemas = {
            "members": {
                "id": "INTEGER PRIMARY KEY",
                "name": "TEXT",
                "age": "INTEGER",
                "email": "TEXT"
            },
            "records": {
                "id": "INTEGER PRIMARY KEY",
                "name": "TEXT",
                "age": "INTEGER",
                "email": "TEXT",
                "gender": "TEXT",
                "studying": "TEXT"
            }
        }

        # Create tables
        for table_name, columns in table_schemas.items():
            db.create_table(table_name, columns)

        # Insert records
        member_data = {"name": "John Doe", "age": 30, "email": "john@example.com"}
        db.create_record("members", member_data)
        saurav = {"name": "Saurav Dhoju", "age": 18, "email": "sauravdhoju@example.com", "gender": "male", "studying": "Bachelor"}
        db.create_record("records", saurav)

        # Retrieve records
        members = db.retrieve_records("members")
        print("Members:")
        for member in members:
            print(member)

        # Update records
        update_data = {"age": 31}
        update_conditions = {"name": "John Doe"}
        db.update_record("members", update_data, update_conditions)

        # Delete records
        delete_conditions = {"name": "John Doe"}
        db.delete_record("members", delete_conditions)

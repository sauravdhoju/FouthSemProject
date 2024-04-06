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
            return True
        except sqlite3.Error as e:
            print(f"Error inserting record into '{table_name}': {e}")
            return False
    
    
    def fetch_if(self, table_name, dict_conditions={}):
        '''Fetches Rows if dict_conditions matches '''
        query = f'SELECT * FROM {table_name} '
        conditions = []
        values = []

        if dict_conditions:
            query += 'WHERE '
            for key, value in dict_conditions.items():
                conditions.append(f'{key} = ?')
                values.append(value)
            query += ' AND '.join(conditions)

        try:
            with self.connection:
                self.cursor.execute(query, values)
                rows = self.cursor.fetchall()

                '''Convert rows to list of dictionaries for easier display'''
                rows_dicts = []
                for row in rows:
                    row_dict = {}
                    for i, column in enumerate(self.cursor.description):
                        row_dict[column[0]] = row[i]
                    rows_dicts.append(row_dict)
                
                return rows_dicts

        except sqlite3.Error as e:
            print(f"Error fetching records from '{table_name}': {e}")
            return []   
    
    
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
            # print(f"Attempting to delete record from {table_name}...")
            # print("Delete conditions:", conditions)
            with self.connection:
                condition_str = ' AND '.join([f"{column} = ?" for column in conditions.keys()])
                sql = f"DELETE FROM {table_name} WHERE {condition_str}"
                # print("SQL query:", sql)
                self.cursor.execute(sql, tuple(conditions.values()))
                if self.cursor.rowcount > 0:
                    print("Record deleted successfully.")
                    return True
                else:
                    print("No matching record found.")
                    return False
        except sqlite3.Error as e:
            print(f"Error deleting record from '{table_name}': {e}")
            return False
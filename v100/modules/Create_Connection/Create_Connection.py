import sqlite3

def create_connection():
    try:
        conn = sqlite3.connect('accounting.db')
        return conn
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    return None

def fetch_if(table_name, dict_conditions={}):
    '''Fetches Rows if dict_conditions matches '''
    conn = create_connection()
    cursor = conn.cursor()
    query = f'SELECT * FROM {table_name} '
    conditions = []
    values = []
    
    if dict_conditions:
        query += 'WHERE '
        for key, value in dict_conditions.items():
            conditions.append(f'{key} = ?')
            values.append(value)
        query += ' AND '.join(conditions)

    cursor.execute(query, values)
    rows = cursor.fetchall()

    '''Convert rows to list of dictionaries for easier display'''    
    rows_dicts = []
    for row in rows:
        row_dict = {}
        for i, column in enumerate(cursor.description):
            row_dict[column[0]] = row[i]
        rows_dicts.append(row_dict)

    return rows_dicts

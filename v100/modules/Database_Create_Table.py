import sqlite3
# from database import insert_default_user

def create_tables(conn):
    if conn is not None:
        try:
            cursor = conn.cursor()
#MEMBER TABLE
            cursor.execute('''CREATE TABLE IF NOT EXISTS Members (
                                member_id INTEGER PRIMARY KEY,
                                username TEXT UNIQUE NOT NULL,
                                hashed_password TEXT NOT NULL,
                                full_name TEXT NOT NULL,
                                email TEXT UNIQUE,
                                phone INTEGER,
                                position TEXT NOT NULL,
                                account_balance REAL DEFAULT 0 CHECK (account_balance >= 0),
                                joined_date DATE,
                                performance_metrics TEXT,
                                active_status BOOLEAN,
                                access_level TEXT NOT NULL,
                                account_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                role_id TEXT NOT NULL
                            )''')
#INSERTING DEFAULT USER
            # insert_default_user(conn)
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS Transactions (
                                transaction_id INTEGER PRIMARY KEY,
                                member_id INTEGER NOT NULL,
                                amount REAL NOT NULL,
                                purpose TEXT NOT NULL,
                                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                transaction_type TEXT CHECK (transaction_type IN ('Club Payment', 'Member Contribution')) NOT NULL,
                                payment_gateway TEXT,
                                FOREIGN KEY (member_id) REFERENCES Members(member_id)
                            )''')
#CLUB EXPENSES TABLE
            
            
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS Transactions (
                                transaction_id INTEGER PRIMARY KEY,
                                transaction_date DATE NOT NULL,
                                description TEXT NOT NULL,
                                amount REAL NOT NULL,
                                transaction_type TEXT NOT NULL,  -- Expense or Income
                                recorded_by TEXT,
                                FOREIGN KEY (recorded_by) REFERENCES Members(username)
                            )''')
            cursor.execute('''CREATE TABLE ExpenseTracking (
                                tracking_id INTEGER PRIMARY KEY,
                                expense_date DATE NOT NULL,
                                description TEXT NOT NULL,
                                amount REAL NOT NULL,
                                category_id INTEGER NOT NULL,
                                recorded_by TEXT,
                                FOREIGN KEY (category_id) REFERENCES ExpenseCategories(category_id),
                                FOREIGN KEY (recorded_by) REFERENCES Members(username)
                            )''')
            cursor.execute('''CREATE TABLE FinancialReports (
                                report_id INTEGER PRIMARY KEY,
                                report_date DATE NOT NULL,
                                description TEXT,
                                report_type TEXT NOT NULL,  -- Income Statement, Balance Sheet, etc.
                                generated_by TEXT,
                                FOREIGN KEY (generated_by) REFERENCES Members(username)
                            )''')
            cursor.execute('''CREATE TABLE ExpenseCategories (
                                category_id INTEGER PRIMARY KEY,
                                category_name TEXT UNIQUE NOT NULL
                            )''')
            
            
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS BankTransactions (
                                transaction_id INTEGER PRIMARY KEY,
                                member_id INTEGER NOT NULL,
                                debit_amount REAL NOT NULL,
                                credit_amount REAL NOT NULL,
                                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                FOREIGN KEY (member_id) REFERENCES Members(member_id) 
                            )''')
            cursor.execute('''CREATE INDEX IF NOT EXISTS idx_member_id ON Transactions(member_id)
                            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            
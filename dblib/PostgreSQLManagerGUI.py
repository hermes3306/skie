import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import psycopg2
from psycopg2 import OperationalError, DatabaseError
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import csv

class PostgreSQLManager:
    def __init__(self, dbname, user, password, host, port):
        self.connection_params = {
            "dbname": dbname,
            "user": user,
            "password": password,
            "host": host,
            "port": port
        }

    def connect(self):
        return psycopg2.connect(**self.connection_params)
    
    def test_connection(self):
        with self.connect() as conn:
            if not self.connection:
                return False
            try:
                with self.connection.cursor() as cur:
                    cur.execute('SELECT 1')
                return True
            except DatabaseError as e:
                print(f"PostgreSQL connection test failed: {e}")
                return False

    def execute_query(self, query, params=None, fetch=False):
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                if fetch:
                    return cur.fetchall()

    def delete_all_tables(self):
        conn = self.connect()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public'
                """)
                tables = cur.fetchall()
                
                for table in tables:
                    table_name = table[0]
                    print(f"Dropping table: {table_name}")
                    cur.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE")
                
                print("All tables have been dropped successfully.")
        
        except Exception as e:
            print(f"An error occurred: {e}")
        
        finally:
            conn.close()

    def create_table(self, table_name, columns):
        columns = [col.strip() for col in columns.split(',')]
        column_definitions = ','.join([f'"{col}" TEXT' for col in columns])
        create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
        
        self.execute_query(create_query)
        print(f"Table '{table_name}' created in PostgreSQL.")

    def get_table_names(self):
        query = """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """
        result = self.execute_query(query, fetch=True)
        return [row[0] for row in result]

    def get_table_columns(self, table_name):
        query = f"""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = %s
        """
        return [row[0] for row in self.execute_query(query, (table_name,), fetch=True)]

    def download_table_as_csv(self, table_name):
        columns = self.get_table_columns(table_name)
        query = f"SELECT * FROM {table_name}"
        rows = self.execute_query(query, fetch=True)

        with open(f'{table_name}.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(rows)
        
        print(f"Table '{table_name}' downloaded as CSV.")

    def upload_csv_to_table(self, csv_file_name):
        table_name = csv_file_name.replace('.csv', '').capitalize()
        
        with open(csv_file_name, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            columns = ', '.join(header)

        self.create_table(table_name, columns)

        with self.connect() as conn:
            with conn.cursor() as cur:
                with open(csv_file_name, 'r') as f:
                    cur.copy_expert(f"COPY {table_name} ({columns}) FROM STDIN CSV HEADER", f)

        print(f"Data from '{csv_file_name}' uploaded to PostgreSQL table '{table_name}'.")

    def list_tables(self):
        query = """
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """
        tables = self.execute_query(query, fetch=True)
        return [table[0] for table in tables]

    def display_table_structure(self, table_name):
        query = """
            SELECT column_name, data_type, character_maximum_length
            FROM information_schema.columns
            WHERE table_name = %s
            ORDER BY ordinal_position
        """
        columns = self.execute_query(query, (table_name,), fetch=True)
        
        if not columns:
            print(f"Table '{table_name}' not found or has no columns.")
            return

        print(f"\nStructure of table '{table_name}':")
        print("Column Name".ljust(30) + "Data Type".ljust(20) + "Max Length")
        print("-" * 70)
        for col in columns:
            col_name, data_type, max_length = col
            max_length = str(max_length) if max_length else 'N/A'
            print(f"{col_name.ljust(30)}{data_type.ljust(20)}{max_length}")


    def execute_custom_query(self, query):
        try:
            result = self.execute_query(query, fetch=True)
            if result:
                # Get column names
                with self.connect() as conn:
                    with conn.cursor() as cur:
                        cur.execute(query)
                        col_names = [desc[0] for desc in cur.description]
                
                # Print results in a tabular format
                print("\nQuery Result:")
                print(" | ".join(col_names))
                print("-" * (sum(len(col) for col in col_names) + 3 * (len(col_names) - 1)))
                for row in result:
                    print(" | ".join(str(item) for item in row))
            else:
                print("Query executed successfully. No results to display.")
        except Exception as e:
            print(f"Error executing query: {e}")

    def execute_ddl(self, ddl_statement):
        try:
            with self.connect() as conn:
                conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                with conn.cursor() as cur:
                    cur.execute(ddl_statement)
            print("DDL statement executed successfully.")
        except Exception as e:
            print(f"Error executing DDL statement: {e}")

def display_menu():
    print("\n--- PostgreSQL Database Manager ---")
    print("1. List all tables")
    print("2. Create a new table")
    print("3. Upload CSV to table")
    print("4. Download table as CSV")
    print("5. Delete all tables")
    print("6. Display table structure")
    print("7. Execute custom query")
    print("8. Execute DDL statement")
    print("9. Exit")
    return input("Enter your choice (1-9): ")

class DatabaseManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("PostgreSQL Database Manager")
        self.master.geometry("800x600")

        self.db_manager = PostgreSQLManager(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Left frame for buttons
        left_frame = ttk.Frame(main_frame, padding="10")
        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Right frame for output
        right_frame = ttk.Frame(main_frame, padding="10")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Buttons
        ttk.Button(left_frame, text="List Tables", command=self.list_tables).pack(fill=tk.X, pady=5)
        ttk.Button(left_frame, text="Create Table", command=self.create_table_dialog).pack(fill=tk.X, pady=5)
        ttk.Button(left_frame, text="Upload CSV", command=self.upload_csv_dialog).pack(fill=tk.X, pady=5)
        ttk.Button(left_frame, text="Download CSV", command=self.download_csv_dialog).pack(fill=tk.X, pady=5)
        ttk.Button(left_frame, text="Delete All Tables", command=self.delete_all_tables_dialog).pack(fill=tk.X, pady=5)
        ttk.Button(left_frame, text="Display Table Structure", command=self.display_table_structure_dialog).pack(fill=tk.X, pady=5)
        ttk.Button(left_frame, text="Execute Custom Query", command=self.execute_custom_query_dialog).pack(fill=tk.X, pady=5)
        ttk.Button(left_frame, text="Execute DDL Statement", command=self.execute_ddl_dialog).pack(fill=tk.X, pady=5)

        # Output text widget
        self.output_text = tk.Text(right_frame, wrap=tk.WORD, width=60, height=30)
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar for output text
        scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=self.output_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.configure(yscrollcommand=scrollbar.set)

    def list_tables(self):
        tables = self.db_manager.list_tables()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Current tables:\n")
        i = 0
        for table in tables:
            self.output_text.insert(tk.END, f"{table}\n")
            i+=1
        self.output_text.insert(tk.END, f"# of tables: {i}\n")


    def create_table_dialog(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Create New Table")
        
        ttk.Label(dialog, text="Table Name:").grid(row=0, column=0, padx=5, pady=5)
        table_name_entry = ttk.Entry(dialog, width=30)
        table_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(dialog, text="Columns (comma-separated):").grid(row=1, column=0, padx=5, pady=5)
        columns_entry = ttk.Entry(dialog, width=30)
        columns_entry.grid(row=1, column=1, padx=5, pady=5)
        
        def create_table():
            table_name = table_name_entry.get()
            columns = columns_entry.get()
            self.db_manager.create_table(table_name, columns)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"Table '{table_name}' created in PostgreSQL.")
            dialog.destroy()
        
        ttk.Button(dialog, text="Create", command=create_table).grid(row=2, column=0, columnspan=2, pady=10)

    def upload_csv_dialog(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.db_manager.upload_csv_to_table(file_path)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"Data from '{file_path}' uploaded to PostgreSQL.")

    def download_csv_dialog(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Download Table as CSV")
        
        ttk.Label(dialog, text="Table Name:").grid(row=0, column=0, padx=5, pady=5)
        table_name_entry = ttk.Entry(dialog, width=30)
        table_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        def download_csv():
            table_name = table_name_entry.get()
            self.db_manager.download_table_as_csv(table_name)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"Table '{table_name}' downloaded as CSV.")
            dialog.destroy()
        
        ttk.Button(dialog, text="Download", command=download_csv).grid(row=1, column=0, columnspan=2, pady=10)

    def delete_all_tables_dialog(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to delete all tables?"):
            self.db_manager.delete_all_tables()
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "All tables have been dropped successfully.")
        else:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Operation cancelled.")

    def display_table_structure_dialog(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Display Table Structure")
        
        ttk.Label(dialog, text="Table Name:").grid(row=0, column=0, padx=5, pady=5)
        table_name_entry = ttk.Entry(dialog, width=30)
        table_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        def display_structure():
            table_name = table_name_entry.get()
            self.db_manager.display_table_structure(table_name)
            dialog.destroy()
        
        ttk.Button(dialog, text="Display", command=display_structure).grid(row=1, column=0, columnspan=2, pady=10)

    def execute_custom_query_dialog(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Execute Custom Query")
        
        ttk.Label(dialog, text="SQL Query:").grid(row=0, column=0, padx=5, pady=5)
        query_text = tk.Text(dialog, width=40, height=10)
        query_text.grid(row=0, column=1, padx=5, pady=5)
        
        def execute_query():
            query = query_text.get("1.0", tk.END).strip()
            self.db_manager.execute_custom_query(query)
            dialog.destroy()
        
        ttk.Button(dialog, text="Execute", command=execute_query).grid(row=1, column=0, columnspan=2, pady=10)

    def execute_ddl_dialog(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Execute DDL Statement")
        
        ttk.Label(dialog, text="DDL Statement:").grid(row=0, column=0, padx=5, pady=5)
        ddl_text = tk.Text(dialog, width=40, height=10)
        ddl_text.grid(row=0, column=1, padx=5, pady=5)
        
        def execute_ddl():
            ddl_statement = ddl_text.get("1.0", tk.END).strip()
            self.db_manager.execute_ddl(ddl_statement)
            dialog.destroy()
        
        ttk.Button(dialog, text="Execute", command=execute_ddl).grid(row=1, column=0, columnspan=2, pady=10)

def main():
    root = tk.Tk()
    app = DatabaseManagerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
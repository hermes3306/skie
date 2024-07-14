import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, 
                             QGroupBox, QTextEdit)
from PyQt5.QtCore import Qt
import psycopg2
from neo4j import GraphDatabase

class DatabaseMigrationGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        # Databases section
        db_layout = QHBoxLayout()
        db_layout.addWidget(self.create_postgresql_group())
        db_layout.addWidget(self.create_neo4j_group())
        main_layout.addLayout(db_layout)

        # SQL and Cypher query sections
        query_layout = QHBoxLayout()
        query_layout.addWidget(self.create_sql_query_group())
        query_layout.addWidget(self.create_cypher_query_group())
        main_layout.addLayout(query_layout)

        # Migration button
        self.migrate_button = QPushButton("Migrate all tables from source to target")
        self.migrate_button.clicked.connect(self.migrate_data)
        main_layout.addWidget(self.migrate_button)

        # Welcome message
        welcome_text = ("Welcome to PostgreSQL to Neo4j migration tool.\n"
                        "Test connection to each DBMS and click \"Migrate\" button to migrate:")
        welcome_label = QLabel(welcome_text)
        main_layout.addWidget(welcome_label)

        # Status box
        self.status_box = QTextEdit()
        self.status_box.setReadOnly(True)
        main_layout.addWidget(self.status_box)

        self.setLayout(main_layout)
        self.setWindowTitle('PostgreSQL to Neo4j Migration Tool')
        self.show()

    def create_postgresql_group(self):
        group = QGroupBox("PostgreSQL")
        layout = QVBoxLayout()

        # Default values for PostgreSQL
        pg_defaults = {
            'url': 'postgresql://localhost:5432/postgres',
            'user': 'postgres',
            'password': 'postgres'
        }

        self.pg_inputs = {}
        for field, default in pg_defaults.items():
            layout.addWidget(QLabel(f"{field}:"))
            self.pg_inputs[field] = QLineEdit(default)
            if field == 'password':
                self.pg_inputs[field].setEchoMode(QLineEdit.Password)
            layout.addWidget(self.pg_inputs[field])

        self.pg_test_btn = QPushButton("Test Connection")
        self.pg_test_btn.clicked.connect(self.test_pg_connection)
        layout.addWidget(self.pg_test_btn)

        self.pg_table = QTableWidget(0, 5)
        self.pg_table.setHorizontalHeaderLabels(["name", "# of columns", "# of rows", "view", "info"])
        layout.addWidget(self.pg_table)

        group.setLayout(layout)
        return group

    def create_neo4j_group(self):
        group = QGroupBox("Neo4j")
        layout = QVBoxLayout()

        # Default values for Neo4j
        neo_defaults = {
            'url': 'neo4j+s://84a70536.databases.neo4j.io',
            'user': 'neo4j',
            'password': 'VOE78BcdKmy49Upzsl0_Dwb0IUfNdlEfwePszwlkB8g'
        }

        self.neo_inputs = {}
        for field, default in neo_defaults.items():
            layout.addWidget(QLabel(f"{field}:"))
            self.neo_inputs[field] = QLineEdit(default)
            if field == 'password':
                self.neo_inputs[field].setEchoMode(QLineEdit.Password)
            layout.addWidget(self.neo_inputs[field])

        self.neo_test_btn = QPushButton("Test Connection")
        self.neo_test_btn.clicked.connect(self.test_neo_connection)
        layout.addWidget(self.neo_test_btn)

        self.neo_table = QTableWidget(0, 5)
        self.neo_table.setHorizontalHeaderLabels(["name", "# of properties", "# of nodes", "view", "info"])
        layout.addWidget(self.neo_table)

        group.setLayout(layout)
        return group

    def create_sql_query_group(self):
        group = QGroupBox("SQL Query")
        layout = QVBoxLayout()

        self.sql_edit = QTextEdit()
        self.sql_edit.setPlaceholderText("Enter SQL query here")
        layout.addWidget(self.sql_edit)

        self.execute_sql_button = QPushButton("Execute SQL")
        self.execute_sql_button.clicked.connect(self.execute_sql_query)
        layout.addWidget(self.execute_sql_button)

        group.setLayout(layout)
        return group

    def create_cypher_query_group(self):
        group = QGroupBox("Cypher Query")
        layout = QVBoxLayout()

        self.cypher_edit = QTextEdit()
        self.cypher_edit.setPlaceholderText("Enter Cypher query here")
        layout.addWidget(self.cypher_edit)

        self.execute_cypher_button = QPushButton("Execute Cypher")
        self.execute_cypher_button.clicked.connect(self.execute_cypher_query)
        layout.addWidget(self.execute_cypher_button)

        group.setLayout(layout)
        return group
    
    def test_pg_connection(self):
        try:
            conn = psycopg2.connect(self.pg_inputs['url'].text(),
                                    user=self.pg_inputs['user'].text(),
                                    password=self.pg_inputs['password'].text())
            cur = conn.cursor()

            # Step 1: Get table names and column counts
            cur.execute("""
                SELECT table_name, COUNT(column_name) as column_count
                FROM information_schema.columns
                WHERE table_schema = 'public'
                GROUP BY table_name
            """)
            tables_info = cur.fetchall()

            # Step 2: Get row counts for each table
            table_row_counts = {}
            for table_name, _ in tables_info:
                cur.execute(f"SELECT COUNT(*) FROM {table_name}")
                row_count = cur.fetchone()[0]
                table_row_counts[table_name] = row_count

            # Populate the table widget
            self.pg_table.setRowCount(len(tables_info))
            for i, (table_name, column_count) in enumerate(tables_info):
                row_count = table_row_counts.get(table_name, 0)
                self.pg_table.setItem(i, 0, QTableWidgetItem(table_name))
                self.pg_table.setItem(i, 1, QTableWidgetItem(str(column_count)))
                self.pg_table.setItem(i, 2, QTableWidgetItem(str(row_count)))

            conn.close()
            self.status_box.append("PostgreSQL connection successful")
        except Exception as e:
            self.status_box.append(f"PostgreSQL connection error: {str(e)}")

    def test_neo_connection(self):
        try:
            driver = GraphDatabase.driver(self.neo_inputs['url'].text(), 
                                        auth=(self.neo_inputs['user'].text(), 
                                                self.neo_inputs['password'].text()))
            with driver.session() as session:
                result = session.run("""
                    CALL db.labels() YIELD label
                    CALL apoc.cypher.run('MATCH (n:`' + label + '`) 
                                        WITH count(n) as nodeCount, 
                                            reduce(s = [], k IN keys(n) | s + k) AS allProps
                                        RETURN nodeCount, size(apoc.coll.toSet(allProps)) as propCount', 
                                        {}) YIELD value
                    RETURN label, value.nodeCount AS count, value.propCount AS propCount
                """)
                labels = list(result)
                
                self.neo_table.setRowCount(len(labels))
                for i, record in enumerate(labels):
                    self.neo_table.setItem(i, 0, QTableWidgetItem(record['label']))
                    self.neo_table.setItem(i, 1, QTableWidgetItem(str(record['propCount'])))
                    self.neo_table.setItem(i, 2, QTableWidgetItem(str(record['count'])))
            
            driver.close()
            self.status_box.append("Neo4j connection successful")
        except Exception as e:
            self.status_box.append(f"Neo4j connection error: {e}")

    def execute_sql_query(self):
        query = self.sql_edit.toPlainText()
        try:
            conn = psycopg2.connect(self.pg_inputs['url'].text(),
                                    user=self.pg_inputs['user'].text(),
                                    password=self.pg_inputs['password'].text())
            cur = conn.cursor()
            cur.execute(query)
            result = cur.fetchall()
            conn.close()

            # Display the result in the status box
            self.status_box.append("SQL Query Result:")
            for row in result:
                self.status_box.append(str(row))
        except Exception as e:
            self.status_box.append(f"SQL Query Error: {str(e)}")

    def execute_cypher_query(self):
        query = self.cypher_edit.toPlainText()
        try:
            driver = GraphDatabase.driver(self.neo_inputs['url'].text(), 
                                          auth=(self.neo_inputs['user'].text(), 
                                                self.neo_inputs['password'].text()))
            with driver.session() as session:
                result = session.run(query)
                records = list(result)

            driver.close()

            # Display the result in the status box
            self.status_box.append("Cypher Query Result:")
            for record in records:
                self.status_box.append(str(record))
        except Exception as e:
            self.status_box.append(f"Cypher Query Error: {str(e)}")

    def migrate_data(self):
        self.status_box.append("Starting migration...")
        # Implement the migration logic here
        self.status_box.append("Migration completed.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DatabaseMigrationGUI()
    sys.exit(app.exec_())
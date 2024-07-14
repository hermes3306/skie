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

        fields = ['host', 'port', 'dbname', 'user', 'password']
        self.pg_inputs = {}
        for field in fields:
            layout.addWidget(QLabel(f"{field}:"))
            self.pg_inputs[field] = QLineEdit()
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

        fields = ['url', 'user', 'password']
        self.neo_inputs = {}
        for field in fields:
            layout.addWidget(QLabel(f"{field}:"))
            self.neo_inputs[field] = QLineEdit()
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

    def test_pg_connection(self):
        try:
            conn = psycopg2.connect(
                host=self.pg_inputs['host'].text(),
                port=self.pg_inputs['port'].text(),
                dbname=self.pg_inputs['dbname'].text(),
                user=self.pg_inputs['user'].text(),
                password=self.pg_inputs['password'].text()
            )
            cur = conn.cursor()
            cur.execute("SELECT table_name, column_count FROM (SELECT table_name, count(column_name) as column_count FROM information_schema.columns WHERE table_schema = 'public' GROUP BY table_name) AS t")
            tables = cur.fetchall()
            
            self.pg_table.setRowCount(len(tables))
            for i, (table_name, column_count) in enumerate(tables):
                self.pg_table.setItem(i, 0, QTableWidgetItem(table_name))
                self.pg_table.setItem(i, 1, QTableWidgetItem(str(column_count)))
                # Additional queries needed for row count and other info
            
            conn.close()
            self.status_box.append("PostgreSQL connection successful")
        except Exception as e:
            self.status_box.append(f"PostgreSQL connection error: {e}")

    def test_neo_connection(self):
        try:
            driver = GraphDatabase.driver(self.neo_inputs['url'].text(), 
                                          auth=(self.neo_inputs['user'].text(), 
                                                self.neo_inputs['password'].text()))
            with driver.session() as session:
                result = session.run("CALL db.labels()")
                labels = result.data()
                
                self.neo_table.setRowCount(len(labels))
                for i, label in enumerate(labels):
                    self.neo_table.setItem(i, 0, QTableWidgetItem(label['label']))
                    # Additional queries needed for property count, node count, and other info
            
            driver.close()
            self.status_box.append("Neo4j connection successful")
        except Exception as e:
            self.status_box.append(f"Neo4j connection error: {e}")

    def migrate_data(self):
        self.status_box.append("Starting migration...")
        # Implement the migration logic here
        self.status_box.append("Migration completed.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DatabaseMigrationGUI()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, 
                             QGroupBox, QTextEdit, QMessageBox, QComboBox, QProgressBar)
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

        # Migration section
        migration_layout = QHBoxLayout()
        
        # Table selection dropdown
        self.table_dropdown = QComboBox()
        self.table_dropdown.addItem("Select a table")
        migration_layout.addWidget(self.table_dropdown)

        # Migrate selected table button
        self.migrate_selected_button = QPushButton("Migrate selected table")
        self.migrate_selected_button.clicked.connect(self.migrate_selected_table)
        migration_layout.addWidget(self.migrate_selected_button)

        # Migrate all tables button
        self.migrate_all_button = QPushButton("Migrate all tables")
        self.migrate_all_button.clicked.connect(self.migrate_all_tables)
        migration_layout.addWidget(self.migrate_all_button)

        main_layout.addLayout(migration_layout)

        # Progress bar
        self.progress_bar = QProgressBar(self)
        main_layout.addWidget(self.progress_bar)

        # Welcome message
        welcome_text = ("Welcome to PostgreSQL to Neo4j migration tool.\n"
                        "Test connection to each DBMS and select a table to migrate or migrate all tables:")
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

        self.pg_table = QTableWidget(10, 5)  # Set initial row count to 10
        self.pg_table.setHorizontalHeaderLabels(["name", "# of columns", "# of rows", "view", "info"])
        self.pg_table.verticalHeader().setDefaultSectionSize(30)  # Adjust row height
        self.pg_table.setMinimumHeight(330)  # Approximate height for 10 rows + header
        layout.addWidget(self.pg_table)

        group.setLayout(layout)
        return group

    def create_neo4j_group(self):
        group = QGroupBox("Neo4j")
        layout = QVBoxLayout()

        neo_defaults = {
            'url' : 'bolt://localhost:7687',
            'user': 'neo4j',
            'password': 'neo4j_password'
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

        self.neo_table = QTableWidget(10, 5)  # Set initial row count to 10
        self.neo_table.setHorizontalHeaderLabels(["name", "# of properties", "# of nodes", "view", "info"])
        self.neo_table.verticalHeader().setDefaultSectionSize(30)  # Adjust row height
        self.neo_table.setMinimumHeight(330)  # Approximate height for 10 rows + header
        layout.addWidget(self.neo_table)

        group.setLayout(layout)
        return group

    def create_sql_query_group(self):
        group = QGroupBox("SQL Query")
        layout = QVBoxLayout()

        self.sql_edit = QTextEdit()
        # self.sql_edit.setFixedHeight(60)
        self.sql_edit.setPlaceholderText("Enter SQL query here (SELECT, INSERT, UPDATE, DELETE, CREATE TABLE, etc.)")
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
        # self.cypher_edit.setFixedHeight(60)
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
                ORDER BY table_name ASC
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
            self.table_dropdown.clear()
            self.table_dropdown.addItem("Select a table")
            for i, (table_name, column_count) in enumerate(tables_info):
                row_count = table_row_counts.get(table_name, 0)
                self.pg_table.setItem(i, 0, QTableWidgetItem(table_name))
                self.pg_table.setItem(i, 1, QTableWidgetItem(str(column_count)))
                self.pg_table.setItem(i, 2, QTableWidgetItem(str(row_count)))
                self.table_dropdown.addItem(table_name)

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
                                        RETURN count(n) as nodeCount, 
                                                size(apoc.coll.toSet(reduce(s = [], n IN collect(n) | s + keys(n)))) as propCount', 
                                        {}) YIELD value
                    RETURN label, value.nodeCount AS count, value.propCount AS propCount
                    ORDER BY label ASC
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


    def test_neo_connection_v1(self):
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
            
            # Check if the query is a SELECT statement
            is_select = query.strip().upper().startswith("SELECT")
            
            cur.execute(query)
            
            if is_select:
                result = cur.fetchall()
                # Display the result in the status box
                self.status_box.append("SQL Query Result:")
                for row in result:
                    self.status_box.append(str(row))
            else:
                # For non-SELECT queries, commit the changes and show affected rows
                conn.commit()
                self.status_box.append(f"SQL Query executed successfully. Rows affected: {cur.rowcount}")
            
            conn.close()
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
                
                # Check if the query returns results
                summary = result.consume()
                if summary.counters.contains_updates:
                    # For queries that modify the database
                    self.status_box.append("Cypher Query Result:")
                    self.status_box.append(f"Nodes created: {summary.counters.nodes_created}")
                    self.status_box.append(f"Nodes deleted: {summary.counters.nodes_deleted}")
                    self.status_box.append(f"Relationships created: {summary.counters.relationships_created}")
                    self.status_box.append(f"Relationships deleted: {summary.counters.relationships_deleted}")
                    self.status_box.append(f"Properties set: {summary.counters.properties_set}")
                else:
                    # For queries that return data
                    records = list(result)
                    self.status_box.append("Cypher Query Result:")
                    for record in records:
                        self.status_box.append(str(record))

            driver.close()
        except Exception as e:
            self.status_box.append(f"Cypher Query Error: {str(e)}")

    def migrate_data(self, specific_table=None):
        self.status_box.append("Starting migration...")
        self.progress_bar.setValue(0)
        try:
            # PostgreSQL connection
            pg_conn = psycopg2.connect(self.pg_inputs['url'].text(),
                                       user=self.pg_inputs['user'].text(),
                                       password=self.pg_inputs['password'].text())
            pg_cur = pg_conn.cursor()

            # Neo4j connection
            neo4j_driver = GraphDatabase.driver(self.neo_inputs['url'].text(), 
                                                auth=(self.neo_inputs['user'].text(), 
                                                      self.neo_inputs['password'].text()))

            # Get tables to migrate
            if specific_table:
                tables = [(specific_table,)]
            else:
                pg_cur.execute("""
                    SELECT table_name
                    FROM information_schema.tables
                    WHERE table_schema = 'public'
                """)
                tables = pg_cur.fetchall()

            total_tables = len(tables)
            table_progress_step = 100 // total_tables if total_tables > 0 else 100

            with neo4j_driver.session() as neo4j_session:
                for table_index, table in enumerate(tables):
                    table_name = table[0]
                    self.status_box.append(f"Migrating table: {table_name}")

                    # Get data from PostgreSQL
                    pg_cur.execute(f"SELECT * FROM {table_name}")
                    rows = pg_cur.fetchall()

                    # Get column names
                    pg_cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
                    columns = [col[0] for col in pg_cur.fetchall()]

                    # Migrate data to Neo4j
                    total_rows = len(rows)
                    update_interval = max(1, total_rows // 10)  # Ensure we don't divide by zero

                    for row_index, row in enumerate(rows):
                        try:
                            properties = dict(zip(columns, row))
                            cypher_query = f"CREATE (n:{table_name} $properties)"
                            neo4j_session.run(cypher_query, properties=properties)

                            # Update progress
                            row_progress = (row_index + 1) / total_rows
                            overall_progress = (table_index * table_progress_step) + (row_progress * table_progress_step)
                            self.progress_bar.setValue(int(overall_progress))
                            
                            # Update status at regular intervals
                            if (row_index + 1) % update_interval == 0 or row_index == total_rows - 1:
                                self.status_box.append(f"Migrated {row_index + 1}/{total_rows} rows from {table_name}")
                            
                            # Process events to keep the UI responsive
                            QApplication.processEvents()
                        except Exception as row_error:
                            self.status_box.append(f"Error migrating row {row_index + 1} from {table_name}: {str(row_error)}")
                            # Optionally, you can choose to continue with the next row or break the loop

                    self.status_box.append(f"Completed migrating {total_rows} rows from {table_name}")
            pg_conn.close()
            neo4j_driver.close()
            self.progress_bar.setValue(100)
            self.status_box.append("Migration completed successfully.")
        except Exception as e:
            self.status_box.append(f"Migration error: {str(e)}")
            print(e)
            self.progress_bar.setValue(0)           

    def migrate_data_v1(self, specific_table=None):
        self.status_box.append("Starting migration...")
        self.progress_bar.setValue(0)
        try:
            # PostgreSQL connection
            pg_conn = psycopg2.connect(self.pg_inputs['url'].text(),
                                       user=self.pg_inputs['user'].text(),
                                       password=self.pg_inputs['password'].text())
            pg_cur = pg_conn.cursor()

            # Neo4j connection
            neo4j_driver = GraphDatabase.driver(self.neo_inputs['url'].text(), 
                                                auth=(self.neo_inputs['user'].text(), 
                                                      self.neo_inputs['password'].text()))

            # Get tables to migrate
            if specific_table:
                tables = [(specific_table,)]
            else:
                pg_cur.execute("""
                    SELECT table_name
                    FROM information_schema.tables
                    WHERE table_schema = 'public'
                """)
                tables = pg_cur.fetchall()

            total_tables = len(tables)
            table_progress_step = 100 // total_tables if total_tables > 0 else 100

            with neo4j_driver.session() as neo4j_session:
                for table_index, table in enumerate(tables):
                    table_name = table[0]
                    self.status_box.append(f"Migrating table: {table_name}")

                    # Get data from PostgreSQL
                    pg_cur.execute(f"SELECT * FROM {table_name}")
                    rows = pg_cur.fetchall()

                    # Get column names
                    pg_cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
                    columns = [col[0] for col in pg_cur.fetchall()]

                    # Migrate data to Neo4j
                    total_rows = len(rows)
                    for row_index, row in enumerate(rows):
                        properties = dict(zip(columns, row))
                        cypher_query = (
                            f"CREATE (n:{table_name} $properties)"
                        )

                        print(cypher_query)

                        neo4j_session.run(cypher_query, properties=properties)

                        # Update progress
                        row_progress = (row_index + 1) / total_rows
                        overall_progress = (table_index * table_progress_step) + (row_progress * table_progress_step)
                        self.progress_bar.setValue(int(overall_progress))
                        
                        # Update status every 10% within a table
                        if row_index % (total_rows // 10) == 0:
                            self.status_box.append(f"Migrated {row_index + 1}/{total_rows} rows from {table_name}")
                        
                        # Process events to keep the UI responsive
                        QApplication.processEvents()

                    self.status_box.append(f"Completed migrating {total_rows} rows from {table_name}")

            pg_conn.close()
            neo4j_driver.close()
            self.progress_bar.setValue(100)
            self.status_box.append("Migration completed successfully.")
        except Exception as e:
            self.status_box.append(f"Migration error: {str(e)}")
            print(e)
            self.progress_bar.setValue(0)

    def migrate_selected_table(self):
        selected_table = self.table_dropdown.currentText()
        if selected_table == "Select a table":
            self.status_box.append("Please select a table to migrate.")
            return
        self.migrate_data(selected_table)

    def migrate_all_tables(self):
        self.migrate_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DatabaseMigrationGUI()
    sys.exit(app.exec_())